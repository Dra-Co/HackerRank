def print_rangoli(size):
    # your code goes here
    arr = [chr(96+size)]
    for i in range(size-1):
        print("-".join(arr).center(4*size-3, "-"))
        arr= arr[:len(arr)//2] + [chr(96+size-i), chr(96+size-i-1)] + arr[len(arr)//2:]
    print("-".join(arr))
    for i in range(size-1):
        del arr[len(arr)//2:len(arr)//2+2]
        print("-".join(arr).center(4*size-3,"-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
