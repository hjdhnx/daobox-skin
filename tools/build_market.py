#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DaBox 官方皮肤市场 · 构建脚本

用法：python tools/build_market.py
做什么：把 SKINS 里的皮肤定义逐个打包成 skins/<id>-<version>.dsz（zip），
       计算 md5/size，扫描 previews/，生成 skin-market.json 索引。

上架新皮肤：在 SKINS 里加一个定义 → 放一张 previews/<id>.webp → 跑本脚本 → 提交。
制作指南见本仓 AUTHORING.md；字段语义速查见本仓 README。
"""
import hashlib
import json
import os
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKINS_DIR = os.path.join(ROOT, 'skins')
PREVIEWS_DIR = os.path.join(ROOT, 'previews')

def skin(meta, color, shape, material=None, comp=None, gradient=None, icons=None,
         type_=None, surface=None, motion=None):
    """组装 skin.json（只收白名单段，与引擎 schema 一一对应）。"""
    doc = {'meta': meta, 'color': color, 'shape': shape}
    for key, val in (('material', material), ('comp', comp), ('gradient', gradient),
                     ('icons', icons), ('type', type_), ('surface', surface), ('motion', motion)):
        if val:
            doc[key] = val
    return doc

def m(meta_id, name, mode, version='1.0.0', author='DaoBox 官方', desc=''):
    return {'id': m_id(meta_id), 'name': name, 'version': version, 'minEngine': 4,
            'mode': mode, 'author': author, 'description': desc}

def m_id(short):
    return 'dao.skin.' + short

# ── 皮肤定义（上架清单）──────────────────────────────────────────────
# 口径：M3 基线不是皮肤，是「未应用任何皮肤」的默认形态，因此不在本市场。
SKINS = [
    # 口径：M3 基线不是皮肤，是「未应用任何皮肤」的默认形态，因此不在本市场。
    # 每款尽量吃满引擎可定制的面（背景图/字体/图标除外）：
    #   颜色 seed · 圆角 shape · 材质 material+elevation · 五个渐变面 · comp 槽位
    dict(entry=dict(id=m_id('aurora-glass'), name='极光玻璃', author='DaoBox 官方',
                    desc='冷蓝玻璃 + 悬浮胶囊底栏：卡片半透明描边，横幅/底栏/选中态极光渐变',
                    version='1.2.0', pro=True, tags=['玻璃', '悬浮底栏', '渐变'],
                    changelog='补齐横幅/主按钮渐变与列表槽位'),
         doc=skin(m('aurora-glass', '极光玻璃', 'both', version='1.2.0',
                    desc='冷蓝玻璃 + 极光渐变横幅/底栏/选中态'),
                  color={'strategy': 'seed',
                         'seed': {'light': '#3B6FD4', 'dark': '#8AB4F8'}, 'neutralBias': 'cool'},
                  shape={'card': 20, 'chip': 12, 'sheet': 28, 'button': 'pill', 'navBar': 'floating'},
                  material={'card': 'glass', 'cardOpacity': 0.55, 'cardBorder': 1,
                            'cardHighlight': True, 'gradientAngle': 135, 'elevation': 'mid'},
                  comp={'banner': {'material': 'gradient', 'gradientAngle': 135,
                                   'border': 'rgba(138,180,248,.45)'},
                        'listItem': {'cardOpacity': 0.40, 'cardBorder': 1}},
                  gradient={
                      'banner': {'type': 'linear', 'angle': 135,
                                 'stops': ['#0B2A5B', '#1E4FA8', '#5B8DEF']},
                      'primary': {'type': 'linear', 'angle': 135,
                                  'stops': ['#3B6FD4', '#6D8FF5']},
                      'chipOn': {'type': 'linear', 'angle': 135,
                                 'stops': ['#3B6FD4', '#7C9CF5']},
                      'navBar': {'type': 'linear', 'angle': 0,
                                 'stops': ['#274A91', '#3B6FD4']},
                  },
                  motion={'curve': 'expressive'})),

    dict(entry=dict(id=m_id('ink-slab'), name='墨石直角', author='DaoBox 官方',
                    desc='纸墨编辑风：全直角描边卡 + 墨色横幅，克制的单色体系',
                    version='1.1.0', pro=False, tags=['直角', '描边', '高对比'],
                    changelog='补齐横幅/选中态墨色渐变'),
         doc=skin(m('ink-slab', '墨石直角', 'both', version='1.1.0',
                    desc='纸墨高对比 · 直角描边卡片'),
                  color={'strategy': 'seed', 'seed': {'light': '#17181A', 'dark': '#E8E4DF'}},
                  shape={'card': 0, 'chip': 0, 'sheet': 0, 'button': 'square', 'navBar': 'attached'},
                  material={'card': 'outline', 'cardBorder': 1, 'elevation': 'low'},
                  comp={'listItem': {'cardBorder': 1},
                        'banner': {'material': 'gradient', 'gradientAngle': 180,
                                   'border': 'rgba(23,24,26,.35)'}},
                  gradient={
                      'banner': {'type': 'linear', 'angle': 180,
                                 'stops': ['#1C1B1D', '#3A3A3E']},
                      'chipOn': {'type': 'linear', 'angle': 135,
                                 'stops': ['#3F3F46', '#18181B']},
                      'navBar': {'type': 'linear', 'angle': 0,
                                 'stops': ['#F7F4EE', '#E6E0D5']},
                  },
                  type_={'family': 'system', 'weightBias': 1})),

    dict(entry=dict(id=m_id('cream-jelly'), name='奶油果冻', author='DaoBox 官方',
                    desc='大圆角奶油渐变：卡片/主按钮/底栏/选中态全套奶油色，Expressive 弹性',
                    version='1.2.0', pro=True, tags=['渐变', '大圆角', '暖色'],
                    changelog='补齐横幅/底栏渐变与列表槽位'),
         doc=skin(m('cream-jelly', '奶油果冻', 'both', version='1.2.0',
                    desc='大圆角 · 奶油渐变卡与底栏'),
                  color={'strategy': 'seed', 'seed': {'light': '#E0568C', 'dark': '#FF8FB4'}},
                  shape={'card': 28, 'chip': 16, 'sheet': 32, 'button': 'pill', 'navBar': 'floating'},
                  material={'card': 'gradient', 'elevation': 'low', 'gradientAngle': 135},
                  comp={'banner': {'material': 'gradient', 'gradientAngle': 120,
                                   'border': 'rgba(255,143,180,.5)'},
                        'listItem': {'cardOpacity': 0.7}},
                  gradient={
                      'card': {'type': 'linear', 'angle': 135,
                               'stops': ['#FFDDE8', '#FFC9B8']},
                      'banner': {'type': 'linear', 'angle': 120,
                                 'stops': ['#F9A8C9', '#FFB88C', '#FFD1A9']},
                      'primary': {'type': 'linear', 'angle': 135,
                                  'stops': ['#E0568C', '#FF8FB4']},
                      'chipOn': {'type': 'linear', 'angle': 135,
                                 'stops': ['#F07AA8', '#FFB3C9']},
                      'navBar': {'type': 'linear', 'angle': 0,
                                 'stops': ['#FBE4EE', '#FFD9C7']},
                  },
                  motion={'curve': 'expressive'})),

    dict(entry=dict(id=m_id('neon-mech'), name='霓虹机甲', author='DaoBox 官方',
                    desc='全局扁平卡 + 横幅/底栏/主按钮/选中态霓虹渐变（青→紫）',
                    version='1.2.0', pro=True, tags=['组件槽位', '霓虹', '深色'],
                    changelog='补齐列表槽位与横幅描边'),
         doc=skin(m('neon-mech', '霓虹机甲', 'both', version='1.2.0',
                    desc='全局扁平卡 + 霓虹渐变横幅/底栏/主按钮'),
                  color={'strategy': 'seed', 'seed': {'light': '#0891B2', 'dark': '#22D3EE'}},
                  shape={'card': 16, 'chip': 10, 'sheet': 24, 'button': 'rounded', 'navBar': 'attached'},
                  material={'card': 'fill', 'elevation': 'low'},
                  comp={'banner': {'material': 'gradient', 'gradientAngle': 120,
                                   'border': 'rgba(34,211,238,.45)'},
                        'listItem': {'cardBorder': 1,
                                     'border': 'rgba(34,211,238,.35)'}},
                  gradient={
                      'banner': {'type': 'linear', 'angle': 120,
                                 'stops': ['#0E7490', '#9333EA']},
                      'navBar': {'type': 'linear', 'angle': 0,
                                 'stops': ['#0B5E75', '#5B21B6']},
                      'primary': {'type': 'linear', 'angle': 135,
                                  'stops': ['#0891B2', '#7C3AED']},
                      'chipOn': {'type': 'linear', 'angle': 135,
                                 'stops': ['#0E7490', '#7C3AED']},
                  })),

    dict(entry=dict(id=m_id('moss'), name='苔原绿', author='DaoBox 官方',
                    desc='低饱和苔绿 · 圆润悬浮底栏，森系渐变横幅（仅亮色域）',
                    version='1.1.0', pro=False, tags=['自然', '单域', '渐变'],
                    changelog='补齐横幅/底栏/主按钮渐变'),
         doc=skin(m('moss', '苔原绿', 'light', version='1.1.0',
                    desc='低饱和苔绿 · 森系渐变'),
                  color={'strategy': 'seed', 'seed': {'light': '#2E7D5B'}},
                  shape={'card': 22, 'chip': 14, 'sheet': 30, 'button': 'pill', 'navBar': 'floating'},
                  material={'card': 'fill', 'elevation': 'low'},
                  comp={'banner': {'material': 'gradient', 'gradientAngle': 135}},
                  gradient={
                      'banner': {'type': 'linear', 'angle': 135,
                                 'stops': ['#0F3D2E', '#2E7D5B', '#A7E8C8']},
                      'primary': {'type': 'linear', 'angle': 135,
                                  'stops': ['#2E7D5B', '#5BB98C']},
                      'chipOn': {'type': 'linear', 'angle': 135,
                                 'stops': ['#2E7D5B', '#7BC9A6']},
                      'navBar': {'type': 'linear', 'angle': 0,
                                 'stops': ['#1F5B42', '#3F9B74']},
                  })),

    dict(entry=dict(id=m_id('nightscape'), name='暗夜紫', author='DaoBox 官方',
                    desc='深紫玻璃 · 贴底通栏，暗色域霓虹紫渐变（仅暗色域）',
                    version='1.1.0', pro=False, tags=['深色', '玻璃', '渐变'],
                    changelog='补齐横幅/底栏/主按钮渐变'),
         doc=skin(m('nightscape', '暗夜紫', 'dark', version='1.1.0',
                    desc='深紫玻璃 · 暗夜紫渐变'),
                  color={'strategy': 'seed', 'seed': {'dark': '#B39DDB'}},
                  shape={'card': 14, 'chip': 10, 'sheet': 20, 'button': 'rounded', 'navBar': 'attached'},
                  material={'card': 'glass', 'cardOpacity': 0.5, 'cardBorder': 1,
                            'cardHighlight': True, 'elevation': 'mid'},
                  comp={'banner': {'material': 'gradient', 'gradientAngle': 120,
                                   'border': 'rgba(179,157,219,.4)'},
                        'listItem': {'cardOpacity': 0.42}},
                  gradient={
                      'banner': {'type': 'linear', 'angle': 120,
                                 'stops': ['#241E33', '#4C1D95', '#9333EA']},
                      'navBar': {'type': 'linear', 'angle': 0,
                                 'stops': ['#1B1230', '#3B2A5A']},
                      'primary': {'type': 'linear', 'angle': 135,
                                  'stops': ['#7C3AED', '#B39DDB']},
                      'chipOn': {'type': 'linear', 'angle': 135,
                                 'stops': ['#4C1D95', '#7C3AED']},
                  })),
]

FORBIDDEN = {'action', 'route', 'feat', 'script', 'url', 'onclick', 'eval'}

def check_forbidden(obj, path=''):
    for k, v in (obj or {}).items():
        if k.lower() in FORBIDDEN:
            raise SystemExit('越权字段 %s%s（红线 14，整包拒载）' % (path, k))
        if isinstance(v, dict):
            check_forbidden(v, path + k + '.')

def main():
    os.makedirs(SKINS_DIR, exist_ok=True)
    index = []
    for item in SKINS:
        entry, doc = item['entry'], item['doc']
        check_forbidden(doc)
        name = '%s-%s.dsz' % (doc['meta']['id'], doc['meta']['version'])
        dest = os.path.join(SKINS_DIR, name)
        with zipfile.ZipFile(dest, 'w', zipfile.ZIP_DEFLATED) as z:
            z.writestr('skin.json', json.dumps(doc, ensure_ascii=False, indent=2) + '\n')
        data = open(dest, 'rb').read()
        row = {
            'id': doc['meta']['id'], 'name': entry['name'], 'author': entry['author'],
            'desc': entry['desc'], 'version': doc['meta']['version'],
            'url': 'skins/' + name, 'size': len(data),
            'md5': hashlib.md5(data).hexdigest(),
            'minEngine': doc['meta']['minEngine'], 'pro': entry['pro'],
            'tags': entry['tags'], 'changelog': entry['changelog'],
        }
        preview = os.path.join(PREVIEWS_DIR, doc['meta']['id'].split('.')[-1] + '.webp')
        if os.path.isfile(preview):
            row['preview'] = 'previews/' + os.path.basename(preview)
        index.append(row)
        print('打包 %s  %6d bytes  md5 %s' % (name, len(data), row['md5']))

    out = os.path.join(ROOT, 'skin-market.json')
    with open(out, 'w', encoding='utf-8', newline='\n') as f:
        json.dump({'name': 'DaBox 官方皮肤市场', 'desc': '官方维护的皮肤分发索引',
                   'updatedAt': __import__('datetime').date.today().isoformat(),
                   'skins': index}, f, ensure_ascii=False, indent=2)
        f.write('\n')
    print('索引 %d 条 → skin-market.json' % len(index))

if __name__ == '__main__':
    main()
