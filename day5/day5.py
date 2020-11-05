import os
import sys
import hashlib

######
input = "abbhdwsy"
password = ""
password2 = ["*"] * 8
free_index = [str(i) for i in range(8)]
######

if __name__ == "__main__":
    i = 0
    while True:
        hash_md5 = hashlib.md5((input + str(i)).encode()).hexdigest()
        if hash_md5[:5] == "00000":
            password += hash_md5[5]
            if hash_md5[5] in free_index:
                password2[int(hash_md5[5])] = hash_md5[6]
                free_index.remove(hash_md5[5])
            if len(password) > 7 and "*" not in password2:
                break
        i += 1
    print("Password = {}".format(password[:8]))
    print("Password2 = {}".format("".join(password2)))

