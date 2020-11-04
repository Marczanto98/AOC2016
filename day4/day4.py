import os
import sys
import collections

#####
sum = 0
search_pattern = "northpole object storage"
search_ID = 0
#####

if __name__ == "__main__":
    with open(os.path.join(sys.path[0],"input.txt"), "r") as f:
        instructions = f.readlines()

    for line in instructions:
        chars = "".join([i for i in line if not i.isdigit()]).split("-")
        num = int("".join([i for i in line if i.isdigit()]))

        letters = {}
        for i in range(len(chars)-1):
            for ch in chars[i]:
                if ch not in letters:
                    letters[ch] = 1
                else:
                    letters[ch] += 1

        letters = dict(sorted(letters.items(),  key=lambda x:x[0].lower())) #sorting alphabetically
        letters = dict(sorted(letters.items(), key=lambda item: -item[1])) #sorting by value descending
        letters = collections.OrderedDict(letters)
    
        flag_new = flag_old = -1
        for ch in chars[-1][1:-2]:
            try:
                flag_new = list(letters.keys()).index(ch)
                if(flag_new < flag_old):
                    break
                flag_old = flag_new
            except:
                break
        else:
            sum += num
        
        name = ""
        for word in chars[:-1]:
            for ch in word:
                name += chr((ord(ch) + num - 97) % 26 + 97)
            name += " "
        if name[:-1] == search_pattern:
            search_ID = num

    print("Sum = {}".format(sum))
    print("ID of the room where North Pole objects are stored = {}".format(search_ID))
    