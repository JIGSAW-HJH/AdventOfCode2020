##  1> Check for a \n character in every line
##  2> Check for the cid CODE if any
##  3> Check for all the other CODES
##  4> Count number of CODES in passport, ONLY CID can be missing in a passport to be valid
##  5> If any codes are missing passport is not valid!

def getAllPassports(file, passports, string):
    for i in range(0, len(file)):
        if len(file[i]) != 1:
            string += " " + file[i]
            string = string.replace("\n"," ")
        else:
            passports.append(string)
            string = ""
    passports.append(string)

    #return passports

def main():
    #import the file to work on -> READ FILE ONLY!
    f = open("test-file1.txt","r")
    path = f.readlines()
    
    print("Length of file is ", len(path))
    

    #Passport required fields:
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

    #detection variables:
    deliminators = [' ', ':']

    #Variables:
    numNPcredentialsPassports = 0
    numValidPassports = 0
    information = ""
    checkCodes = 0
    numCodes = 8
    cid = False
    data = []
    
    #Simplify all the passport data:
    getAllPassports(path, data, information)

    
    for i in range(0, len(data)):#Check if passports are valid:
        if data[i].find(fields[7],0,len(data[i])) != -1:# check if cid is present,
            cid = True# if cid is present set a flag
            
        for j in range(0, len(fields)):# check each line to see if all 8 fields are present
            if data[i].find(fields[j],0,len(data[i])) != -1:# if fields are present,
                checkCodes += 1#add fields count
                #print("CheckCodes: ", checkCodes)
        #print("=====================================")
        #Check if all 8 fields are present in passport:
        if checkCodes == 8:
            numValidPassports += 1
        elif checkCodes == 7 and cid != True:
            numValidPassports += 1
        checkCodes = 0
        cid = False
        
    print("Valid passports: ", numValidPassports)

if __name__ == "__main__":
    main()
