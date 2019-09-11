import re
from derive_mod import derive_fun


def call_derivative(input_val):
	temparray = input_val.split()
	print(temparray)
	derive_fun(temparray)
	
def call_integral():
	print("test")


def main():
	input_val = ""
	quit_token = "-quit"

	while input_val != quit_token:
		first_message = "Welcome to m7thpy. Input a command, according the the key. Type help(command) for clarification "
		print(first_message)
		input_val = input()

		#Might assign "graph" to variable so it can be changed to anything to user may want, if I add that feature
		#Note from September 10th: Allow regex to accept fractions and special constants
		regex_rules = "^(derive)\s+((graph\s[^\s]+)|([^\s]+))\s+((([a-zA-Z])\s+([-+]?\d+(\.\d+)?){0,1})|([a-zA-Z]))\s*$"
		match = re.search(regex_rules, input_val)

		#have seperate module for adding "*" when doing multiplication
		#input problems with e. sympy requires exp(x) to understand e^x. Seperate module must be made for cleaning input	
		if (match):
			print("acceptable input")
			call_derivative(input_val)
		elif (input_val != quit_token):
			print("unacceptable input")
	print("Program closed")


if __name__ == '__main__':
	main()
