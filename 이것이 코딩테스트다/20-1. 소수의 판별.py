# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 18:22:58 2022

@author: khb16
"""

# 기타 알고리즘
# 소수 판별 함수

def is_prime_number():
    # 2부터 (x-1)까지 모든 수를 확인하며
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

print(is_prime_numger(4))    
# False
    
# 개선된 알고리즘
import math
# 소수 판별 함수(2이상의 자연수에 대하여)
def is_prime_numger(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

print(is_prime_numger(4))
# False

# 에라토스테네스의 체
import math

n = 1000
# 처음엔 모든 수가 소수인 것으로 초기화
array = [True for i in range(n+1)]

# 2부터 n의 제곱근까지의 모든 수를 확인 
for i in range(2, int(math.sqrt(n)) + 1): 
    if array[i] == True:
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            array[i*j] = False
            j += 1
            
for i in range(2,n+1):
    if array[i]:
        print(i, end=' ')
        
```
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 
83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 
167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 
257 263 269 271 277 281 283 293 307 311 313 317 331 337 347 349 
353 359 367 373 379 383 389 397 401 409 419 421 431 433 439 443 
449 457 461 463 467 479 487 491 499 503 509 521 523 541 547 557 
563 569 571 577 587 593 599 601 607 613 617 619 631 641 643 647 
653 659 661 673 677 683 691 701 709 719 727 733 739 743 751 757 
761 769 773 787 797 809 811 821 823 827 829 839 853 857 859 863 
877 881 883 887 907 911 919 929 937 941 947 953 967 971 977 983 
991 997 
```        
    