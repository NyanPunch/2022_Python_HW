infp, outfp = None, None
inStr, outStr = "",""
i, secu = 0,0

secuYN = input("1 2.")
infname = input("입력파일")
outfname = input("출력파일")

if secuYN == "1":
    secu = 100
elif secuYN == "2" :
    secu = - 100

infp = open(infname, 'r', encoding = 'utf-8')
outfp = open(outfname, 'w', encoding = 'utf-8')

while True :
    inStr = infp.readlines()
    if not inStr :
        break
    outStr = ""
    for i in range(0, len(inStr)) :
        ch = inStr[i]
        chNum = ord(ch)
        chNum = chNum + secu
        ch2 = chr(chNum)
        outStr = outStr + ch2

    outfp.write(outStr)
    
outfp.close()
infp.close()
