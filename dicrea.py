import sys
import re
import argparse
from urllib.request import urlopen

parser = argparse.ArgumentParser(description='This is a dictionary creator')
parser.add_argument('-f','--file', help='Input file')
parser.add_argument('-u','--url', help='Input url')
parser.add_argument('-o','--output', help='Output file')
parser.add_argument('-a','--append', help='Append to output file')

args = parser.parse_args()
contents=''

if not (args.file or args.url):
	print('No input file or input url selected. Use -h for help')
	exit()
else:
	if args.file:
		with open(args.file) as f:
			contents = f.read()
	if args.url:
		html = urlopen(args.url)
		charset = html.info().get_content_charset()
		contents = html.read().decode(charset, 'ignore')
		
if not args.output:
	print('No output file specified. Use -h for help')
	exit()
	
terms = ''
terms = re.findall('<p><b>([a-zA-Z ]+)', contents)
#print(terms)

with open(args.output, 'a') as f:
	for term in terms :
		f.writelines(str(term).replace(' ','') + '\n')


