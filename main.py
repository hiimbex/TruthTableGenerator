import sys, math, threading, pprint
from sympy import *

class myThread (threading.Thread):
	def __init__(self, threadID, name, values, expr, finArr):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.values = values
		self.expr = expr
		self.finArr = finArr
	def run(self):
		x = self.values.items()
		y = self.expr.subs(self.values)
		lock.acquire()
		try:
			# Append the variable truth values for that row
			self.finArr.append(x)
            # Append the ultimate result of the expression for that row in the truth table
			self.finArr.append(y)
		finally:
			lock.release()
		# print "Ending " + self.name, self.finArr

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
        # add each thread to a list so that we can join them later
        threads.append(thread)
        threadID += 1
    #join the finished threads together
    for t in threads:
        t.join()
    return finalArray

# Main part of the program
userInput = raw_input("Write a truth expression: ")
lock = threading.Lock()
expr = sympify(userInput)
table = rows(expr)
print(table)
