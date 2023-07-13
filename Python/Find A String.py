def count_substring(string, sub_string):
    res = 0
    for i in range(len(string)-len(sub_string)+1):
       res += string[i:len(sub_string)+i].count(sub_string)
    return res
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
