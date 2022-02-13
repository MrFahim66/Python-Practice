print("Printing 1 to 50 fulfilling given conditions:")
for number in range(1, 50 + 1):
    if number % 3 == 0:
        print("bang")
    elif number % 5 == 0:
        print("YooHoo")
    elif number % 3 == 0 and number % 5 == 0:
        print("BangYooHoo")
    else:
        print(number)
