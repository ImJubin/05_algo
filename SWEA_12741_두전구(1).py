'''
 
3
1 3 5 7
0 5 2 4
0 5 1 6
 
#1 0
#2 2
#3 4
 
낑겨있는 ij의 차이 구하기
낑겨있다?
A~B
C~D
사이 겹치는 구간 길이구하기
안겹치면 0 출력
그럼 ABCD로 쪼개놓는 게 편할까, 리스트 값으로 넣는 게 편할 까 ?
 
1) B가 C보다 커야 겹쳐짐. 안겹쳐지면 값은 0
2) B가 C보다 큰 경우
ABCD를 작은 순으로 정렬시킨 뒤, 3번째 값 - 2번째 값 하면 겹치는 구간 구할 수 있음.
'''
T = int(input())
for tc in range(1,T+1):
    A,B,C,D = map(int, input().split())
    ans = 0
    bright = []
    if B < C:
        ans = 0
    else:
        bright.append(A)
        bright.append(B)
        bright.append(C)
        bright.append(D)
        # print(bright)
        bright.sort()
        # print(bright)
        for i in range(len(bright)):
            ans = bright[2]-bright[1]
         
    print(f'#{tc} {ans}')