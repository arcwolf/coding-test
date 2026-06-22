'''
[BOJ 2178] 미로 탐색

문제
N×M 크기의 미로가 주어진다. (1,1)에서 출발하여 (N,M)까지 이동할 때
지나야 하는 최소 칸 수를 구하라. (출발칸과 도착칸 포함)

입력
- 첫째 줄: N M (2 ≤ N, M ≤ 100)
- N개의 줄: 미로 (0: 이동 불가, 1: 이동 가능)

출력
- 최소 칸 수

핵심
- BFS: 최단 경로 탐색에 최적
- 4방향 이동 (상하좌우)
- visited 배열 또는 방문 시 거리 기록
- from collections import deque
'''

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(input().strip()) for _ in range(N)]

# 4방향: 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# dist[i][j]: (0,0)에서 (i,j)까지 거리 (-1: 미방문)
dist = [[-1] * M for _ in range(N)]
dist[0][0] = 1  # 시작칸 포함

queue = deque([(0, 0)])

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        # 범위 내 + 이동 가능 + 미방문
        if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == '1' and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            queue.append((nx, ny))

print(dist[N-1][M-1])

