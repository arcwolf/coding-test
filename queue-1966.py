'''
[BOJ 1966] 프린터 큐

문제
프린터는 다음과 같은 방식으로 동작한다.
1. 큐에서 문서를 꺼낸다.
2. 큐에 남은 문서 중 현재 문서보다 우선순위가 높은 문서가 있으면, 현재 문서를 큐 맨 뒤에 넣는다.
3. 그렇지 않으면 현재 문서를 인쇄한다.

특정 문서가 몇 번째로 인쇄되는지 구하라.

입력
- 첫째 줄: 테스트 케이스 수 T
- 각 테스트 케이스 첫째 줄: 문서 수 N, 궁금한 문서 위치 M (0-indexed)
- 둘째 줄: N개 문서의 우선순위

출력
- M번째 문서가 몇 번째로 인쇄되는지 출력

예시)
N=6, M=0, 우선순위: 1 1 9 1 1 1  → 출력: 5
'''

from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    priorities = list(map(int, input().split()))

    # (우선순위, 원래인덱스) 쌍으로 deque 구성
    queue = deque((p, i) for i, p in enumerate(priorities))
    count = 0  # 인쇄된 문서 수

    while queue:
        cur_p, cur_i = queue.popleft()

        # 큐에 우선순위가 더 높은 문서가 있으면 맨 뒤로
        if any(cur_p < p for p, _ in queue):
            queue.append((cur_p, cur_i))
        else:
            count += 1
            if cur_i == M:   # 궁금한 문서가 인쇄되면 종료
                print(count)
                break

