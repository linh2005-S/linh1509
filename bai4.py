# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:56:16 2024

@author: linh
"""
a = int(input("nhập giá trị trong [-99,99]: "))
while a>=100 or a<=(-100):
    a= int(input("nhập lại: "))
print("hợp lệ")