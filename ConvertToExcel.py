import json
import os
import pandas
import xlsxwriter
path = r"DataOfMatch"
NoOfColomns = []
increment = 0

os.remove('ExcelFiles/output1.xlsx')
data1 = []
teamData = []
DataFr = []
for x in os.listdir(path):
    increment +=1
    NoOfColomns.append(increment)
    with open("DataOfMatch/" + x) as json_file:
        data = json.load(json_file)
        data1.append(data)

writer = pandas.ExcelWriter('ExcelFiles/output1.xlsx', engine = 'xlsxwriter')
increment = 0
for x in data1:
    teamData.clear()
    teamNum = x["Team#"]
    for y in data1:
        if(y["Team#"] == teamNum):
            teamData.append(y)
    DataFr.append(pandas.DataFrame(teamData))
    DataFr[increment].to_excel(writer, sheet_name="Team "+teamData[0]["Team#"])       
    increment +=1
writer.close()