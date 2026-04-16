# 코딩 테스트 풀이 정리

백준 온라인 저지 풀이 모음 및 복습 노트

---

## 풀이 목록

### 기본 입출력
| 번호 | 파일 | 문제 제목 |
|------|------|-----------|
| 1000 | [io-1000.py](io-1000.py) | A+B |
| 1001 | [io-1001.py](io-1001.py) | A-B |

### 문자열
| 번호 | 파일 | 문제 제목 |
|------|------|-----------|
| 1032 | [string-1032.py](string-1032.py) | 명령 프롬프트 |
| 1157 | [string-1157.py](string-1157.py) | 단어 공부 |
| 1259 | [string-1259.py](string-1259.py) | 팰린드롬수 |

### 수학 / 완전탐색
| 번호 | 파일 | 문제 제목 |
|------|------|-----------|
| 1037 | [math-1037.py](math-1037.py) | 약수 |
| 1145 | [bruteforce-1145.py](bruteforce-1145.py) | 적어도 대부분의 배수 |

### 그리디 / 시뮬레이션 / 구현
| 번호 | 파일 | 문제 제목 |
|------|------|-----------|
| 1080 | [greedy-1080.py](greedy-1080.py) | 행렬 |
| 1110 | [simulation-1110.py](simulation-1110.py) | 더하기 사이클 |
| 1236 | [greedy-1236.py](greedy-1236.py) | 성 지키기 |
| 1292 | [implementation-1292.py](implementation-1292.py) | 쉽게 푸는 문제 |

### 스택 / 큐 / 힙
| 번호 | 파일 | 문제 제목 |
|------|------|-----------|
| 1874 | [stack-1874.py](stack-1874.py) | 스택 수열 |
| 9012 | [stack-9012.py](stack-9012.py) | 괄호 |
| 1966 | [queue-1966.py](queue-1966.py) | 프린터 큐 |
| 11286 | [heap-11286.py](heap-11286.py) | 절댓값 힙 |

### 이분탐색
| 번호 | 파일 | 문제 제목 |
|------|------|-----------|
| 1920 | [binary-1920.py](binary-1920.py) | 수 찾기 |
| 2805 | [binary-2805.py](binary-2805.py) | 나무 자르기 |
| 1300 | [binary-1300.py](binary-1300.py) | K번째 수 |

### BFS / DFS
| 번호 | 파일 | 문제 제목 |
|------|------|-----------|
| 1260 | [bfs_dfs-1260.py](bfs_dfs-1260.py) | DFS와 BFS |
| 2178 | [bfs-2178.py](bfs-2178.py) | 미로 탐색 |
| 2206 | [bfs-2206.py](bfs-2206.py) | 벽 부수고 이동하기 |
| 7569 | [bfs-7569.py](bfs-7569.py) | 토마토 (3차원) |

### 다이나믹 프로그래밍
| 번호 | 파일 | 문제 제목 |
|------|------|-----------|
| 1463 | [dp-1463.py](dp-1463.py) | 1로 만들기 |
| 2193 | [dp-2193.py](dp-2193.py) | 이친수 |
| 9251 | [dp-9251.py](dp-9251.py) | LCS |
| 12865 | [dp-12865.py](dp-12865.py) | 평범한 배낭 |

---

## 복습 노트

### 기본 입출력

```python
import sys
input = sys.stdin.readline  # 입력이 많을 때 속도 향상

n = int(input())
a, b = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]
```

---

### 문자열

| 문제 | 핵심 |
|------|------|
| 1032 명령 프롬프트 | 첫 파일명 기준으로 다른 위치만 `?` 교체. 문자열은 immutable → `list()` 분해 후 `''.join()` |
| 1157 단어 공부 | `Counter(char.upper())` 또는 dict로 빈도수 집계. 최빈값 동률이면 `?` 출력 |
| 1259 팰린드롬수 | `N == N[::-1]` 또는 양끝 투포인터 비교 |

---

### 수학 / 완전탐색

