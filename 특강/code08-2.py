# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 22:54:33 2022

@author: khb16
"""

# 이진 트리 순회 구현
## 함수/클래스
class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

def preorder(node):
    if node == None:
        return
    print(node.data, end= '->')
    preorder(node.left)
    preorder(node.right)

def inorder(node):
    if node == None:
        return
    inorder(node.left)
    print(node.data, end= '->')
    inorder(node.right)
    
def postorder(node):
    if node == None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data, end= '->')
    
## 전역


## 메인
# 08-1 참조
print('전위 순회 :', end=' ')
preorder(node1)
print('끝')

print('중위 순회 :', end=' ')
inorder(node1)
print('끝')

print('후위 순회 :', end=' ')
postorder(node1)
print('끝')

# 전위 순회 : 화사->솔라->휘인->쯔위->문별->선미->끝
# 중위 순회 : 휘인->솔라->쯔위->화사->선미->문별->끝
# 후위 순회 : 휘인->쯔위->솔라->선미->문별->화사->끝