'''
[BOJ 2206] 벽 부수고 이동하기

문제
N×M 크기의 맵이 주어진다. (1,1)에서 (N,M)까지 이동할 때
벽을 최대 1개 부수고 이동할 수 있다. 이동할 수 있는 최단 경로의 길이를 구하라.
이동 불가능하면 -1 출력.

입력
- 첫째 줄: N M (1 ≤ N, M ≤ 1,000)
- N개의 줄: 맵 (0: 이동 가능, 1: 벽)

출력
- 최단 경로 길이 (불가능하면 -1)

핵심
- 3차원 visited[i][j][k]: k=0 벽을 아직 안 부순 상태, k=1 부순 상태
- BFS에서 현재 상태를 (x, y, 벽_부순_여부)로 관리
- 벽을 만나면 k=0일 때만 부수고 이동 가능
'''

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# visited[x][y][k]: k=0(벽 안 부숨), k=1(벽 부숨)
visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = True

# 큐: (x, y, 벽부순여부, 거리)
queue = deque([(0, 0, 0, 1)])

while queue:
    x, y, broke, dist = queue.popleft()

    # 도착
    if x == N - 1 and y == M - 1:
        print(dist)
        break

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not (0 <= nx < N and 0 <= ny < M):
            continue

        if board[nx][ny] == '0' and not visited[nx][ny][broke]:
            # 빈 칸: 그냥 이동
            visited[nx][ny][broke] = True
            queue.append((nx, ny, broke, dist + 1))
        elif board[nx][ny] == '1' and broke == 0 and not visited[nx][ny][1]:
            # 벽: 아직 부순 적 없을 때만 부수고 이동
            visited[nx][ny][1] = True
            queue.append((nx, ny, 1, dist + 1))
else:
    print(-1)

