import json
import os
import pandas
import xlsxwriter
path = r"DataOfMatch"
NoOfColomns = []
increment = 0

os.remove('ExcelFiles/output1.xlsx')
data1 = []
for x in os.listdir(path):
    increment +=1
    NoOfColomns.append(increment)
    with open("DataOfMatch/" + x) as json_file:
        data = json.load(json_file)
        data1.append(data)

DataFr = pandas.DataFrame(data1, index= [NoOfColomns])

print(DataFr)
DataFr.to_excel('output1.xlsx', engine='xlsxwriter')
FixDirectory = os.rename('output1.xlsx','ExcelFiles/output1.xlsx' )





