import os
import sys
import string

######
lettercounter = [dict.fromkeys(string.ascii_lowercase, 0) for i in range(8)] # *8 make shallow copies
######

if __name__ == "__main__":
    with open(os.path.join(sys.path[0],"input.txt"), "r") as f:
        instructrions = f.readlines()
    for line in instructrions:
        for i, ch in enumerate(line[:-1]):
            lettercounter[i][ch] += 1

    lettercounter = [dict(sorted(column.items(), key=lambda item: -item[1])) for column in lettercounter]
    password1 = "".join([list(column.keys())[0] for column in lettercounter])
    password2 = "".join([list(column.keys())[25] for column in lettercounter])

    print("Password nr. 1 = {}".format(password1)) 
    print("Password nr. 2 = {}".format(password2)) 