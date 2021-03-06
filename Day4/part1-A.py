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

def CheckAllPassports(data):
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    checkCodes = 0
    numCodes = 8
    cid = False
    count = 0
    
    for i in range(0, len(data)):#Check if passports are valid:
        if data[i].find(fields[7],0,len(data[i])) != -1:# check if cid is present,
            cid = True# if cid is present set a flag
            
        for j in range(0, len(fields)):# check each line to see if all 8 fields are present
            if data[i].find(fields[j],0,len(data[i])) != -1:# if fields are present,
                checkCodes += 1#add fields count
                
        #Check if all 8 fields are present in passport:
        if checkCodes == 8:
            count += 1
        elif checkCodes == 7 and cid != True:
            count += 1
        checkCodes = 0
        cid = False
    return count

def main():
    #import the file to work on -> READ FILE ONLY!
    f = open("List-of-passports.txt","r")
    path = f.readlines()
    
    print("Length of file is ", len(path))
    
    #detection variables:
    deliminators = [' ', ':']

    #Variables:
    numNPcredentialsPassports = 0
    numValidPassports = 0
    information = ""
    data = []
    
    #Simplify all the passport data:
    getAllPassports(path, data, information)
    
    #Get the total number of passports:
    numValidPassports = CheckAllPassports(data)
        
    print("Valid passports: ", numValidPassports)

if __name__ == "__main__":
    main()
