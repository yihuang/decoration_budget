# coding: utf-8
from collections import OrderedDict

sizes = OrderedDict([
    (u'主卧', (3680*3200 + (3680/2)*500) / (1000*1000.0)),
    (u'次卧', 2350*3200  / (1000*1000.0)),
    (u'客厅', (5937*3554) / (1000*1000.0)),
    (u'卫生间', 3537*1800  / (1000*1000.0)),
    (u'厨房', (2350+1800+60)*1500  / (1000*1000.0)),
    (u'阳台', (1840*3800 / (1000*1000.0))),
    (u'墙砖', ((2350+1800+60)*2800 + 3537*2800*2 + 1800*2800*2 + 1840*2800) / (1000*1000.0)),
    (u'墙漆', 120),
])

wall_size = (3200 * 2800) / (1000*1000.0) # 主卧次卧墙面积
#cabinet_size = (3200 * 2800) / (1000*1000.0) # 衣柜面积
cabinet_size = (1840 * 2800) / (1000*1000.0) # 衣柜面积
#cabinet_price = 900
cabinet_price = 720 # 好莱客 团购套餐一
cabinet_door_price = 500

prices = OrderedDict({
    #u'地板': 135,   # 扬子木地板团购价
    u'地板': 108,   # 圣象特价地板
    #u'地板': 400,   # 圣象折扣价
    #u'地砖': 140 * (1000*1000) / (800*800),   # 中档偏上
    u'地砖': 80 * (1000*1000) / (800*800),   # 普通
    #u'墙砖': (10*(1000*1000)/(300*300)),       # 中档偏上
    #u'防滑地砖': (10*(1000*1000)/(300*300)),   # 中档偏上
    u'墙砖': (7*(1000*1000)/(300*300)),        # 普通
    u'防滑地砖': (5*(1000*1000)/(300*300)),    # 普通
    u'找平': 30,
    u'拆墙': 45,
    u'砌墙': 80,
    u'墙面铺砖': 48,
    u'厨房地面铺砖': 48,
    u'刷漆': 12,
    u'腻子': 30,
})

print u'面积'
for k,v in sizes.items():
    print k, v, u'平'
print

majors_totals = OrderedDict([
    #(u'装修公司', 18000),
    (u'卫生间基础工程', 952+840+660),
    #(u'墙面刷漆', prices[u'刷漆'] * sizes[u'墙漆']),
    (u'墙面天花处理', (prices[u'刷漆'] + prices[u'腻子']) * sizes[u'墙漆']),
    (u'地面找平', prices[u'找平'] * (sizes[u'客厅'] + sizes[u'主卧'] + sizes[u'次卧'])),
    (u'厨卫阳台地砖铺设', prices[u'厨房地面铺砖'] * sizes[u'厨房']),
    (u'墙砖铺设', prices[u'墙面铺砖'] * sizes[u'墙砖']),
    (u'各种安装', 2000),
    #(u'拆墙砌墙', wall_size * (prices[u'拆墙'] + prices[u'砌墙'])),

    (u'门（换大门）', 3000+800*3),
    (u'客厅地板', prices[u'地板'] * sizes[u'客厅']),
    #(u'客厅地砖', 80*40),
    (u'房间地板', prices[u'地板'] * (sizes[u'主卧'] + sizes[u'次卧'])),
    (u'厨卫阳台地砖', (sizes[u'卫生间'] + sizes[u'厨房'] + sizes[u'阳台']) * prices[u'防滑地砖']),
    (u'墙砖', sizes[u'墙砖']*prices[u'墙砖']),
    (u'厨卫吊顶', 2180), # 欧斯宝团购方案
    #(u'衣柜', cabinet_size*cabinet_price),
    (u'衣柜', 6982), # 欧派报价
    #(u'欧派橱柜', 10000),   # 团购套餐
    (u'橱柜+厨电', 12000),    # 樱花  团购套餐系列一
    #(u'厨电', 8365.14), # 方太 EH22Q 团购套餐
    #(u'厨电', 7800), # 方太非团购套餐, + 1000消毒碗柜
    (u'卫浴', 5000),
    (u'热水器', 3000),
    #(u'电视/音响', 10000),
    (u'沙发', 4000),
    (u'主卧床', 2000),
    (u'次卧床', 2000),
    #(u'次卧床', 2000),
    (u'床垫', 2000),
    (u'灯具', 2000),
    #(u'空调', 2000),
    (u'封阳台', 5000),
    #(u'餐桌', 2000),
])

print u'总价：'
for k, v in majors_totals.items():
    print k, v
print

print u'合计：', sum(majors_totals.values())

digital = OrderedDict([
    (u'airport extreme', 1200),
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
