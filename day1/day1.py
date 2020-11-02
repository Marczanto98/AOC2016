import os
import sys

######################
dirs = {0:"N", 1:"E", 2:"S", 3:"W"}
cords = {"X":0, "Y":0}
turns = {"R":1, "L":-1}
moves = {"N":("Y",1), "E":("X",1), "S":("Y",-1), "W":("X",-1)}
######################
visited_cords = []


if __name__ == "__main__":
    with open(os.path.join(sys.path[0],"input.txt"), "r") as f:
        steps = f.read().split(", ")
        curdir = 0
        flag = True
        for step in steps:
            turn = turns[step[0]]
            curdir = (curdir + turn) % 4
            dist = int(step[1:len(step)+1])

            for xy in range(dist):
                if moves[dirs[curdir]][0] == "X":
                    toappend = {"X" : cords["X"] + xy, "Y" : cords["Y"]}
                else:
                    toappend = {"X" : cords["X"], "Y" : cords["Y"]  + xy}
                if toappend in visited_cords and flag:
                    first_loc_visited_twice = toappend
                    flag = False 
                visited_cords.append(toappend)
            cords[moves[dirs[curdir]][0]] += dist * moves[dirs[curdir]][1]
            dist = abs(cords["X"]) + abs(cords["Y"])
        # print(visited_cords)
        print("Final cords = {}".format(cords))
        print("Distance is = {}".format(dist))
        if first_loc_visited_twice != None:
            print("Firts location visited twice = {}".format(first_loc_visited_twice))
            print("Dist to this location = {}".format(abs(first_loc_visited_twice["X"]) + abs(first_loc_visited_twice["Y"])))
            
