import sys
import re

fname = sys.argv[1]
terms = ''
with open(fname) as f:
	contents = f.read()
	#print(contents)
	terms = re.findall('<p><b>([a-zA-Z ]+)', contents)
print terms
with open('output.txt', 'w') as f:
	for term in terms :
		f.writelines(str(term)+'\n')
