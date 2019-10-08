import requests
import csv

# PARAMS = {'id': "1"}

res = requests.get(
    url="https://jsonplaceholder.typicode.com/todos/")
    
data = res.json()

list1=[]
for key in data[0]:
    list1.append(key.title())

with open("response.csv","w") as csvObj:
    writeObj=csv.writer(csvObj)
    writeObj.writerow(list1)
    list1=[]
    for element in data:
        for key in element:
            if key=="completed" :
                if element[key]==True:
                    list1.append("Yes")
                else:
                    list1.append("No")
            else:
                list1.append(element[key])
        writeObj.writerow(list1)
        list1=[]
