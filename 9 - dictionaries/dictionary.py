
#ask for the file name
name = input("Enter file:")

if len(name) < 1 : name = "mbox-short.txt"

handle = open(name)

lines = handle.readlines()

for line in lines:
    line = line.strip()
    print(line)


#counting
counts = dict()

names = ['cwen@iupui.edu']

for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] - counts[name] + 1
print(counts)

# get method
print counts.get(name,0)

# counts 
counts = dict()
names =[]
for name in names:
    count[names] = counts.get(name.o)+1
print (counts)




# desired output "cwen@iupui.edu 5"
