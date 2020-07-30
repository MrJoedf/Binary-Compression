import sys
def compress(string):
    newString = ""

    count = 1
    newString += string[0]

    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            count += 1
        else:
            if (count > 1):
                newString += str(count)
            newString += string[i + 1]

            count = 1
    if (count > 1):
        newString += str(count)
    return(newString)

#test = open('binary-output.txt', 'r')
#file = test.read()
#with open('binary-output-compressed.txt', 'w') as f:
    #sys.stdout=f
    #print(compress(file))
