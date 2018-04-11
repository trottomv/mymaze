already_visited=[]
def solve1(x,y):
    global already_visited
    matrix = draw(load('txt/maze.txt'))
    print (x,y)

    #base cases
    if matrix[x][y] == "E":
        for row in matrix:
            row = str(row)[1:-1]
            print (row)
            print(already_visited)
        return True
    if matrix[x][y] == "*":
        return False
    if matrix[x][y] == "X":
        return False

    matrix[x][y] = "x"

    #---------------------
    if (x,y) in already_visited: #check if we have already been here
        return False

    already_visited.append((x,y)) #add position to list
    #---------------------


    # recursive cases (matrix traversal)
    if (x < len(matrix)-1 and solve1(x+1,y)):
        return True
    elif (y > 0 and solve1(x,y-1)):
        return True
    elif (x > 0 and solve1(x-1,y)):
        return True
    elif (y < len(matrix)-1 and solve1(x,y+1)):
        return True
    else:
        return False
