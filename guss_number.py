winning_number = 27
user_input = int(input(" guess number"))
if user_input==winning_number:
    print("you won!!!")
else:
    if user_input<winning_number:
        print("too low")
    else:
        print("too high")
