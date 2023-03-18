import json
import os
import time

print("Sure, Why not?")

path = r"%USERPROFILE%\Downloads"


for x in os.listdir(path):
    if x.endswith('.json'):
        os.path.join('DataOfMatch', x)
        open(x, "x")
