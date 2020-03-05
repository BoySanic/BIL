#Brainfuck intermediary Language (BIL)

#+ Subtract(number)
#- Add(number)
#[ {
#] }
#< Left(number)
#> Right(number)
#. Print
#, Input


def parse(c):
	output = ""
	cinput = c.Split(' ')
	num = 0
	while(True):
		word = cinput[num]
		if(cinput.Contains("Add")):
			param = (cinput.Split('(')[0].replace(')', ''))
			for x in range(int(param)):
				output += '+'
			num += 1
		if(cinput.Contains("Subtract")):
			param = (cinput.Split('(')[0].replace(')', ''))
			for x in range(int(param)):
				output += '-'
			num += 1
		if(cinput.Contains("Left")):
			param = (cinput.Split('(')[0].replace(')', ''))
			for x in range(int(param)):
				output += '<'
			num += 1
		if(cinput.Contains("Right")):
			param = (cinput.Split('(')[0].replace(')', ''))
			for x in range(int(param)):
				output += '>'
			num += 1
		if(cinput.Contains("Print")):
			output += '.'
		if(cinput.Contains("Input")):
			output += ','
		if(cinput.Contains("{")):
			output += '{'
		if(cinput.Contains("}")):
			output += '}'

def main():
	f = fopen(sys.argv[1])
	contents = f.read()
	output = parse(contents)