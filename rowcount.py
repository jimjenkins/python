filehandle = open('file.txt', 'r')

count = 0

for i in filehandle:
    count=count+1

print(count)