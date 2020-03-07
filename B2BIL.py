#Brainfuck intermediary Language (BIL)

#+ Subtract(number)
#- Add(number)
#[ {
#] }
#< Left(number)
#> Right(number)
#. Print
#, Input

import sys

def parse(c):
	output = ""
	cinput = c.split('\n')
	num = 0
	limit = len(cinput)
	while(True):
		word = cinput[num]
		if("Add" in word):
			param = (word.split('(')[1].replace(')', ''))
			for x in range(int(param)):
				output += '+'
			num += 1
		if("Subtract" in word):
			param = (word.split('(')[0].replace(')', ''))
			for x in range(int(param)):
				output += '-'
			num += 1
		if("Left" in word):
			param = (word.split('(')[1].replace(')', ''))
			for x in range(int(param)):
				output += '<'
			num += 1
		if("Right" in word): 
			param = (word.split('(')[1].replace(')', ''))
			for x in range(int(param)):
				output += '>'
			num += 1
		if("Print" in word):
			output += '.'
			num += 1
		if("Input" in word):
			output += ','
			num += 1
		if("{" in word):
			output += '{'
			num += 1
		if("}" in word):
			output += '}'
			num += 1
		if(num == limit):
			return output
def main():
	f = open(sys.argv[1])
	contents = f.read()
	f.close()
	output = parse(contents)
	of = open("out.b", "w+")
	of.write(output)
	of.close()

main()