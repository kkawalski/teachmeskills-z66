while True:
    number = int(input("Enter number "))
    i = 0
    s = 0
    while i <= number:
        if i % 5 != 0:
            if s + i > 100:
                print("Need less")
                break
            s += i
        i += 3
    else:
        if s + i <= 100:
            print("Need more")
            continue
        elif number % 3 != 0:
            print("Need less")
            continue
        print("Exactly!")
        print("Sum", s)
        break
        
