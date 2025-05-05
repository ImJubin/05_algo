'''

'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    #버정 경로리스트
    bus_stop =[]
    for _ in range(N):
        Ai, Bi = map(int, input().split())
        bus_stop.append((Ai,Bi))
        #버정 노선리스트
    P_list = []
    P = int(input())
    for _ in range(P):
        Cj = int(input())
        P_list.append(Cj)

        #방문 경로 세기
    bus_root_count = [0]*P
    for Ai, Bi in bus_stop:
        for i in range(len(P_list)):
            if Ai <= P_list[i]<=Bi:
                bus_root_count[i] += 1



    print(f'#{tc}', *bus_root_count)