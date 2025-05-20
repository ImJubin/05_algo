'''
1. 길이 : r2와 r1 겹치는 부분 count
2. 높이 : c2와 c1 겹치는 부분 count


3
2 2 4 5
3 3 6 6
1 2 3 3
3 6 6 8
2 2 4 5
4 3 7 6

#1 3 2
#2 0 0
#3 3 1

'''
T = int(input())
for tc in range(1,T+1):
    redr1, redc1, redr2, redc2 = map(int, input().split())
    bluer1, bluec1, bluer2, bluec2 = map(int, input().split())

    r_count = 0
    c_count = 0


    for i in range(redr1,redr2+1):
        for j in range(bluer1,bluer2+1):
            if i==j:
                r_count += 1
    
    for i in range(redc1,redc2+1):
        for j in range(bluec1,bluec2+1):
            if i==j:
                c_count += 1
    
    if r_count == 0:
        c_count = 0
    if c_count == 0:
        r_count = 0


    # print(fr_count)


    print(f'#{tc} {c_count} {r_count}')