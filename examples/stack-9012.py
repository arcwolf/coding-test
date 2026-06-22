'''
[BOJ 9012] 괄호

문제
괄호 문자열(Parenthesis String)이란 '(' 와 ')' 로만 이루어진 문자열이다.
올바른 괄호 문자열(Valid PS)이 되려면:
1. 빈 문자열은 올바른 괄호 문자열
2. S가 올바른 괄호 문자열이면 (S)도 올바른 괄호 문자열
3. S, T가 올바른 괄호 문자열이면 ST도 올바른 괄호 문자열

입력
- 첫째 줄: 테스트 케이스 수 T
- 각 줄: 괄호 문자열

출력
- 각 줄마다 올바른 괄호 문자열이면 YES, 아니면 NO

핵심
- 스택(또는 카운터)으로 '(' 를 push, ')' 를 만나면 pop
- 마지막에 스택이 비어있으면 YES
'''

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    s = input().strip()
    cnt = 0       # 열린 괄호 개수 (스택 대신 카운터로 대체)
    valid = True

    for c in s:
        if c == '(':
            cnt += 1
        else:             # ')'
            cnt -= 1
            if cnt < 0:   # 닫는 괄호가 더 많아지면 즉시 불가
                valid = False
                break

    # 끝까지 봤을 때 열린 괄호가 남아있어도 불가
    if valid and cnt == 0:
        print('YES')
    else:
        print('NO')

