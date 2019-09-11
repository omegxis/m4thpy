from sympy import symbols
from sympy.plotting import plot
from sympy import diff
from sympy.parsing.sympy_parser import parse_expr

def derive_fun(input_val):
        #Evaluates single variable derivative
        #Non-polar, parametric.
        #Add more documentation and clean up code. 
        evaluate_at = True
        x = None
        der = None
        gr = None
        point = None
        is_frac = True


        fr_ar = input_val[len(input_val)-1].split("/")
        
        if (len(fr_ar) == 1):
                #last input is only a single entity. We can check if its an int or anything else
                try:
                        int(input_val[len(input_val)-1])
                        
                except ValueError:
                        evaluate_at = False

        else:
                #Last input must be a fraction
                tn = input_val[len(input_val)-1]
                input_val[len(input_val)-1] = eval(tn)

        #Not the most efficient method for determining what the user wants. Find another way to make it more efficient
        #Maybe use switch cases

        #to evaluate a derivative at point: derivative_variable.evalf(subs={x: value1, y: value2, ...})

        #graph and evaluate
        if (input_val[1] == "graph" and evaluate_at == True):
                point = float(input_val[4])
                x = symbols(input_val[3])

                der = diff(input_val[2], x)
                pder = der.evalf(subs={x: point})

                print("Derivative: ", der)
                print("Derivative evaluated at given value = ", pder)
                gr = plot(der, show=False)
                gr.show()
               
        #graph and do not evaluate
        elif(input_val[1] == "graph" and evaluate_at == False):

                x = symbols(input_val[3])
                der = diff(input_val[2], x)
                print("Derivative: ", der)
                gr = plot(der, show=False)
                gr.show()

        #do not graph and evaluate
        elif (input_val[1] != "graph" and evaluate_at == True):
                point = float(input_val[3])
                x = symbols(input_val[2])

                der = diff(input_val[1], x)
                pder = der.evalf(subs={x:point})

                print("Derivative: ", der)
                print("Derivative evaluated at given value = ", pder)

        #do not graph and do not evaluate
        elif (input_val[1] != "graph" and evaluate_at == False):
                x = symbols(input_val[2])
                der = diff(input_val[1], x)
                print("Derivative: ", der)
                
        else: #This expression might not be needed, since regex takes care of problematic input. It doesn't hurt to have a fail safe
                print("Error in expression. Type help(derivative) to read about input. Type example derivative to see an example")



