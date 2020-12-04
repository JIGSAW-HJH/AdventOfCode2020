def main():
    f= open("Report-file-data.txt","r")
    #if f.mode == "r":
    #use the read function to read the content
    #contents = f.read()
    #print(contents)
    
    #or, readlines reads the individual lines
    f1 = f.readlines()
    #get the length of the file
    length = len(f1)
    print("The length is -> ", length)

    #change list to int
    for i in range(0,len(f1)):
        f1[i] = int(f1[i])

    #Store the first number as an integer
    number = f1[0]
    #n = f1[1]

    #q = n + number
    

    print(number)
    print("========")
    for i in range(0, len(f1)):
        number = f1[i]
        for i in range(0, len(f1)):
            a = f1[i]
            #print(a)
        
            answer = number + a
            #print(answer)
            #print("========")
            if answer == 2020:
                break
            #print("========")
            #print("========")
            #print(answer)
        if answer == 2020:
            break
    print("========")
    print("========")
    print(answer)
    print("The one number is   ->", a)
    print("The other number is ->",number)
    print("Multiplied together is ->", (a*number))
    
    #for x in f1:
        #answer = number + x
        #print(answer)
        #print("===============")

if __name__ == "__main__":
    main()
