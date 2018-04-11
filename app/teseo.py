from collections import namedtuple
# from app import mazegen
import time

Dir = namedtuple("Dir", ["char", "dy", "dx"])

class Maze:
    START = "S"
    END   = "E"
    WALL  = "X" #, "|", "-",
    PATH  = " "
    OPEN  = {PATH, END}  # map locations you can move to (not WALL or already explored)

    RIGHT = Dir(">",  0,  1)
    DOWN  = Dir("v",  1,  0)
    LEFT  = Dir("<",  0, -1)
    UP    = Dir("^", -1,  0)
    DIRS  = [RIGHT, DOWN, LEFT, UP]
    MOVESCOUNT = []
    MOVESARR = []
    SOLCOUNT = []
    SOLARR = [[]]

    @classmethod
    def load_maze(cls, fname):
        with open(fname) as inf:
            lines = (line.rstrip("\r\n") for line in inf)
            maze  = [list(line) for line in lines]
        return cls(maze)

    def __init__(self, maze):
        self.maze = maze

    def __str__(self):
        return "\n".join(''.join(line) for line in self.maze)

    def find_start(self):
        for y,line in enumerate(self.maze):
            try:
                x = line.index("S")
                return y, x
            except ValueError:
                pass

        # not found!
        raise ValueError("Sorry, Teseo don't find any start location")

    def solve(self, y, x):
        if self.maze[y][x] == Maze.END:
            # base case - endpoint has been found
            return True
        else:
            # search recursively in each direction from here
            for dir in Maze.DIRS:
                ny, nx = y + dir.dy, x + dir.dx
                if self.maze[ny][nx] in Maze.OPEN:  # can I go this way?
                    if self.maze[y][x] != Maze.START: # don't overwrite Maze.START
                        self.maze[y][x] = dir.char  # mark direction chosen
                        Maze.MOVESCOUNT.append(1)
                        Maze.MOVESARR.append([y,x])
                        # Maze.SOLARR[0].append(Maze.MOVESARR)

                    if self.solve(ny, nx):          # recurse...
                        # Maze.SOLCOUNT.append(1)
                        # Maze.anothersolve(self, y, x)
                        return True                 # solution found!
                        # no solution found from this location
                        if self.maze[y][x] != Maze.START:       # don't overwrite Maze.START
                            self.maze[y][x] = Maze.PATH         # clear failed search from map
                        return False

    def anothersolve(self, y, x):
        for i in Maze.MOVESARR:
            self.maze
        # if self.maze[y][x] == Maze.END:
        #     # base case - endpoint has been found
        #     return True
        # else:
        #     for i in range (len(Maze.MOVESARR)):
        #         # try:
        #             # if self.maze[y][x] == (Maze.MOVESARR[i+1][0], Maze.MOVESARR[i+1][1]):
        #         for dir in Maze.DIRS:
        #             ny, nx = y + dir.dy, x + dir.dx
        #             if self.maze[ny][nx] in Maze.OPEN:  # can I go this way?
        #                 if self.maze[y][x] != Maze.START: # don't overwrite Maze.START
        #                     if self.maze[y][x] in Maze.MOVESARR:
        #                     # self.maze.Maze.MOVESARR[i+1] = Maze.WALL
        #                     # Maze.MOVESARR[i] = WALL
        #                         self.maze[y][x] = dir.char
        #                         Maze.MOVESARR.append([y,x])
        #                         Maze.SOLARR[0].append(Maze.MOVESARR)
        #
        #
        #                     if self.solve(ny, nx):          # recurse...
        #                         return True
        #                         Maze.SOLCOUNT.append(1)
        #                         Maze.SOLARR[0].append(Maze.MOVESARR)
        #                         for i in range (len(Maze.SOLARR)):
        #                             print(Maze.SOLARR)
        #                             # if Maze.SOLARR[-1] == Maze.SOLARR[len(Maze.SOLARR)-1]:
        #                                 # return True
        #
        #                         # return True                 # solution found!
        #                         # no solution found from this location
        #                         if self.maze[y][x] != Maze.START:       # don't overwrite Maze.START
        #                             self.maze[y][x] = Maze.PATH         # clear failed search from map
        #                         return False
        #
        #         # except:
        #         #     self.maze[y][x] = [1, 1]
        #         # finally:
        #         #     if self.solve(ny, nx):          # recurse...
        #         #         print(Maze.SOLARR)
        #         #         # print("ciao")
        #
        #     # if self.maze[ny][nx] in Maze.OPEN:  # can I go this way?
        #     #     if self.maze[y][x] != Maze.MOVESARR: #[1:len(Maze.MOVESARR)]:
        #     #         if self.maze[y][x] != Maze.START: # don't overwrite Maze.START
        #     #             self.maze[y][x] = dir.char  # mark direction chosen
        #     #             Maze.MOVESCOUNT.append(1)
        #     #             Maze.MOVESARR.append([y,x])
        #             # for i in range (len(Maze.MOVESARR)):


def main():
    maze = Maze.load_maze("txt/maze.txt")

    def __init__(self, maze):
        self.maze = maze

    # print("Maze loaded:")
    # print(maze)

    try:
        sy, sx = maze.find_start()
        print("solving...")
        time.sleep(2)
        if maze.solve(sy, sx):
            # maze.bettersolve(sy, sx)
            print(maze)
            print("Teseo is save in", sum(Maze.MOVESCOUNT), "moves") #, sum(Maze.SOLCOUNT))
            print(Maze.MOVESARR)
            # print(Maze.SOLARR)
            # for i in range (len(Maze.MOVESARR)):
            #     # try:
            #     self.maze[Maze.MOVESARR[i+1][0]][Maze.MOVESARR[i+1][1]] = "|"
            #     if maze.solve(sy, sx):
            #         print("funziona????")
        else:
            print("There is no solution for Teseo... sorry, try again!")
            # print(Maze.MOVESARR)
            print("Try to generate a new maze")
    except ValueError:
        print("No start point found.")

if __name__=="__main__":
    main()
