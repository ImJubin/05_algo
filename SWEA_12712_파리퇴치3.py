'''
1. 델타
2. 끝까지 들어가서 다 더해주기
3. 최댓값 구하기
'''
#델타
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

xdr = [-1, -1, 1, 1]
xdc = [-1, 1, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]

    max_val = 0

    for i in range(N):
        for j in range(N):
            start = flies[i][j]
            # r = i
            # c = j

            # 끝까지 들어가 다 더해주기
            
            for dir in range(4):
                for distance in range(1, M):
                    nr = i + dr[dir]*distance
                    nc = j + dc[dir]*distance
                    if 0<=nr<N and 0<=nc<N:
                        start += flies[nr][nc]
                    #최댓값뽑기
            if max_val < start:
                max_val = start
            # 끝까지 들어가 다 더해주기

            x_start = flies[i][j]
            for dir in range(4):
                for distance in range(1, M):
                    nr = i + xdr[dir]*distance
                    nc = j + xdc[dir]*distance
                    if 0<=nr<N and 0<=nc<N:
                        x_start += flies[nr][nc]
                    #최댓값뽑기
            if max_val < x_start:
                max_val = x_start

    print(f'#{tc} {max_val}')