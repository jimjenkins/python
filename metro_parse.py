import csv

#open the sourcefile
source_filename = 'metro_dvctr_xaml.txt'



#try/except for opening the file
try:
    text = open(source_filename)
except:
    print ('cannot open the file')
    exit()

#create the buckets
projects = list()

#clean off a line in the text file
for lines in text:
    lines = lines.strip(' \t\n\r')
    lines = lines.lower()
    
    #find the lines with hxt projects
    if not lines.startswith('<helptocnode nodetype="toc" url="win|'): 
        continue
    words = lines.split()
    words = words[2]

    #find the start position for the hxt file
    start_pos = words.find('$\\')
    
    #find the end position for the hxt file
    end_pos = words.find('@', start_pos)

    #create the list of projects
    projects = words[start_pos+2:end_pos]

    with open('test.csv','w') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(projects)