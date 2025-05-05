T = int(input())
for tc in range(1, T+1):
    bits = input()

    cnt = 0
    flag = False

    for bit in bits:
        if flag and bit == '0':
            cnt +=1
            flag = False
        
        elif not flag and bit == '1':
            cnt +=1
            flag = True
            
    print(f'#{tc} {cnt}')