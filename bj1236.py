'''
bj1236의 Docstring

문제
영식이는 직사각형 모양의 성을 가지고 있다. 성의 1층은 몇 명의 경비원에 의해서 보호되고 있다. 영식이는 모든 행과 모든 열에 한 명 이상의 경비원이 있으면 좋겠다고 생각했다.

성의 크기와 경비원이 어디있는지 주어졌을 때, 몇 명의 경비원을 최소로 추가해야 영식이를 만족시키는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 성의 세로 크기 N과 가로 크기 M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 성의 상태가 주어진다. 성의 상태는 .은 빈칸, X는 경비원이 있는 칸이다.

출력
첫째 줄에 추가해야 하는 경비원의 최솟값을 출력한다.

'''

# INPUT
N, M = map(int, input().split())
rows = []
for n in range(N):
    rows.append(list(input()))


X_rows = set()
X_cols = set()

for i in range(N):
    for j in range(M):
        if rows[i][j] == 'X':
            X_rows.add(i)
            X_cols.add(j)


# X가 없는 행과 열의 갯수
empty_rows = N - len(X_rows)
empty_cols = M - len(X_cols)

print(max(empty_rows, empty_cols))

# # 야메
# row_projection = ['.']*M

# for row in rows:
#     for i, c in enumerate(row_projection):
#         if row[i] == 'X':
#             row_projection[i] = 'X'

# # col 기준 X 아닌갯수 & row 기준 X 아닌갯수 -> 세서 max 값 배치
# cnt_nonX_in_col = 0

# for c in row_projection:
#     if c == '.':
#         cnt_nonX_in_col+= 1        

# # cnt_nonX_in_col =  row_projection

# print(row_projection)
# print(cnt_nonX_in_col)