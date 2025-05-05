'''
1. 델타
2. 끝까지 들어가서 다 더해주기
3. 최댓값 구하기
'''

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]
    for _ in range(N):
        flies = [list(map(int, input().split())) for _ in range(N)]
        #지점찍기
        for i in range(N):
            for j in range(N):                
                start = flies[i][j]
                r = i
                c = j

                #사방탐색    
                for dir in range(4):
                    nr = r + dr[dir]
                    nc = c + dc[dir]

                    r = nr
                    c = nc
                # 이제 값을 더해야 하는데.
                # 대각선을 어케함 ?????

                    


    
    
    print(f'#{tc}')
