import sys, math, threading, pprint
from sympy import *

class myThread (threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
	def run(self):
		print "Starting " + self.name, self.counter
		# what you want the thread to do during its existence
		print "Ending " + self.name

# This is the first function of the program to run.
# Input: the user's logic expression in the form of a string
# Output: the 2D table of truth values
def main(expr_string):
    expr = sympify(expr_string)
    table = rows(expr)
    return table

# This function creates the final table of truth values with the variables and the final expression for each row
# Input: the preformatted logic string
# Output: the final array
def rows(expr):
    finalArray = []
    counter = 1
    # Get the variables out of the expression
    variables = expr.free_symbols
    # Go through the initial generation of the truth values
    for truth_values in cartes([True, False], repeat=len(variables)):
        # Pair each individual variable with its truth value and add to dictionary
        values = dict(zip(variables, truth_values))
        thread = myThread(1, "Thread-"+str(counter), counter)
        thread.start()
        # Append the variable truth values for that row
        finalArray.append(values.items())
        # Append the ultimate result of the expression for that row in the truth table
        finalArray.append(expr.subs(values))
        counter += 1
    return finalArray


# userInput = raw_input("Write a truth expression: ")
userInput = "(A | B) & C & ~B"
print(main(userInput))
