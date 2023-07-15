from textwrap import wrap

def merge_the_tools(string, k):
    # your code goes here
    string = wrap(string, k)
    for i in string:
        print(*dict.fromkeys(i).keys(), sep="")

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
