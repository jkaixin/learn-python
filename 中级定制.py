# -*- coding:utf-8 -*-

class Time60(object):
    'Time60 - track hours and minutes'

    def __init__(self,hr,minu):
        self.hr = hr
        self.minu = minu

    def __str__(self):
        return '{0}:{0}'.format(self.hr,self,minu)

    __repr__ = __str__

    def __add__(self,other):
        return self.__class__(self.hr + other.hr,self.minu +\
                other.minu)

    def __iadd__(self,other):
        self.hr += other.hr
        self.minu += other.minu

        return self

if __name__ == '__main__':
    pass

