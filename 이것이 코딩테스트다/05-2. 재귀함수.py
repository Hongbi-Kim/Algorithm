# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 18:45:26 2022

@author: khb16
"""

# 재귀함수
# 5-4. 재귀함수 종료
def recursive_function(i):
    # 100번째 출력했을 때 종료되도록 종료 조건 명시
    if i == 3:
        return
    print(i, '번째 재귀함수에서', i+1, '번째 재귀함수를 호출합니다.')
    recursive_function(i+1)
    print(i, '번째 함수를 종료합니다.')
    
recursive_function(1)
```
1 번째 재귀함수에서 2 번째 재귀함수를 호출합니다.
2 번째 재귀함수에서 3 번째 재귀함수를 호출합니다.
2 번째 함수를 종료합니다.
1 번째 함수를 종료합니다.
```

# 5-5. 팩토리얼
# 1) 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *= i
    return result

# 2) 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n<=1:
        return 1
    return n * factorial_recursive(n-1)

print('반복적으로 구현: ', factorial_iterative(5))
print('재귀적으로 구현: ', factorial_recursive(5))
# 반복적으로 구현:  120
# 재귀적으로 구현:  120


# 최대공약수 계산(유클리드 호제법)
def gcd(a,b):
    if a % b ==0: # 나머지
        return b
    else:
        return gcd(b, a % b)
    
print(gcd(192, 162))
# 6
