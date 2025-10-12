print(10%3)

while input != "q":
    number = input("Enter a number to see if it is odd orr even: ('q' to quit)")
    if number == 'q':
        break
    if int(number) % 2 == 0:
        print("number is even")
    else:
        print("Number is odd")