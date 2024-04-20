from slist import SList as sl

if __name__ == '__main__':
    s = sl()
    s.insert_front('orange')
    s.insert_front('apple')
    s.insert_after('cherry',s.head.next)
    s.insert_after('banana',s.head.next)

    s.print_list()
