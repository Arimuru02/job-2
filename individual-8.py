#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

a=float(input("Длинна большего основания а: "))
b=float(input("Длинна меньшего основания b: "))
alpha=float(input("Угол при большем основании в градусах: "))
alpha=alpha*math.pi/180
print("Площадь трапеции равна ",(a**2-b**2)/4*math.tan(alpha))
