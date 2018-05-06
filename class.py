# 1519100058 黄杰 第七次作业
# 二分法找方程根

import numpy as np
a=float(input('请输入左边界a:'))
b=float(input('请输入右边界b:'))
e=float(input('请输入精确度e:'))
func=input("请输入函数：")
def f(x):
    return eval(func)
for k in range(10):
    if f(a)*f(b)<=0:
        if f(a)*f(b)==0:
            if f(a)==0:
                print(a,k)
                break
            else:
                print(b,k)
                break
        else:
            m=(a+b)/2
            if abs(a-b)<e:
                print(m,k)
                break
            else:
                if f(m)*f(a)>0:
                    a=m
                else:
                    b=m