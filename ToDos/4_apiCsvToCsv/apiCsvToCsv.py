import requests
import csv


def writeCSV(row):
    writeObj.writerow(row)


def convert(data):
    return dict(data)


def getValue(key):
    return userData[key]


def refineEmail():
    email = getValue("email")
    return email.casefold()


def refinePhone():
    phone = getValue("phone")
    for char in badChar:
        phone = phone.replace(char, '')
    return phone


def getWebsite():
    return "https://"+getValue("website")


def getCity():
    return userData["address"]["city"]


def getCompanyName():
    return userData["company"]["name"]


with open("input.txt", "r")as fileObj, open("output.csv", "w") as csvObj:

    writeObj = csv.writer(csvObj)
    fileContent = fileObj.readline()

    header = ["S.No", "Id", "Name", "Username", "Email",
              "City", "Phone", "Website", "Company Name"]
    badChar = ["-", "(", ")", ".", "x"]
    sNo = 0
    URL = "https://jsonplaceholder.typicode.com/users"

    writeCSV(header)

    while fileContent:
        userList = []
        sNo += 1

        PARAMS = {"email": fileContent.strip()}
        res = requests.get(url=URL, params=PARAMS)
        data = res.json()

        userData = convert(data[0])

        userList.append(sNo)

        id = getValue("id")
        userList.append(id)

        name = getValue("name")
        userList.append(name)

        username = getValue("username")
        userList.append(username)

        email = refineEmail()
        userList.append(email)

        phone = refinePhone()
        userList.append(phone)

        website = getWebsite()
        userList.append(website)

        city = getCity()
        userList.append(city)

        companyName = getCompanyName()
        userList.append(companyName)

        writeCSV(userList)
        fileContent = fileObj.readline()
