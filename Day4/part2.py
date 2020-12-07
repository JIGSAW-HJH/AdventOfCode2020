############################################################################################

def getAllPassports(file, passports):
    string = ""
    for i in range(0, len(file)):
        if len(file[i]) != 1:
            string += " " + file[i]
            string = string.replace("\n"," ")
        else:
            passports.append(string)
            string = ""
    passports.append(string)

############################################################################################

def CheckAllPassports(data, CorrectPassports):
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
            CorrectPassports.append(data[i])
        elif checkCodes == 7 and cid != True:
            count += 1
            CorrectPassports.append(data[i])
        checkCodes = 0
        cid = False
    return count, CorrectPassports

############################################################################################

def Check_byr_iyr_eyr(tempData,code):
        if code == 'byr':
            minimum = 1920
            maximum = 2002
        elif code == 'iyr':
            minimum = 2010
            maximum = 2020
        else:
            minimum = 2020
            maximum = 2030
            
        for z in range(0, len(tempData)):#Go through list of codes for this password:
            if tempData[z].find(code) == 0:#if you find the code, then:
                year = int(tempData[z][4:])
                if minimum <= year <= maximum:#if true, then:
                    return 1#if falls within spec return a 1
                else:
                    return 0#if falls without spec return a 0
            else:
                pass
        #Finished looking for the code but, no luck in finding it, so:
        return -1
    
############################################################################################

def CheckHeight(tempData, code):
    centimeters = "cm"
    inches = "in"
    length = ""
    dim = ""
    q = 0

    for z in range(0, len(tempData)):#Go through list of codes for this password:
        if tempData[z].find(code) == 0:#if you find the code, then:
            q = 0
            unitA = tempData[z].find('cm')
            unitB = tempData[z].find('in')
            if unitA != -1:
                #this length is in centimeters
                dim = tempData[z][len(tempData[z])-2:len(tempData[z])]
                length = int(tempData[z][4:len(tempData[z])-2])
                minimum = 150
                maximum = 193
                if minimum <= length <= maximum:#if true, then:
                    return 1#if falls within spec return a 1
                else:
                    return 0#if falls without spec return a 0
            elif unitB != -1:
                #this length is in inches
                dim = tempData[z][len(tempData[z])-2:len(tempData[z])]
                length = int(tempData[z][4:len(tempData[z])-2])
                minimum = 59
                maximum = 76
                if minimum <= length <= maximum:#if true, then:
                    return 1#if falls within spec return a 1
                else:
                    return 0#if falls without spec return a 0
            elif unitA == -1 or unitB == -1:
                #there is no units for length, invalid data so,
                return -1
        else:
            pass
    return -1

############################################################################################

def CheckHairColor(tempData, code):#hcl:#c0946f     hcl:z       hcl:#f97e30
    for z in range(0, len(tempData)):#Go through list of codes for this password:
        if tempData[z].find(code) == 0:#if you find the code, then:
            hashChar = tempData[z].find('#')
            if hashChar != -1:#there is a # char in the code,so:
                color = tempData[z][5:]
                return filterColorCode(color)
            else:#There is no # char, so color is invalid, so:
                return -1
        else:
            pass
        
    return -1#If no code is present
    
############################################################################################

def filterColorCode(color):
    num = ['0','1','2','3','4','5','6','7','8','9']
    alpha = ['a','b','c','d','e','f']
    Allnum = color.isdigit()
    Acount = 0
    Ncount = 0
    All = 0
    
    if Allnum == False:#If the whole code is not all digits, then:
        for i in range(0,len(color)):            
            if color[i].isalpha() == True:
                for j in range(0,len(alpha)):
                    if alpha[j] != color[i]:
                        Acount = 0
                    else:
                        Acount = 1
                        break
            else:
                Ncount = 1
                
    else:
        All = 1
    if All == 1:
        return 1
    if Acount == 1 and Ncount == 0:
        return 1
    if Acount == 1 and Ncount == 1:
        return 1
    if Acount == 0:
        return -1
    
