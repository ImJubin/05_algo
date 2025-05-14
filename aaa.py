for _ in range(4):
    square = list(map(int, input().split()))
        
    if square[0] < square[4]:
        square_1 = square[0:4]
        square_2 = square[4:8]
    elif square[0] == square[4] and square[2] > square[6]:
        square_1 = square[0:4]
        square_2 = square[4:8]
    else:
        square_2 = square[0:4]
        square_1 = square[4:8]

    answer = 'z'

    if square_1[2] < square_2[0]:
        answer = 'd'
    elif square_1[2] == square_2[0] and square_1[1] == square_2[3]:
        answer = 'c'
    elif square_1[2] == square_2[0] or square_1[1] == square_2[3]:
        answer = 'b'
    else:
        answer = 'a'

    print(answer)
