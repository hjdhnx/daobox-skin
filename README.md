# daobox-skin — DaBox 官方皮肤市场

DaBox 的**内置官方皮肤市场**：一个静态托管的 `skin-market.json` 索引 + 皮肤包（`.dsz`）。
客户端（DaoBox）预置本市场地址，用户也可在 App 内添加任意三方市场（协议相同）。

**市场索引直链**（GitHub Pages 开启后）：

```
https://hjdhnx.github.io/daobox-skin/skin-market.json
```

## 当前货架

| 皮肤 | 域 | 形态要点 | 权益 |
|---|---|---|---|
| 极光玻璃 aurora-glass | 双域 | 玻璃卡 · 悬浮胶囊底栏 · 冷色 | Pro |
| 墨石直角 ink-stone | 双域 | 直角描边 · 编辑风 | 免费 |
| 奶油果冻 cream-jelly | 双域 | 大圆角 · 奶油渐变卡 | Pro |
| 霓虹机甲 neon-mech | 双域 | 全局扁平 · 仅横幅霓虹（组件槽位演示） | Pro |
| 苔原绿 moss | 仅亮色 | 苔绿圆润 | 免费 |
| 暗夜紫 nightscape | 仅暗色 | 深紫玻璃 | 免费 |

> **M3 基线不是皮肤**——它是「未应用任何皮肤」时的默认形态，因此不在市场上架。
> 所以上架皮肤全部为纯 token 包（不含背景图/字体资产），`minEngine: 4`。

## 仓库结构

```
skin-market.json     市场索引（客户端拉取这一个文件；url 均为相对路径，仓库整体迁移零改动）
skins/*.dsz          皮肤包（zip：skin.json；发布后不可改名——md5 与索引绑定）
previews/*.webp      预览图 750×520（App 商店页展示用，不进运行时内存）
SLOTS.md / slots.json 图标槽位表（可自定义的图标键白名单 + 位置槽位，由源码机械派生）
AUTHORING.md         皮肤制作指南（公开镜像）
prototype.html       交互原型（五套皮肤，浏览器直接打开）
tools/build_market.py 构建脚本：定义 → .dsz + md5 + 索引 一条命令
```

## 上架新皮肤

1. 按 **[AUTHORING.md](AUTHORING.md)**（本仓制作指南，含 AI 提示词模板）制作并通过本地导入测试；想先玩玩看 → [prototype.html](prototype.html)（五套皮肤交互原型）；
2. 在 `tools/build_market.py` 的 `SKINS` 里加定义，`previews/` 放一张 `预览.webp`；
3. `python tools/build_market.py` → 提交 PR；
4. 审核三条：校验器全绿、双域 AA 对比度通过、描述与实际相符（**不审审美**）。

## 字段语义速查

`md5` 下载后强制校验，不符拒装；`pro` 仅对官方市场有意义（皮肤会员 `ui.skin.*` 可装）；
`delisted: true` 下架不删条目（已装用户不受影响）；`minEngine` 低于宿主则安装按钮置灰。
完整协议见 DaoBox 仓库 `docs/SKIN-SYSTEM-DESIGN.md` §七。
