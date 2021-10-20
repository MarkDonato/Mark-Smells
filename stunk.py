import os
import random

def stunker():
    if not os.path.exists("../../stinky"):
        os.makedirs("../../stinky")

    for i in range(random.randrange(50,200)):
        with open(os.path.join("../../stinky/","stinky",str(i),".txt"), 'w') as temp_file:
            temp_file.write("stinky")

    return 1
