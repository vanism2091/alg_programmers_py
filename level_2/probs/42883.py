
import os
import sys
sys.path.insert(0, os.getcwd())
from my_utils import test_cases
"""
find

채점 결과
정확성: 83.3
합계: 83.3 / 100.0

시간초과 2개
"""

# 큰 수 만들기
# https://programmers.co.kr/learn/courses/30/lessons/42883?language=python3
from collections import deque
def solution_1(number, k):
    number = deque(list(number))
    new = []
    while k > 0:
        for i in range(9,0,-1):
            if str(i) not in number:
                continue
            digit_idx = number.index(str(i))
            if digit_idx <= k :
                new.append(number[digit_idx])
                for _ in range(digit_idx+1):
                    number.popleft()
                k -= digit_idx
                break
    return ''.join(new+list(number))

"""
내가 하려는 방법,
1. number을 k개만큼 잘라서 그 중 max의 index를 구한다.
2. 그 앞은 버리고, 
    2.2 max는 new에 넣는다.
    2.3 k -= m_idx
    2.4 새 넘버는 max 뒤부터.

채점 결과
정확성: 83.3
합계: 83.3 / 100.0

조금 더 발전하긴 했는데, 런타임 에러 1개 났음. 1개는 시간 초과
?? 합계가 똑같네? 발전한게 아니었네? ㅋㅋㅋㅋ
런타임 에러는 11111 같이, 다 똑같아서, k = 0인 경우... while문에서 종료 조건을 안뒀음..:)
이걸 고치니까 1개는 해결. 다른 1개는 아직 시간초과가 나옴.

# 9인 경우 패스하라를 넣으면 성능이 비약적으로 발전한다는데,
이걸 내 코드에 어떻게 구현하며 좋을까 고민중
"""

# from collections import deque
def solution_2(number, k):
    num_li = list(number)
    look_idx = 0 
    new = []
    len_answer = len(num_li) - k
    while k > 0:
        while num_li[look_idx] == '9':
            new.append('9')
            look_idx += 1
            if len(new) == len_answer:
                return ''.join(new)
        # 1
        max_idx = num_li[look_idx:].index(max(num_li[look_idx:look_idx+k+1]))
        # 2. 
        new.append(num_li[look_idx+max_idx])
        look_idx += max_idx + 1
        k -= max_idx
        if len(new) == len_answer:
            return ''.join(new)
    new.extend(num_li[look_idx:])    
    return ''.join(new)


##
def solution(number, k):
    num_li = list(number)
    read_idx = 0 
    write_idx = 0
    len_answer = len(num_li) - k
    while k > 0:
        while num_li[read_idx] == '9':
            num_li[write_idx] = '9'
            write_idx += 1
            read_idx += 1
            if write_idx == len_answer:
                return ''.join(num_li[:write_idx])
        # 1
        max_idx = num_li[read_idx:].index(max(num_li[read_idx:read_idx+k+1]))
        # 2.
        num_li[write_idx] = num_li[read_idx+max_idx]
        write_idx += 1
        read_idx += max_idx + 1
        k -= max_idx
        if write_idx == len_answer:
            return ''.join(num_li[:write_idx])
    return ''.join(num_li[:write_idx] + num_li[read_idx:])



# examples = [['1924', 2, '94'], ['1231234', 3, '3234'], ['4177252841', 4, '775841']]
# examples = [['4177252841', 4, '775841']]
examples = [['99199919999', 4, '9999999']]

test_cases(solution, examples)

"""

"""
# https://programmers.co.kr/learn/courses/30/lessons/42883/solution_groups?language=python3
def others():
    pass



