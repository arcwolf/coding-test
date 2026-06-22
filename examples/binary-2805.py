'''
[BOJ 2805] 나무 자르기

문제
절단기 높이 H를 정하면, H보다 키가 큰 나무는 H를 제외한 나머지를 잘라낸다.
집에 가져가려는 나무의 총 길이가 적어도 M미터 이상이 되도록 하는 절단기의 최대 높이 H를 구하라.

입력
- 첫째 줄: N M (1 ≤ N ≤ 1,000,000 / 1 ≤ M ≤ 2,000,000,000)
- 둘째 줄: 나무 높이 N개

출력
- 절단기의 최대 높이 H

핵심
- 파라메트릭 서치: lo=0, hi=max(나무 높이)
- is_valid(mid): sum(max(0, h-mid) for h in trees) >= M 이면 True
- True이면 lo를 올리고 ans 갱신, False이면 hi 낮춤
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

def is_valid(mid):
    # 절단기 높이가 mid일 때 얻는 나무 총량이 M 이상인지 확인
    total = sum(h - mid for h in trees if h > mid)
    return total >= M

lo, hi = 0, max(trees)
ans = 0

while lo <= hi:
    mid = (lo + hi) // 2
    if is_valid(mid):
        ans = mid      # 가능한 높이 중 최대를 갱신
        lo = mid + 1   # 더 높게 자를 수 있는지 탐색
    else:
        hi = mid - 1   # 너무 높으니 낮춤

print(ans)

