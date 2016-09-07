fname = raw_input("Enter file name: ")

try:
    fh = open(fname)
except:
    print('cannot open the file')

wordlist = []

for line in fh:
    words = line.split()
    for word in words:
        if word in wordlist: continue
        wordlist.append(word)
wordlist.sort() 
print (wordlist)

fh.close