############################################################################################

def CheckEyeColor(tempData, code):
    colors = ["amb","blu","brn","gry","grn","hzl","oth"]
    Rule = False
    for z in range(0, len(tempData)):#Go through list of codes for this password:
        if tempData[z].find(code) == 0:#if you find the code, then:
            CurCol = tempData[z][4:]
            for i in range(0,len(colors)):
                if colors[i] == CurCol:#if the color is in the rules list, then:
                    Rule = True
                    break
                else:
                    Rule = False

            if Rule == True:
                return 1
            else:
                return -1
        
    return -1

############################################################################################

def CheckPassportID(tempData, code):
    for z in range(0, len(tempData)):#Go through list of codes for this password:
        
        if tempData[z].find(code) == 0:#if you find the code, then:
            nums = tempData[z][4:]
            digit = nums.isdigit()
            
            if digit == True:
                l = len(nums)
                
                if l == 9:
                    return 1
                else:
                    return -1
            else:
                return -1
    

############################################################################################

def filterPassports(CorrectPassports, valid):
    for i in range(0,len(CorrectPassports)):#go through the file one by one: len(CorrectPassports)
        count = 0
        done = False
        
        filteredPassports = CorrectPassports[i].split(' ')#split current line string up into seperate sections
        
        for j in range(0,len(filteredPassports)):#Count all the empty spaces in this array
            if filteredPassports[j] == '':
                count += 1
                
        if count != 0:
            #Remove all the empty spots in te array:
            while done != True:
                l = len(filteredPassports)
                for k in range(0,l):
                    if filteredPassports[k] == '':
                        del filteredPassports[k]
                        count -= 1
                        if count == 0:
                            done = True
                        break
        #print(filteredPassports)
        #CHECK THIS LINE IF CORRECT:
        print("=========================================================")
        BYR = Check_byr_iyr_eyr(filteredPassports, 'byr')
        IYR = Check_byr_iyr_eyr(filteredPassports, 'iyr')
        EYR = Check_byr_iyr_eyr(filteredPassports, 'eyr')
        HGT = CheckHeight(filteredPassports, 'hgt')
        HCL = CheckHairColor(filteredPassports, 'hcl')
        ECL = CheckEyeColor(filteredPassports, 'ecl')
        PID = CheckPassportID(filteredPassports, 'pid')
 
        print("byr: %d\tiyr: %d\teyr: %d\thgt: %d\thcl: %d\tecl: %d\tpid: %d\tline: %d" % (BYR,IYR,EYR,HGT,HCL,ECL,PID,i) )
        print("#########################################################")

        if BYR == 1 and IYR == 1 and EYR == 1 and HGT == 1 and HCL == 1 and ECL == 1 and PID == 1:
            valid +=1
            print("VALID ENTRIES: ", valid)
            print("#######################################################################")
        else:
            print(" ")
            print("#######################################################################")

    return valid




def main():
    #import the file to work on -> READ FILE ONLY!
    f = open("List-of-passports.txt","r")
    #Raw file:
    file = f.readlines()
    #print("Length of file is ", len(file))

    #Variables:
    filteredPassports = []      # Just the codes and values of passports, nothing more!!!
    numValidPassports = 0       # Valid passports with correct # of codes
    CorrectPassports = []       # Only Correct Passports with correct # of Codes
    passports = []              # All passports
    valid = 0                   # Passed passports count

    #All passport IDs grouped together:
    getAllPassports(file, passports)
    #print(passports)

    #Only correct passports that passed Code check and the final count of them:
    numValidPassports, CorrectPassports = CheckAllPassports(passports, CorrectPassports)

    print("Valid passports: ", numValidPassports)
    #print(CorrectPassports[0])

    #Filter out the passwords
    valid = filterPassports(CorrectPassports, valid)

    print("Filtered VALID passwords: ", valid)#103

if __name__ == "__main__":
    main()
