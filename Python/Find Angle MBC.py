# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import degrees, atan
AB, BC = int(input()), int(input())
print(round(degrees(atan(AB / BC))), chr(176), sep = '')
