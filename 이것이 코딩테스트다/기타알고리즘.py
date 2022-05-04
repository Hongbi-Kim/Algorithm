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

# --------------
number = "1231234"
k = 3
L=[]
for i in number:
    L.append(i)
L.sort(reverse = True)
answer = ""
for i in L[0:len(number)-k]:
    answer += "".join(i)
def solution(number, k):
    L=[]
    for i in number:
        L.append(i)
    L.sort(reverse = True)
    answer = ""
    for i in L[0:len(number)-k]:
        answer += "".join(i)
    return answer
    
solution("1231234",3)

"".join([123])


L=[]
for n in number:
    while L and L[-1] < n and k>0:
        L.pop()
        k -= 1
    L.append(n)
while k > 0:
    L.pop()
    k -= 0
answer = "".join(L)
L.sort(reverse = True)

### -------
import re
new_id = "...!@BaT#*..y.abcdefghijklm"
new_id = new_id.lower()
new_id = re.sub(r"[^a-z0-9\-\_\.]","",new_id)
new_id = new_id.replace("..",".")
if new_id == "":
    new_id = "a"
elif len(new_id) >= 16:
    new_id = new_id[:15]
    if new_id[-1] == ".":
        new_id = new_id[:14]
if len(new_id) <= 2:
    while len(new_id) == 3:
        new_id += new_id[-1]
new_id + new_id[-1]
"bat.y.abcdefghi"

import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st

solution("...!@BaT#*..y.abcdefghijklm")

numbers = [6, 10, 2]
numbers = [str(x) for x in numbers]
numbers.sort(key = lambda x : (x*4)[:4], reverse = True)
''.join(numbers)
