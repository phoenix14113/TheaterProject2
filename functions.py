'''
file name: functions.py
creator: Adam Taylor (taylad)
This file contains the funtions to run the theater program

a little difficult to understand in some spots
'''
import csv

def pickSeat(numberOfRows, numberOfColumns, theater):
    '''
    numberOfRows = the int number of rows that theater has
    numberOfColumns = the int number of columns that theater has
    theater = the list of lists that is the layout of the theater

    This function asks for a column and row to purchase a seat and
    then changes that position in the theater list to an x

    returns a new updated version of theater with a seat changed
    '''

    while True:
        print("\n\n\n\n")
        # Find what column a user wants to purchase from.
        while True:
            print("\n\n")
            try:
                chooseColumn = int(input("what column would you like? "))
                if chooseColumn > 0 and chooseColumn <= numberOfColumns-1:
                    break
                else:
                    print("invalid input")
            except(NameError, SyntaxError):
                print("invalid input")
        # Find what seat a user wants to purchase
        while True:
            print("\n\n")
            try:
                chooseSeat = int(input("what seat number would you like? "))
                if chooseSeat > 0 and chooseSeat <= numberOfRows:
                    break
                else:
                    print("invalid input")
            except(NameError, SyntaxError):
                print("invalid input")
        # check if seat is taken
        if theater[chooseColumn-1][chooseSeat-1] == 'x':
            print("That seat is already take. Try again.")
            continue

        # ask user if they want to buy the seat
        while True:
            print("You are currently purchasing seat " + str(chooseSeat) + " from column "
                  + str(chooseColumn) + " for $" + str(theater[numberOfColumns-1][chooseColumn-1]) + "\n")
            try:
                print("Type '1' if you would like to continue your purchase.")
                userContinue = input(
                    "Type anything else to not purchase this seat: ")
                if userContinue == 1:
                    newRow = []
                    # recreate the column the user is wanting to buy from except
                    # with their selected seat crossed out too
                    for i in range(numberOfRows):
                        if theater[chooseColumn-1][i] == 'x' or i == chooseSeat-1:
                            newRow.append('x')
                        else:
                            newRow.append('o')
                    theater[chooseColumn-1] = newRow
                    try:
                        input(
                            "\nYour purchase was succesful. Enter anything to continue. ")
                    except:
                        print
                    break
                else:
                    break
            except(NameError, SyntaxError):
                break

        # updates the list in the theater file
        with open("theater.cvs", "w") as fout:
            w = csv.writer(fout, delimiter=',')
            for i in range(numberOfColumns):
                w.writerow(theater[i])
        return theater


def pickMultipleSeats(numberOfRows, numberOfColumns, theater):
    '''
    numberOfRows = the int number of rows that theater has.
    numberOfColumns = the int number of columns that theater has.
    theater = the list of lists that is the layout of the theater.

    this function asks for how many seats the use wants and runs the pickseat
    that many times.

    returns a new updated version of theater (aka a list) with changed seats.
    '''
    print("\n\n\n\n")
    # ask how many seats a user would like to buy
    seatsPurchased = 0
    for i in range(numberOfColumns-1):
        for j in range(numberOfRows):
            if theater[i][j] == 'x':
                seatsPurchased += 1
    seatsLeft = ((numberOfColumns-1)*(numberOfRows)) - seatsPurchased
    if int(seatsLeft) == 0:
        try:
            print("There are no seats available")
            input("Enter anything to return to the menu. ")
        except:
            print
    while True:
        print("\n\n")
        try:
            SeatsToPurchase = input("How many seats would you like to buy? ")
            if SeatsToPurchase > 0 and SeatsToPurchase <= seatsLeft:
                break
            else:
                print("invalid input")
        except(NameError, SyntaxError):
            print("invalid input")
    # purchases however many seats the user indicated
    for i in range(int(SeatsToPurchase)):
        print("For seat " + str(i+1))
        theater = pickSeat(numberOfRows, numberOfColumns, theater)
    # updates the theater layout with the new purchased seats
    return theater