| 문제 | 핵심 |
|------|------|
| 1037 약수 | 진짜 약수 중 `min * max = N`. 약수는 대칭 구조 |
| 1145 적어도 대부분의 배수 | 완전탐색 상한 = 가장 큰 세 수의 곱. LCM 조합으로 최적화 가능 |

---

### 그리디 / 시뮬레이션

| 문제 | 핵심 |
|------|------|
| 1080 행렬 | 좌상단부터 스캔, 다르면 3×3 flip. 순서대로 처리하면 이전 위치 재방문 불필요 |
| 1110 더하기 사이클 | 두 자리 수 XY → `Y + (X+Y)의 일의 자리`. 원래 수로 돌아올 때 종료 |
| 1236 성 지키기 | `set`으로 경비원 있는 행/열 수집. 빈 행수와 빈 열수 중 `max` |
| 1292 쉽게 푸는 문제 | `extend([i]*i)`로 수열 생성. `Seq[a-1:b]` 슬라이싱 합산 |

---

### 스택 / 큐 / 힙

| 문제 | 핵심 |
|------|------|
| 1874 스택 수열 | target까지 오름차순 push, top != target이면 NO |
| 9012 괄호 | `(` 카운터 증가, `)` 감소. 음수되면 즉시 NO, 끝에 0이면 YES |
| 1966 프린터 큐 | `(우선순위, 인덱스)` deque. 더 높은 우선순위 존재 시 맨 뒤로 |
| 11286 절댓값 힙 | `heapq.heappush(heap, (abs(x), x))` → 절댓값 기준 정렬, 동률 시 음수 우선 |

---

### 이분탐색

| 문제 | 핵심 |
|------|------|
| 1920 수 찾기 | `bisect_left` 또는 `set()`. O(log N) |
| 2805 나무 자르기 | 파라메트릭 서치. `is_valid(mid)`: 얻는 나무 합 >= M. 최댓값 탐색이므로 가능하면 lo↑ |
| 1300 K번째 수 | `count_le(mid) = sum(min(mid//i, N))`. 개수 >= K이면 hi↓, ans 갱신 |

**이분탐색 템플릿**
```python
lo, hi = 0, max_val
ans = -1
while lo <= hi:
    mid = (lo + hi) // 2
    if is_valid(mid):
        ans = mid
        lo = mid + 1   # 최댓값 탐색
        # hi = mid - 1 # 최솟값 탐색
    else:
        hi = mid - 1   # 최댓값 탐색
        # lo = mid + 1 # 최솟값 탐색
```

---

### BFS / DFS

| 문제 | 핵심 |
|------|------|
| 1260 DFS와 BFS | DFS 재귀 + BFS deque. 인접리스트 정렬 필수 (낮은 번호 우선) |
| 2178 미로 탐색 | BFS = 최단 경로. `dist` 배열에 거리 직접 기록 |
| 2206 벽 부수고 이동 | `visited[x][y][broke]` 3차원. 벽은 `broke==0`일 때만 부수고 이동 |
| 7569 토마토 (3D) | 다중 출발지 BFS (익은 토마토 전부 큐에 넣고 시작). 6방향 이동 |

**BFS 템플릿**
```python
from collections import deque
queue = deque([(sx, sy)])
visited[sx][sy] = True
while queue:
    x, y = queue.popleft()
    for nx, ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
        if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
            visited[nx][ny] = True
            queue.append((nx, ny))
```

---

### 다이나믹 프로그래밍

| 문제 | 점화식 |
|------|--------|
| 1463 1로 만들기 | `dp[i] = min(dp[i-1], dp[i//2]?, dp[i//3]?) + 1` |
| 2193 이친수 | `dp[i][0] = dp[i-1][0]+dp[i-1][1]` / `dp[i][1] = dp[i-1][0]` (피보나치 구조) |
| 9251 LCS | `A[i]==B[j]`: `dp[i][j]=dp[i-1][j-1]+1` / 다름: `max(dp[i-1][j], dp[i][j-1])` |
| 12865 배낭 | 1D: `dp[w] = max(dp[w], dp[w-W]+V)` — **w를 역순 순회** (중복 방지) |

