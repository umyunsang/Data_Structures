from circlelist import CircleList as cl

## Function
def menu():
    print()
    print("###########################")
    print("   1. CREATE HEAD-NODE")
    print("   2. APPEND NODE ")
    print("   3. INSERT NODE ")
    print("   4. MODIFTY NODE ")
    print("   5. DELETE NODE ")
    print("   6. PRINT ALL-NODE")
    print("   7. NODE END")
    print("###########################")
    print()


print("###########################################################")
print(" Hey Guys, A simple linked list has been created..... ")
print(" Please select one of the menus below to continue.")
print("###########################################################")

clist = cl()
choice = "999"

while choice != 6:
    menu()
    choice = input("select menu? ==> ")

    if choice == "1":
        clist.create_head()

    elif choice == "2":
        print()
        data = input("Enter the data you want to add.. ==> ")
        if data == "":
            print("No data has been entered. Please check the data...")
        else:
            clist.node_append(data)

    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        pass
    elif choice == "6":
        clist.all_print()
        pass
    elif choice == "7":
        print("Exit the program. Goodbye....")
        break

