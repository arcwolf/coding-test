import sys
input = sys.stdin.readline
INF = float('inf')

# BOJ 11404 플로이드 — 모든 도시 쌍 최단비용
n = int(input())
m = int(input())

dist = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dist[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a][b] = min(dist[a][b], c)  # 중복 노선은 최소 비용만

# k: 경유지 (가장 바깥 루프)
for k in range(1, n + 1):
    for i in range(1, n + 1):
        if dist[i][k] == INF:
            continue
        for j in range(1, n + 1):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

out = []
for i in range(1, n + 1):
    row = [0 if dist[i][j] == INF else dist[i][j] for j in range(1, n + 1)]
    out.append(' '.join(map(str, row)))
print('\n'.join(out))
