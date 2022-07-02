
import os
import sys
sys.path.insert(0, os.getcwd())
from my_utils import test_cases
"""
가격이 떨어지지 않은 기간 몇 초인지 return
가격 [1, 10_000]
len(가격) [2, 100_000]
"""
# 주식가격
# https://programmers.co.kr/learn/courses/30/lessons/42584?language=python3
from collections import deque
# 일단 반복문 2개로 풀어보죠
def solution(prices):
    answer = []
    for i in range(len(prices)):
        cnt = 0
        curr_p = prices[i]
        for price in prices[i+1:]:
            if curr_p > price:
                cnt += 1
                break
            cnt += 1
        answer.append(cnt)
    return answer

"""
1차 시도
반복문 2개로 :)
요약: 정확성은 모두 통과했으나 효율성은 모두 실패

테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.05ms, 10.1MB)
테스트 3 〉	통과 (0.93ms, 10.2MB)
테스트 4 〉	통과 (0.89ms, 10.1MB)
테스트 5 〉	통과 (1.20ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 9.92MB)
테스트 7 〉	통과 (0.40ms, 10.3MB)
테스트 8 〉	통과 (0.53ms, 10.1MB)
테스트 9 〉	통과 (0.02ms, 10.3MB)
테스트 10 〉	통과 (1.23ms, 10.1MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	실패 (시간 초과)
채점 결과
정확성: 66.7
효율성: 0.0
합계: 66.7 / 100.0
"""

def solution(prices):
    answer = []
    return answer

# prices = [1, 2, 2, 3, 4, 3, 5, 2, 3, 1, 4]
# [10, 8, 7, 4, 1, 2, 1, 2, 1, 1, 0]
examples = [[[1, 2, 3, 2, 3], [4, 3, 1, 1, 0]]]

test_cases(solution, examples)

"""

"""
# https://programmers.co.kr/learn/courses/30/lessons/42584/solution_groups?language=python3
def others():
    pass



