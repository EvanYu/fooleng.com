#!/usr/bin/env python3
# coding: utf-8


from math import sqrt


class Stair:
    def __init__(self, H_0, n):
        self.H_0 = H_0
        # 梯跑数
        self.n = n
        # 建筑面层厚度
        self.c = 0.05
        # 梯段尺寸
        self.l_0 = 0.26
        self.h_0 = 0.16
        # 荷载放大系数
        self.gamma = 1.2
        # 材料容重
        self.con = 20
        self.scon = 25

    # 楼梯主要尺寸
    @property
    def L_0(self):
        return float('%.3f' % (self.H_0 * self.l_0 / self.h_0))

    @property
    def L(self):
        return float('%.3f' % sqrt(pow(self.L_0, 2) + pow(self.H_0, 2)))

    # 梯板厚度
    @property
    def h_1(self):
        return float('%.3f' % (self.L / self.scon / self.n))

    # 梯段折算厚度
    @property
    def h_2(self):
        return float('%.3f' % (self.h_0 * self.l_0 / sqrt(pow(self.h_0, 2) + pow(self.l_0, 2)) / 2))

    # 建筑面层折算厚度
    @property
    def h_3(self):
        temp = self.c * (self.h_0 + self.l_0) / sqrt(pow(self.h_0, 2) + pow(self.l_0, 2))
        return float('%.3f' % (temp * self.con / self.scon))


    # 楼梯折算厚度
    @property
    def h(self):
        return float('%.3f' % (self.h_1 + self.h_2 + self.h_3))


    # 恒面荷载
    @property
    def areaStaticLoad(self):
        return float('%.3f' % (self.h * self.scon * self.gamma))


    # 活面荷载
    @property
    def areaLiveLoad(self):
        if self.n == 1 or 2:
            n1 = 1
        elif self.n == 3:
            n1 = 1.5
        else:
            n1 = 2

        return float('%.3f' % (3.5 * n1))


    # 恒线荷载
    @property
    def lineStaticLoad(self):
        return float('%.3f' % (self.h * self.scon * self.L * self.gamma / 2))


    # 活线荷载
    @property
    def lineLiveLoad(self):
        return float('%.3f' % (self.areaLiveLoad * self.L))
