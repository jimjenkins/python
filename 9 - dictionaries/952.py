#ask for the file name, if none then use the default
filename = input("Enter file:")
if len(filename) < 1 : filename = 'mbox-short.txt'

try:
    text = open(filename)
except:
    print ('cannot open this file')
    exit()

#create the dictionary
counts = dict()
textlist = list()

#split each line into words and print the ones that start with 'From'
for line in text :
    line = line.rstrip()
    if not line.startswith ('From ') : continue
    text = line.split()
    words = text[1]
    for word in words :
        textlist.append(words)
        print (textlist)
        if word not in counts :
           counts[word] = 1
        else:
            counts[word] = counts[word] + 1
    #print(counts)

#using the dictionary look for the maximum key and the associated email
maxkey = 0
maxvalue = ''
for eachkeyvalue in counts:
    if counts[eachkeyvalue] > maxkey :
        maxkey = counts[eachkeyvalue]
        maxvalue = eachkeyvalue
print (maxvalue, maxkey)

# Desired output 'cwen@iupui.edu 5'