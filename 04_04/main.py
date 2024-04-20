from stacklist import Stack
### MENU
def menu():
    print()
    print("##########################")
    print("  1. CREATE STACK ")
    print("  2. PUSH ")
    print("  3. POP ")
    print("  4. PRINT ")
    print("  5. QUIT ")
    print("##########################")
    print()

#### MAIN
print("######################################################")
print(" Hey Guys, A Simple linked list has been created....")
print(" Please select one of the menus below to continue.")
print("#####################################################")

stk = Stack()
choice = "999"

while choice != "5":
    menu()
    choice = input("SELECT MENU? ==>  ")

    if choice == "1":
       result = stk.create_top()
       stk.result_message(result)
    elif choice == "2":
        print()
        data = input("Enter the data you want to add.. ==> ")
        if data == None:
            print("No data has been entered. Please check the data...")
        else:
            result = stk.push(data)
            stk.result_message(result)

    elif choice == "3":

        result = stk.pop()
        stk.result_message(result)

    elif choice == "4":
        stk.print_items()

    elif choice == "5":
        print("Exit the program, Good-Bye....")
        break
    else:
        print(" Wrong menu-number...")


