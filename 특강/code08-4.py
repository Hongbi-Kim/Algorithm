# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 13:29:29 2022

@author: khb16
"""
# 이진 탐색 트리
## 함수
class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

## 전역
memory = []
root = None

nameAry = ['블랙핑크','레드벨벳','에이핑크','걸스데이','트와이스','마마무']

## 메인
node = TreeNode()
node.data = nameAry[0]
root = node
memory.append(node)

for name in nameAry[1:]:
    node = TreeNode()
    node.data = name
   
    current = root
    while True:
        if name < current.data:
            if (current.left == None):
                current.left = node
                break
            current = current.left
        else:
            if (current.right == None):
                current.right = node
                break
            current = current.right
    memory.append(node)
            
findName = '마마무'
current = root
while True:
    if current.data == findName:
        print(findName, '찾았다!!')
        break
    elif current.data > findName:
        if current.left == None:
            print(findName,"이 트리에 없음.")
            break
        current = current.left
    else:
        if current.right == None:
            print(findName,"이 트리에 없음.")
            break
        current = current.right
# 마마무 찾았다!!        
        