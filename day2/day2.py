import os
import sys

keypad = [[1,2,3],
          [4,5,6],
          [7,8,9]]

keypad2 = [[0,0,1,0,0],
           [0,2,3,4,0],
           [5,6,7,8,9],
           [0,10,11,12,0],
           [0,0,13,0,0]]

num_to_char = {10 : "A", 11 : "B", 12 : "C", 13 : "D"}

position = {"x" : 1, "y" : 1} # 3x3 tab
code = ""
code2 = ""

if __name__ == "__main__":
    with open(os.path.join(sys.path[0],"input.txt"), "r") as f:
        instructrions = f.readlines()
        for line in instructrions:
            for turn in line:
                if position["x"] > 0:
                    if turn == "L":
                        position["x"] -= 1 
                if position["x"] < 2:
                    if turn == "R":
                        position["x"] += 1 
                if position["y"] > 0:
                    if turn == "U":
                        position["y"] -= 1 
                if position["y"] < 2:
                    if turn == "D":
                        position["y"] += 1 
            code += str(keypad[position["y"]][position["x"]])
        print("Code nr 1 = {}".format(code))
    ###Part 2
    position["x"] = position["y"] = 2
    with open(os.path.join(sys.path[0],"input.txt"), "r") as f:
        instructrions = f.readlines()
        for line in instructrions:
            for turn in line:
                if position["x"] > 0 and keypad2[position["y"]][position["x"]-1] != 0:
                    if turn == "L" :
                        position["x"] -= 1 
                if position["x"] < 4 and keypad2[position["y"]][position["x"]+1] != 0:
                    if turn == "R":
                        position["x"] += 1 
                if position["y"] > 0 and keypad2[position["y"]-1][position["x"]] != 0:
                    if turn == "U":
                        position["y"] -= 1
                if position["y"] < 4 and keypad2[position["y"]+1][position["x"]] != 0:
                    if turn == "D":
                        position["y"] += 1
            if keypad2[position["y"]][position["x"]] < 10:
                to_add = keypad2[position["y"]][position["x"]]
            else:
                to_add = num_to_char[keypad2[position["y"]][position["x"]]]
            code2 += str(to_add)
        print("Code nr 2 = {}".format(code2))