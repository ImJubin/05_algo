'''
1. 델타
2. 끝까지 들어가서 다 더해주기
3. 최댓값 구하기
'''
T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]
    max_value = 0
            #지점찍기
    for r in range(N):
        for c in range(N):                
            start = flies[r][c]

            dr = [-1, 1, 0, 0]
            dc = [0, 0, -1, 1]
        
            #사방탐색, 값을 더해야 함
            for dir in range(4):
                for distance in range(1,M):
                    nr = r + dr[dir]*distance
                    nc = c + dc[dir]*distance
                    if 0<= nr< N and 0<= nc <N:
                        start += flies[nr][nc]
            if max_value < start:
                max_value = start

            # 대각선을 어케함 ?????
            dr = [1, 1, -1, -1]
            dc = [1, -1, -1, 1]
            start = flies[r][c]
            for dir in range(4):
                for distance in range(1,M):
                    nr = r + dr[dir]*distance
                    nc = c + dc[dir]*distance
                    if 0<= nr< N and 0<= nc <N:
                        start += flies[nr][nc]
            if max_value < start:
                max_value = start
            
    print(f'#{tc} {max_value}')
