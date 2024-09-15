# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:19:01 2024

@author: linh
"""
a = float(input("nhập giá trị trong [-89,9,88,8]: "))
while a>= 88.9 or a<=-89.91:
    a= float(input("nhập lại: "))
print("hợp lệ")
