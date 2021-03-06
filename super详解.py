# -*- coding:utf-8 -*-

"""
当我们调用super()时，实际上是实例化了一个 super 类。
super 包含了两个非常重要的信息: 一个 MRO 以及 MRO 中的一个类。
可以通过 D.mro() (Python 2 使用 D.__mro__ ) 来查看 D 的 MRO 信息

super 的工作原理如下：
    def super(cls,inst):
        mro = inst.__class__.mro()  #返回当前 inst 实例的类的MRO列表
        return mro[mro.index(cls) + 1]
        
"""


# 单继承演示

class A(object):
    def __init__(self):
        self.n = 2

    def add(self,m):
        print('self is {0} @A.add'.format(self))
        self.n += m

class B(A):
    def __init__(self):
        self.n = 3

    def add(self,m):
        print('self is {0} @B.add'.format(self))
        super().add(m)
        self.n += 3


# 多继承

class C(A):
    def __init__(self):
        self.n = 4
    def add(self,m):
        print('self is {0} @C.add'.format(self))
        super().add(m)
        self.n += 4

class D(B,C):
    def __init__(self):
        self.n = 5

    def add(self,m):
        print('self is {0} @D.add'.format(self))
        super().add(m)
        self.n += 5


if __name__ == '__main__':
    b = B()
    print('B class MRO list: {0}'.format(B.mro()))
    b.add(2)
    print('b.n is {0}'.format(b.n))

    # 多继承
    d = D()
    print('D class MRO list {0}'.format(D.mro()))
    d.add(2)
    print('d.n is {0}'.format(d.n))



