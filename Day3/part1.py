def main():

    f = open("Toboggan-Trajectory.txt","r")
    f1 = f.readlines()

    length = len(f1)
    
    count = 0
    down = 1
    row = 0

    for i in range(0, length):

        if f1[i][row%31] == '#':
            count += 1;
            down += 1;
        row += 3

        
    print(count)#answer is 247



if __name__ == "__main__":
    main()
