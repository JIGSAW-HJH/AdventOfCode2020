def travel(horizontalMovement, verticalConstant, horizontalConstant, fileLength, character, file):
    verticalMovement = verticalConstant
    numTrees = 0
    
    for i in range(0, len(file),verticalConstant):

        horizontalMovement += horizontalConstant
        verticalMovement += verticalConstant

        if verticalConstant == 1:
            if file[i][horizontalMovement % fileLength] == '#':
                numTrees += 1
        elif verticalConstant == 2:
            if (file[i][horizontalMovement % fileLength] == '#') and (verticalMovement % 2 == 0):
                numTrees += 1

    return numTrees

def main():

    f = open("Toggoban-Trajectory.txt","r")
    path = f.readlines()
    print("Length of file is ", len(path))
    
    countA = travel(-1,1,1,31,'#',path)#Right 1, down 1 = 78  Trees in the path.
    countB = travel(-3,1,3,31,'#',path)#Right 3, down 1 =  247  Trees in the path.
    countC = travel(-5,1,5,31,'#',path)#Right 5, down 1 =  68  Trees in the path.
    countD = travel(-7,1,7,31,'#',path)#Right 7, down 1 =  69  Trees in the path.
    countE = travel(-1,2,1,31,'#',path)#Right 1, down 2 =  33  Trees in the path.

    Total = countA * countB * countC * countD * countE# 2983070376  Trees.
    
    print("Right 1, down 1 path = ", countA, " Trees in the path.")
    print("Right 3, down 1 path = ", countB, " Trees in the path.")
    print("Right 5, down 1 path = ", countC, " Trees in the path.")
    print("Right 7, down 1 path = ", countD, " Trees in the path.")
    print("Right 1, down 2 path = ", countE, " Trees in the path.")
    print("Multiplied together  = ", Total, " Trees.")


if __name__ == "__main__":
    main()
