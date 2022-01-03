# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 11:37:36 2022

@author: khb16
"""

# 선형 리스트 처리 프로그램
def add_data(friend):
    katok.append(None)
    kLen = len(katok)
    katok[kLen-1] = friend

def insert_data(position, friend):
    if position < 0 or position > len(katok):
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return
    
    katok.append(None)
    kLen = len(katok)
    
    for i in range(kLen-1, position,-1):
        katok[i] = katok[i-1]
        katok[i-1] = None
        
    katok[position] = friend
    
def delete_data(position):
    if position < 0 or position > len(katok):
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return
    
    kLen












    