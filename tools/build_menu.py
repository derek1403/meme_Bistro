"""迷因酒館 菜單產生器。

讀取 memes/*.md 的 front matter，檢查資料，並生成：
  menu/<topic>.md      各主題畫廊
  menu/index.md        全部迷因總表（方便 Ctrl+F）
  menu/humor.md        依笑點類型
  menu/tags.md         標籤索引
  menu/explained.md    附笑點解說的梗（看不懂專區）
  menu/bartender_pick.md  調酒師今日精選（依日期隨機）
  README.md 中 <!-- MENU:START --> ... <!-- MENU:END --> 區塊

用法：
  py tools/build_menu.py          檢查並生成
  py tools/build_menu.py --check  只檢查，不寫檔
只用標準函式庫。
"""
import datetime
import random
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MEMES = ROOT / 'memes'
IMAGES = ROOT / 'images'
MENU = ROOT / 'menu'
README = ROOT / 'README.md'

TOPICS = {
    'math':     ('🧮', '數學'),
    'science':  ('🔬', '物理與自然科學'),
    'cs-ai':    ('💻', '程式與 AI'),
    'academia': ('🎓', '學術與研究生活'),
    'language': ('🗣️', '語言與諧音'),
    'life':     ('🍺', '日常與生活'),
    'society':  ('🌍', '社會與地獄梗'),
}
HUMOR = {
    'hardcore':  ('🧠', '硬核', '要有學科背景才笑得出來'),
    'intuitive': ('👀', '直觀', '看圖就懂'),
    'pun':       ('🔤', '諧音／文字梗', '雙關、諧音、字面意思'),
    'dark':      ('🔥', '地獄梗', '拿敏感題材開玩笑，請斟酌'),
}
LANGS = {'zh', 'en', 'ja', 'es', 'mixed', 'none'}
STARS = {1: '★', 2: '★★', 3: '★★★'}
EXPLAIN_HEADING = '## 🍸 笑點解說'
GALLERY_COLS = 3
THUMB_WIDTH = 240
PICK_COUNT = 12


def parse_value(raw):
    raw = raw.strip()
    if raw.startswith('[') and raw.endswith(']'):
        return [x.strip() for x in raw[1:-1].split(',') if x.strip()]
    if raw.startswith('"') and raw.endswith('"'):
        return raw[1:-1].replace('\\"', '"').replace('\\\\', '\\')
    if raw.isdigit():
        return int(raw)
    return raw


def load_card(path):
    text = path.read_text(encoding='utf-8')
    m = re.match(r'^---\n(.*?)\n---\n(.*)$', text, re.S)
    if not m:
        raise ValueError('缺少 front matter')
    meta = {}
    for line in m.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        key, _, value = line.partition(':')
        meta[key.strip()] = parse_value(value)
    meta['body'] = m.group(2)
    meta['path'] = path
    return meta


def validate(cards):
    errors = []
    seen = set()
    used_images = set()
    for c in cards:
        name = c['path'].name
        for key in ('id', 'title', 'image', 'topic', 'humor', 'tags', 'difficulty', 'lang'):
            if key not in c or c[key] in ('', []):
                errors.append(f'{name}: 缺少欄位 {key}')
        if c.get('id') in seen:
            errors.append(f'{name}: id 重複 {c.get("id")}')
        seen.add(c.get('id'))
        if c.get('id') and c['path'].stem != c['id']:
            errors.append(f'{name}: 檔名與 id 不一致')
        img = (MEMES / str(c.get('image', ''))).resolve()
        if not img.is_file():
            errors.append(f'{name}: 找不到圖片 {c.get("image")}')
        used_images.add(img.name)
        if c.get('topic') not in TOPICS:
            errors.append(f'{name}: 未知 topic {c.get("topic")}')
        for h in c.get('humor', []):
            if h not in HUMOR:
                errors.append(f'{name}: 未知 humor {h}')
        if c.get('difficulty') not in STARS:
            errors.append(f'{name}: difficulty 需為 1~3')
        if c.get('lang') not in LANGS:
            errors.append(f'{name}: 未知 lang {c.get("lang")}')
        if isinstance(c.get('difficulty'), int) and c['difficulty'] >= 2 and EXPLAIN_HEADING not in c['body']:
            errors.append(f'{name}: 難度 ≥2 必須有「{EXPLAIN_HEADING}」段落')
        if 'dark' in c.get('humor', []) and not c.get('content_warning'):
            errors.append(f'{name}: 地獄梗必須填 content_warning')
    for img in IMAGES.iterdir():
        if img.is_file() and img.name not in used_images:
            errors.append(f'images/{img.name}: 沒有對應的卡片')
    return errors


# ---------- 產生 Markdown ----------

def card_link(c, prefix='../memes/'):
    return f'[{c["title"]}]({prefix}{c["id"]}.md)'


