# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
	print ('file cannot be opened: ', fname)

count = 0
tot = 0

# find the line
for line in fh:
    
    # clean off the line
    line=line.rstrip()

    # identify the correct row
    if not line.startswith('X-DSPAM-Confidence:') : 
        continue

    # count the number of rows
    count = count + 1

    # remove extra verbiage
    line = line.lstrip('X-DSPAM-Confidence: ')    

    tot = tot + float(line)
        
    avg = tot/count

print ('Average spam confidence: ', avg)