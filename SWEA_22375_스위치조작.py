'''
3
3
0 0 0
0 1 0
5
0 1 1 0 0
0 0 0 1 1
10
1 1 1 1 1 0 0 0 1 1
1 1 0 1 1 0 1 1 0 0

#1 2
#2 1
#3 3

'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Ai = list(map(int, input().split()))
    Bi = list(map(int, input().split()))
    count = 0
    
    for i in range(N):
        if Ai[i] != Bi[i]:
            for j in range(N):
                Bi[j] = (Bi[j]+1)%2
            count += 1

        

    print(f'#{tc} {count}' )