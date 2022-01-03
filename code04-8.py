# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 14:01:51 2022

@author: khb16
"""

# 함수/클래스 선언부
class Node:
    def __init__(self):
        self.data = None
        self.link = None

def printNode(start):
    current = start
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
        
def insertNode(findData, insertData):
    global memory, head, current, pre
    if head.data == findData:
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        memory.append(node)
        return
    # 사나 앞에 솔라를 삽입
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            memory.append(node)
            return
    # 마지막에 추가할 때 (=삽입할 이름이 존재하지 않을 때)
    node = Node()
    node.data = insertData
    current.link = node
    memory.append(node)
    return

def deleteNode(deleteData):
    global memory, head, current, pre
    # 첫 노드 삭제
    if deleteData == head.data:
        current = head
        head = head.link
        del(current)
        return
    #첫 노드 외의 노드 삭제
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del(current)
            return

def findNode(findData):
    global memory, head, current, pre
    current = head
    if current.data == findData:
        return current
    while current.link != None:
        current= current.link
        if current.data == findData:
            return current
    return Node()

# -----------------------------------------------
# 전역 변수
memory = []
head, current, pre = None, None, None
dataArray = ['다현','정연','쯔위','사나','지효']

# -----------------------------------------------
# 메인 코드부
node = Node()
node.data = dataArray[0]
head = node
memory.append(node)

for data in dataArray[1:] :
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)
    
printNode(head)
# 다현 정연 쯔위 사나 지효 

insertNode('다현', '화사')
printNode(head)
# 화사 다현 정연 쯔위 사나 지효 

insertNode('사나','솔라')
printNode(head)
# 화사 다현 정연 쯔위 솔라 사나 지효 

# 마지막 노드까지 '재남'을 찾지 못한 경우
insertNode('재남','문별')
printNode(head)
# 화사 다현 정연 쯔위 솔라 사나 지효 문별 

deleteNode('화사')
printNode(head)
# 다현 정연 쯔위 솔라 사나 지효 문별 

deleteNode('쯔위')
printNode(head)
# 다현 정연 솔라 사나 지효 문별 

fNode = findNode('다현')
print(fNode.data)
# 다현

fNode = findNode('사나')
print(fNode.data)
# 사나

fNode = findNode('재남')
print(fNode.data)
# None