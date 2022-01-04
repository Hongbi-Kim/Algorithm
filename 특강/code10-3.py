# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 17:19:04 2022

@author: khb16
"""
# 재귀 3
## 1부터 10까지 합계
def addNumber(num):
    if num <= 1:
        return 1
    return num + addNumber(num-1)

print(addNumber(10))
# 55

#---------------------------------------------------
# 팩토리얼
def factorial(num):
    if num <= 1:
        return 1
    return num*factorial(num-1)

print('\n10! = ', factorial(10))
# 10! =  3628800

#---------------------------------------------------
# 우주선 발사 카운트다운
def countDown(n):
    if n == 0:
        print("발사")
    else:
        print(n)
        countDown(n-1)
        
countDown(5)
# 5
# 4
# 3
# 2
# 1
# 발사

#---------------------------------------------------
# 별 모양 출력하기
def printStar(n):
    if n >0 :
        printStar(n-1)
        print('★'*n)

printStar(5)
# ★
# ★★
# ★★★
# ★★★★
# ★★★★★

#---------------------------------------------------
# 구구단 출력하기
def gugu(dan, num):
    print("%d x %d = %d" %(dan,num,dan*num))
    if num<9:
        gugu(dan, num+1)
        
for dan in range(2,4):
    print("## %d단 ##" %dan)
    gugu(dan,1)
'''    
## 2단 ##
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
## 3단 ##
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
'''

#---------------------------------------------------
# N제곱 계산하기
tab = ''
def pow(x,n):
    global tab
    tab += ' '
    if n==0:
        return 1
    print(tab + "%d*%d&(%d-%d)"%(x,x,n,1))
    return x*pow(x,n-1)

print('2^4')
print('답 -->', pow(2,4))
# 2^4
#  2*2&(4-1)
#   2*2&(3-1)
#    2*2&(2-1)
#     2*2&(1-1)
# 답 --> 16

#---------------------------------------------------
# 배열의 합 계산
import random

def arySum(arr, n):
    if n <= 0:
        return arr[0]
    return arySum(arr, n-1) + arr[n]

ary = [random.randint(0,255) for _ in range
       (random.randint(10,20))]
print(ary)
print('배열 합계 -->', arySum(ary, len(ary)-1))
# [172, 22, 143, 34, 177, 170, 90, 94, 209, 179]
# 배열 합계 --> 1290
