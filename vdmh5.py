# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:50:25 2024

@author: linh
"""
count = 0
n = int(input(" nhập vào số lần cần lặp: "))
while (count < n):
    print(" lần lập thứ:", count +1, "\t biến đếm:",count)
    count = count +1
else:
    print("\n thực hiện lệnh trong else, do:",
          "\n count = ", count, "\n n=",n,
          "\n bool(count<n)=", bool (count<n))