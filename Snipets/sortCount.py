# s = raw_input()
# a=list(s)
# res=sorted(dict.fromkeys(a),key=lambda ele:a.count(ele),key=sorted(a))
# print(res)
# for i in range(3):
#     print(res[len(res)-1-i],a.count(res[i]))

# s = "EBBBAAACCD"    
# p = [(i,s.count(i)) for i in sorted(set(s))]
# print(p)

s="qwertyuiopasdfghjklzxcvbnm"
a=list(s)
res=sorted(dict.fromkeys(a),key=lambda ele:a.count(ele),reverse=True)
for i in range(3):
    print(res[i],a.count(res[i]))   