import re

str="Hello RamBabu. Have fun. guru99"

print(re.findall("Have",str))
print(re.search("Have",str))

print(re.search("Babu",str).span)
print(re.search("Babu",str).string)
print(re.search("Babu",str).group)

print(re.match("Have",str))
print(re.split(" ",str))

print(re.search("[abc]",str).group)

print(re.findall("^\w",str))
print(re.findall("^\w+",str))
print(re.findall("\w+$",str))
print(re.split("\s",str))
print(re.split("\d",str))
print(re.findall("R(\w+)",str))

if re.search("fun",str):
    print("Found")
else:
    print("Not found")