'''
() 면 공임
ㅣ+) 공임
(+ㅣ 도 공임

이 경우를 더하면 됨.

'''

T = int(input())
for tc in range(1, T+1):
    grass = input()
    cnt = 0

    for i in range((len(grass))):
        if (i+1< len(grass)) and (grass[i] =='(') and (grass[i+1] == ')'):
            cnt += 1
        if (i+1< len(grass)) and (grass[i] =='(') and (grass[i+1] == 'ㅣ'):
            cnt += 1            
        if (0<=i-1) and (grass[i] ==')') and (grass[i-1] == 'ㅣ'):
            cnt += 1 

    print(f'#{tc} {cnt}')