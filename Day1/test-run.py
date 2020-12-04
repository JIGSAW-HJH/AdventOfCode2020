def main():
    Solved = False
    Check = 0
    count = 0
    f = open("Test-file.txt","r")

    f1 = f.readlines()

    length = len(f1)

    print("The length is -> ", length)

    for i in range(0,length):
        f1[i] = int(f1[i])

    for i in range(0, length):
        test1 = f1[i]
        if Solved == True:
                break
        for j in range(0, length):
            if Solved == True:
                break
            test2 = f1[j]
            print("Number 1: ",test1)
            print("Number 2: ",test2)
            add = test1 + test2
            print("added: ", add)
            if add < 2020:
                Check = 2020 - add
                print("Check: ",Check)
                for k in range(0, length):
                    if f1[k] == Check:
                        print("1st Number: ", test1)
                        print("2nd Number: ", test2)
                        print("3rd Number: ", Check)
                        print("1st x 2nd x 3rd is: ", (test1 * test2 * Check))
                        Solved = True
                        break
                    print("###############checking number...")
        
        print("=================================================")

    print("Failed operation!!!!")

if __name__ == "__main__":
    main()    
