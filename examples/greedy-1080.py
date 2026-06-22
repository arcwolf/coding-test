'''
bj1080의 Docstring

문제
0과 1로만 이루어진 행렬 A와 행렬 B가 있다. 이때, 행렬 A를 행렬 B로 바꾸는데 필요한 연산의 횟수의 최솟값을 구하는 프로그램을 작성하시오.

행렬을 변환하는 연산은 어떤 3×3크기의 부분 행렬에 있는 모든 원소를 뒤집는 것이다. (0 → 1, 1 → 0)

입력
첫째 줄에 행렬의 크기 N M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 행렬 A가 주어지고, 그 다음줄부터 N개의 줄에는 행렬 B가 주어진다.

출력
첫째 줄에 문제의 정답을 출력한다. 만약 A를 B로 바꿀 수 없다면 -1을 출력한다.


'''

### INPUT
N, M = map(int, input().split())

A = []
B = []

for _ in range(N):
    A.append(list(input()))

for _ in range(N):
    B.append(list(input()))

# print(A, B, N, M)

### SOLVE
def flip(A, i, j):
    for i_sub in range(i, i+3):
        for j_sub in range(j, j+3):
            A[i_sub][j_sub] = str(1 - int(A[i_sub][j_sub]))
    
    return A

cnt_filp = 0

for i in range(0, N-2):
    for j in range(0, M-2):
        if A[i][j] != B[i][j]:
            A = flip(A, i, j)
            cnt_filp+= 1


### OUTPUT
if A == B:
    print(cnt_filp)

else:
    print(-1)

# print(A)
