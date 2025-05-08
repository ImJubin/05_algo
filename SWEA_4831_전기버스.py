'''
정렬해야함 (무작위로 주어질 수 있기 때문)
충전기 지점에서, 더 갈 수 있는지 꼭 충전해야 하는지 체크
K, N, M

3
3 10 5
1 3 5 7 9
3 10 5
1 3 7 8 9
5 20 5
4 7 9 14 17

'''

T = int(input())
for tc in range(1, T+1):
    # K : 1회 충전 시 이동 가능 칸 수
    # N : 버스 정류장 종점 번호
    # M : 충전소 수
    # charges : 충전소 위치 리스트(길이 : M, 0 ~ M-1)
    K, N, M = map(int, input().split())
    charges = list(map(int, input().split()))
    charges.sort()

    # cur : 버스의 현 위치(인덱스 기준)
    # count : 누적 충전 횟수
    cur = count = 0
    

    while cur+K < N: 

        flag = False
        # 1. 다음 지점을 찾아라
        for i in range(len(charges)-1,-1,-1):
            # ㄱ. 다음 지점 발견
            if cur < charges[i] <= cur+K:
               cur = charges[i]
               count += 1
               flag = True
               break
            # print(cur ,count )
        
        # 2. 다음 지점을 찾지 못했을 때
        if not flag:
            count = 0
            break
                
    print(f'#{tc} {count}')