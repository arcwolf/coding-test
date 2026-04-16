'''
[BOJ 11286] 절댓값 힙

문제
절댓값 힙은 다음과 같은 연산을 지원한다.
1. 배열에 정수 x를 넣는다.
2. 배열에서 절댓값이 가장 작은 값을 출력하고 제거한다.
   (절댓값이 같으면 음수 우선, 그래도 같으면 더 작은 수 우선)

입력
- 첫째 줄: 연산 수 N
- N개의 줄: 정수 x
  - x ≠ 0 이면 배열에 추가
  - x = 0 이면 최솟값 출력 (배열이 비어있으면 0 출력)

출력
- x = 0 인 연산마다 결과 출력

핵심
- heapq 사용: (절댓값, 원래값) 쌍으로 push → 자동 정렬
import heapq
heapq.heappush(heap, (abs(x), x))
'''

import heapq
import sys
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    x = int(input())

    if x != 0:
        # (절댓값, 원래값) 쌍으로 push
        # 절댓값이 같으면 원래값(음수가 더 작으므로) 기준으로 자동 정렬
        heapq.heappush(heap, (abs(x), x))
    else:
        if heap:
            # heappop은 (절댓값, 원래값) 중 가장 작은 것 반환
            print(heapq.heappop(heap)[1])  # 원래값만 출력
        else:
            print(0)

