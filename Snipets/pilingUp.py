n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))

while l:
    M=max(l)

    if l[0]==M or l[len(l)-1]==M:
        l.remove(M)
    else:
        print("no")
        break
