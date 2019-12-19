from collections import OrderedDict
string=raw_input()
k=int(input())

i=0
str1=""
while i<len(string):
    l=list(OrderedDict.fromkeys(string[i:i+k]))
    print("".join(l))
    i+=k


# i=0
# for c in string[i:i+k]:
#     l=[]
#     if c not in l:
#         l.append(c)
    
#     # print("".join(filter(lambda ele: l.append(ele) if ele not in l else None,string[i:i+k])))
#     i+=k


