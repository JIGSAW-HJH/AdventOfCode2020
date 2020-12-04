def main():
    count = 0

    f = open("List-of-passwords.txt","r")
    f1 = f.readlines()

    length = len(f1)

    print("The length is -> ",length)

    for c in range(0, length):
        
        test = f1[c].split(' ')

        code = test[1]
        val = test[0]
        com = test[2]

        code = code.replace(':',"")
        letterCNT = com.count(code)

        val = val.split('-')
        low = int(val[0])
        high = int(val[1])

        if letterCNT >= low and letterCNT <= high:
            count += 1
    

    print("Total count of valid passwords is: ", count)   


    


if __name__ == "__main__":
    main()
