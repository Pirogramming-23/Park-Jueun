import random

num = 0

def brGame(who):
    global num

    if who == "player":
        while True:
            try:
                n = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : "))
            except ValueError:
                print("정수를 입력하세요")
            else :
                if (n != 1 and n != 2 and n != 3):
                    print("1, 2, 3 중 하나를 입력하세요")
                else : break
    else :
        n = random.randint(1, 3)

    for i in range(n):
        num += 1
        print(who,":", num, sep="")
        if num == 31:
            return True
    return False
    

while True:
    x = brGame("computer")
    if x == True: 
        print("player win!")
        break
    x = brGame("player")
    if x == True: 
        print("computer win!")
        break
