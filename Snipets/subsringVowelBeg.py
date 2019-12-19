#miniongame
#hackerrank

s=raw_input()
kevin=0
stuart=0
vowels=set("aeiou")
for i in range(0,len(s)):
    if s[i] in vowels:
        kevin+=(len(s)-i)
    else :
        stuart+=(len(s)-i)
if stuart>kevin:
    print("Stuart "+str(stuart))
else:
    print("Kevin "+str(kevin))