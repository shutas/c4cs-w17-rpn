#!/usr/bin/env python3
import operator
import readline
import sys
from termcolor import colored, cprint

OPERATORS = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow,
}
def calculate(arg):
	stack = list()
	for operand in arg.split():
		try:
			operand = float(operand)
			stack.append(operand)
		except:
			arg2 = stack.pop()
			arg1 = stack.pop()
			operator_fn = OPERATORS[operand]
			result = operator_fn(arg1, arg2)
			stack.append(result)
	
	return stack.pop()

def lessenCoverage():
	print("This should lower the coverage percentage")
	print("Because new codeis added.")
	print("But I never execute this.")
	print(":)")

def main():
	while True:
		user_input = input('rpn calc> ')
		if (user_input == 'quit'):
			break
		else:
			result = calculate(user_input)
			print("You entered: ", end = '')
			for i in user_input:
				if (i == '+'):
					cprint(i, 'red', attrs=['bold'], end = '')
				elif (i == '-'):
					cprint(i, 'blue', attrs=['bold'], end = '')
				elif (i == '*'):
					cprint(i, 'grey', attrs=['bold'], end = '')
				elif (i == '/'):
					cprint(i, 'yellow', attrs=['bold'], end = '')
				else:
					print(i, end = '')
			print()
			print("Result:", result)

if __name__ == '__main__':
	main()
