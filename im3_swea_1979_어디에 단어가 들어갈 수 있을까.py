'''
cnt
행 순회 해서 글자 카운트
연속K개 다 되었으면 브레이크
cnt에 1 적립


행순회 해서 하나씩 카운트
K개 다 되었으면 브레이크
cnt에 1 적립
'''

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    for i in range(N):
        length = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                length += 1
            else:
                if length == K:
                    cnt += 1
                length = 0

        if length == K:
            length = 0
            cnt += 1

    for j in range(N):
        length = 0
        for i in range(N):
            if puzzle[i][j] == 1:
                length += 1
            else:
                if length == K:
                    cnt += 1
                length = 0
                
        if length == K:
            length = 0
            cnt += 1

    print(f'#{tc} {cnt}')
