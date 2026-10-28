# 皮肤图标槽位表

> 由 DaoBox 源码机械派生（`tools/export_skin_slots.py`），**勿手改**。更新：2026-10-28 · 引擎版本 4。

图标名键（不含点号）写 iconNames 里的名字；位置槽位键（含点号）写 slots 里的 slot。值除 M3 名外可用图片 scheme（见 valueSchemes）；加载失败一律回落默认。

## 位置槽位（键含 `.`，换 A 留 B）

| 槽位 | 默认图标 | 说明 |
|---|---|---|
| `tab.agent` | `auto_awesome` | 底栏「AI」tab（TABS 派生） |
| `tab.home` | `home` | 底栏「首页」tab（TABS 派生） |
| `tab.lab` | `science` | 底栏「实验室」tab（TABS 派生） |
| `tab.live` | `live_tv` | 底栏「电视」tab（TABS 派生） |
| `tab.more` | `more_horiz` | 底栏「更多」tab（TABS 派生） |
| `tab.profile` | `person` | 底栏「我的」tab（TABS 派生） |
| `tab.search` | `search` | 底栏「搜索」tab（TABS 派生） |
| `tab.shelf` | `menu_book` | 底栏「书架」tab（TABS 派生） |
| `tab.vod` | `movie` | 底栏「点播」tab（TABS 派生） |

## 图标名白名单（键不含 `.`，同名全换）

共 121 个在用图标。值 = M3 名或下方任一图片 scheme。

| 图标 | 调用点 |
|---|---|
| `chevron_right` | 14 |
| `arrow_back` | 11 |
| `refresh` | 8 |
| `search` | 8 |
| `grid_view` | 7 |
| `expand_more` | 7 |
| `delete_outline` | 7 |
| `check` | 7 |
| `image` | 6 |
| `bolt` | 6 |
| `link` | 6 |
| `radar` | 6 |
| `play_arrow` | 5 |
| `download` | 5 |
| `restart_alt` | 5 |
| `tune` | 5 |
| `cloud_off` | 4 |
| `settings` | 4 |
| `close` | 4 |
| `add` | 4 |
| `content_copy` | 4 |
| `memory` | 4 |
| `more_vert` | 4 |
| `edit` | 4 |
| `sort` | 3 |
| `folder_open` | 3 |
| `inventory_2` | 3 |
| `movie` | 3 |
| `filter_alt` | 3 |
| `music_note` | 3 |
| `dns` | 3 |
| `auto_awesome` | 3 |
| `travel_explore` | 3 |
| `public` | 3 |
| `menu_book` | 3 |
| `list` | 3 |
| `tv` | 3 |
| `arrow_upward` | 2 |
| `lock_outline` | 2 |
| `qr_code_2` | 2 |
| `folder_zip` | 2 |
| `bookmark` | 2 |
| `history` | 2 |
| `north_east` | 2 |
| `arrow_forward` | 2 |
| `tab` | 2 |
| `cast` | 2 |
| `repeat` | 2 |
| `fast_forward` | 2 |
| `subtitles` | 2 |
| `description` | 2 |
| `text_fields` | 2 |
| `high_quality` | 2 |
| `bedtime` | 2 |
| `flip` | 2 |
| `workspace_premium` | 2 |
| `check_circle` | 2 |
| `extension` | 2 |
| `block` | 2 |
| `error_outline` | 2 |
| `delete_sweep` | 2 |
| `swap_vert` | 1 |
| `movie_filter` | 1 |
| `warning_amber` | 1 |
| `warning` | 1 |
| `bookmark_border` | 1 |
| `cast_connected` | 1 |
| `swap_horiz` | 1 |
| `more_horiz` | 1 |
| `alt_route` | 1 |
| `checklist` | 1 |
| `radio_button_unchecked` | 1 |
| `subtitles_off` | 1 |
| `power_settings_new` | 1 |
| `search_off` | 1 |
| `volume_up` | 1 |
| `aspect_ratio` | 1 |
| `chat_bubble_outline` | 1 |
| `playlist_add` | 1 |
| `menu` | 1 |
| `star` | 1 |
| `favorite` | 1 |
| `timeline` | 1 |
| `favorite_border` | 1 |
| `info` | 1 |
| `folder_special` | 1 |
| `skip_previous` | 1 |
| `skip_next` | 1 |
| `account_balance_wallet` | 1 |
| `info_outline` | 1 |
| `code` | 1 |
| `shopping_cart` | 1 |
| `palette` | 1 |
| `apps` | 1 |
| `content_paste_go` | 1 |
| `crop` | 1 |
| `download_for_offline` | 1 |
| `save_alt` | 1 |
| `auto_stories` | 1 |
| `format_bold` | 1 |
| `schedule` | 1 |
| `percent` | 1 |
| `battery_full` | 1 |
| `lightbulb` | 1 |
| `vertical_align_bottom` | 1 |
| `network_check` | 1 |
| `dashboard_customize` | 1 |
| `verified_user_outlined` | 1 |
| `playlist_add_check` | 1 |
| `folder` | 1 |
| `data_usage` | 1 |
| `restore` | 1 |
| `upload_file` | 1 |
| `pie_chart` | 1 |
| `select_all` | 1 |
| `hourglass_empty` | 1 |
| `rule` | 1 |
| `verified_user` | 1 |
| `health_and_safety` | 1 |
| `data_object` | 1 |
| `fullscreen_exit` | 1 |

