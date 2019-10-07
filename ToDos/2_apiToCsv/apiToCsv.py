import requests
import csv

# PARAMS = {'id': "1"}

res = requests.get(
    url="https://jsonplaceholder.typicode.com/todos/")
    
data = res.json()

list1=[]
for key in data[0]:
    list1.append(key)

with open("response.csv","w") as csvObj:
    writeObj=csv.writer(csvObj)
    writeObj.writerow(list1)
    list1=[]
    count=0
    for row in data:
        for key in data[count]:
            list1.append(row[key])
        writeObj.writerow(list1)
        list1=[]
        count=count+1

