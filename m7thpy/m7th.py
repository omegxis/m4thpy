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


		regex_rules = "^(derive)\s+((g\s[^\s]+)|([^\s]+))\s+((([a-zA-Z])\s+([-+]?\d+(\.\d+)?){0,1})|([a-zA-Z]))\s*$"
		match = re.search(regex_rules, input_val)

		if (match):
			print("acceptable input")
			call_derivative(input_val)
		elif (input_val != quit_token):
			print("unacceptable input")
	print("Program closed")


if __name__ == '__main__':
	main()
