# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 11:16:07 2022

@author: khb16
"""
# 함수
def add_date(friend):
    katok.append(None)
    kLen = len(katok)
    katok[kLen-1] = friend
    
def insert_data(position, friend):
    katok.append(None)
    kLen = len(katok)
    for i in range(kLen-1, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None
    katok[position] = friend

def delete_data(position):
    katok[position] = None
    kLen = len(katok)
    for i in range(position+1, kLen, 1):
        katok[i-1] = katok[i]
        katok[i] = None
    del(katok[kLen-1])
    

# 전역
katok = []

# 메인
add_date('다현')
add_date('정연')
add_date('쯔위')
add_date('사나')
add_date('지효')
print(katok)

insert_data(3, '미나')
delete_data(4)
