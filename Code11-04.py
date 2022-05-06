infp = None
inList, inStr = [],""

infp = open("C:/Users/WhoLook/Documents/Python/data.txt", "r")

inList = infp.readlines()
for inStr in inList :
    for i in range (0, inStr) :
        print(i,":")
    print(inStr, end ="")

infp.close()
