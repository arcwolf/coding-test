'''
[BOJ 1874] 스택 수열

문제
1부터 n까지의 수를 스택에 넣었다가 뽑아 수열을 만들 수 있다.
스택에는 반드시 오름차순으로 push해야 한다.
임의의 수열이 주어졌을 때, 그 수열을 만들기 위해 필요한 push/pop 연산의 순서를 출력하라.
만약 만들 수 없으면 NO를 출력한다.

입력
- 첫째 줄: n (1 ≤ n ≤ 100,000)
- 둘째 줄부터 n개의 줄: 수열의 각 원소

출력
- push는 +, pop은 -를 한 줄에 하나씩 출력
- 불가능하면 NO 출력

예시)
n = 8
수열: 4 3 6 8 7 5 2 1
출력:
+ + + + - - + + - + + - - - - -
'''

import sys
input = sys.stdin.readline

n = int(input())
sequence = [int(input()) for _ in range(n)]

stack = []
result = []
current = 1   # 다음에 push할 숫자 (1부터 오름차순)
possible = True

for target in sequence:
    # target이 될 때까지 오름차순으로 push
    while current <= target:
        stack.append(current)
        result.append('+')
        current += 1

    # 스택 top이 target과 같으면 pop
    if stack and stack[-1] == target:
        stack.pop()
        result.append('-')
    else:
        # top이 target보다 작으면 이미 지나쳐서 불가능
        possible = False
        break

if possible:
    print('\n'.join(result))
else:
    print('NO')

