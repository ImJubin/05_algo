''' 
규칙

비교 인덱스
* 짧은 리스트 : 인덱스 변화 없음
* 긴 리스트 : 인덱스 증가

총 비교 횟수 = 긴 리스트 길이 - 짧은 리스트 길이 + 1

목적 : 마주보는 숫자를 곱한 뒤 모두 합해서 최대 값을 구하는 것
'''
'''
입력 조건
Ai (i = 1 ~ N) : A1, A2, ... , AN
Bj (j = 1 ~ M) : B1, B2, ... , BM

3 <= N, M <= 20
T : 테스트 케이스 갯수
N, M : 테스트 케이스의 첫 번째 줄
Ai : 두 번째 줄
Bj : 세 번째 줄
'''

T = int(input())    # 테스트 케이스 갯수
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))

    # print(N, M, Ai, Bj)

    # 어느 것이 더 긴 리스트 인지 확인
    # why? 긴 리스트의 인덱스를 변화하면서 비교해야 하기 때문
    if N < M:   # B가 긴 리스트
        long = Bj
        short = Ai
        count = M - N + 1
    else:
        long = Ai
        short = Bj
        count = N - M + 1   # 비교 횟수

    # 조건 표현식으로 나타낼 수 도 있음 (가독성이 안 좋아 질 수 있음)
    # long, short = Bj, Ai if N < M else Ai, Bj

    max_value = 0
    for i in range(count):
        total = 0   # 곱의 합을 저장하는 변수
        for idx in range(len(short)):   # 비교 인덱스는 짧은 리스트 기준
            total += short[idx] * long[idx + i] # 두 수의 곱을 더하기
        # 곱의 모든 합을 구하고 나서 최대 인지 확인
        if max_value < total:
            max_value = total

    print(f'#{tc} {max_value}')