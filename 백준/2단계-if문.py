# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 20:43:36 2022

@author: khb16
"""
# if문
# https://www.acmicpc.net/step/4

#1
A, B = map(int, input().split())
if A>B: 
    print(">")
elif A<B:
    print("<")
else:
    print("==")

#2
score = int(input())
if score>=90: 
    print("A")
elif score >=80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
    
#3
year = int(input())
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("1")
else:
    print("0")
    
#4
x = int(input())
y = int(input())
if x >0 and y>0:
    print("1")
elif x<0 and y>0:
    print("2")
elif x<0 and y<0:
    print("3")
elif x>0 and y<0:
    print("4")
    
#5
H , M = map(int, input().split())
if M<45:
    if H == 0:
        H = 23
        M += 15
    else:
        H -= 1
        M += 15
elif M<=59:
    M -= 45
print(H,M)


H , M = map(int, input().split())
if M>44:
    print(H,m-45)
elif H>0 and M<=44:
    print(H-1, M+15)
else:
    print(23,M+15)