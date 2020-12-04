def main():
    f1 = "7-15 m: mmkvmwmklnqpmggbgn"
    # 9-10 m: mmmmnxmmmwm
    # 6-8 w: wpwwhxnv
    # 4-6 n: trwpnnnvq
    # 12-15 p: zfpmpphpgghpppppppp
    # 5-10 z: bqlbzfzzzbzwsz
    # 7-15 m: mmkvmwmklnqpmggbgn
    count = 0
    right = 0
    savedVal = 0
    pos =[]
    lowDetect = False
    highDetect = False
    
    test = f1.split(' ')

    code = test[1]
    val = test[0]
    com = test[2]

    length = len(com)

    val = val.split('-')
    low = int(val[0]) - 1
    high = int(val[1]) - 1

    code = code.replace(':',"")
    letterCNT = com.count(code)
    print("Code        = ", str(code))
    print("Letter cnt  = ", letterCNT)
    print("Pos         = ", str(val))
    print("Pass        = ", str(com))
    print("Pass length = ", length)
    print("Low Pos     = ", low)
    print("High Pos    = ", high)
    print("--------------------------------------------")
    if letterCNT > 0:
        print("The code is there...")
        for i in range(0,length):
            if com[i] == code:
                print("********")
                print("Loop counter = ", i)
                print("Count val    = ", count)
                pos.append(count)
                print("Saved position is ", pos[savedVal])
                print("********")
                savedVal += 1
            count += 1

        d = len(pos)
        print("$$$$$$$$$$$$$$$$$$$")
        print("total spots in pasword = ", d)
        for i in range(0,d):
            if pos[i] == low:
                lowDetect = True
            if pos[i] == high:
                highDetect = True

        if (lowDetect and not highDetect) or (not lowDetect and highDetect):
            right += 1
            print("VALID")
        else:
            print("WRONG")
    print("##############################################################")    


    print("Total count of valid passwords is: ", right)   


    


if __name__ == "__main__":
    main()
