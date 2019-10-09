# Accept a number "N" from command line and generate N user data and write it to csv file

# Columns

# name random name (two words)
# website abc.xyz (abc, xyz - random)
# email slug-name@company-website
# mobile random 10 digit number starting with 7 or 8 or 9
# gender "M" or "F"
# salutation (Mr, Dr) if Male, (Miss, Mrs, Dr) if Female
# country India, China, Singapore, Malaysia or any proper country name. you can have hard coded set
# country code IN, CN - valid code as per country
# dob any valid date but the age must be >= 18 and <= 80
# mother tongue
# (Tamil/Telugu/Malayalam/Hindi) if India;
# (Chinese/Simplified Chinese) if China;
# (Malay/Tamil) if Malaysia;
# (Tamil/Chinese/Malay/English) if Singapore;
# (English) if other countries

import random
import string
import csv

letters = string.ascii_lowercase
domainList = ["com", "in", "co"]
genderList = {"M": ["Mr", "Dr"], "F": ["Miss", "Mrs", "Dr"]}
countryList = {"India": {"motherTongue": ['Tamil', 'Telugu', 'Malayalam', 'Hindi'], "countryCode": "IN"},
               "China": {"motherTongue": ['Chinese', 'Simplified Chinese'], "countryCode": "CN"},
               "Malaysia": {"motherTongue": ['Malay', 'Tamil'], "countryCode": "ML"},
               "Singapore": {"motherTongue": ['Tamil', 'Chinese', 'Malay', 'English'], "countryCode": "SG"}}


def getRandomNumber(start, end):
    return random.randint(start, end)


def getRandomString():
    return ''.join(random.choice(letters) for i in range(0, getRandomNumber(1, 10)))


def generateName():
    fName = getRandomString()
    lName = getRandomString()
    return f'{" ".join([fName,lName])}'.title()


def generateCompanyWebsite():
    companyName = getRandomString()
    domain = random.choice(domainList)
    return f'{".".join([companyName,domain])}'.casefold()


def generateEmail(name, companyWebsite):
    return f'{"@".join([name.replace(" ","").casefold(),companyWebsite])}'


def getGender():
    return random.choice(list(genderList))


def getSalution(gender):
    return random.choice(list(genderList[gender]))


def getCountry():
    return random.choice(list(countryList))


def getMotherTongue():
    return random.choice(list(countryList[country]["motherTongue"]))


def getCountryCode():
    return random.choice(list([countryList[country]["countryCode"]]))


N = int(input("Enter N : "))

with open("output.csv", "w") as csvObj:
    writeObj = csv.writer(csvObj)
    writeObj.writerow(["Name", "CompanyWebsite", "Email", "PhoneNo",
                       "Gender", "Salution", "Country", "MotherTongue", "CountryCode"])

    while N:
        userData = []

        name = generateName()
        userData.append(name)

        companyWebsite = generateCompanyWebsite()
        userData.append(companyWebsite)

        email = generateEmail(name, companyWebsite)
        userData.append(email)

        phoneNo = getRandomNumber(7000000000, 9999999999)
        userData.append(phoneNo)

        gender = getGender()
        userData.append(gender)

        salution = getSalution(gender)
        userData.append(salution)

        country = getCountry()
        userData.append(country)

        motherTongue = getMotherTongue()
        userData.append(motherTongue)

        countryCode = getCountryCode()
        userData.append(countryCode)

        writeObj.writerow(userData)
        N = N-1
