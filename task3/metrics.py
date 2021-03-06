import math

__author__ = 'vks'


def manhattan(x, y):
    ans = 0.0
    for i in range(len(x)):
        ans += abs(float(x[i]) - float(y[i]))
    return ans


def euclides(x, y):
    ans = 0.0
    for i in range(len(x)):
        ans += (float(x[i]) - float(y[i])) ** 2
    return math.sqrt(ans)


def l_inf(x, y):
    ans = 0.0
    for i in range(len(x)):
        ans = max(ans, abs(float(x[i]) - float(y[i])))
    return ans
