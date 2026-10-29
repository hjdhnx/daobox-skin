# 皮肤图标槽位表

> 由 DaoBox 源码机械派生（`tools/export_skin_slots.py`），**勿手改**。更新：2026-10-30 · 引擎版本 4。

图标名键（不含点号）写 iconNames 里的名字；位置槽位键（含点号）写 slots 里的 slot。值除 M3 名外可用图片 scheme（见 valueSchemes）；加载失败一律回落默认。源码约定（红线 41）：图标只允许 icon('名') 调用与 icon: '名' 数据字段两种形态，本表由两种形态机械派生，出现第三种形态导出即失败。

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

共 190 个在用图标（`icon(…)` 调用 + `icon: …` 数据字段两种形态合计）。值 = M3 名或下方任一图片 scheme。

| 图标 | 出现次数 |
|---|---|
| `search` | 26 |
| `chevron_right` | 15 |
| `arrow_back` | 14 |
| `download` | 12 |
| `grid_view` | 11 |
| `close` | 11 |
| `travel_explore` | 11 |
| `cloud_off` | 10 |
| `refresh` | 10 |
| `check` | 10 |
| `dns` | 10 |
| `content_copy` | 10 |
| `auto_awesome` | 9 |
| `radar` | 9 |
| `bolt` | 9 |
| `delete_outline` | 9 |
| `error_outline` | 8 |
| `delete_sweep` | 8 |
| `history` | 8 |
| `extension` | 8 |
| `movie` | 7 |
| `live_tv` | 7 |
| `menu_book` | 7 |
| `settings` | 7 |
| `expand_more` | 7 |
| `music_note` | 7 |
| `image` | 7 |
| `repeat` | 7 |
| `search_off` | 7 |
| `edit` | 7 |
| `link` | 7 |
| `tune` | 7 |
| `play_arrow` | 6 |
| `public` | 6 |
| `info` | 6 |
| `more_vert` | 6 |
| `tab` | 6 |
| `folder_open` | 5 |
| `folder` | 5 |
| `add` | 5 |
| `restart_alt` | 5 |
| `movie_filter` | 4 |
| `hourglass_empty` | 4 |
| `bookmark` | 4 |
| `arrow_forward` | 4 |
| `memory` | 4 |
| `workspace_premium` | 4 |
| `sort` | 3 |
| `filter_alt` | 3 |
| `photo_size_select_large` | 3 |
| `crop_landscape` | 3 |
| `view_stream` | 3 |
| `view_agenda` | 3 |
| `view_column` | 3 |
| `play_circle` | 3 |
| `subtitles` | 3 |
| `share` | 3 |
| `bug_report` | 3 |
| `cleaning_services` | 3 |
| `cast` | 3 |
| `description` | 3 |
| `list` | 3 |
| `code` | 3 |
| `terminal` | 3 |
| `data_object` | 3 |
| `tv` | 3 |
| `auto_stories` | 3 |
| `check_circle` | 3 |
| `shield` | 3 |
| `newspaper` | 3 |
| `palette` | 3 |
| `science` | 2 |
| `more_horiz` | 2 |
| `arrow_upward` | 2 |
| `inventory_2` | 2 |
| `repeat_on` | 2 |
| `repeat_one` | 2 |
| `lock_outline` | 2 |
| `subject` | 2 |
| `child_care` | 2 |
| `speed` | 2 |
| `qr_code_2` | 2 |
| `warning` | 2 |
| `folder_zip` | 2 |
| `bookmark_border` | 2 |
| `north_east` | 2 |
| `keyboard_arrow_down` | 2 |
| `radio_button_checked` | 2 |
| `swap_horiz` | 2 |
| `playlist_remove` | 2 |
| `fast_forward` | 2 |
| `text_fields` | 2 |
| `chat_bubble_outline` | 2 |
| `high_quality` | 2 |
| `bedtime` | 2 |
| `flip` | 2 |
| `star` | 2 |
| `schedule` | 2 |
| `tag` | 2 |
| `lock` | 2 |
| `verified_user` | 2 |
| `favorite_border` | 2 |
| `gavel` | 2 |
| `storage` | 2 |
| `block` | 2 |
| `data_usage` | 2 |
| `logout` | 2 |
| `home` | 1 |
| `person` | 1 |
| `swap_vert` | 1 |
| `view_list` | 1 |
| `photo_library` | 1 |
| `reorder` | 1 |
| `pause` | 1 |
| `theaters` | 1 |
| `list_alt` | 1 |
| `settings_outlined` | 1 |
| `stop` | 1 |
| `verified` | 1 |
| `dangerous` | 1 |
| `plagiarism` | 1 |
| `warning_amber` | 1 |
| `add_circle_outline` | 1 |
| `bookmarks` | 1 |
| `find_in_page` | 1 |
| `fullscreen` | 1 |
| `keyboard_arrow_up` | 1 |
| `cast_connected` | 1 |
| `alt_route` | 1 |
| `checklist` | 1 |
| `radio_button_unchecked` | 1 |
| `subtitles_off` | 1 |
| `power_settings_new` | 1 |
| `link_off` | 1 |
| `volume_up` | 1 |
| `aspect_ratio` | 1 |
| `filter_alt_off` | 1 |
| `note_add` | 1 |
| `create_new_folder` | 1 |
| `folder_off` | 1 |
| `code_off` | 1 |
| `menu` | 1 |
| `save_outlined` | 1 |
| `drive_file_rename_outline` | 1 |
| `cloud_outlined` | 1 |
| `timeline` | 1 |
| `category` | 1 |
| `language` | 1 |
| `favorite` | 1 |
| `cloud_upload` | 1 |
| `push_pin` | 1 |
| `folder_special` | 1 |
| `skip_previous` | 1 |
| `skip_next` | 1 |
| `queue_music` | 1 |
| `account_balance_wallet` | 1 |
| `info_outline` | 1 |
| `shopping_cart` | 1 |
| `cloud_sync` | 1 |
| `apps` | 1 |
| `phone_iphone` | 1 |
| `content_paste_go` | 1 |
| `crop` | 1 |
| `download_for_offline` | 1 |
| `save_alt` | 1 |
| `format_bold` | 1 |
| `percent` | 1 |
| `battery_full` | 1 |
| `lightbulb` | 1 |
| `vertical_align_bottom` | 1 |
| `clear_all` | 1 |
| `label_outline` | 1 |
| `local_fire_department` | 1 |
| `sports_soccer` | 1 |
| `animation` | 1 |
| `network_check` | 1 |
| `storefront` | 1 |
| `send` | 1 |
| `dashboard_customize` | 1 |
| `verified_user_outlined` | 1 |
| `playlist_add_check` | 1 |
| `restore` | 1 |
| `library_music` | 1 |
| `upload_file` | 1 |
| `pie_chart` | 1 |
| `select_all` | 1 |
| `rule` | 1 |
| `health_and_safety` | 1 |
| `fullscreen_exit` | 1 |
| `open_in_new` | 1 |

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
