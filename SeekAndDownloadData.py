import json
import os
import time

print("Sure, Why not?")

path = r"" + os.environ['USERPROFILE'] +"\\Downloads"
path2 = "DataOfMatch"


def DeleteCurrent():
    for x in os.listdir(path2):
        if x.endswith('.json') & x.__contains__('-'):
            os.remove(path2 + "/" + x)
    NowConvert()


def NowConvert():
    for x in os.listdir(path):
        if x.endswith('.json') & x.__contains__('-'):
            name = os.path.join('DataOfMatch/', x)
            f = open(name, "x")
        with open(path + "/" + x) as json_file:
            data = json.load(json_file)
            Converted = json.dumps(data)
            f.write(Converted)
            f.close


DeleteCurrent()