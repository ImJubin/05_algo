'''
2
5 3
0 0 1 1 1
1 1 1 1 0
0 0 1 0 0
0 1 1 1 1
1 1 1 0 1
5 3
1 0 0 1 0
1 1 0 1 1
1 0 1 1 1
0 1 1 0 1
0 1 1 1 0
'''

T= int(input())
for tc in range(1, T+1):
    N, K = list(map(int, input().split()))
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    # print(puzzle)
    
    for i in range(N):
        length = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                length += 1
            else:
                if length == K:
                    cnt += 1
                length=0
        if length == K:
            cnt += 1

    for j in range(N):
        length = 0
        for i in range(N):
            if puzzle[i][j] == 1:
                length += 1 #계속 세
            else:
                if length == K: #0 이면 줄 끊김
                    cnt += 1 # K이면 기록
                length=0    #그 다음 0 초기화
        if length == K:
            cnt += 1

    print(f'#{tc} {cnt}')