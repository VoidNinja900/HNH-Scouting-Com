import json
import os

path = r"DataOfMatch"

for x in os.listdir(path):
    with open("DataOfMatch/" + x) as json_file:
        data = json.load(json_file)
        print(data)

