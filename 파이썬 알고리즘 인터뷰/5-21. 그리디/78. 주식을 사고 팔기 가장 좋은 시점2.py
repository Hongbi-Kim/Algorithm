# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 22:42:30 2022

@author: khb16
"""

# 그리디
# 78. 주식을 사고 팔기 가장 좋은 시점2
# 리트코드 /best-time-to-buy-and-sell-stock-ii

# 입력
[7,1,5,3,6,4]

# 출력
# 7
# 1일 때 사서 5일 때 팔아 4의 이익을 얻고
# 3일 때 사서 6일 때 팔아 3의 이익을 얻는다.
# 내리기 전에 팔고, 오르기 전에 사면 됨.

# 풀이 1
def maxProfit(prices):
    result = 0
    # 값이 오르는 경우 매번 그리디 계산
    for i in range(len(prices) - 1):
        if prices[i+1] > prices[i]:
            result += prices[i+1] - prices[i]
    return result

maxProfit([7,1,5,3,6,4])
# 7

# ------------------------------------------------------------------

# 풀이 2(파이썬 다운 방식)
def maxProfit(prices):
    return sum(max(prices[i+1]-prices[i],0) for i in range(len(prices)-1))

maxProfit([7,1,5,3,6,4])
# 7
