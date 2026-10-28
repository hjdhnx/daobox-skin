# 皮肤制作与上架指南（Skin Authoring Guide）

> 本文件是 DaBox 官方皮肤市场（本仓）的制作指南**公开镜像**；权威源在 DaoBox
> 项目仓库的 `docs/SKIN-AUTHORING-GUIDE.md`（私有仓）。**不要直接改本文件**——
> 它由导出脚本生成，直接改会在下次导出时被覆盖。文档修正请提 Issue；
> 皮肤/资产 PR 欢迎（见 §五 上架与分发）。
> 配套原型：[prototype.html](prototype.html)（浏览器直接打开，五套皮肤交互演示）。
## 〇、三分钟理解皮肤包

一套皮肤 = 一个 zip（后缀 `.dsz`），里面没有任何可执行代码：

```
my-skin.dsz
├─ skin.json     皮肤声明（唯一必选；一张「token 表」）
├─ preview.webp  市场预览图（750×520，≤120KB，可选）
├─ bg/           背景图（可选）
│  ├─ home_light.webp
│  └─ home_dark.webp
├─ icons/        自绘图标（可选，48/96px webp/png）
└─ font/         字体（可选，仅 ttf/otf，≤5MB）
```

三个心智模型：

1. **换皮不换骨**：皮肤只改变视觉（颜色/圆角/材质/渐变/图标/字体/背景），布局、交互、功能一概不许碰——你在 JSON 里也写不了它们（写了会被拒载）。
2. **token 表**：App 里每个控件的每个视觉参数都有一个「字段名」。做皮肤 = 给其中一些字段填新值；没填的用默认值。
3. **三级取值**：你填的值生效优先级是 `包内自绘图 > 明确声明的值 > App 默认`，每个字段独立回退——做一半的皮肤也能用。

## 一、三条上手路径

### 路径 A：从 App 导出改起（最快，10 分钟出成品）

1. App：设置 → 外观 → 把主题色/圆角/玻璃/背景调成你喜欢的样子；
2. 高级 → **导出当前效果为皮肤包**（你的全部调节会合并进 skin.json）；
3. 解压 zip，用任意文本编辑器打开 skin.json 继续改（见 §二字段表）；
4. 压回 zip 改后缀 `.dsz` → 高级 → **导入皮肤包** 验证。

### 路径 B：抄官方模板

