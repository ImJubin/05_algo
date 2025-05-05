'''
A열 값과 B열 값을 곱하는데, 최댓값인 경우.
#롱, 숏 정하기
#인덱스 곱하기
#최댓값 뽑아내기.

'''
T = int(input())
for tc in range(1, T+1):

    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))
     
    #롱, 숏 정하기
    if N<M:
        short = Ai
        long = Bj
        cnt = M-N+1
    else:
        short = Bj
        long = Ai
        cnt = N-M+1
    
    #인덱스 곱하기
    max_value=0  
    for i in range(cnt):
        total = 0 #곱의 합 저장
        for idx in range(len(short)):
            total += short[idx] * long[idx+i] #두 수 곱한거 더해주기

    #최댓값 뽑아내기.
      
        if max_value < total:
            max_value = total

    print(f'#{tc} {max_value}')