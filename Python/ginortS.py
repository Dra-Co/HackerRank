# Enter your code here. Read input from STDIN. Print output to STDOUT
print(*sorted(input(), key = lambda x:(x in '02468', x.isdigit(), x.isupper(), x)), sep='')
