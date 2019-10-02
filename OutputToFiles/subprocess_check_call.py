import subprocess;
 
with open("output.txt","wb") as fileobj:
    subprocess.check_call(["python","hello.py"],stdout=fileobj)

# print(subprocess.call("pwd",shell=True))