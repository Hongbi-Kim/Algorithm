# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 16:19:04 2022

@author: khb16
"""
# 카카오_2019 블라인드 리크루트
# Level2
# 오픈채팅방

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234",
          "Enter uid1234 Prodo","Change uid4567 Ryan"]

answer = [] # 정답 리스트
user = {}   # {'아이디' : '닉네임'}
sen = {'Enter' : '님이 들어왔습니다.', 'Leave' : '님이 나갔습니다.'}
for i in record:
    info = i.split(' ')
    if info[0] in ['Enter', 'Change']:
        user[info[1]] = info[2] 
        # 딕셔너리이므로 '아이디'가 동일하면 
        # '닉네임' 자동 변환
        
for i in record:
    if i.split(' ')[0] != 'Change':
        answer.append(user[i.split(' ')[1]] + sen[i.split(' ')[0]])
        
answer
# ['Prodo님이 들어왔습니다.', 'Ryan님이 들어왔습니다.', 
# 'Prodo님이 나갔습니다.', 'Prodo님이 들어왔습니다.']