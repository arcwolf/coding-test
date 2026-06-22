'''
[BOJ 9251] LCS

문제
LCS(Longest Common Subsequence, 최장 공통 부분 수열)는
두 수열이 주어졌을 때 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

입력
- 첫째 줄: 문자열 A
- 둘째 줄: 문자열 B

출력
- LCS의 길이

핵심 (DP 점화식)
dp[i][j] = A의 i번째, B의 j번째까지 고려했을 때 LCS 길이
- A[i] == B[j]: dp[i][j] = dp[i-1][j-1] + 1
- A[i] != B[j]: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
'''

A = input().strip()
B = input().strip()

la, lb = len(A), len(B)

# dp[i][j]: A[:i], B[:j]의 LCS 길이 (1-indexed로 처리하여 경계 처리 단순화)
dp = [[0] * (lb + 1) for _ in range(la + 1)]

for i in range(1, la + 1):
    for j in range(1, lb + 1):
        if A[i-1] == B[j-1]:
            # 두 문자가 같으면 이전 대각선 + 1
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            # 다르면 위쪽, 왼쪽 중 더 큰 값
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[la][lb])

