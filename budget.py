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

other_sizes = OrderedDict([
    (u'墙砖', ((2970*2+1580+710)*2800 + (3700+2120+1330*2+1340+640)*2800) / (1000*1000.0)),
    (u'刷漆', 139),
    (u'地砖', sizes[u'阳台'] + sizes[u'生活阳台'] + sizes[u'厨房'] + sizes[u'卫生间']),
])

print u'施工面积'
for k,v in other_sizes.items():
    print k, v, u'平'
print

wall_size = (3200 * 2800) / (1000*1000.0) # 主卧次卧墙面积
#cabinet_size = (3200 * 2800) / (1000*1000.0) # 衣柜面积
cabinet_size = (1840 * 2800) / (1000*1000.0) # 衣柜面积
#cabinet_price = 900
cabinet_price = 720 # 好莱客 团购套餐一
cabinet_door_price = 500

prices = OrderedDict({
    #u'地板': 135,   # 扬子木地板团购价
    u'地板': 117,   # 圣象特价地板
    #u'地板': 400,   # 圣象折扣价
    #u'地砖': 140 * (1000*1000) / (800*800),   # 中档偏上
    u'地砖': 80 * (1000*1000) / (800*800),   # 普通
    #u'墙砖': (10*(1000*1000)/(300*300)),       # 中档偏上
    #u'防滑地砖': (10*(1000*1000)/(300*300)),   # 中档偏上
    u'墙砖': (7*(1000*1000)/(300*300)),        # 普通
    u'防滑地砖': (5*(1000*1000)/(300*300)),    # 普通
    u'找平': 35,
    u'拆墙': 45,
    u'砌墙': 80,
    u'墙面铺砖': 58,
    u'厨房地面铺砖': 58,
    u'刷漆': 28,
    u'防水': 42,
})

basic_totals = OrderedDict([
    (u'卫生间基础工程', 3000),
    (u'墙面天花刷漆', prices[u'刷漆'] * other_sizes[u'刷漆']),
    (u'地面找平', prices[u'找平'] * (sizes[u'客厅'] + sizes[u'主卧'] + sizes[u'次卧'])),
    (u'厨卫阳台地砖铺设', prices[u'厨房地面铺砖'] * (sizes[u'厨房'] + sizes[u'阳台'] + sizes[u'卫生间'])),
    (u'防水', prices[u'防水'] * (other_sizes[u'墙砖'] + other_sizes[u'地砖'])),
    (u'墙砖铺设', prices[u'墙面铺砖'] * other_sizes[u'墙砖']),
    (u'水电改造', 7000),
    (u'各种安装', 2000),
    (u'拆墙砌墙', 1000),
])

majors_totals = OrderedDict([
    (u'防盗门', 3000),
    (u'主卧次卧门', 1500*2),
    (u'卫生间门', 1619),
    (u'多乐士套装', 2592),
    (u'地板', 5708.16),
    #(u'客厅地板', prices[u'地板'] * sizes[u'客厅']),
    #(u'房间地板', prices[u'地板'] * (sizes[u'主卧'] + sizes[u'次卧'])),
    (u'厨卫阳台地砖', (sizes[u'卫生间'] + sizes[u'厨房'] + sizes[u'阳台']) * prices[u'防滑地砖']),
    (u'墙砖', other_sizes[u'墙砖']*prices[u'墙砖']),
    (u'厨卫吊顶', 2500),    # 欧斯宝团购方案
    (u'衣柜', 5100),        # 好莱客报价
    (u'橱柜', 10000),       # 皮阿诺
    (u'厨电', 6000),        # 老板
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
