n = int(input())
s = set(map(int, input().split()))
for _ in range(int(input())):
    m, *a = input().split()
    if m == 'pop': s.pop()
    elif m == 'remove': s.remove(int(*a))
    else: s.discard(int(*a))
print(sum(s))
