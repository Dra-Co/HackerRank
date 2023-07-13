if __name__ == '__main__':
    s = input()
    print(any(i.isalnum() for i in s), any(i.isalpha() for i in s), any(i.isdigit() for i in s), any(i.islower() for i in s), any(i.isupper() for i in s), sep="\n")
