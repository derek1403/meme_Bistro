# 整理紀錄 findings

2026-09-26 首次整理：把 `pic/` 裡自行下載的 262 張迷因（meme_001–262）整理成一圖一卡。

## 結果

- 262 張 → 刪除 6 張完全重複 → **256 張**，每張一份 `memes/m####.md` 卡片。
- 重複檢查：md5 雜湊＋感知雜湊（dHash，閾值 20/256）。只找到 6 組位元完全相同的檔案，沒有其他近似重複。
- `physics` 與 `science` 合併為 `science`（物理與自然科學）。

## 刪除的重複檔

| 刪除 | 與它相同的保留檔 | 新 id |
|---|---|---|
| meme_036.png | meme_035.png | m0035 |
| meme_046.png | meme_045.png | m0044 |
| meme_052.png | meme_051.png | m0049 |
| meme_081.png | meme_080.png | m0077 |
| meme_111.png | meme_110.png | m0106 |
| meme_169.png | meme_168.png | m0163 |

## 待確認（解說把握度較低）

| id | 標題 | 疑點 |
|---|---|---|
| m0055 | 名人格言錄（數學家版） | 最後一格人物與百合的連結是依網路傳聞推測 |
| m0081 | 從 82 倒數到 1 竟是質數 | 「82 是少數會得到質數的起點之一」未獨立驗證 |
| m0098 | 心裡想一個數字（理科人版） | 上半的心算步驟是依圖轉述，算式細節待對照原圖 |
| m0179 | KFC 為啥只寫拉拉 | 「給給」的網路用法有多種解讀 |
| m0195 | VIBE 代表什麼？ | 推文為偽造截圖，卡片已註明 |
| m0208 | 我是你的法向量啦！ | 原梗笑點眾說紛紜，解說採最常見解讀 |
| m0230 | JavaScript 工程師的分號鍵 | 可正反兩種解讀（狂打分號 / 從不打分號） |
| m0247 | 你手上沒有槓桿，但你有 20 元 | 湯匙選項的笑點不明確 |

## 舊檔名 → 新 id 對照

