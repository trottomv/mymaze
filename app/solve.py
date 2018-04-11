import networkx as nx
import numpy as np
import time

class Mazesolve:
    MOVESARR = []
    SOLARR = []
    TMPARR = []

    def solve():
        with open('txt/maze.txt', 'r') as f:
            lines = (line.rstrip("\r\n") for line in f)
            maze  = np.array([list(line) for line in lines])
            mazesolve = np.asarray(maze)

        G = nx.Graph()
        for y in range(len(maze)):
            for x in range(len(maze)):
                G.add_node((y,x))
                if y >0:
                    G.add_edge((y-1,x),(y,x))
                if x >0:
                    G.add_edge((y,x),(y,x-1))

        for y in range(len(maze)):
            for x in range(len(maze)):
                if maze[y][x]=='X':
                    G.remove_node((y,x))

        try:
            for point in nx.algorithms.astar_path(G,(1,0),(len(maze)-2,len(maze[0])-1)):
                Mazesolve.MOVESARR.append(point)
                Mazesolve.TMPARR.append(point)
                mazesolve[point[0]][point[1]] = '+'
                if point == (1,0):
                    mazesolve[point[0]][point[1]] = 'S'
                elif point == (len(maze)-2,len(maze[0])-1):
                    mazesolve[point[0]][point[1]] = 'E'

            Mazesolve.SOLARR.append(Mazesolve.MOVESARR)
            Mazesolve.SOLARR.append(Mazesolve.TMPARR)
            print("solving... (Teseo is running away from Minotaur)")
            time.sleep(2)
            for i in range (len(mazesolve)):
                print("".join(mazesolve[i]))

            print("Teseo is save in", len(Mazesolve.MOVESARR)-1, "moves")
            return True

        except:
                if (len(maze)-2,len(maze[0])-1) in Mazesolve.MOVESARR:
                    pass
                else:
                    print("solving... (Teseo is running away from Minotaur)")
                    time.sleep(2)
                    print("There is no solution for Teseo... sorry, try again!")
                    # print(Maze.MOVESARR)
                    print("Try to generate a new maze")
                    return False

def main():
    Mazesolve.solve()


if __name__=="__main__":
    main()
