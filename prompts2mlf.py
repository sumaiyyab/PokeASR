"""List phones used in the pronunciation dictionary.

$ python removeDupes.py [prompts] > prompts
"""

import sys
import re

if __name__ == '__main__':
	f = open(sys.argv[1])
	lines = f.readlines()
	f.close()
	cleanLines = []
	splitByWord = []
	final = ""
	for line in lines:
		line = re.sub(r'\d+. ', '', line)
		line = re.sub(r' \n', '', line)
		line = line.split()
		splitByWord.append(line)
	for i in range(len(splitByWord)):
		j = 0
		while j < len(splitByWord[i]) - 2:
			word1 = splitByWord[i][j]
			word2 = splitByWord[i][j+1]
			word3 = splitByWord[i][j+2]
			if word1 == word2 or word1 == word3:
				del splitByWord[i][j]
			else:
				j += 1
	print("#!MLF!#")
	for i, sent in enumerate(splitByWord, 1):
		print("\"*00"+str(i)+".lab\"")
		for word in sent:
			print (word)
		print(".")