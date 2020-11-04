import os
import sys
import numpy as np

#########
possible_triangles = 0
possible_triangles_vertically = 0
all_triangles = []
#########

def check_triangle_valid(sides):
    a, b, c = sorted(sides)
    if (a + b > c):
        return True
    else:
        return False

if __name__ == "__main__":
    with open(os.path.join(sys.path[0],"input.txt"), "r") as f:
        instructrions = f.readlines()

    for line in instructrions:
        sides = list(map(int,line.split()))
        all_triangles.append(sides)
        sides = sorted(sides)
        if check_triangle_valid(sides):
            possible_triangles += 1
            
    for i in range(0, len(all_triangles)-2, 3):
        tmp = np.transpose(all_triangles[i:i+3])
        for sides in tmp:
            if check_triangle_valid(sides):
                possible_triangles_vertically += 1

    print("Number of possible triangles is: {}".format(possible_triangles))
    print("Number of possible triangles vertically is: {}".format(possible_triangles_vertically))

            