---

## 자주 쓰는 패턴

```python
# 빠른 입력
import sys
input = sys.stdin.readline

# 재귀 제한 해제 (DFS)
sys.setrecursionlimit(10000)

# 최대공약수 / 최소공배수
from math import gcd
lcm = lambda a, b: a * b // gcd(a, b)

# 조합
from itertools import combinations
for combo in combinations(arr, 3): ...

# 빈도수
from collections import Counter
cnt = Counter(s.upper())

# 힙
import heapq
heapq.heappush(h, val)
heapq.heappop(h)

# 이분탐색
from bisect import bisect_left, bisect_right
```


```python
# 공백으로 구분된 여러 값 한 번에 받기
A, B = map(int, input().split())
```

- `input().split()` → 공백 기준으로 나눠 리스트 반환
- `map(int, ...)` → 리스트의 각 원소에 `int` 변환 적용
- 여러 줄 입력은 리스트 컴프리헨션: `[input() for _ in range(n)]`

---

### 2. 문자열 패턴 매칭 (1032 - 명령 프롬프트)

**핵심 아이디어**: 첫 파일명을 기준으로, 나머지와 비교하며 다른 위치만 `?`로 교체

```python
pattern = list(filenames[0])
for i in range(1, n):
    for j in range(len(pattern)):
        if pattern[j] != '?' and filenames[i][j] != pattern[j]:
            pattern[j] = '?'
result = ''.join(pattern)
```

**복습 포인트**
- 문자열은 `list()`로 분해해야 개별 원소 수정 가능 (문자열은 immutable)
- `''.join(list)` 로 다시 문자열 합치기
- 타입 힌트 활용: `from typing import List` → `List[str]`

---

### 3. 약수 (1037)

**핵심 아이디어**: 진짜 약수 중 최솟값 × 최댓값 = N

```python
result = min(divisors) * max(divisors)
```

- N의 진짜 약수(1과 N 제외)가 모두 주어졌을 때, 가장 작은 약수와 가장 큰 약수의 곱이 N
- 약수는 대칭 구조: `d` 가 약수이면 `N/d` 도 약수

---

### 4. 행렬 (1080) - 그리디

**핵심 아이디어**: 좌상단부터 순서대로 스캔 → A[i][j] ≠ B[i][j] 이면 반드시 (i,j)를 좌상단으로 하는 3×3을 flip

```python
for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            A = flip(A, i, j)
            cnt_filp += 1
```

**복습 포인트**
- 좌상단부터 처리하면 이미 처리한 위치는 다시 건드리지 않아도 됨 → 그리디 정당성
- 최종적으로 `A == B` 인지 확인해 불가능한 경우 `-1` 출력
- 2중 for문으로 부분행렬 뒤집기: `range(i, i+3)`

---

### 5. 더하기 사이클 (1110) - 시뮬레이션

**연산 규칙**: 두 자리 수 XY → 새 수 = Y(X+Y의 일의 자리)

```python
right_num = str(int(N[0]) + int(N[1]))[-1]  # 합의 일의 자리
left_num = N[-1]                              # 기존 수의 일의 자리
new_N = left_num + right_num
```

**복습 포인트**
- 한 자리 수 입력도 두 자리로 처리: `if len(orig_N) == 1: orig_N = '0' + orig_N`
- 종료 조건: 원래 수로 돌아올 때 (순환 탐지)
- `global` 변수 또는 반환값으로 카운터 관리
- 문자열 인덱싱으로 각 자릿수 접근: `N[0]`, `N[-1]`

---

### 6. 적어도 대부분의 배수 (1145) - 완전탐색 / LCM

**핵심 아이디어**: 3개 이상의 수로 나누어지는 가장 작은 자연수 탐색

```python
for candidate in range(1, upperbound):
    cnt = sum(1 for N in Ns if candidate % N == 0)
    if cnt >= 3:
        break
```

