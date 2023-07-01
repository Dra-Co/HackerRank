if __name__ == '__main__':
    lst = []
    N = int(input())
    for i in range(N):
        com, *num = input().split()
        if com == 'insert':
            lst.insert(int(num[0]), int(num[1]))
        elif com == 'print':
            print(lst)
        elif com == 'remove':
            lst.remove(int(num[0]))
        elif com == 'append':
            lst.append(int(num[0]))
        elif com == 'sort':
            lst.sort()
        elif com == 'pop':
            lst.pop()
        else:
            lst.reverse()
