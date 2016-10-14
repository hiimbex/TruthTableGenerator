import sys, math, threading, pprint
from sympy import *

class myThread (threading.Thread):
	def __init__(self, threadID, name, finalArray):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
	def run(self):
		print "Starting " + self.name
		# what you want the thread to do during its existence
		print "Ending " + self.name

# This is the first function of the program to run.
# Input: the user's logic expression in the form of a string
# Output: the 2D table of truth values
def main(expr_string):
    expr = sympify(expr_string)
    table = rows(expr)
    return table

def rows(expr):
    finalArray = []
    # Get the variables out of the expression
    variables = expr.free_symbols
    # Go through the initial generation of the truth values
    for truth_values in cartes([True, False], repeat=len(variables)):
        # Pair each individual variable with its truth value and add to dictionary
        values = dict(zip(variables, truth_values))
        # thread1 = myThread(1, "Thread-1", finalArray)
        # thread1.start()
        # Append the variable truth values for that row
        finalArray.append(values.items())
        # Append the ultimate result of the expression for that row in the truth table
        finalArray.append(expr.subs(values))
    return finalArray

# This function creates the intial combinations of possible truth values for the variables.
# Input: the set of variables that are used in the final equation
# Output: the array of initial truth values

# This function determines the truth value of the ultimate expression based on the inital truth values for that row
# Input: the array of truth values and the ultimate expression
# Output: the truth value for a the ultimate expression


userInput = raw_input("Write a truth expression: ")
# userInput = "(A | B) & C & ~B"
print(main(userInput))
