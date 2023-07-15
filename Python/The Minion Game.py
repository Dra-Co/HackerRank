def minion_game(string):
    # your code goes here
    a = b = 0
    for i in range(len(string)):
        if string[i] in "AEIOU":
            b += len(string)-i
        else:
            a += len(string)-i
    print("Stuart", a) if a > b else print("Kevin", b) if b > a else print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
