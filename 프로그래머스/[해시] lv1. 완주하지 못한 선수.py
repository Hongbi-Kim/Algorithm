# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 15:35:24 2022

@author: khb16
"""
# 해시
# 완주하지 못한 선

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

# sol 1)

def solution(participant, completion):
    for n in completion:
        participant.remove(n)
    answer = participant[0]
    return answer

solution(participant, completion)
# 'mislav'

# sol 2)
hashDict = {}
sumHash = 0

participant[0] #'mislav'
hashDict[hash('mislav')] = 'mislav' # {-1124252976200594368: 'mislav'}
hash('mislav')

for a in participant:
    hashDict[hash(a)] = a # 고유값 저장
    sumHash += hash(a)

for b in completion:
    sumHash -= hash(b)
    
# sol 3)
d = {}
d.get('mislav',0)
for x in participant:         # O(n)
        d[x] = d.get(x, 0) + 1
for x in completion:          # O(n)
        d[x] -= 1
dnf = [k for k, v in d.items() if v > 0]   # O(n)
answer = dnf[0]
