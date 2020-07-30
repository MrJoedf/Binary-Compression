def decompress(string):
    newString = ""
    for i in range(len(string) - 1):
        if string[i] == '0' or string[i] == '1':
            if string[i + 1] != '0' and string[i + 1] != '1':
                newString += string[i] * int(string[i + 1])
            else:
                newString+=string[i]
    newString+=string[len(string)-1]

    return(newString)
