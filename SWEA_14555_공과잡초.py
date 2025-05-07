'''
() 면 공임
ㅣ+) 공임
(+ㅣ 도 공임

이 경우를 더하면 됨.

'''

T = int(input())
for tc in range(1, T+1):
    grass = input()
    count = 0
    
    for i in range((len(grass))):
        if (grass[i] == '(') and (grass[i+1] == '|'):
            count += 1
        if (grass[i] == ')') and (grass[i-1] == '|'):
            count += 1
        if (grass[i] == '(') and (grass[i+1] == ')'):
            count += 1
    
    print(f'#{tc} {count}')