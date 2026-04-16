'''
bj1145의 Docstring

문제
다섯 개의 자연수가 있다. 이 수의 적어도 대부분의 배수는 위의 수 중 적어도 세 개로 나누어 지는 가장 작은 자연수이다.

서로 다른 다섯 개의 자연수가 주어질 때, 적어도 대부분의 배수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 다섯 개의 자연수가 주어진다. 100보다 작거나 같은 자연수이고, 서로 다른 수이다.

출력
첫째 줄에 적어도 대부분의 배수를 출력한다.

'''
# NOTE
'''
완전탐색? ㄴㄴ GCD, LCM

'''

# INPUT
Ns = list(map(int, input().split())) # 5개 자연수를 입력으로 받음, sep=' '

# SORTING
Ns = sorted(Ns) # 오름차순 sorted

# 계산범위
upperbound = Ns[4]*Ns[3]*Ns[2] # maximum 

# 완전탐색
for candidate in range(1, upperbound):
    cnt = 0

    for N in Ns:
        if candidate % N == 0:
            cnt+= 1

    if cnt >= 3:
        break

print(candidate)
    
    


# GCD, LCM 이용

# GCD 함수 (유클리드 호제법)
def gcd(a, b): # a > b
    while b: # 나머지가 0이 될 때 까지
        a, b = b, a % b

    return a

# LCM 함수
def lcm(a, b):
    return a * b // gcd(a, b)

# 5개 중 3개 조합으로 LCM 계산
min_result = float('inf')

for i in range(5):
    for j in range(i+1, 5):
        for k in range(j+1, 5):
            result = lcm(lcm(Ns[i], Ns[j]), Ns[k])
            min_result = min(min_result, result)

print(min_result)