'''
[BOJ 1920] 수 찾기

문제
N개의 정수 A[]가 주어진다.
M개의 수를 입력받아 A 안에 존재하는지 구하라.

입력
- 첫째 줄: N (1 ≤ N ≤ 100,000)
- 둘째 줄: A[]의 원소 N개
- 셋째 줄: M (1 ≤ M ≤ 100,000)
- 넷째 줄: 찾을 수 M개

출력
- 존재하면 1, 없으면 0을 한 줄에 하나씩 출력

핵심
- 정렬 후 이분탐색 또는 set() 사용
- bisect 모듈: bisect_left / bisect_right 활용
'''

import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
A = sorted(map(int, input().split()))  # 이분탐색을 위해 정렬

M = int(input())
targets = list(map(int, input().split()))

for t in targets:
    # bisect_left: t가 삽입될 가장 왼쪽 인덱스
    idx = bisect_left(A, t)
    # 해당 인덱스의 값이 t와 같으면 존재
    if idx < len(A) and A[idx] == t:
        print(1)
    else:
        print(0)

# --- set()을 이용한 더 간단한 방법 ---
# A_set = set(A)
# for t in targets:
#     print(1 if t in A_set else 0)

