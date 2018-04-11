from __future__ import print_function, division
from app import solve
import random
import time

class Mazegen:
    asciiart = '''
 888             d8888 888888b.  8888888 8888888b.  8888888 888b    888 88888888888 888    888
 888            d88888 888  "88b   888   888   Y88b   888   8888b   888     888     888    888
 888           d88P888 888  .88P   888   888    888   888   88888b  888     888     888    888
 888          d88P 888 8888888K.   888   888   d88P   888   888Y88b 888     888     8888888888
 888         d88P  888 888  "Y88b  888   8888888P"    888   888 Y88b888     888     888    888
 888        d88P   888 888    888  888   888 T88b     888   888  Y88888     888     888    888
 888       d8888888888 888   d88P  888   888  T88b    888   888   Y8888     888     888    888
 88888888 d88P     888 8888888P" 8888888 888   T88b 8888888 888    Y888     888     888    888
 8888888888 .d8888b.   .d8888b.        d8888 8888888b.  8888888888      888 888
 888       d88P  Y88b d88P  Y88b      d88888 888   Y88b 888             888 888
 888       Y88b.      888    888     d88P888 888    888 888             888 888
 8888888    "Y888b.   888           d88P 888 888   d88P 8888888         888 888
 888           "Y88b. 888          d88P  888 8888888P"  888             888 888
 888             "888 888    888  d88P   888 888        888             Y8P Y8P
 888       Y88b  d88P Y88b  d88P d8888888888 888        888              "   "
 8888888888 "Y8888P"   "Y8888P" d88P     888 888        8888888888      888 888
 '''

    print(asciiart)
    print("Personalize your labirinth...")

    while True:
        try:
            row = eval(input("How many row do you want? (from 8 to 56) [default is 12]:") or "12")
            if 8 <= row <= 56:
                break
            else:
                print ("You have insert a value out of range")
        except NameError:
            print("Input was not a digit - please try again.")

    while True:
        try:
            column = eval(input("How many column do you want? (from 8 to 56) [default is 12]:") or "12")
            if 8 <= column <= 56:
                break
            else:
                print ("You have insert a value out of range")
        except NameError:
            print("Input was not a digit - please try again.")

    while True:
        try:
            density = eval(input("Wich density of black blocks do you want? (from 0 to 1 es 0.35) [default is 0.15]:") or "0.15")
            if 0.01 <= density <= 1.00:
                break
            else:
                print ("You have insert a value out of range")
        except NameError:
            print("Input was not a digit - please try again.")

    print("Generate your maze...")
    time.sleep(1)

    ##grid array of array
    arr = []
    blackblocks = round(column*row*density)
    whiteoveralls = round(column*row*(1-density))
    for i in range (blackblocks): arr.insert(0, "X")
    for i in range (whiteoveralls): arr.insert(0, " ")
    random.shuffle(arr)

    @classmethod
    def __init__(self, maze):
        super(Mazegen, self).__init__()
        self.maze = maze

    def split(arr, size):
         arrs = []
         while len(arr) > size:
             pice = arr[:size]
             arrs.append(pice)
             arr   = arr[size:]
         arrs.append(arr)
         return arrs

    def gridarr():
        gridarr = Mazegen.split(Mazegen.arr, Mazegen.column)
        return gridarr

    def print_maze():
        open("txt/maze.txt", "w").close()
        text_file = open("txt/maze.txt", "a")
        text_file.write('X'+'X'*int(Mazegen.column)+'X\n')
        text_file.write('S' + "".join(Mazegen.gridarr()[0]) + 'X\n')
        for i in range (1, Mazegen.row-1): text_file.write('X' + "".join(Mazegen.gridarr()[i]) + 'X\n')
        text_file.write('X' + "".join(Mazegen.gridarr()[Mazegen.row-1]) + 'E\n')
        text_file.write('X'+'X'*int(Mazegen.column)+'X\n')
        text_file.close()
        f = open("txt/maze.txt", "r")
        print(f.read())
        f.close

    def output():
        Mazegen.print_maze()
        ask = input("If you want to solve this maze ask to Teseo...[Y/n]?") or "y"
        if ask == "n":
            pass
        elif ask == "y":
            solve.main()
