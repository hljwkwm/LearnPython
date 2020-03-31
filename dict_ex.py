# -*-coding:utf-8-*-

dict1 = {'liangdianshui': '111111', 'twowater': '222222', '两点水': '333333'}
print(dict1)
# 新增一个键值对
dict1['jack'] = '444444'
print(dict1)
# 修改键值对
dict1['liangdianshui'] = '555555'
print(dict1)
# 通过 key 值，删除对应的元素
del dict1['twowater']
print(dict1)
# 删除字典中的所有元素
dict1.clear()
print(dict1)
# 删除字典
del dict1
