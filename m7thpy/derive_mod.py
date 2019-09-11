from sympy import symbols
from sympy.plotting import plot
from sympy import diff
from sympy.parsing.sympy_parser import parse_expr

def derive_fun(input_val):
	evaluate_at = True
	x = None
	der = None
	gr = None
	point = None

	try:
		int(input_val[len(input_val)-1])
	except ValueError:
		evaluate_at = False


	#not the most efficient method for determining what the user wants. Find another way to make it more efficient
	#Maybe use switch cases

	#to evaluate a derivative at point: derivative_variable.evalf(subs={x: value1, y: value2, ...})

	#graph and evaluate
	if (input_val[1] == "graph" and evaluate_at == True):

		point = int(input_val[4])
		x = symbols(input_val[3])

		der = diff(input_val[2], x)
		pder = der.evalf(subs={x: point})

		print(pder)
		gr = plot(der, show=False)
		gr.show()
		gr.close()

	#graph and do not evaluate
	elif(input_val[1] == "graph" and evaluate_at == False):

		x = symbols(input_val[3])
		der = diff(input_val[2], x)
		print(der)
		gr = plot(der, show=False)
		gr.show()

	#do not graph and evaluate
	elif (input_val[1] != "graph" and evaluate_at == True):
		point = int(input_val[3])
		x = symbols(input_val[2])

		der = diff(input_val[1], x)
		pder = der.evalf(subs={x:point})

		print(pder)


	#do not graph and do not evaluate
	elif (input_val[1] != "graph" and evaluate_at == False):
		x = symbols(input_val[2])
		der = diff(input_val[1], x)
		print(der)
	else: #This expression might not be needed, since regex takes care of problematic input. It doesn't hurt to have a fail safe
		print("Error in expression. Type help(derivative) to read about input. Type example derivative to see an example")


		





