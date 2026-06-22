'''
[BOJ 7569] 토마토 (3차원)

문제
M×N×H 크기의 상자에 토마토가 들어있다.
익은 토마토(1)는 인접한 6방향(상하좌우앞뒤)의 안 익은 토마토(0)를 익게 한다.
모든 토마토가 익는 최소 일수를 구하라. 불가능하면 -1 출력.

입력
- 첫째 줄: M N H (1 ≤ M, N ≤ 100 / 1 ≤ H ≤ 100)
- H개의 층, 각 층은 N개의 줄, 각 줄에 M개의 정수

출력
- 최소 일수 (불가능하면 -1)

핵심
- 다중 출발지 BFS: 처음부터 모든 익은 토마토를 큐에 넣고 시작
- 3차원 이동: dx, dy, dz 방향 벡터 6개
- 2D 토마토(BOJ 7576)의 3D 확장 버전
'''

from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())  # 가로, 세로, 높이

# box[h][n][m]
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

# 6방향: 상하(층), 동서남북
dh = [-1, 1, 0, 0, 0, 0]
dn = [0, 0, -1, 1, 0, 0]
dm = [0, 0, 0, 0, -1, 1]

queue = deque()

# 처음부터 익은 토마토 모두 큐에 삽입 (다중 출발지 BFS)
for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 1:
                queue.append((h, n, m))

while queue:
    ch, cn, cm = queue.popleft()
    for i in range(6):
        nh, nn, nm = ch + dh[i], cn + dn[i], cm + dm[i]
        if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M and box[nh][nn][nm] == 0:
            box[nh][nn][nm] = box[ch][cn][cm] + 1  # 거리 = 일수
            queue.append((nh, nn, nm))

# 결과 확인: 안 익은 토마토(0)가 남아있으면 -1
ans = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 0:
                print(-1)
                exit()
            ans = max(ans, box[h][n][m])

print(ans - 1)  # 시작 값이 1이었으므로 -1

