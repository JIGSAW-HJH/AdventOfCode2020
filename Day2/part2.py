def main():
    count = 0
    right = 0
    savedVal = 0
    pos = []
    lowDetect = False
    highDetect = False

    f = open("List-of-passwords.txt","r")
    f1 = f.readlines()

    length = len(f1)

    #print("The length is -> ",length)

    for c in range(0, length):
        count = 0
        pos = []
        savedVal = 0
        
        test = f1[c].split(' ')

        code = test[1]
        val = test[0]
        com = test[2]

        length2 = len(com)

        val = val.split('-')
        low = int(val[0]) - 1
        high = int(val[1]) - 1

        code = code.replace(':',"")
        letterCNT = com.count(code)
        #print("Code        = ", str(code))
        #print("Letter cnt  = ", letterCNT)
        #print("Pos         = ", str(val))
        #print("Pass        = ", str(com))
        #print("Pass length = ", length2)
        #print("Low Pos     = ", low)
        #print("High Pos    = ", high)
        #print("--------------------------------------------")
        if letterCNT > 0:
            for i in range(0,length2):
                if com[i] == code:
                    pos.append(count)
                    savedVal += 1
                count += 1
            count = 0
            savedVal = 0

            d = len(pos)
            for j in range(0,d):
                if pos[j] == low:
                    lowDetect = True
                if pos[j] == high:
                    highDetect = True

            if (lowDetect and not highDetect) or (not lowDetect and highDetect):
                right += 1
                #print("VALID")
                lowDetect = False
                highDetect = False
            else:
                #print("WRONG")
                lowDetect = False
                highDetect = False
                pass
        #print("##############################################################")    


    print("Total count of valid passwords is: ", right)   


    


if __name__ == "__main__":
    main()
