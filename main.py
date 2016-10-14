import sys, math, threading, pprint
from sympy import *

class myThread (threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
	def run(self):
		print "Starting " + self.name
		# what you want the thread to do during its existence
		rows()
		print "Ending " + self.name

# This is the first function of the program to run.
def main():
    # get input of truth expression from user
    # find the number of variables in the expression
    # initialize the values
    # in a loop, calculate the truth variable for each row
    # 	create a new thread in each loop
    thread1 = myThread(1, "Thread-1", 1)
    # 	call start on each thread
    thread1.start()
    # print the resulting table
    #print(initializeValues(3))

def rows():
    expr_string = raw_input("Enter an expression: ")
    expr = sympify(expr_string)
    variables = expr.free_symbols
    finalArray = []
    for truth_values in cartes([False, True], repeat=len(variables)):
        values = dict(zip(variables, truth_values))
        finalArray.append(expr.subs(values))
        finalArray.append(values.items())
    print finalArray[::-1]

# This function creates the intial combinations of possible truth values for the variables.
# Input: the set of variables that are used in the final equation
# Output: the array of initial truth values
# def initializeValues(numberOfVariables):
#     if numberOfVariables < 1:
#         return [[]]
#     subtable = initializeValues(numberOfVariables - 1)
#     return [row + [v] for row in subtable for v in [True, False]]


# This function determines the truth value of the ultimate expression based on the inital truth values for that row
# Input: the array of truth values and the ultimate expression
# Output: the truth value for a the ultimate expression

# def rows(rowArray):
#     #returns reults for each individual row given initial columns
#     #assuming p ^ q
#     print rowArray
#     expr = takeInput()
#     print expr
#     return expr.subs(rowArray)
    # OR = False
    # AND = False
	#
    # if AND:
    #     for x in rowArray:
    #         if not x:
    #             return False
    #     return True
    # if OR:
    #     for x in rowArray:
    #         if x:
    #             return True
    #     return False

main()
