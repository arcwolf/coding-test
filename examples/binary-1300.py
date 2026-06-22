'''
[BOJ 1300] K번째 수

문제
N×N 배열 A에서 A[i][j] = i*j 일 때,
이 배열을 1차원 배열로 펼쳤을 때 K번째로 작은 수를 구하라.

입력
- N (1 ≤ N ≤ 100,000)
- K (1 ≤ K ≤ min(N^2, 10^9))

출력
- K번째로 작은 수

핵심
- mid값이 정해진다면, A에서 mid 이하인 원소의 개수 = sum(min(mid//i, N) for i in 1..N)
- 이 개수 >= K 이면 hi를 낮추고 ans 갱신, 아니면 lo를 올리는 이분탐색
- lo=1, hi=K
'''

N = int(input())
K = int(input())

def count_le(mid):
    # A[i][j] = i*j 에서 mid 이하인 원소 개수
    # i행에서 mid//i 개가 mid 이하 (단, N을 초과할 수 없음)
    result = 0
    for i in range(1, N + 1):
        result += min(mid // i, N)
    return result

lo, hi = 1, K
ans = K

while lo <= hi:
    mid = (lo + hi) // 2
    if count_le(mid) >= K:
        ans = mid      # K번째 이상 있으므로 정답 후보
        hi = mid - 1   # 더 작은 값에서도 가능한지 확인
    else:
        lo = mid + 1   # mid 이하 원소가 K개 미만 → 더 큰 값 필요

print(ans)

