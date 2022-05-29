#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('Введите 4 числа:')
a=int(input())
b=int(input())
c=int(input())
d=int(input())
summ1=a+b
summ2=c+d
x=summ1/summ2
print("сумма первого и второго числа равна", summ1)
print("сумма третьего и четвертого числа равна",summ2)
print("(a+b)/(c+d)= "'%.2f' % x)