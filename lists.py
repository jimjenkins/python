fhand = open('mbox-short')
for line in fhand:
    line = line.rstrip()
    if not line.startswith ('From ') : continue
    word = line.split()
    print (words(2))

line = 