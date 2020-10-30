import os
import sys

######################
dirs = {1:"N", 2:"E", 3:"S", 4:"W"}
cords = {"X" : 0, "Y" : 0}
######################

if __name__ == "__main__":
    with open(os.path.join(sys.path[0],"input.txt"), "r") as f:
        steps = f.read().split(", ")
        # print(steps)
        cudir = dirs[1]
        for step in steps:
            pass

