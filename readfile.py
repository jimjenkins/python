def main():
	#read file
	file = open( "Yesno.txt", "r")
	lines = file.readlines()
	file.close()

	# look for patterns
	for line in lines:
		line = line.strip()
		print(line)
	
	#display reslts

main()