**복습 포인트**
- 완전탐색 상한: 가장 큰 세 수의 곱 (`Ns[4]*Ns[3]*Ns[2]`)
- 더 효율적인 방법: 5C3 = 10가지 조합 각각의 LCM을 구해 최솟값
  ```python
  from math import gcd
  from itertools import combinations
  def lcm(a, b): return a * b // gcd(a, b)
  ```
- 유클리드 호제법: `gcd(a, b) = gcd(b, a % b)`

---

### 7. 단어 공부 (1157) - 딕셔너리

**핵심 아이디어**: 딕셔너리로 각 알파벳 등장 횟수 카운트

```python
count_dict = {}
for c in char:
    c = c.upper()
    count_dict[c] = count_dict.get(c, 0) + 1
```

**복습 포인트**
- `str.upper()` / `str.lower()` 로 대소문자 통일
- `dict.get(key, default)` → KeyError 없이 기본값 반환
- 더 간결한 방법: `from collections import Counter`
  ```python
  from collections import Counter
  cnt = Counter(char.upper())
  # cnt.most_common(1) 로 최빈값 바로 접근
  ```
- 최빈값이 여럿일 때 `?` 출력 처리 주의

---

### 8. 성 지키기 (1236) - 그리디 + 집합

**핵심 아이디어**: 경비원이 없는 행 수와 없는 열 수 중 큰 값을 추가

```python
X_rows = set()
X_cols = set()
for i in range(N):
    for j in range(M):
        if rows[i][j] == 'X':
            X_rows.add(i)
            X_cols.add(j)

empty_rows = N - len(X_rows)
empty_cols = M - len(X_cols)
print(max(empty_rows, empty_cols))
```

**복습 포인트**
- `set()`으로 중복 없이 인덱스 수집 → `len(set)` 으로 커버된 행/열 수 파악
- 빈 행과 빈 열 중 더 많은 쪽에 맞춰 배치 → `max()`
- 한 경비원이 행과 열 모두 커버 가능하므로 두 값의 최댓값이 답

---

### 9. 팰린드롬수 (1259) - 두 포인터

**핵심 아이디어**: 문자열의 양 끝에서 중앙으로 비교

```python
for l in range(len(N) // 2):
    if N[l] != N[len(N)-1-l]:
        ans = 'no'
        break
```

**복습 포인트**
- 더 간결한 방법: `N == N[::-1]` (슬라이싱 역순)
- 입력 종료 조건 `'0'` 처리: `while True` + `break`
- 여러 테스트 케이스 결과를 리스트에 모아 출력하거나 즉시 출력

---

### 10. 쉽게 푸는 문제 (1292) - 수열 구현

**규칙**: 1이 1번, 2가 2번, 3이 3번, ... 반복되는 수열의 구간 합

```python
Seq = []
i = 1
while len(Seq) < b:
    Seq.extend([i] * i)
    i += 1
print(sum(Seq[a-1:b]))
```

**복습 포인트**
- `list.extend([val] * n)` 으로 같은 값을 n번 추가
- 슬라이싱 인덱스 주의: 1-indexed 입력 → `Seq[a-1:b]` (b는 포함이므로 그대로)
- 수열 길이가 b 이상이 될 때까지만 생성 → 충분한 길이만큼만 만들기

---

## 자주 쓰는 패턴 정리

### 입력 처리
```python
# 정수 1개
n = int(input())

# 공백 구분 여러 정수
a, b = map(int, input().split())

# n줄 받아 리스트로
lines = [input() for _ in range(n)]

# 2D 배열 (문자)
grid = [list(input()) for _ in range(n)]

# 종료조건 있는 반복 입력
while True:
    x = input()
    if x == '0': break
```

### 자주 쓰는 내장 함수
```python
min(), max()          # 최솟값, 최댓값
sum()                 # 합계
sorted(), sort()      # 정렬
set()                 # 중복 제거 / 집합 연산
''.join(list)         # 리스트 → 문자열
list(str)             # 문자열 → 문자 리스트
str[::-1]             # 문자열 뒤집기
Counter(iterable)     # 빈도수 계산 (collections)
combinations(iter,r)  # 조합 (itertools)
gcd(a, b)             # 최대공약수 (math)
```
