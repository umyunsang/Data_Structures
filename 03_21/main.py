from singlelist import SingleList as sl

### MENU
def menu():
    print()
    print("##########################")
    print("  1. CREATE HEAD-NODE ")
    print("  2. APPEND NODE ")
    print("  3. INSERT NODE ")
    print("  4. MODIFY NODE ")
    print("  5. DELETE NODE ")
    print("  6. PRINT NODES ")
    print("  7. QUIT ")
    print("##########################")
    print()

#### MAIN
print("######################################################")
print(" Hey Guys, A Simple linked list has been created....")
print(" Please select one of the menus below to continue.")
print("#####################################################")

slist = sl()
choice = "999"

while choice != "7":
    menu()
    choice = input("SELECT MENU? ==>  ")

    if choice == "1":
       slist.create_head()
    elif choice == "2":
        print()
        data = input("Enter the data you want to add.. ==> ")
        if data == None:
            print("No data has been entered. Please check the data...")
        else:
            slist.node_append(data)

    elif choice == "3":
        find = input("Insert data value ==> ")
        data = input("Enter the data you want to add.. ==> ")
        result = slist.node_insert(find, data)
        if result[0] == 100:
            print(result[1])
        else: print(result[1])

        pass
    elif choice == "4":
        slist.all_print()
        raw = input("raw data? ")
        change = input("Input change data? ")
        slist.node_modify(raw, change)
        pass
    elif choice == "5":
        slist.all_print()
        raw = input("Input delete data ? ")
        slist.node_delete(raw)
        pass
    elif choice == "6":
        slist.all_print()
        pass
    elif choice == "7":
        print("Exit the program, Good-Bye....")
        break

    else:
        print(" Wrong menu-number...")

# slist.create_head()
#
# slist.node_append("park")
# slist.node_append("choi")
# slist.node_append("lee")
# slist.node_insert("choi", "hwang")
#
# slist.all_print()

