# read "input.txt" file and generate suggested email address and write to "output.txt" file

import csv

with open("details.csv") as csvObj, open("emailList.txt", "a") as txtObj:
    try:
        content = csv.reader(csvObj)
        for row in content:
            # print(f'{", ".join(row)}')
            # print(row[2])
            txtObj.write(row[2])
            txtObj.write("\n")
    except Exception:
        print("Error :(")
