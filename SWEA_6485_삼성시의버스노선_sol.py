T = int(input())

for tc in range(1, T + 1):
    """
    이 문제의 핵심은 버스 노선의 번호는 최대 5000
    이를 활용하여 모든 버스 정류장을 미리 초기화
    그렇지 않은 경우 시간 초과 발생
    """
    # 버스 정류장 초기화
    all_stations = [0 for _ in range(1, 5001)]
    # print(len(all_stations)) # 5000

    # 버스 노선의 개수
    N = int(input())

    # 버스 노선의 개수 만큼 반복을 돌면서
    for _ in range(N):
        # A이상 B이하의 정류장을 변수에 담고
        A, B = map(int, input().split())

        # 버스 노선 시작 ~ 끝까지 체크
        # index 기준으로는 -1을 해줘야 첫 번째 노선에 체크 된다.
        for i in range(A - 1, B):
            # 해당 노선에 포함되는 정류장은 1로 체크
            all_stations[i] += 1

    # 체크 해야 할 정류장 번호의 개수
    P = int(input())

    # 버스 정류장
    bus_stops = []
    for _ in range(1, P + 1):
        # check 할 정류장 번호
        check = int(input())

        # 해당하는 인덱스(정류장)에 버스 노선의 개수를 찾아서 bus_stops에 넣기
        # index라서 -1이 필요
        bus_stops.append(all_stations[check - 1])

    result = ' '.join(map(str, bus_stops))
    print(f'#{tc} {result}')