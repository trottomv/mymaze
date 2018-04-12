import networkx as nx
import numpy as np
import time

class Maze:
    MOVESARR = []
    SOLARR = []
    TMPARR = []

    with open('txt/maze.txt', 'r') as f:
        lines = (line.rstrip("\r\n") for line in f)
        maze  = np.array([list(line) for line in lines])

    G = nx.Graph()

    def mazesolve():
        with open('txt/mazesolve.txt', 'r') as f:
            lines = (line.rstrip("\r\n") for line in f)
            maze  = np.array([list(line) for line in lines])
            mazesolve = np.asarray(maze)
        return mazesolve

    def solve():
        with open('txt/maze.txt', 'r') as f:
            lines = (line.rstrip("\r\n") for line in f)
            maze  = np.array([list(line) for line in lines])
            mazesolve = np.asarray(maze)

        G = nx.Graph()
        for y in range(len(maze)):
            for x in range(len(maze[y])):
                G.add_node((y,x))
                if y >0:
                    G.add_edge((y-1,x),(y,x))
                    G.add_edge((y,x-1),(y,x))
                if x >0:
                    G.add_edge((y,x-1),(y,x))
                    G.add_edge((y-1,x),(y,x))

        for y in range(len(maze)):
            for x in range(len(maze[y])):
                if maze[y][x]=='X':
                    G.remove_node((y,x))

        try:
            TMPARR = []
            for point in nx.algorithms.astar_path(G,(1,0),(len(maze)-2,len(maze[0])-1)):
                Maze.MOVESARR.append(point)
                Maze.TMPARR.append(point)
                mazesolve[point[0]][point[1]] = '+'
                if point == (1,0):
                    mazesolve[point[0]][point[1]] = 'S'
                elif point == (len(maze)-2,len(maze[0])-1):
                    mazesolve[point[0]][point[1]] = 'E'

            Maze.SOLARR.append(Maze.MOVESARR)
            Maze.SOLARR.append(Maze.TMPARR)

            open("txt/mazesolve.txt", "w").close()
            for i in range (len(mazesolve)):
                text_file = open("txt/mazesolve.txt", "a")
                text_file.write("".join(mazesolve[i])+ '\n')
                text_file.close()

            return True

        except:
            return False

    def output():
        print("solving... (Teseo is running away from Minotaur)")
        time.sleep(2)
        f = open("txt/mazesolve.txt", "r")
        print(f.read())
        f.close

        print("Teseo is save in", len(Maze.SOLARR[0])-1, "moves")

    def nosoloutput():
        print("solving... (Teseo is running away from Minotaur)")
        time.sleep(2)
        print("There is no solution for Teseo... sorry, try again!")
        print("Try to generate a new maze")

    # def  countsol():
    #     with open('txt/mazesolve.txt', 'r') as f:
    #         lines = (line.rstrip("\r\n") for line in f)
    #         maze  = np.array([list(line) for line in lines])
    #         # mazesolve = np.asarray(maze)
    #
    #     G = nx.Graph()
    #     for y in range(len(maze)):
    #         for x in range(len(maze[y])):
    #             G.add_node((y,x))
    #             if y >0:
    #                 G.add_edge((y-1,x),(y,x))
    #             if x >0:
    #                 G.add_edge((y,x),(y,x-1))
    #
    #     for y in range(len(maze)):
    #         for x in range(len(maze)):
    #             if maze[y][x]=='X':
    #                 G.remove_node((y,x))
    #                 if maze[y][x]=='+':
    #                     G.remove_node((y,x))
    #
    #     # try:
    #     TMPARR = []
    #     for point in nx.algorithms.astar_path(G,(1,0),(len(maze)-2,len(maze[0])-1)):
    #         Maze.MOVESARR.append(point)
    #         Maze.TMPARR.append(point)
    #         mazesolve[point[0]][point[1]] = '+'
    #         if point == (1,0):
    #             mazesolve[point[0]][point[1]] = 'S'
    #         elif point == (len(maze)-2,len(maze[0])-1):
    #             mazesolve[point[0]][point[1]] = 'E'
    #
    #     Maze.SOLARR.append(Maze.MOVESARR)
    #     Maze.SOLARR.append(Maze.TMPARR)
    #
    #     open("txt/mazesolve.txt", "w").close()
    #     for i in range (len(mazesolve)):
    #         text_file = open("txt/mazesolve.txt", "a")
    #         text_file.write("".join(mazesolve[i])+ '\n')
    #         text_file.close()
    #
    #     return True
    #     ######################3
    #         #         for i in range (len(Maze.SOLARR)):
    #         #             try:
    #         #                 Maze.TMPARR = []
    #         #                 for point in nx.algorithms.astar_path(Maze.G,(1,0),(len(Maze.maze)-2,len(Maze.maze[0])-1)):
    #         #                     Maze.TMPARR.append(point)
    #         #             except:
    #         #                     Maze.G.add_node((Maze.SOLARR[i][j][0],Maze.SOLARR[i][j][1]))
    #         #
    #         #                 #     pass
    #         #
    #         #             for i in range(len(Maze.SOLARR)):
    #         #                 if Maze.TMPARR != Maze.SOLARR[i]:
    #         #                     Maze.SOLARR.append(Maze.TMPARR)
    #         #                     # print(len(Maze.SOLARR))
    #         # print(Maze.SOLARR)
    #         #                 # print(Maze.SOLARR[0:4])
    #         #
    #         # print("(There where", len(Maze.SOLARR), "possible solutions for Teseo)")
    #         # # print(Maze.SOLARR)
    #
    #     # except:
    #     #     for i in range (len(Maze.SOLARR)):
    #     #         for j in range (len(Maze.SOLARR[i])): #Maze.SOLARR[i-1], Maze.SOLARR[-1]):
    #     #             if maze[i][j] == '+':
    #     #                 Maze.G.add_node((i,j))
    #     #                 Maze.G.add_node((Maze.SOLARR[i][0],Maze.SOLARR[i][1]))
    #     #                 # try:
    #     #                 Maze.TMPARR = []
    #     #                 for point in nx.algorithms.astar_path(Maze.G,(1,0),(len(Maze.maze)-2,len(Maze.maze[0])-1)):
    #     #                     Maze.TMPARR.append(point)
    #     #         for i in range(len(Maze.SOLARR)):
    #     #             if Maze.TMPARR != Maze.SOLARR[i]:
    #     #                 Maze.SOLARR.append(Maze.TMPARR)
    #     #     pass
    #     #     # Maze.countsol()



def main():
    # for y in range(len(maze)):
    #     for x in range(len(maze)):
    if Maze.solve() is False:
        Maze.nosoloutput()
    else:
        Maze.output()
        # Maze.countsol()
        pass
    # if Maze.solve() is False:
    #     Maze.nosoloutput()
    # else:
    #     Maze.output()
    #     pass

if __name__=="__main__":
    main()
