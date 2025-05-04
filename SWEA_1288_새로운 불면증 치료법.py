'''
N
2N
0부터 9까지 다 들어갈 때까지 N에다가 1, 2, 3,,, K 곱하기. 

'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    sleep = set()
    cnt = 0
    while (len(sleep)<10):
        cnt += 1
        num = N*cnt
        nums = str(num)
        for i in range(len(nums)):
            sleep.add(nums[i])

    print(f'#{tc} {nums}')