import time

print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))

for i in range(1,5):
    print(i)
    time.sleep(1)