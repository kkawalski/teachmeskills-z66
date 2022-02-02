while True:
    x = int(input("Enter number "))
    if x == -1:
        print("Good bye")
        break
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")