def printBoard(numberOfRows, numberOfColumns, theater):
    '''
    numberOfRows = the int number of rows that theater has.
    numberOfColumns = the int number of columns that theater has.
    theater = the list of lists that is the layout of the theater.

    displays the content of theater, without the price, in a grid. Shows what seats are taken
    with numbered rows and columns for reference

    no return
    '''
    # user instructions
    print
    print("'x' means the seat is already purchased.")
    print("'o' means the seat has not been pruchased.")
    print
    print("\tSeats")
    # number the seats rows (ones)
    currPlace1 = "        "
    for i in range(numberOfRows):
       if i == 0:
           currPlace1 += "0        "
       if (i+1) % 10 == 0:
           currPlace1 += str((i+1) / 10) + "         "
    currPlace2 = "        "
    j = 1
    for i in range(numberOfRows):
        if j % 10 == 0:
            j = 0
        currPlace2 += str(j)
        j += 1
    print(currPlace1)
    print(currPlace2)
    print

    # number the columns and print the layout of the theater
    for i in range(numberOfColumns-1):
        if i < 9:
            currRow = "Row " + str(i+1) + "   "
        else:
            currRow = "Row " + str(i+1) + "  "
        for j in range(numberOfRows):
            currRow = currRow + theater[i][j]
        print(currRow)
    print("\n\n")
    # wait to leave function until the user says to return
    try:
        input("Enter anything to return to the menu. ")
    except(NameError, SyntaxError):
        print


def createTheater(overwritefile):
    '''
    overwritefile = boolean that indicates weather you want to automatically overwrite the file or not

    builds a list full of lists to represent the layout of the theater
    contains 1 extra slot in each column to store the price of that column

    returns a list of lists
    '''
    # collect the length of each row

    # check if the file exists to be read from
    try:
        # automatically activates the exception if you want skip the file reading
        if overwritefile:
            1/0
        columns = []
        with open("theater.cvs", 'r') as fin:
            r = csv.reader(fin, delimiter=",")
            for rows in r:
                columns.append(rows)
    except:
        print("\n\n\n\n")
        while True:
            print("\n\n")
            try:
                rowsNumber = input(
                    "How many rows would you like in the theater\n" + 
                    "(greater than 0 and less than 100)? ")
                if int(rowsNumber) >= 100 or int(rowsNumber) <= 0:
                    print("That number is not in the range")
                    continue
                break
            except(NameError, SyntaxError):
                print("invalid input")
        seats = []

        # creates a list for seats in a row
        for i in range(rowsNumber):
            seats.append('o')

        # collect the number of columns
        while True:
            print("\n\n")
            try:
                columnsNumber = input(
                    "How many columns would you like in the theater\n" + 
                    "(greater than 0 and less than 100)? ")
                if int(columnsNumber) >= 100 or int(columnsNumber) <= 0:
                    print("That number is not in the range")
                    continue
                break
            except(NameError, SyntaxError):
                print("invalid input")

        columns = []

        # add the number of columns the user asked for and ask before creating what the price
        # for that row should be.
        price = []
        for i in range(columnsNumber):
            while True:
                print("\n\n")
                try:
                    columnPrice = float(
                        input("How much would you like column " + str(i+1) + " to cost? $"))
                    if columnPrice < 0:
                        print("You can't have a negative price.")
                        continue
                    columnPrice = round(columnPrice, 2)
                    price.append(columnPrice)
                    break
                except(NameError, SyntaxError):
                    print("invalid input")
            columns.append(seats)
        columns.append(price)
        # writes the columns list to the file
        with open("theater.cvs", "w") as fout:
            w = csv.writer(fout, delimiter=',')
            for i in range(len(columns)):
                w.writerow(columns[i])
    return columns


def statistics(numberOfRows, numberOfColumns, theater):
    revenue = 0.00
    seatsPurchased = 0
    for i in range(numberOfColumns-1):
        for j in range(numberOfRows):
            if theater[i][j] == 'x':
                seatsPurchased += 1
                revenue += float(theater[numberOfColumns-1][i])
    seatsLeft = ((numberOfColumns-1)*(numberOfRows)) - seatsPurchased

    print("\n\n\n")
    print(str(seatsPurchased) + " seats have been sold.")
    print("$" + str(revenue) + " has been made.")
    print(str(seatsLeft) + " seats are still unsold.\n")

    try:
        input("Enter anything to return to the menu. ")
    except:
        print