## 图片取值 scheme

| scheme | 示例 | 说明 |
|---|---|---|
| `(裸 M3 名)` | `east` | Material Symbols 字体 glyph |
| `skin:` | `skin:icons/x.webp` | 皮肤包内图片（裸相对路径视为 skin: 简写） |
| `assets://` | `assets://images/logo.webp` | App 内置 assets 资源图（壳子既有协议；裸 assets/ 路径不用于皮肤语法） |
| `file://` | `file:///storage/emulated/0/Pictures/x.png` | 本机图片（平台访问权限照常约束） |
| `http(s)://` | `https://cdn.example.com/x.webp` | 网络图片（≤200KB、5s 超时、磁盘缓存、失败回落默认） |

## 预留语义键（页面落键后生效，暂不可用）

| 语义键 | 默认 Material 名 |
|---|---|
| `home` | `home` |
| `movie` | `movie` |
| `live` | `live_tv` |
| `shelf` | `menu_book` |
| `search` | `search` |
| `agent` | `auto_awesome` |
| `lab` | `science` |
| `profile` | `person` |
| `more` | `more_horiz` |
| `back` | `arrow_back` |
| `forward` | `arrow_forward` |
| `close` | `close` |
| `menu` | `menu` |
| `refresh` | `refresh` |
| `settings` | `settings` |
| `play` | `play_arrow` |
| `pause` | `pause` |
| `favorite` | `favorite` |
| `favoriteOff` | `favorite_border` |
| `history` | `history` |
| `download` | `download` |
| `folder` | `folder` |
| `chevronRight` | `chevron_right` |
| `chevronDown` | `expand_more` |
| `check` | `check` |
| `add` | `add` |
| `delete` | `delete` |
| `edit` | `edit` |
| `moreVert` | `more_vert` |
| `filter` | `filter_alt` |
| `sort` | `sort` |
| `grid` | `grid_view` |
| `list` | `view_list` |
| `music` | `music_note` |
| `book` | `auto_stories` |
| `plugin` | `extension` |
| `backup` | `cloud_upload` |
| `lock` | `lock` |
| `qr` | `qr_code_2` |
| `tv` | `tv` |
| `cast` | `cast` |
| `volume` | `volume_up` |
| `fullscreen` | `fullscreen` |
| `light` | `light_mode` |
| `dark` | `dark_mode` |
| `auto` | `brightness_auto` |
| `info` | `info` |