从[官方市场](#五十上架分发)下载任意一款皮肤的 `.dsz` 解包当起点——结构与字段完全一致，改名改值即可。

### 路径 C：让 AI 生成（异想天开的主通道）

把 §二的字段表 + §六的提示词模板喂给任何大模型（ChatGPT / Claude / Gemini 均可），描述你想要的感觉，让它产出 skin.json；图片资产让它生成 SVG 再转 webp。产出后走路径 A 第 4 步导入验证，报错信息直接贴回给 AI 迭代。

## 二、skin.json 完整字段参考

### 2.1 meta（必填）

| 字段 | 必填 | 说明 |
|---|---|---|
| `id` | ✓ | 全局唯一，反向域名风格（`dao.skin.xxx` / `com.you.xxx`）；你自己的皮肤用你自己的前缀 |
| `name` | ✓ | 展示名 |
| `version` | ✓ | 语义化版本（`1.0.0`），市场更新判定锚点 |
| `minEngine` | ✓ | 皮肤引擎版本——**用了哪一版的字段就填哪一版**，见下表；当前目标 = `4` |
| `mode` | ✓ | `both`（双域）/ `light` / `dark`（单域皮肤在另一域回落默认色板，市场标注「仅暗色」等） |
| `author` / `description` | | 展示用 |

**引擎版本对照表**（`minEngine` 填多少由你用了哪些字段决定；旧引擎遇到不认识的字段会丢弃并降级，不会崩——但用新版字段却把 `minEngine` 填低了，用户会看到「效果少了一半」）：

| minEngine | 字段组 | 你大概在做 |
|---|---|---|
| `1` | `color` / `shape` / `material`(fill·glass·outline) / `type` / `surface` / `motion` | 基础换色换形状 |
| `2` | `comp` 槽位、`material.elevation` | 想某一块单独不一样 / 要立体感 |
| `3` | `icons` 图标轨、`material.card: gradient` | 换图标 / 渐变卡 |
| `4` | `gradient` 显式渐变段 | 按钮、横幅、底栏渐变 |

**不确定就填 `4`**（当前目标版本），除非你想兼容更老的 App。

### 2.2 color——颜色（三种玩法，复杂度递增）

**玩法 1：种子色（推荐，90% 场景）**——给一个种子，引擎自动生成整套协调的明暗双色板（M3 算法）：

```json
"color": { "strategy": "seed", "seed": { "light": "#0B57D0", "dark": "#8AB4F8" } }
```

**玩法 2：中性色调偏**——在种子之上让灰色系偏冷/偏暖：`"neutralBias": "cool" | "warm" | "plain"`。

**玩法 3：override 精确色表**——逐角色手写（必须 light/dark 成对、40 角色齐全、全部过 AA 对比度校验；设计期一般用不到）：

```json
"color": { "strategy": "override",
  "override": { "light": { "primary": "#…", "surface": "#…", "…": "共 40 个角色" },
                "dark":  { "…": "…" } } }
```

### 2.3 shape——形状（域无关，明暗共用）

| 字段 | 值域 | 作用 |
|---|---|---|
| `card` | 0–28 | 卡片圆角 |
| `chip` | 0–16 | 小控件/徽标圆角 |
| `sheet` | 0–32 | 底部弹层圆角 |
| `button` | `pill` / `rounded` / `square` | 按钮形态 |
| `navBar` | `floating` / `attached` | 底栏：悬浮胶囊 / 贴底通栏 |

### 2.4 material——材质与立体感

| 字段 | 值域 |
|---|---|
| `card` | `fill`（实色）/ `glass`（半透明+描边+棱线）/ `outline`（描边空心）/ `gradient`（渐变，等价 §2.6 显式写法） |
| `cardOpacity` | 0.35–0.85（glass 时的表面不透明度） |
| `cardBorder` | 描边像素宽，0 = 无 |
| `cardHighlight` | true = 玻璃顶部 1px 高光棱线 |
| `elevation` | `none` / `low` / `mid` / `high`——立体感档位，映射引擎内置阴影配方（**不能自定义任意阴影**，这是质感守恒的关键） |

### 2.5 comp——组件槽位（某一块单独不一样）

只开放全局段的字段子集，取值回落链 `comp.<slot> → 全局段 → 默认`：

```json
"comp": {
  "banner":   { "material": "gradient", "gradientAngle": 120, "border": "rgba(34,211,238,.45)" },
  "navBar":   { "tint": "#101623" },
  "searchBar": { "material": "outline" },
  "listItem": {}
}
```

### 2.6 gradient——渐变（v1.3）

**铁律：渐变只进「面」，不进「字」**。文字与图标色永远是单色，且必须压得住渐变两端。

```json
"gradient": {
  "primary": { "type": "linear", "angle": 135, "stops": ["#8E2DE2", "#4A00E0"] },
  "card":    { "type": "linear", "angle": 120, "stops": ["#FFE29F", "#FFA99F", "#FF719B"] },
  "banner":  null,
  "navBar":  null,
  "chipOn":  null
}
```

- 可渐变的面：`primary`（主按钮/强调面）、`card`、`banner`、`navBar`、`chipOn`（选中态标签）；
- `stops` 2–4 个 hex，`angle` 0–360，`type` 目前仅 `linear`；
- 校验：`onPrimary`/`onSurface` 必须对 **最亮和最暗两个 stop** 都达到 AA 对比度——给 AI 的需求里直接说「渐变要保证白字可读」，它懂。

### 2.7 icons——图标换装

**双键取值**，每处图标独立解析：语义槽位（`images` > `map` 里的槽位键）＞ 图标名替换（`map` 里的图标名键）＞ 默认。

```json
"icons": {
  "tint": "auto",
  "map":   { "chevron_right": "east",           ← 图标名键（不含点号）：全站所有这个图标一起换
             "settings.row.chevron": "east",    ← 槽位键（含点号）：只换「设置行行尾箭头」这个位置
             "tab.home": "cottage",             ← 槽位键：只换底栏 home
             "tab.profile": "person_rounded" },
  "images":{ "tab.ai": "icons/sparkle_line.webp",
             "tab.lab": { "light": "icons/flask_light.webp", "dark": "icons/flask_dark.webp" } }
}
```

**「换 A 留 B」规则**：键**含点号 = 位置槽位**（Material 名不含点号，零歧义）。两个控件
用了同一个图标时：只写图标名键 → A、B 一起换；只想换 A → 给 A 的位置写一条槽位键，
B 不写就保持默认。槽位由页面侧标注（常见位置类别如底栏 `tab.*`、设置行、播放控制条
已内置），未标注的位置只有图标名粒度。

**「能写哪些键」查槽位表**：市场仓根目录的 [SLOTS.md](SLOTS.md)（机器版 `slots.json`）
由 DaoBox 源码机械派生、随引擎版本更新——**图标名白名单**（在用的 Material 名 + 调用点
计数）、**位置槽位清单**（`tab.home`、`tab.live`…）、**预留语义键**。写了表里没有的名字
不会报错，但不生效。

**值不只是 M3 图标——五种取值语法**：

| 语法 | 示例 | 说明 |
|---|---|---|
| 裸 M3 名 | `"east"` | Material Symbols 字体 glyph |
| `skin:` | `"skin:icons/x.webp"` | 皮肤包内图片（裸相对路径 = `skin:` 简写） |
| `assets://` | `"assets://images/logo.webp"` | App 内置资源图（壳子既有协议；裸 `assets/...` 不用于皮肤语法） |
| `file://` | `"file:///storage/.../x.png"` | 本机图片（≤200KB，平台访问权限照常约束） |
| `http(s)://` | `"https://cdn.example.com/x.webp"` | 网络图片（≤200KB、5s 超时、磁盘缓存） |

图片统一走 tint 染色（auto = 随语义色染色）；任何加载失败（名字不存在/文件缺失/断网/超限）
一律回落默认图标，**绝不阻塞页面**——所以放手用网络图，挂了也只是图标回到默认。

其余规则：
- `map` 的值不符合上述语法（如 `ftp://`、裸绝对路径）→ 该键回落默认，不拒包；
- `tint: "auto"`（推荐）：图片按单色处理、随语义色染色——**一张图自动适配明暗**；`tint: "color"` 原色渲染则必须明暗各一张；
- 图片规格：48×48 或 96×96（2x）、webp/png、包内单张 ≤20KB、合计 ≤500KB；file/http 单张 ≤200KB；
- `file://`/`http(s)://` 只能出现在 `map`/`images` 的**值**里；皮肤包内引用外部资源不计入整包限额，但作者应优先 `skin:` 自带（离线可用、渲染零延迟）。

### 2.8 type / surface / motion

```json
"type":    { "family": "system", "scale": 1.0, "weightBias": 0 },
"surface": { "background": { "light": "bg/home_light.webp", "dark": "bg/home_dark.webp" },
             "backgroundDim": 0.35, "backgroundBlur": true, "scrimBlend": true },
"motion":  { "curve": "expressive", "durationScale": 1.0 }
```

- `type.family`：`system` 或包内字体名（`font/` 下的文件）；**官方市场不收带字体的皮肤**（授权风险），三方市场与本地导入随便用；
- 背景：明暗各一张（单域皮肤可以只给一张）；`backgroundDim` 压暗保可读（0–0.6）；`backgroundBlur` 走 App 既有的整层模糊通道；
- `motion.curve`：`standard` / `expressive`（弹簧感）/ `snappy`。

## 三、资产规格速查

| 资产 | 格式 | 尺寸 | 限额 |
|---|---|---|---|
| 背景图 | webp | ≤ 2× 屏幕分辨率 | 单张 ≤300KB |
| 图标 | webp/png | 48×48 或 96×96 | 单张 ≤20KB，合计 ≤500KB |
| 字体 | ttf/otf | — | ≤5MB |
| 预览图 | webp | 750×520 | ≤120KB |
| 整包 | — | — | ≤8MB |

## 四、本地测试清单（发布前全过一遍）

1. **导入校验**：App 导入 `.dsz`——schema/限额/越权字段/对比度任何一条不过都会拒载并给出原因；
2. **双域目检**：亮色/暗色各切一遍主要页面（首页/详情/设置/弹层），确认没有「亮域好看暗域翻车」；**单域皮肤**（`mode: light|dark`）确认另一域回落默认色板后仍协调；
3. **渐变可读性**：白字放渐变最亮和最暗两端看是否糊；
4. **图标抽查**：每个自定义槽位两域都看一眼（tint:auto 应自动变色）；
5. **comp 槽位**：单独改过的组件（如只有横幅霓虹）在两域各看一眼，确认没有引用到旧值；
6. **预览图**：截一张首页亮色域当 preview。

## 五、上架与分发

### 5.1 官方市场（免费/Pro）

官方市场 = 一个静态托管的索引仓库（GitHub）。上架流程：

1. 皮肤在本地导入测试通过；
2. 向官方仓库提 PR：`skins/<id>-<version>.dsz` + `previews/<id>.webp` + 索引条目（id/name/author/desc/version/url/size/md5/tags/changelog）；
3. 审核点只有三条：校验器全绿、双域 AA 通过、描述与实际相符（**不审审美**——市场只保证能装、能读，不保证好看）；
4. 免费/Pro 由官方标记 `pro` 字段（Pro = 皮肤会员可装）；**官方市场不收带字体的皮肤**。

### 5.2 自建三方市场（任何人 5 分钟）

三方市场 = 一个 `skin-market.json` + 一堆 `.dsz` 文件，任何静态托管都行（GitHub Pages / 对象存储 / 你的服务器）：

1. 建仓，放入 `skin-market.json` 与皮肤包：

```json
{
  "name": "极客社区皮肤市场",
  "desc": "社区自制皮肤",
  "updatedAt": "2026-10-28",
  "skins": [
    { "id": "com.geek.cyber-sunset", "name": "赛博落日", "author": "@geek",
      "desc": "橙紫渐变 + 霓虹描边", "version": "1.0.0",
      "url": "skins/cyber-sunset-1.0.0.dsz", "size": 240112,
      "md5": "…", "minEngine": 1, "tags": ["渐变", "赛博"] }
  ]
}
```

2. 开 GitHub Pages（仓库 Settings → Pages → main 分支）；
3. 把 `https://<你>.github.io/<仓>/skin-market.json` 发给用户；
4. 用户在 App：皮肤 → 皮肤市场 → 添加市场 → 粘贴 URL → 浏览安装。

`url` 用相对路径（如上）——仓库整体换域名零改动。`md5` 强烈建议填（客户端下载后强制校验）。`delisted: true` = 下架但保留条目（已装用户不受影响）。三方市场条目**没有 Pro 语义**，全部免费安装，但仍过同一道校验闸门。

## 六、AI 协作指南（异想天开主通道）

### 6.1 生成 skin.json 的提示词模板（直接复制改描述）

```
你是 DaoBox 皮肤设计师。DaoBox 的皮肤是一份 JSON 声明（不含代码）。
请为我设计一套皮肤，主题：<这里写你的异想天开，越具体越好，
例如「午夜太空站：深蓝黑底、舷窗玻璃卡片、青色霓虹描边、
图标用细线风格、底栏悬浮胶囊、按钮从深青渐变到亮青」>。

要求：
1. 只输出一个 JSON 对象，字段范围与写法严格如下（不要发明字段）：
meta 必填 id/name/version(语义化如"1.0.0")/minEngine:4/mode(both|light|dark)
color.strategy 用 seed，给 light 与 dark 两个种子色（dark 种子是给黑底用的，要亮）
shape: card(0-28)/chip(0-16)/sheet(0-32)/button(pill|rounded|square)/navBar(floating|attached)
material: card(fill|glass|outline|gradient)/cardOpacity/cardBorder/cardHighlight/elevation(none|low|mid|high)
comp: 可选 banner/navBar/searchBar 槽位覆盖
gradient: 可选 primary/card/banner/navBar/chipOn，{type:"linear",angle,stops:2-4个hex}，
  只用于面；确保白色文字在渐变最亮最暗两端都清晰可读
icons: 可选 map（Material Symbols 图标名）
type/surface/motion 可省略
2. 亮色暗色两版都要好看（给两个种子色时注意暗域用亮色调）；
3. id 用 com.<你的名字>.<皮肤名>。
```

拿到 JSON 后：存成 `skin.json` → 按 §一·路径 A 第 4 步导入验证；**报错原文贴回给 AI**（校验器的报错都是人类可读的），两三轮就能收敛。

### 6.2 生成图标

提示词：`生成 5 个 96×96 的单色 SVG 图标（首页/AI/实验室/我的/返回），风格：<描述>，viewBox 24，只用 currentColor`。SVG 转 webp：任何在线转换器或 `magick icon.svg -resize 96x96 icon.webp`。

### 6.3 生成背景

提示词：`生成一张手机竖屏壁纸，<描述>，主体避开上 1/4 与下 1/4（被状态栏和底栏遮挡），整体偏暗以便白字可读`。导出 webp 压到 300KB 内。

### 6.4 AI 常见翻车点（提前打预防针）

- **发明字段**：模型偶尔加 `shadow`、`radius` 之类不存在的字段——校验器按白名单丢弃并告警，让 AI 严格按模板字段输出；
- **暗域种子太暗**：暗色域种子应该选**亮一点的颜色**（暗底上的主色），告诉 AI「dark 种子是在黑底上用的，要亮」；
- **渐变文字**：模板已限制渐变只进面，如果它给 `onPrimary` 塞渐变，删掉即可；
- **图标名编造**：Material Symbols 名字让它「不确定就删掉该行」，回落默认不丢人。

## 七、校验规则速查（会被拒载的全部条件）

| 条件 | 后果 |
|---|---|
| 出现 `action` / `route` / `feat` / `script` / `url`(顶层) 等越权字段 | **整包拒载**（皮肤是视觉数据，红线 14） |
| `meta.id` 缺失 / `minEngine` > 宿主版本 | 拒载，提示升级或修包 |
| override 色表角色缺失 / 明暗不成对 / AA 不达标 | 拒载回落默认皮肤 |
| 渐变 on 色对极端 stop 不过 AA | 该槽位回落单色并告警 |
| 资产超限（§三表）/ 图片路径含 `http`、`file`、绝对路径 | 拒载 |
| 图标名不在 M3 字体清单 | 该槽位回落默认图标 |
| `md5` 与市场声明不符 | 拒装（市场下载链路） |
| `meta.minEngine` 高于宿主引擎 | 拒载，提示升级 App（市场列表则直接置灰安装按钮） |

记住一个原则：**校验器是你的朋友**——所有报错都写得人话，AI 也能读懂。拒载信息 + 原因贴回给 AI，就是最快的迭代循环。
