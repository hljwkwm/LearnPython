# -*- coding: UTF-8 -*-
def add(num1, num2):
    # 两数之和
    if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
        raise TypeError('参数类型错误')
    return num1 + num2


def division(num1, num2):
    # 求商与余数
    a = num1 % num2
    b = (num1 - a) / num2
    return b, a


print(add(1, 2))

n1, n2 = division(9, 4)
tuple1 = division(9, 4)

print(n1, n2)
print(tuple1)
