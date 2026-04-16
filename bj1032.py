"""
dir *.exe
 "dir 패턴"
  dir a?b.exe

검색 결과가 먼저 주어졌을 때, 패턴으로 뭘 쳐야 그 결과가 나오는지를 출력하는 문제이

"""

'''
입력 패턴: 

3
config.sys
config.inf
configures

출력 패턴:

config????

'''
from typing import List # type hint 작성 목적

# input
n: int = int(input())
filenames: List[str] = [input() for _ in range(n)]

# 패턴 찾기
pattern: List[str] = list(filenames[0]) # 문자 하나하나 쪼개기
# print(pattern, type(pattern)) # 확인용

for i in range(1, n):
    for j in range(len(pattern)):
        if pattern[j] != '?' and filenames[i][j] != pattern[j]: # 비교/대조 통해서 다른 부분만 ? 로 치환
            pattern[j] = '?'

result = ''.join(pattern)
# print(pattern, result) # 확인용

# output
print(result)
