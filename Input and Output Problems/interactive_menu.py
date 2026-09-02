print("Choose an option:" \
"\n1.Say Hello"\
"\n2.Calculate Square"\
"\n3.Exit")
option = int(input("Enter your choice (1-3): "))
match option:
    case 1:
        print("Hello!")
    case 2:
        number = int(input("Enter a number: "))
        print("The square of {} is {}".format(number, number**2))
    case 3:
        print("Exiting the program.")
    case _:
        print("Invalid option. Please choose a valid option (1-3).")