def humor_badges(c):
    return ''.join(HUMOR[h][0] for h in c['humor'])


def cw_note(c):
    return f' ⚠️ {c["content_warning"]}' if c.get('content_warning') else ''


def cell(c):
    img = c['image']  # 相對於 memes/，在 menu/ 也同樣是 ../images/
    return (f'<a href="../memes/{c["id"]}.md"><img src="{img}" width="{THUMB_WIDTH}" '
            f'alt="{c["title"]}"></a><br>'
            f'<a href="../memes/{c["id"]}.md">{c["title"]}</a><br>'
            f'<sub>{humor_badges(c)} {STARS[c["difficulty"]]}</sub>')


def gallery(cards):
    if not cards:
        return '_（暫無）_\n'
    rows = ['<table>']
    for i in range(0, len(cards), GALLERY_COLS):
        rows.append('<tr>')
        for c in cards[i:i + GALLERY_COLS]:
            rows.append(f'<td align="center" valign="top" width="33%">{cell(c)}</td>')
        rows.append('</tr>')
    rows.append('</table>')
    return '\n'.join(rows) + '\n'


GENERATED = '<!-- 此檔由 tools/build_menu.py 自動生成，請勿手動修改 -->\n\n'
BACK = '[⬅ 回酒館大廳](../README.md) ・ [📋 總表](index.md) ・ [🏷️ 標籤](tags.md) ・ [🍸 看不懂專區](explained.md)\n'


def build_topic_page(topic, cards):
    emoji, label = TOPICS[topic]
    safe = [c for c in cards if 'dark' not in c['humor'] and not c.get('content_warning')]
    warned = [c for c in cards if c not in safe]
    out = [GENERATED, f'# {emoji} {label}\n\n', BACK, '\n',
           f'共 {len(cards)} 張。依難度排序：★ 一看就懂 → ★★★ 要有學科背景。\n\n']
    for d in (1, 2, 3):
        group = [c for c in safe if c['difficulty'] == d]
        if group:
            out.append(f'## {STARS[d]}（{len(group)}）\n\n')
            out.append(gallery(group) + '\n')
    if warned:
        out.append(f'## ⚠️ 需斟酌（{len(warned)}）\n\n')
        out.append('> 以下迷因涉及性、死亡、種族、宗教、政治等敏感題材，點開前請確認你能接受。\n\n')
        for c in warned:
            out.append(f'<details><summary>{c["title"]} — ⚠️ {c["content_warning"] or "地獄梗"}</summary>\n\n')
            out.append(gallery([c]))
            out.append('\n</details>\n\n')
    return ''.join(out)


def build_index(cards):
    out = [GENERATED, '# 📋 全部迷因總表\n\n', BACK, '\n',
           f'共 {len(cards)} 張。用瀏覽器的 Ctrl+F 搜尋關鍵字最快。\n\n',
           '| ID | 標題 | 主題 | 笑點 | 難度 | 標籤 |\n|---|---|---|---|---|---|\n']
    for c in cards:
        emoji, label = TOPICS[c['topic']]
        out.append(f'| {c["id"]} | {card_link(c)}{cw_note(c)} | {emoji} {label} | {humor_badges(c)} | '
                   f'{STARS[c["difficulty"]]} | {"、".join(c["tags"])} |\n')
    return ''.join(out)


def build_humor(cards):
    out = [GENERATED, '# 😂 依笑點類型\n\n', BACK, '\n']
    for key, (emoji, label, desc) in HUMOR.items():
        group = [c for c in cards if key in c['humor']]
        out.append(f'- [{emoji} {label}（{len(group)}）](#{key})\n')
    out.append('\n')
    for key, (emoji, label, desc) in HUMOR.items():
        group = [c for c in cards if key in c['humor']]
        out.append(f'<a id="{key}"></a>\n\n## {emoji} {label}（{len(group)}）\n\n{desc}\n\n')
        for c in group:
            t_emoji = TOPICS[c['topic']][0]
            out.append(f'- {t_emoji} {card_link(c)} {STARS[c["difficulty"]]}{cw_note(c)}\n')
        out.append('\n')
    return ''.join(out)


def build_tags(cards):
    tags = defaultdict(list)
    for c in cards:
        for t in c['tags']:
            tags[t].append(c)
    out = [GENERATED, '# 🏷️ 標籤索引\n\n', BACK, '\n',
           f'共 {len(tags)} 個標籤。出現 2 次以上的標籤排在前面。\n\n']
    common = sorted((t for t in tags if len(tags[t]) > 1), key=lambda t: (-len(tags[t]), t))
    rare = sorted((t for t in tags if len(tags[t]) == 1), key=str.lower)
    out.append('## 常見標籤\n\n')
    for t in common:
        links = '、'.join(card_link(c) for c in tags[t])
        out.append(f'- **{t}**（{len(tags[t])}）：{links}\n')
    out.append('\n## 其他標籤\n\n')
    for t in rare:
        out.append(f'- **{t}**：{card_link(tags[t][0])}\n')
    return ''.join(out)