| 舊檔名 | 新 id | 新圖檔 |
|---|---|---|
| meme_001.png | m0001 | m0001-discriminant-stay-positive.png |
| meme_002.png | m0002 | m0002-math-teacher-joke-coset.png |
| meme_003.png | m0003 | m0003-unsettled-tom-continuum-hypothesis.png |
| meme_004.png | m0004 | m0004-gauss-bonnet-powerpuff.png |
| meme_005.png | m0005 | m0005-ai-low-hanging-fruit.png |
| meme_006.png | m0006 | m0006-evolution-of-letter-a.png |
| meme_007.png | m0007 | m0007-password-must-be-unique.png |
| meme_008.png | m0008 | m0008-rich-gpt-astra-max.png |
| meme_009.png | m0009 | m0009-you-less-than-three.png |
| meme_010.png | m0010 | m0010-eyes-keeping-up-with-ai-news.png |
| meme_011.png | m0011 | m0011-do-calculus-everywhere.png |
| meme_012.png | m0012 | m0012-cursed-rows-columns.png |
| meme_013.png | m0013 | m0013-bayesians-dogs-tina-venn.png |
| meme_014.png | m0014 | m0014-telepathic-grin.png |
| meme_015.png | m0015 | m0015-twins-binary-search.png |
| meme_016.png | m0016 | m0016-physicist-froze-0k.png |
| meme_017.png | m0017 | m0017-nvidia-watches-ai-fight.png |
| meme_018.png | m0018 | m0018-ugly-algebra-physics.png |
| meme_019.png | m0019 | m0019-gpt-vs-navier-stokes.png |
| meme_020.png | m0020 | m0020-most-tempting-rtx5090.png |
| meme_021.jpg | m0021 | m0021-why-ghosts-are-white-cotton.jpg |
| meme_022.png | m0022 | m0022-why-ghosts-are-white-work.png |
| meme_023.png | m0023 | m0023-cancel-20-dollar-subscription.png |
| meme_024.png | m0024 | m0024-365-divisible-by-73.png |
| meme_025.png | m0025 | m0025-you-just-listed-my-fetish.png |
| meme_026.png | m0026 | m0026-laplacian-spherical-coordinates.png |
| meme_027.png | m0027 | m0027-perfect-thesis-never-finished.png |
| meme_028.png | m0028 | m0028-sudo-open-your-eyes.png |
| meme_029.png | m0029 | m0029-absolute-positive-feedback.png |
| meme_030.png | m0030 | m0030-eyes-designers-ai-tools.png |
| meme_031.png | m0031 | m0031-drunk-math-notation.png |
| meme_032.png | m0032 | m0032-why-llm-hallucinates.png |
| meme_033.png | m0033 | m0033-red-envelope-kfc.png |
| meme_034.png | m0034 | m0034-eating-with-yuri-anime.png |
| meme_035.png | m0035 | m0035-bikini-force-equilibrium.png |
| meme_036.png | （刪除，同 meme_035.png） | — |
| meme_037.png | m0036 | m0036-can-you-drink-pee.png |
| meme_038.png | m0037 | m0037-proof-obvious-spinor.png |
| meme_039.png | m0038 | m0038-derivative-of-constant.png |
| meme_040.png | m0039 | m0039-phenolphthalein-red-ink.png |
| meme_041.jpg | m0040 | m0040-made-in-abyss-invite.jpg |
| meme_042.png | m0041 | m0041-adhd-introvert-with-ai.png |
| meme_043.png | m0042 | m0042-ai-paints-the-fence.png |
| meme_044.png | m0043 | m0043-math-then-vs-now.png |
| meme_045.png | m0044 | m0044-number-systems-beyond-octonions.png |
| meme_046.png | （刪除，同 meme_045.png） | — |
| meme_047.png | m0045 | m0045-land-breeze-at-night.png |
| meme_048.png | m0046 | m0046-ring-finger-blood-vessel.png |
| meme_049.png | m0047 | m0047-lolita-condensed-milk-avocado.png |
| meme_050.png | m0048 | m0048-ai-engineer-2026-dog-walker.png |
| meme_051.png | m0049 | m0049-xiang-yu-chu-broken.png |
| meme_052.png | （刪除，同 meme_051.png） | — |
| meme_053.png | m0050 | m0050-mbti-nt-kings-debate.png |
| meme_054.png | m0051 | m0051-afraid-of-math-take-physics.png |
| meme_055.png | m0052 | m0052-lhospital-kermit.png |
| meme_056.png | m0053 | m0053-summer-vacation-plan.png |
| meme_057.png | m0054 | m0054-vibe-coder-claude-pro.png |
| meme_058.png | m0055 | m0055-mathematician-quotes-yuri.png |
| meme_059.png | m0056 | m0056-wrong-fumo-no-math.png |
| meme_060.png | m0057 | m0057-gu-ming-baby-name.png |
| meme_061.png | m0058 | m0058-first-idol-ave-mujica.png |
| meme_062.png | m0059 | m0059-integral-sin-dx-engineer.png |
| meme_063.png | m0060 | m0060-scary-bell-pepper-faces.png |
| meme_064.png | m0061 | m0061-claude-3-months-3-hours.png |
| meme_065.png | m0062 | m0062-claude-guess-color-purple.png |
| meme_066.png | m0063 | m0063-meta-ai-misidentifies-lu.png |
| meme_067.png | m0064 | m0064-meta-ai-misidentifies-chang.png |
| meme_068.png | m0065 | m0065-elmo-brain-vs-claude-cursor.png |
| meme_069.png | m0066 | m0066-amazing-chemistry-ideas.png |
| meme_070.png | m0067 | m0067-jacobian-conjecture-almost-surely.png |
| meme_071.png | m0068 | m0068-taiwanese-homophones-guiqulai.png |
| meme_072.png | m0069 | m0069-spoiled-on-airplane.png |
| meme_073.png | m0070 | m0070-vibe-coding-expectation-reality.png |
| meme_074.png | m0071 | m0071-norway-flag-czech-recursion.png |
| meme_075.png | m0072 | m0072-claude-test-deploy-meetings.png |
| meme_076.png | m0073 | m0073-programmer-uses-claude.png |
| meme_077.png | m0074 | m0074-mathematician-doing-research.png |
| meme_078.png | m0075 | m0075-2020-days-since-2020.png |
| meme_079.png | m0076 | m0076-octal-halloween-christmas.png |
| meme_080.png | m0077 | m0077-senren-banka-rephrase.png |
| meme_081.png | （刪除，同 meme_080.png） | — |
| meme_082.png | m0078 | m0078-group-is-groupoid-joke.png |
| meme_083.png | m0079 | m0079-python-arch-energy-drink.png |
| meme_084.png | m0080 | m0080-x4-plus-1-factorization-cat.png |
| meme_085.png | m0081 | m0081-countdown-82-prime.png |
| meme_086.png | m0082 | m0082-integral-ex-de.png |
| meme_087.png | m0083 | m0083-developers-beaten-by-everyone.png |
| meme_088.png | m0084 | m0084-seven-factors-eisenstein.png |
| meme_089.png | m0085 | m0085-typhoon-names-taiwan-vote.png |
| meme_090.png | m0086 | m0086-cube-age-square-two-years-ago.png |
| meme_091.png | m0087 | m0087-preskill-lecture-notes-recommend.png |
| meme_092.png | m0088 | m0088-ring-abelian-group-monoid.png |
| meme_093.png | m0089 | m0089-dont-become-like-claude-uncle.png |
| meme_094.png | m0090 | m0090-typhoon-i-tried-my-best.png |
| meme_095.png | m0091 | m0091-grad-school-depression-pattern.png |
| meme_096.png | m0092 | m0092-shiba-shirt-recursion.png |
| meme_097.png | m0093 | m0093-open-vscode-after-sex.png |
| meme_098.png | m0094 | m0094-thunderous-copywriting.png |
| meme_099.png | m0095 | m0095-claude-rejects-love-confession.png |
| meme_100.png | m0096 | m0096-ml-interview-answer-15.png |
| meme_101.png | m0097 | m0097-salmon-saltwater-monsters.png |
| meme_102.png | m0098 | m0098-think-of-a-number-ordinal.png |
| meme_103.png | m0099 | m0099-ai-random-numbers-find-pattern.png |
| meme_104.png | m0100 | m0100-topologist-smoking.png |
| meme_105.png | m0101 | m0101-useless-backend-cat.png |
| meme_106.png | m0102 | m0102-direct-integral-upgrade.png |
| meme_107.png | m0103 | m0103-jellyfish-launch-button.png |
| meme_108.png | m0104 | m0104-eight-legs-dietitians.png |
| meme_109.png | m0105 | m0105-last-stroke-of-death.png |
| meme_110.png | m0106 | m0106-rip-stupid-im-with-stupid.png |
| meme_111.png | （刪除，同 meme_110.png） | — |
| meme_112.png | m0107 | m0107-save-dollars-owe-one-twelfth.png |
| meme_113.png | m0108 | m0108-grad-student-skips-stairs.png |
| meme_114.png | m0109 | m0109-chiikawa-chromosome-contest.png |
| meme_115.png | m0110 | m0110-traitor-among-us-pun.png |
| meme_116.png | m0111 | m0111-funny-fat-friend-study.png |
| meme_117.png | m0112 | m0112-lust-to-electricity-bracelet.png |
| meme_118.png | m0113 | m0113-gave-her-my-heart-comment.png |
| meme_119.png | m0114 | m0114-glasgow-ufo-spongebob.png |
| meme_120.png | m0115 | m0115-do-it-yourself-or-ai-flowchart.png |
| meme_121.png | m0116 | m0116-contour-integral-in-novel.png |
| meme_122.png | m0117 | m0117-page-fold-linear-programming.png |
| meme_123.png | m0118 | m0118-topologist-same-picture.png |
| meme_124.png | m0119 | m0119-programmer-husband-cake-condition.png |
| meme_125.png | m0120 | m0120-claude-cold-response.png |
| meme_126.png | m0121 | m0121-mujica-mygo-mugo.png |
| meme_127.png | m0122 | m0122-hungry-whatever-is-fine.png |
| meme_128.png | m0123 | m0123-von-neumann-ordinal-four.png |
| meme_129.png | m0124 | m0124-how-much-procrastination-vtuber.png |
| meme_130.png | m0125 | m0125-living-tree-burial.png |
| meme_131.png | m0126 | m0126-density-theorem-unmasked.png |
| meme_132.png | m0127 | m0127-mathematics-gf.png |
| meme_133.png | m0128 | m0128-split-the-atom-weapon.png |
| meme_134.png | m0129 | m0129-hk-security-law-gears-jam.png |
| meme_135.png | m0130 | m0130-min-yi-shi-wei-ten.png |
| meme_136.png | m0131 | m0131-before-becoming-great-circle.png |
| meme_137.png | m0132 | m0132-grandpa-turned-over-by-caregiver.png |
| meme_138.png | m0133 | m0133-multiply-age-by-i-four-times.png |
| meme_139.png | m0134 | m0134-hilbert-godel-wet-concrete.png |
| meme_140.png | m0135 | m0135-great-wall-protects-cheating.png |
| meme_141.png | m0136 | m0136-tilde-gentle-person-similar.png |
| meme_142.png | m0137 | m0137-type-c-taipuxi.png |
| meme_143.png | m0138 | m0138-xkcd-reverse-engineer-units.png |
| meme_144.png | m0139 | m0139-uninstall-earth-online.png |
| meme_145.png | m0140 | m0140-programmer-vampire-twilight.png |
| meme_146.png | m0141 | m0141-i-love-animals-tech-logos.png |
| meme_147.png | m0142 | m0142-whale-in-amazon-jungle.png |
| meme_148.jpg | m0143 | m0143-kimetsu-100-times-aniplex.jpg |
| meme_149.png | m0144 | m0144-delinquent-manga-broken-bone.png |
| meme_150.png | m0145 | m0145-rationalized-period-formula.png |
| meme_151.png | m0146 | m0146-two-wolves-code.png |
| meme_152.png | m0147 | m0147-we-never-ordered-fried-rice.png |
| meme_153.png | m0148 | m0148-viral-math-ambiguous-notation.png |
| meme_154.png | m0149 | m0149-imaginary-parents-real-number.png |
| meme_155.png | m0150 | m0150-topologist-donut-torus.png |
| meme_156.png | m0151 | m0151-ampere-right-hand-exam.png |
| meme_157.png | m0152 | m0152-its-twelve-then.png |
| meme_158.png | m0153 | m0153-smbc-fahrenheit-celsius-agree.png |
| meme_159.png | m0154 | m0154-when-x-equals-y-x-is-y.png |
| meme_160.png | m0155 | m0155-shame-corner-spongebob.png |
| meme_161.png | m0156 | m0156-krabby-patty-no-love.png |
| meme_162.png | m0157 | m0157-mama-ganbatte-icu.png |
| meme_163.png | m0158 | m0158-cos-sin-tan-tiger-board-game.png |
| meme_164.png | m0159 | m0159-vibe-coders-dont-debug.png |
| meme_165.png | m0160 | m0160-matrix-2x3-usb.png |
| meme_166.png | m0161 | m0161-ai-surgery-robot-operation-game.png |
| meme_167.png | m0162 | m0162-jesus-holy-semen.png |
| meme_168.png | m0163 | m0163-power-of-a-point-chopsticks.png |
| meme_169.png | （刪除，同 meme_168.png） | — |
| meme_170.png | m0164 | m0164-tennis-ball-orbit-linear-fit.png |
| meme_171.png | m0165 | m0165-baby-doubled-extrapolation.png |
| meme_172.png | m0166 | m0166-love-note-pass-forward.png |
| meme_173.png | m0167 | m0167-macos-windows-linux-old-program.png |
| meme_174.png | m0168 | m0168-pregnancy-test-cardioid.png |
| meme_175.png | m0169 | m0169-lawyer-mouth-pun.png |
| meme_176.png | m0170 | m0170-oral-defense-passed-plane.png |
| meme_177.png | m0171 | m0171-iodine-hydrogen-motorcycle.png |
| meme_178.png | m0172 | m0172-military-interrupts-holiday-mood.png |
| meme_179.png | m0173 | m0173-barber-pde-haircut.png |
| meme_180.png | m0174 | m0174-jojo-roots-crystal-reaction.png |
| meme_181.png | m0175 | m0175-research-work-behind-you.png |
| meme_182.png | m0176 | m0176-30-days-friends-wont-recognize.png |
| meme_183.png | m0177 | m0177-math-major-riemann-hypothesis.png |
| meme_184.png | m0178 | m0178-floating-mug-topologist.png |
| meme_185.png | m0179 | m0179-kfc-pull-pull-door.png |
| meme_186.png | m0180 | m0180-japan-phillips-curve-japan.png |
| meme_187.png | m0181 | m0181-2-union-3-equals-3.png |
| meme_188.png | m0182 | m0182-errata-typo-90-minutes.png |
| meme_189.png | m0183 | m0183-spongebob-snow-sculpture-kids.png |
| meme_190.png | m0184 | m0184-uniquely-euclidean-domains.png |
| meme_191.png | m0185 | m0185-yuri-tastes-good.png |
| meme_192.png | m0186 | m0186-yachiyo-sings-every-era.png |
| meme_193.png | m0187 | m0187-population-after-decimal-point.png |
| meme_194.png | m0188 | m0188-souls-message-no-qualification.png |
| meme_195.png | m0189 | m0189-freshman-sum-finite-field.png |
| meme_196.png | m0190 | m0190-miyu-illya-war.png |
| meme_197.png | m0191 | m0191-mosquito-blood-boyfriend.png |
| meme_198.png | m0192 | m0192-np-hard-illusion-of-choice.png |
| meme_199.png | m0193 | m0193-infosec-boyfriend-rce.png |
| meme_200.png | m0194 | m0194-claude-mythos-throne.png |
| meme_201.png | m0195 | m0195-vibe-stands-for.png |
| meme_202.png | m0196 | m0196-loop-quantum-cosmology-derivative.png |
| meme_203.png | m0197 | m0197-thesis-database-folklore.png |
| meme_204.jpg | m0198 | m0198-xu-zhimo-plane-crash.jpg |
| meme_205.png | m0199 | m0199-mokou-kaguya-through-wall.png |
| meme_206.png | m0200 | m0200-basal-metabolism-5000-kcal.png |
| meme_207.png | m0201 | m0201-buddha-amen.png |
| meme_208.png | m0202 | m0202-data-are-vs-data-is.png |
| meme_209.png | m0203 | m0203-certified-vs-linux-user.png |
| meme_210.png | m0204 | m0204-strait-of-hormuz-clopen.png |
| meme_211.png | m0205 | m0205-ph-paper-turns-black.png |
| meme_212.png | m0206 | m0206-claude-5-hour-token-stamina.png |
| meme_213.png | m0207 | m0207-basketball-falls-field.png |
| meme_214.png | m0208 | m0208-i-am-your-normal-vector.png |
| meme_215.png | m0209 | m0209-friends-replaced-by-ai.png |
| meme_216.png | m0210 | m0210-doppler-red-light-fine.png |
| meme_217.png | m0211 | m0211-zebra-crossing-double-slit.png |
| meme_218.png | m0212 | m0212-exclamation-taylor-series-cute.png |
| meme_219.png | m0213 | m0213-griffiths-solution-manual.png |
| meme_220.png | m0214 | m0214-how-to-handle-cats-touhou.png |
| meme_221.png | m0215 | m0215-einstein-hands-perspective.png |
| meme_222.png | m0216 | m0216-claude-first-try-addiction.png |
| meme_223.png | m0217 | m0217-count-eggs-multiply-source.png |
| meme_224.png | m0218 | m0218-projection-dog-flattened.png |
| meme_225.png | m0219 | m0219-zariski-topology-hint.png |
| meme_226.png | m0220 | m0220-small-face-abstract-differential.png |
| meme_227.png | m0221 | m0221-run-as-administrator.png |
| meme_228.png | m0222 | m0222-6-9-pulley-perpetual-motion.png |
| meme_229.png | m0223 | m0223-change-thinking-statistician.png |
| meme_230.png | m0224 | m0224-crater-lake-transparent.png |
| meme_231.png | m0225 | m0225-dont-wake-sleeping-person.png |
| meme_232.png | m0226 | m0226-fortune-cookie-cite-paper.png |
| meme_233.png | m0227 | m0227-transformer-vs-nan.png |
| meme_234.png | m0228 | m0228-nature-weird-sequence-mathematicians.png |
| meme_235.png | m0229 | m0229-3-plus-3-times-3-taiwan.png |
| meme_236.png | m0230 | m0230-javascript-semicolon-key.png |
| meme_237.png | m0231 | m0231-denominator-molecule.png |
| meme_238.png | m0232 | m0232-loofah-matcha-cake.png |
| meme_239.png | m0233 | m0233-consequences-of-studying-physics.png |
| meme_240.png | m0234 | m0234-sleep-8-hours-in-3-relativity.png |
| meme_241.png | m0235 | m0235-should-have-learned-linear-algebra.png |
| meme_242.png | m0236 | m0236-sinx-over-x-galaxy-brain.png |
| meme_243.png | m0237 | m0237-iff-ww3-girlfriend.png |
| meme_244.png | m0238 | m0238-uika-i-want-to-see-sakiko.png |
| meme_245.png | m0239 | m0239-professor-assigns-own-paper.png |
| meme_246.png | m0240 | m0240-adult-rated-topics-reactions.png |
| meme_247.png | m0241 | m0241-scnice-science-fair.png |
| meme_248.png | m0242 | m0242-wagyu-no-wenti.png |
| meme_249.png | m0243 | m0243-van-der-waals-super-saiyan.png |
| meme_250.png | m0244 | m0244-thighs-wish-depression.png |
| meme_251.png | m0245 | m0245-happy-education-evolution.png |
| meme_252.png | m0246 | m0246-pi-as-fraction-hbar.png |
| meme_253.png | m0247 | m0247-trolley-problem-buy-spoon.png |
| meme_254.png | m0248 | m0248-levitated-mass-pressure.png |
| meme_255.png | m0249 | m0249-water-bottles-at-2am.png |
| meme_256.png | m0250 | m0250-invertible-matrix-spiderman.png |
| meme_257.png | m0251 | m0251-error-percent-engineer.png |
| meme_258.png | m0252 | m0252-riemann-openclaw-fermat.png |
| meme_259.png | m0253 | m0253-factorial-vs-not-equal.png |
| meme_260.png | m0254 | m0254-better-to-be-man-list.png |
| meme_261.png | m0255 | m0255-coulomb-looks-like-newton.png |
| meme_262.png | m0256 | m0256-goldfish-pond-lie.png |
