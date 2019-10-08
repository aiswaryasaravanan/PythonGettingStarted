import requests
import csv
import stringcase

# PARAMS = {'id': "1"}

res = requests.get(url="https://jsonplaceholder.typicode.com/todos/")

data = res.json()

with open("response.csv", "w") as csvObj:
    # write header
    header = []
    for key in data[0]:
        header.append(stringcase.pascalcase(key))
    writeObj = csv.writer(csvObj)
    writeObj.writerow(header)

    # write record
    for row in data:
        record = []
        for key in row:
            if key == "completed":
                record.append("Yes" if row[key] == True else "No")
            else:
                record.append(row[key])
        writeObj.writerow(record)
