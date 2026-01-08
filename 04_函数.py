# 1. 求请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程ax^2 + bx + c = 0的两个解。
import math
def quadratic(a, b, c):
    d = b**2 - 4*a*c  # 计算判别式
    if d < 0:
        return "无实数解"
    elif d == 0:
        x = -b / (2*a)
        return (x,)
    else:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        return (x1, x2)

# 2. 定义一个函数，求一个数的指定n次方。
def power(x, n):
    s = 1
    while n > 0:
        s = s * x
        n = n - 1
    return s