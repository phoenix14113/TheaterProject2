
import functions


theater = functions.createTheater(False)

NumberOfColumns = len(theater)
NumberOfRows = len(theater[0])

while True:
    # print the menu
    print("\n\n\n\n")
    print("This is the menus.\nEnter the number for the option you would like.\n")
    print("1. Print theater layout.")
    print("2. Purchase 1 or more seats.")
    print("3. Display theater statistics.")
    print("4. Reset theater.")
    print("5. Quit program.")
    # try:
    # collect user's decision on what function to use
    userChoice = str(input("\n\nWhich option would you like to select? "))

    if userChoice == '1':
        # displays the layout of the theater
        functions.printBoard(NumberOfRows, NumberOfColumns, theater)
        continue
    elif userChoice == '2':
        # allows users to purchase seats
        theater = functions.pickMultipleSeats(
            NumberOfRows, NumberOfColumns, theater)
        continue
    elif userChoice == '3':
        # displays how many seats have been purchased, how many seats left, and theater revenue
        functions.statistics(NumberOfRows, NumberOfColumns, theater)
        continue
    elif userChoice == '4':
        # resets the layout and seats taken in the theater
        # makes sure that the user really wants to completely reset the program
        print("Do you really want to do this. It will reset the entire theater")
        try:
            safeGuard = input("Enter '1' if you would like to proceed: ")
            if safeGuard == 1:
                theater = functions.createTheater(True)
                NumberOfColumns = len(theater)
                NumberOfRows = len(theater[0])
        except:
            continue
        continue
    elif userChoice == '5':
        # quits program
        print(
            "\nThank you for using my program. You will return to where you\nleft off when you come back.")
        print
        break
    else:
        print("invalid input 1")
    # except(NameError, SyntaxError):
    #    print("invalid input 2")
