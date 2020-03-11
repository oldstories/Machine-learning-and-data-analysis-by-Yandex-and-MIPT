string = input()
for i in range(0, len(string), 1):
    if string[i] == 'K':  # M
        string = string[:i-1] + 'M' + string[i+1:]
        continue
    if string[i] == 'O':  # Q
        string = string[:i] + 'Q' + string[i:]
        continue
    if string[i] == 'I':  # G
        string = string[:i] + 'G' + string[i:]
        continue
print(string)
