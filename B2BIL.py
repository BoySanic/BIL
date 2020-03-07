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
class Operation:
	def __init__(self, o, c):
		self.opcode = o
		self.count = c
def compress(brainfuck):
	operList = []
	num = 0
	while(True):
		count = 0
		char = brainfuck[num]
		if(char == ">"):
			for x in range(num, len(brainfuck)):
				if(brainfuck[x] == ">"):
					count += 1
					num += 1
				if(brainfuck[x] == "<"):
					count -= 1
					num += 1
				if((brainfuck[x] == "<" or brainfuck[x] == ">") == False):
					break

		elif(char == "<"):
			for x in range(num, len(brainfuck)):
				if(brainfuck[x] == "<"):
					count += 1
					num += 1
				if(brainfuck[x] == ">"):
					count -= 1
					num += 1
				if((brainfuck[x] == "<" or brainfuck[x] == ">") == False):
					break
		elif(char == "+"):
			for x in range(num, len(brainfuck)):
				if(brainfuck[x] == "+"):
					count += 1
					num += 1
				if(brainfuck[x] == "-"):
					count -= 1
					num += 1
				if((brainfuck[x] == "+" or brainfuck[x] == "-") == False):
					break
		elif(char == "-"):
			for x in range(num, len(brainfuck)):
				if(brainfuck[x] == "+"):
					count -= 1
					num += 1
				if(brainfuck[x] == "-"):
					count += 1
					num += 1
				if((brainfuck[x] == "+" or brainfuck[x] == "-") == False):
					break
		elif(char == "."):
			count += 1
			num += 1
		elif(char == ","):
			count += 1
			num += 1
		elif(char == "["):
			count += 1
			num += 1
		elif(char == "]"):
			count += 1
			num += 1
		else:
			num += 1
		#raw_input()
		o = Operation(char, count)
		print(o.opcode + " " +str(o.count))
		operList.append(o)
		if(num == len(brainfuck)):
			return operList
def parse(operations):
	output = ""
	num = 0
	while(True):
		if(num == len(operations)):
			break
		if(operations[num].opcode == "+"):
			output += "Add(" + str(operations[num].count) + ")\n"
		if(operations[num].opcode == "-"):
			output += "Subtract(" + str(operations[num].count) + ")\n"
		if(operations[num].opcode == "<"):
			output += "Left(" + str(operations[num].count) + ")\n"
		if(operations[num].opcode == ">"):
			output += "Left(" + str(operations[num].count) + ")\n"
		if(operations[num].opcode == "["):
			output += "{\n"
		if(operations[num].opcode == "]"):
			output += "}\n"
		if(operations[num].opcode == "."):
			output += "Print\n"
		if(operations[num].opcode == ","):
			output += "Input\n"
		num += 1
	return output
def main():
	f = open(sys.argv[1])
	contents = f.read()
	f.close()
	operations = compress(contents)
	output = parse(operations)
	of = open(sys.argv[2], "w+")
	of.write(output)
	of.close()

main()