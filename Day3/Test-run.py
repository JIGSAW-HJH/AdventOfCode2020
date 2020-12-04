def travel(horizontalMovement, verticalConstant, horizontalConstant, fileLength, character, file):
    verticalMovement = verticalConstant
    numTrees = 0
    
    for i in range(1, len(file)):
        
        if verticalConstant == 1:
            if file[i][(horizontalMovement % fileLength)] == '#':
                numTrees += 1
        elif verticalConstant == 2:
            if (file[i][(horizontalMovement % fileLength)] == '#') and (verticalMovement % 2 == 0):
                numTrees += 1
           
        horizontalMovement += horizontalConstant
        verticalMovement += verticalConstant

    return numTrees

def main():

    path = ["..##.......",
	    "#...#...#..",
	    ".#....#..#.",
	    "..#.#...#.#",
	    ".#...##..#.",
	    "..#.##.....",
	    ".#.#.#....#",
	    ".#........#",
	    "#.##...#...",
	    "#...##....#",
	    ".#..#...#.#"]

##    f = open("Toboggan-Trajectory.txt","r")
##    path = f.readlines()
    
    
    countB = travel(3,1,3,11,'#',path)#Right 3, down 1
    
    print("Right 3, down 1 path = ", countB, " Trees in the path.")


if __name__ == "__main__":
    main()