def build_explained(cards):
    group = [c for c in cards if EXPLAIN_HEADING in c['body']]
    out = [GENERATED, '# 🍸 看不懂專區\n\n', BACK, '\n',
           f'這裡收錄附有「笑點解說」的 {len(group)} 張迷因。先看圖，想不通再點進去看解說。\n\n']
    for d in (3, 2, 1):
        sub = [c for c in group if c['difficulty'] == d]
        if not sub:
            continue
        out.append(f'## {STARS[d]}（{len(sub)}）\n\n')
        by_topic = defaultdict(list)
        for c in sub:
            by_topic[c['topic']].append(c)
        for topic in TOPICS:
            if by_topic[topic]:
                emoji, label = TOPICS[topic]
                links = '、'.join(card_link(c) + cw_note(c) for c in by_topic[topic])
                out.append(f'- {emoji} **{label}**：{links}\n')
        out.append('\n')
    return ''.join(out)


def build_pick(cards):
    today = datetime.date.today()
    rng = random.Random(today.isoformat())
    pool = [c for c in cards if not c.get('content_warning')]
    picks = rng.sample(pool, min(PICK_COUNT, len(pool)))
    return ''.join([GENERATED, '# 🎲 調酒師今日精選\n\n', BACK, '\n',
                    f'每次執行 `tools/build_menu.py` 會依當天日期（{today.isoformat()}）隨機抽出 {len(picks)} 杯，'
                    '不含需斟酌的內容。\n\n', gallery(picks)])


def build_readme_block(cards):
    lines = ['| 主題 | 數量 | 說明 |', '|---|---:|---|']
    desc = {
        'math': '微積分、代數、拓樸、集合論、統計……從國中到研究所',
        'science': '物理、化學、地科，外加相對論與量子力學',
        'cs-ai': '工程師日常、LLM、Claude、vibe coding',
        'academia': '研究生、論文、口試、教授',
        'language': '諧音、雙關、台語、選字錯誤',
        'life': '動畫、日常、戀愛、萬用反應圖',
        'society': '歷史、宗教、政治與地獄梗（多數附警示）',
    }
    for topic, (emoji, label) in TOPICS.items():
        n = sum(c['topic'] == topic for c in cards)
        lines.append(f'| [{emoji} {label}](menu/{topic}.md) | {n} | {desc[topic]} |')
    humor = ' ・ '.join(f'{e} {l} {sum(k in c["humor"] for c in cards)}' for k, (e, l, _) in HUMOR.items())
    diff = ' ・ '.join(f'{STARS[d]} {sum(c["difficulty"] == d for c in cards)}' for d in (1, 2, 3))
    explained = sum(EXPLAIN_HEADING in c['body'] for c in cards)
    lines += ['', f'**共 {len(cards)} 張** ・ 附笑點解說 {explained} 張', '',
              f'笑點：{humor}', '', f'難度：{diff}']
    return '\n'.join(lines)


def main():
    check_only = '--check' in sys.argv
    cards = []
    errors = []
    for path in sorted(MEMES.glob('*.md')):
        try:
            cards.append(load_card(path))
        except ValueError as e:
            errors.append(f'{path.name}: {e}')
    errors += validate(cards)
    if errors:
        print(f'❌ {len(errors)} 個問題：')
        for e in errors:
            print('  -', e)
        sys.exit(1)
    print(f'✅ {len(cards)} 張卡片檢查通過')
    if check_only:
        return

    MENU.mkdir(exist_ok=True)
    pages = {'index.md': build_index(cards), 'humor.md': build_humor(cards),
             'tags.md': build_tags(cards), 'explained.md': build_explained(cards),
             'bartender_pick.md': build_pick(cards)}
    for topic in TOPICS:
        pages[f'{topic}.md'] = build_topic_page(topic, [c for c in cards if c['topic'] == topic])
    for name, text in pages.items():
        (MENU / name).write_text(text, encoding='utf-8', newline='\n')

    readme = README.read_text(encoding='utf-8')
    block = f'<!-- MENU:START -->\n{build_readme_block(cards)}\n<!-- MENU:END -->'
    readme, n = re.subn(r'<!-- MENU:START -->.*?<!-- MENU:END -->', lambda _: block, readme, flags=re.S)
    if n != 1:
        print('❌ README.md 找不到 MENU 區塊')
        sys.exit(1)
    README.write_text(readme, encoding='utf-8', newline='\n')
    print(f'📝 已生成 menu/ 共 {len(pages)} 頁，並更新 README.md')


if __name__ == '__main__':
    main()
