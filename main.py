import sys, math, threading, pprint
from sympy import *

lock = threading.Lock()

class myThread (threading.Thread):
	def __init__(self, threadID, name, values, expr, finArr):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.values = values
		self.expr = expr
		self.finArr = finArr
	def run(self):
		# print "Starting " + self.name, self.threadID
		# what you the thread does during its existence
		x = self.values.items()
		y = self.expr.subs(self.values)
		lock.acquire()
		try:
			# Append the variable truth values for that row
			# Append the ultimate result of the expression for that row in the truth table
			self.finArr.append(x)
			self.finArr.append(y)
		finally:
			lock.release()
		# print "Ending " + self.name, self.finArr

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
    threads = []
    threadID = 1
    # Get the variables out of the expression
    variables = expr.free_symbols
    # Go through the initial generation of the truth values
    for truth_values in cartes([True, False], repeat=len(variables)):
        # Pair each individual variable with its truth value and add to dictionary
        values = dict(zip(variables, truth_values))
		#start a unique thread for each row
        thread = myThread(threadID, "Thread-"+str(threadID), values, expr, finalArray)
        thread.start()
        threads.append(thread)
        threadID += 1

    for t in threads:
        # print("joining thread")
        t.join()
    return finalArray

# userInput = raw_input("Write a truth expression: ")
userInput = "(a & b) | (c & ~d)"

print(main(userInput))
