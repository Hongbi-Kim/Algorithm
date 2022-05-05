# -*- coding: utf-8 -*-
"""
Created on Thu May  5 12:45:16 2022

@author: khb16
"""

info=["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
# [1,1,1,1,2,4]



from itertools import combinations
from bisect import bisect_left


answer = []

# info를 파싱한다 딕셔너리에!
db = {}
for i in info:
    tokens = i.split(" ")
    cond = tokens[0:4]
    score = int(tokens[4])
    keys = []
    for i in range(5):
        for combi in combinations(cond, i):
            key = ('').join(list(combi))
            db.setdefault(key, []).append(score)
   
for key in db.keys():
    db[key].sort()

# query를 파싱한다!
for q in query:
    q = q.split(" ")
    qq = ('').join([s for s in q[0:7] if s != "-" and s !="and"])
    score = int(q[7])
    if qq not in db.keys():
        answer.append(0)
    else:
        result = db[qq]
        index = bisect_left(result, score)
        answer.append(len(result) - index)


tokens = info[0].split(" ")
cond = tokens[0:4]
score = int(tokens[4])
keys = []
for i in range(5):
    for combi in combinations(cond, i):
        key = ('').join(list(combi))
        db.setdefault(key, []).append(score)

combinations(cond, 0)


