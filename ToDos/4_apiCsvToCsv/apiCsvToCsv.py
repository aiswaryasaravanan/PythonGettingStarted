import requests
import csv

res = requests.get(url="https://jsonplaceholder.typicode.com/users")
data = res.json()

with open("input.txt", "r")as fileObj, open("output.csv", "w") as csvObj:
    writeObj = csv.writer(csvObj)
    fileContent = fileObj.readline()
    header = ["S.No", "Id", "Name", "Username", "Email",
              "City", "Phone", "Website", "Company Name"]
    writeObj.writerow(header)

    badChar = ["-", "(", ")", ".", "x"]
    sNo = 0

    while fileContent:
        sNo += 1
        for i in range(len(data)):

            if data[i]["email"] == fileContent.strip():

                phone = data[i]["phone"]
                for char in badChar:
                    phone = phone.replace(char, '')

                website = "https://"+data[i]["website"]

                userList = [sNo, data[i]["id"], data[i]["name"], data[i]["username"], data[i]["email"].casefold(
                ), data[i]["address"]["city"], phone, website, data[i]["company"]["name"]]
                writeObj.writerow(userList)
                break
        fileContent = fileObj.readline()
