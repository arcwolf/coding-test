'''
[BOJ 1260] DFS와 BFS

문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
낮은 번호부터 탐색한다.

입력
- 첫째 줄: 정점 수 N, 에지 수 M, 시작 정점 V
- M개의 줄: 에지 정보

출력
- 첫째 줄: DFS 탐색 순서
- 둘째 줄: BFS 탐색 순서

핵심
- DFS: 재귀 또는 스택, 연결 리스트 정렬 선택
- BFS: deque 사용 (from collections import deque)
- 구현 시 방문 배열 visited[] 사용
'''

from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N, M, V = map(int, input().split())

# 인접 리스트 구성 (양방향)
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 낮은 번호 먼저 방문하기 위해 정렬
for i in range(N + 1):
    graph[i].sort()

# --- DFS (재귀) ---
visited_dfs = [False] * (N + 1)
dfs_result = []

def dfs(v):
    visited_dfs[v] = True
    dfs_result.append(v)
    for nxt in graph[v]:
        if not visited_dfs[nxt]:
            dfs(nxt)

dfs(V)
print(*dfs_result)   # 공백 구분 출력

# --- BFS (deque) ---
visited_bfs = [False] * (N + 1)
bfs_result = []
queue = deque([V])
visited_bfs[V] = True

while queue:
    v = queue.popleft()
    bfs_result.append(v)
    for nxt in graph[v]:
        if not visited_bfs[nxt]:
            visited_bfs[nxt] = True
            queue.append(nxt)

print(*bfs_result)

