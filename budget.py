# coding: utf-8
from collections import OrderedDict

sizes = OrderedDict([
    (u'主卧', (1900*2900 + 1360*3560) / (1000*1000.0)),
    (u'次卧', 2430*2970  / (1000*1000.0)),
    (u'客厅', (3540*5980) / (1000*1000.0)),
    (u'卫生间', (1580*2970) / (1000*1000.0)),
    (u'厨房', (3700*1340) / (1000*1000.0)),
    (u'生活阳台', (1330*1340) / (1000*1000.0)),
    (u'阳台', (1360*3540 / (1000*1000.0))),
])

print u'面积'
for k,v in sizes.items():
    print k, v, u'平'
print
print u'合计：', sum(sizes.values()), u'平'
print

foot_line_length = 2670*3+3560 +2430+1440 +1900+440+1260 +1560+290*2+340+440 +2360+710+300+3160+300+300+2880

#WATER_KEEP_HEIGHT = 1800 # 防水高度
WATER_KEEP_HEIGHT = 2500 # 防水高度

other_sizes = OrderedDict([
    (u'墙砖', ((2970*2+1580+710)*2500 + (3700+2120+1330*2+1340+640)*2500) / (1000*1000.0)),
    (u'防水', ((2970*2+1580+710)*WATER_KEEP_HEIGHT + (3700+2120+1330*2+1340+640)*WATER_KEEP_HEIGHT) / (1000*1000.0)),
    (u'刷漆', 139),
    (u'地砖', sizes[u'阳台'] + sizes[u'生活阳台'] + sizes[u'厨房'] + sizes[u'卫生间']),
    (u'地板', sizes[u'客厅'] + sizes[u'主卧'] + sizes[u'次卧']),
    (u'踢脚线', foot_line_length / 1000.0),
])

print u'施工面积'
for k,v in other_sizes.items():
    print k, v, u'平'
print

prices = OrderedDict({
    u'地板': 91.8+17,   # 圣象特价地板 + 服务包
    u'墙砖': (14*(1000*1000)/(300*600)),   # 普通
    u'地砖': (14*(1000*1000)/(300*600)),    # 普通
    u'找平': 35,
    u'拆墙': 45,
    u'砌墙': 80,
    u'墙面铺砖': 58,
    u'厨房地面铺砖': 58,
    u'刷漆': 28,
    u'防水': 42,
    u'踢脚线': 25,
})

basic_totals = OrderedDict([
    (u'卫生间基础工程', 3000),
    (u'墙面天花刷漆', prices[u'刷漆'] * other_sizes[u'刷漆']),
    (u'地面找平', prices[u'找平'] * (sizes[u'客厅'] + sizes[u'主卧'] + sizes[u'次卧'])),
    (u'地砖铺设', prices[u'厨房地面铺砖'] * (sizes[u'厨房'] + sizes[u'阳台'] + sizes[u'卫生间'])),
    (u'防水', prices[u'防水'] * (other_sizes[u'防水'] + other_sizes[u'地砖'])),
    (u'墙砖铺设', prices[u'墙面铺砖'] * other_sizes[u'墙砖']),
    (u'水电改造', 7000),
    #(u'各种安装', 2000),
    (u'拆墙砌墙', 300),
])

majors_totals = OrderedDict([
    #(u'防盗门', 3000),
    (u'主卧次卧门', (1605+268)*2),
    (u'卫生间门', 1619+268),
    (u'多乐士两套10L', 1816.00),
    (u'地板', prices[u'地板'] * other_sizes[u'地板']),
    (u'踢脚线', prices[u'踢脚线'] * other_sizes[u'踢脚线']),
    (u'地砖', (sizes[u'卫生间'] + sizes[u'厨房'] + sizes[u'阳台']) * prices[u'地砖']),
    (u'墙砖', other_sizes[u'墙砖']*prices[u'墙砖']),
    (u'厨卫吊顶', 2500),    # 欧斯宝团购方案
    (u'衣柜', 5100),        # 好莱客报价
    (u'橱柜', 10000),       # 皮阿诺
    (u'厨电', 4788 + 450),  # 老板两件套 + 侧吸装饰罩
    (u'卫浴', 5000),
    (u'热水器', 2600),      # 能率
    (u'沙发', 4000),
    (u'主卧床', 2000),
    (u'次卧床', 2000),
    (u'床垫', 2000),
    (u'灯具', 2000),
    (u'空调', 2000),
    (u'封阳台', 5000),
    (u'餐桌', 2000),
    (u'鞋柜', 1000),
])

print u'人工辅料：'
for k, v in basic_totals.items():
    print k, v
print

print u'合计：', sum(basic_totals.values())
print

print u'主材：'
for k, v in majors_totals.items():
    print k, v
print

print u'合计：', sum(majors_totals.values())
print

digital = OrderedDict([
    (u'airport express', 700),
    (u'树莓派', 300),
    (u'电视', 4000),
    (u'音箱', 1000),
    (u'NAS', 1000),
    (u'XBOX', 3500),
])

print u'电子产品：'
for k, v in digital.items():
    print k, v
print

print u'合计：', sum(digital.values())
print

pays = [
    (u'淘宝', u'TATA木门', 4809.00+804.00),
    (u'淘宝', u'多乐士', 1816.00),
    (u'淘宝', u'地板', 3673.92),
    (u'淘宝', u'能率', 2598.00),
]

print u'支出：'
for row in pays:
    print u'【%s】%s %s元' % row
print

print u'合计：', sum(digital.values())
print
