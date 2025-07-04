num = 0
check = 0 #A순서인지 B순서인지 체크(0 이면 A, 1 이면 B)
finish = False #게임이 끝났는지 체크
while True:
    while True:
        try:
            n = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : "))
        except ValueError:
            print("정수를 입력하세요")
        else :
            if (n != 1 and n != 2 and n != 3):
                print("1, 2, 3 중 하나를 입력하세요")
            else : break

    for i in range(n):
        num += 1
        if check == 0: print("playerA:", num, sep="")
        else: print("playerB:", num, sep="")
        if num == 31:
            if (check == 0) : print("playerB win!")
            else : print("playerA win!")
            finish = True
            break
    if finish == True: break
    check = 1 - check