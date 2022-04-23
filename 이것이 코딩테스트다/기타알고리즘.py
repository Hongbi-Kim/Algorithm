# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 22:40:28 2022

@author: khb16
"""


def solution(numbers):
    num = list(map(str, numbers))
    num.sort(key = lambda x : x*3, reverse = True)
    answer = int(''.join(num))
    return str(answer)

numbers = [6,10,2]
num = list(map(str, numbers))
num.sort(key = lambda x : x*3, reverse = True)
answer = int(''.join(num))

text = 'aabbaccc'
list(range(1, int(len(text)/2)+1)) # [1,2,3,4]
[len(text)] # [8]
list(range(1, int(len(text)/2)+1)) + [len(text)] # [1, 2, 3, 4, 8]

tok_len = 2
words = [text[i: i+tok_len] for i in range(0, len(text), tok_len)]
res = []
cur_word = words[0]
cur_cnt = 1
for a, b in zip(words, words[1:] + ['']):
    if a = b:
        cur_cnt += 1
    else:
        res.append([cur_word, cur_cnt])
        cut_word = b
        cur_cnt = 1
sum(len(word) + (len(str(cnt)) if cnt >1 else 0) for word, cnt in res)
    

