'''
[BOJ 12865] 평범한 배낭 (0/1 Knapsack)

문제
N개의 물건이 있다. 각 물건은 무게 W와 가치 V를 가진다.
최대 무게 K를 버틸 수 있는 배낭에 넣을 수 있는 물건들의 가치 합의 최댓값을 구하라.
물건은 한 번씩만 담을 수 있다. (0/1 배낭 문제)

입력
- 첫째 줄: N K (1 ≤ N ≤ 100 / 1 ≤ K ≤ 100,000)
- N개의 줄: 물건의 무게 W, 가치 V

출력
- 배낭에 넣을 수 있는 최대 가치

핵심 (DP 점화식)
dp[i][w] = i번째 물건까지 고려하고 무게 제한이 w일 때 최대 가치
- W[i] > w: dp[i][w] = dp[i-1][w]        (현재 물건 담을 수 없음)
- W[i] <= w: dp[i][w] = max(dp[i-1][w], dp[i-1][w-W[i]] + V[i])

공간 최적화 (1D DP):
dp[w] = max(dp[w], dp[w - W[i]] + V[i])  # w를 역순으로 순회
'''

N, K = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]  # (무게, 가치)

# 1D DP로 공간 최적화 (2D의 i번째 행만 유지)
dp = [0] * (K + 1)  # dp[w]: 무게 제한 w일 때 최대 가치

for w_item, v_item in items:
    # 역순으로 순회해야 같은 물건을 중복 사용하지 않음
    # (순방향이면 이미 갱신된 값을 재참조하게 됨)
    for w in range(K, w_item - 1, -1):
        dp[w] = max(dp[w], dp[w - w_item] + v_item)

print(dp[K])

