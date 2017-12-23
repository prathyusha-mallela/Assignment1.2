# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 17:20:56 2017

@author: Prathyusha Mallela
"""
def filter_for_mult7_notin5(lower_range,upper_range):
    a=list(range(lower_range,upper_range+1))
    res=list(filter(lambda x: (x%7==0) & (x%5!=0),a))
   # print(res)
    return res

print(filter_for_mult7_notin5(2000,3200));