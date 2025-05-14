'''
3
3 3
0 1 0
0 1 0
0 1 0
3 3
0 1 0
1 1 1
0 0 0
8 8
0 0 0 0 0 0 1 0
0 1 1 1 1 0 1 0
0 0 0 0 0 0 1 0
0 0 0 1 0 0 1 0
0 0 0 1 0 0 1 0
0 1 1 0 0 0 1 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
 
구해야 할 것 
: 가장 긴 구조물의 길이.
 
T
N*M의 배열
행 : N, 열 : M 
2차원 배열 : land
구조물 길이 : length
가장 긴 구조물 길이 : max_length
 
어떻게?
1. 행순회
    연속된 1 개수 세주기.
        1길이가 1뿐이면 세주는거 break
         
2. 열순회
    for문 i j 바꾸면됨
 
3. 구조물 길이들 빈리스트에 담은 후, 최댓값 뽑기
구조가 하나도 없다면 0 출력
 
 
'''
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    land = [list(map(int, input().split())) for _ in range(N)]
    max_length = 0
    #1. 행순회
    for i in range(N):
        length = 0
        for j in range(M):
            if land[i][j] == 1: #1 만나면 길이+1
                length += 1           
                if max_length < length:
                    max_length = length
            else:
                length = 0
                     
            # print(length,"가로길이")
 
    if max_length == 1:
        max_length = 0
 
    # #2. 열순회
    for j in range(M):
        length = 0
        for i in range(N):
 
            if land[i][j] == 1: #1 만나면 길이+1
                length += 1                 
                if max_length < length:
                    max_length = length
            else:
                length = 0
                 
            # print(length,"세로길이")
 
    if max_length == 1:
        max_length = 0
 
        # print(max_length, "찐길이")
 
    print(f'#{tc} {max_length}')