fname = input("Enter file name: ")

try:
    filehandle = open(fname)
except:
    print ('cannot open this file')

count = 0

for line in filehandle:
    line = line.rstrip()
    if not line.startswith ('From ') : continue
    word = line.split()
    print (word[1])
    count = count + 1

print ('There were', count, 'lines in the file with From as the first word.')