#!/usr/bin/env python3
import os
import random

def stunker():
    if not os.path.exists("../../stinky"):
        os.makedirs("../../stinky")

    for i in range(random.randrange(50,200)):
        filename = "stinky"+str(i)+".txt"
        with open(os.path.join("../../stinky/",filename), 'w') as temp_file:
            temp_file.write("stinky" * random.randrange(100,1000))

    return 1
