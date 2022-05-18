# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# SWeiss,5.17.2022,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

objFile = open("ToDoList.txt", "r")

# read each line of file and create dicRow
lines = objFile.readlines()
for line in lines:
    lineSplit = line.strip("\n").split(",")
    dicRow = {"Task": lineSplit[0], "Priority": lineSplit[1]}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks


    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("Displaying Current To-Do List")
        for i in lstTable:
            print(i)
        continue


    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        Task2 = input("Please Enter New Task ")
        Priority2 = input("Please Enter the Priority ")
        dicRow = {"Task": Task2, "Priority": Priority2}
        lstTable.append(dicRow)
        continue


    # Step 5 - Remove a item from the list/Table
    elif (strChoice.strip() == '3'):
        r = input("Which list item would you like removed? ")
        r = r.lower()
        for dicRow in lstTable:
            if (dicRow["Task"].lower() == r):
                lstTable.remove(dicRow)
                print("The item has been removed from your To Do list.")
        continue


    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("ToDoList.txt", "a")
        objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
        objFile.close()
        print("Changes Have Been Saved.")
        continue


    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print('ToDo list has been closed.')
        break  # and Exit the program
