import json
import os
import time

print("Sure, Why not?")

path = r"C:/Users/mike1/Downloads"


for x in os.listdir(path):
    if x.endswith('.json') & x.__contains__('-'):
        name = os.path.join('DataOfMatch/', x)
        f = open(name, "x")
        with open(path + "/" + x) as json_file:
            data = json.load(json_file)
            Converted = json.dumps(data)
            f.write(Converted)
            f.close
