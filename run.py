print("\033[92m" "Android mass junk file maker by Danii Saahir")
print("\033[31m" "(CHECK YOUR MAIN STORAGE xD)")
import random

for i in range(100000):
    f = open("/storage/emulated/0/Kote {}".format(i), "w")
    for w in range(1000):
        f.write(str(random.randint(17348574, 73457689345677)))
