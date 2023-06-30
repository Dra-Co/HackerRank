x = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        x+=[[name,score]]

s = list(sorted(set([i[1] for i in x])))[1]
print(*sorted([i[0] for i in x if i[1] == s]), sep="\n")
