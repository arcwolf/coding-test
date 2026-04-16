# 코딩 테스트 풀이 정리

백준 온라인 저지 풀이 모음 및 복습 노트

---

## 풀이 목록

| 번호 | 파일 | 문제 제목 | 분류 |
|------|------|-----------|------|
| 1000 | [baekjoon1000.py](baekjoon1000.py) | A+B | 기본 입출력 |
| 1001 | [baekjoon1001.py](baekjoon1001.py) | A-B | 기본 입출력 |
| 1032 | [bj1032.py](bj1032.py) | 명령 프롬프트 | 문자열 |
| 1037 | [bj1037.py](bj1037.py) | 약수 | 수학 |
| 1080 | [bj1080.py](bj1080.py) | 행렬 | 그리디 |
| 1110 | [bj1110.py](bj1110.py) | 더하기 사이클 | 시뮬레이션 |
| 1145 | [bj1145.py](bj1145.py) | 적어도 대부분의 배수 | 완전탐색 / 수학 |
| 1157 | [bj1157.py](bj1157.py) | 단어 공부 | 문자열 |
| 1236 | [bj1236.py](bj1236.py) | 성 지키기 | 그리디 |
| 1259 | [bj1259.py](bj1259.py) | 팰린드롬수 | 문자열 |
| 1292 | [bj1292.py](bj1292.py) | 쉽게 푸는 문제 | 수열 / 구현 |

---

## 복습 노트

### 1. 기본 입출력 (1000, 1001)

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
