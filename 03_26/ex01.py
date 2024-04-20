from doublelinked import doublelinked as dl

### MENU
def menu():
    print()
    print("###########################")
    print("  1. CREATE HEAD-NODE ")
    print("  2. APPEND NODE ")
    print("  3. INSERT NODE ")
    print("  4. MODIFY NODE ")
    print("  5. DELETE NODE ")
    print("  6. ORDER PRINT NODE ")
    print("  7. REVERSE PRINT NODE ")
    print("  8. QUIT ")
    print("###########################")
    print()

### Main
print("#######################################################")
print(" Hey Guys, A simple Linked List has been created....")
print(" Please select on of the menus below to continue.")
print("#######################################################")

dlist = dl()
choice ='999'

while choice != '7':
    menu()
    choice = input('SELECT MENU ==> ')

    if choice == "1":
        dlist.create_ht()
    elif choice == "2":
        print()
        data = input("Enter the data yo want to add.. ==> ")
        if data == "" or data == None:
            print("No data has been entered.")
        else:
            result = dlist.node_append(data)
            if result[0] == 100:
                print(result[1])
            else : print(result[1])

    elif choice == "4":
        pass
    elif choice == "5":
        pass
    elif choice == "6":
        dlist.order_print()
    elif choice == "7":
        dlist.reverse_print()
    elif choice == "8":
        print("Exit the program. Good-Bye...")
        break
    else :
        print(" Wrong menu-number...")

