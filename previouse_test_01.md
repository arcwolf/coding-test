# 이전 코딩 테스트 복기 - 01

## 문제 1

기억이 잘 나지 않아 생략.

---

## 문제 2. 이분탐색 - 파라메트릭 서치

### 문제 설명

배에 사람을 태우는데, **사람들의 무게**와 **배의 수(M)**가 주어졌을 때  
한 배에 태우는 **최적의 무게(상한선)**를 구하는 문제.

- 배에 사람들이 **주어진 순서대로** 타야 한다.
- 한 배의 무게 제한이 `mid`일 때, M대 이하의 배로 모든 사람을 태울 수 있으면 유효한 값.

### 입력 예시

```
10 6 4 3 8 9   # 사람들의 무게
4              # 배의 대수 M
```

### 출력 예시

```
11   # 한 배에 태울 수 있는 최적의 무게(최솟값)
```

---

### 풀이 코드

```python
def is_valid(mid):
    if weights[0] > mid:   # 첫 번째 사람이 이미 초과하면 불가
        return False
    weight_sum = 0
    ans = 1
    for i in range(len(weights)):
        weight_sum += weights[i]
        if weight_sum <= mid:
            continue
        else:
            weight_sum = 0
            weight_sum += weights[i]
            ans += 1
    return ans <= m

def f():
    lo = 0
    hi = sum(weights)
    mid = (lo + hi) // 2
    ans = -1
    while lo <= hi:
        if is_valid(mid):
            hi = mid - 1
            ans = mid
        else:
            lo = mid + 1
        mid = (lo + hi) // 2
    return ans

print(f())
```

---

### 핵심 아이디어

- **파라메트릭 서치**: "가능/불가능"을 판별하는 함수(`is_valid`)를 만들고, 이분탐색으로 경계값 탐색
- 탐색 범위: `lo = 0`, `hi = sum(weights)` (최대 한 배에 모두 태우는 경우)
- 최솟값 탐색이므로 `is_valid`이면 `hi`를 줄이고, `ans`를 갱신

### 주의사항

- `is_valid` 내부에서 첫 번째 사람의 무게가 `mid`를 초과하면 즉시 `False` 반환
- 순서를 바꿀 수 없으므로 그리디하게 앞에서부터 채움
- 이분탐색 종료 후 `ans == -1`이면 불가능한 케이스

---

## 문제 3. DFS (깊이 우선 탐색)

### 문제 설명

양식장(격자)에 물고기를 가두는데, 한 칸에는 물고기가 한 마리만 들어갈 수 있음.

- **연결된 물고기끼리는 같은 종**
- 같은 종의 물고기끼리 **한 그룹**에 가두려 할 때, 그 그룹을 감싸는 **최소 둘레 길이**를 구하라
- 모든 종을 다 가둘 필요는 없고, **같은 종을 가둘 수 있는 그룹 둘레의 최솟값**을 출력
- 그룹에 해당하는 물고기가 **1마리뿐**이면, 그 한 마리가 있는 곳의 둘레를 구하면 됨 (= 4)
- 위 그림 예시의 답: **12**

### 입력 형식

```
N = 6  # 물고기 수

# 각 물고기의 좌표 (0-indexed)
fish = [[0,1], [2,2], [5,5], [2,4], [4,4], [4,5]]
#        1번    2번    3번    4번    5번    6번

# 물고기 연결 정보 (같은 종)
# 연결 번호  i  j
#    1      1  2   → 물고기 1번 ↔ 2번
#    2      2  3   → 물고기 2번 ↔ 3번
#    3      4  5   → 물고기 4번 ↔ 5번
#    4      5  6   → 물고기 5번 ↔ 6번
```

### 풀이 코드

```python
N = 6
adj = [[0] * N for _ in range(N)]  # 인접 행렬
chk = [False] * N

def valid_coord(info, adj):
    for c in info:
        adj[c[0]-1][c[1]-1] = adj[c[1]-1][c[0]-1] = 1
    return adj

adj = valid_coord(info, adj)

def dfs(now):
    for nxt in range(N):
        if adj[now][nxt] == 1 and not chk[nxt]:
            chk[nxt] = True
            dfs(nxt)

idx_list = []
for i in range(N):
    if not chk[i]:
        chk = chk.copy()
        chk[i] = True
        dfs(i)
        idx_list.append([l for l in range(N) if chk_grp[l] != chk[l]])

# 각 그룹별 물고기 좌표 묶기
grp_coord = []
for i in range(len(idx_list)):
    tmp = []
    for j in range(len(idx_list[i])):
        tmp.append(fish[idx_list[i][j]])
    grp_coord.append(tmp)

# 각 그룹의 둘레(bounding box 둘레) 계산
size = []
for i in range(len(grp_coord)):
    x_list = list(map(lambda x: x[0], grp_coord[i]))
    y_list = list(map(lambda x: x[1], grp_coord[i]))
    x_min, x_max = min(x_list), max(x_list)
    y_min, y_max = min(y_list), max(y_list)
    size.append((x_max - x_min + 1) * 2 + (y_max - y_min + 1) * 2)

print(min(size))
```

---

### 핵심 아이디어

- **DFS**로 연결된 물고기끼리 같은 그룹으로 묶음
- 각 그룹에 속한 물고기 좌표의 **최솟값/최댓값**으로 bounding box 계산
- bounding box 둘레 = `(x범위 + 1) * 2 + (y범위 + 1) * 2`
- 모든 그룹의 둘레 중 **최솟값** 출력

### 주의사항

- 인접 행렬 초기화: `adj = [[0]*N for _ in range(N)]` (리스트 곱 중첩 시 얕은 복사 주의)
- 방문 체크 배열 `chk`를 그룹 탐색 시마다 스냅샷(`copy()`) 저장해 그룹 인덱스 추출
- 물고기가 1마리인 그룹은 bounding box 둘레가 자동으로 4가 됨
