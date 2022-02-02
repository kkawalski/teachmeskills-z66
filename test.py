year = int(input("Enter year "))

if year % 4 == 0:
    print("Summer games")
elif year % 2 == 0:
    print("Winter games")
else:
    print("Non olympic year")

