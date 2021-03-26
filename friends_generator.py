from os import startfile
import random as rn
import os
list_to_extract='.mkv'
my_paths=[]
path=os.getcwd()
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(list_to_extract):
            my_paths.append(os.path.join(root, file))
startfile(rn.choice(my_paths))