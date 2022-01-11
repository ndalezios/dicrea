import sys
import re
import argparse

parser = argparse.ArgumentParser(description='This is a dictionary creator')
parser.add_argument('-f','--file', help='Input file')
parser.add_argument('-u','--url', help='Input url')
parser.add_argument('-o','--output', help='Output file')

args = parser.parse_args()

if not (args.file or args.url):
	print('No input file or input url selected. Use -h for help')
	exit()

if not args.output:
	print('No output file specified. Use -h for help')
	exit()

fname = sys.argv[1]
terms = ''
with open(fname) as f:
	contents = f.read()
	#print(contents)
	terms = re.findall('<p><b>([a-zA-Z ]+)', contents)
#print terms
with open('output.txt', 'w') as f:
	for term in terms :
		f.writelines(str(term).replace(' ','') + '\n')
