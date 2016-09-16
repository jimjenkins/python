#create the dictionary
counts = dict()

#ask for the file name
filename = input("Enter file:")
if len(filename) < 1 : filename = 'mbox-short.txt'

#open the file
text = open(filename)

lines = text.split()
for line in lines :
    print (line)

#words = text.split('')
#print ('words:', words)

#print ('counting...')
#for word in words:
    #counts[word] = counts.get(word,0) +1

#print ('counts', counts)