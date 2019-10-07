# read "input.txt" file and generate suggested email address and write to "output.txt" file


import csv

with open("input.csv") as rCSV, open("output.csv", "w") as wCSV:
    try:
        readObj = csv.reader(rCSV)
        writeObj=csv.writer(wCSV)
        count=0
        for row in readObj:
            list1=[]
            if count==0:
                list1=["name","email"]
            else:
                list1.append(f'{" ".join([row[0],row[1]])}')
                list1.append(row[2])
            writeObj.writerow(list1)
            count=count+1
    except Exception:
        print("Error :(")



