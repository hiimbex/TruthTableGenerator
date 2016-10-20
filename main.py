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
        # Get the list of variables and their truth values
        x = self.values.items()
        # Calculate the result of the expression from the variables
        y = self.expr.subs(self.values)
        # Lock the array so we can alter it
        lock.acquire()
        try:
            # Append the variable truth values for that row
            self.finArr.append(x)
            # Append the ultimate result of the expression for that row in the truth table
            self.finArr.append(y)
        finally:
            lock.release()

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
    for truthRow in cartes([True, False], repeat=len(variables)):
        # Pair each individual variable with its truth value and add to dictionary
        values = dict(zip(variables, truthRow))
        # Start a unique thread for each row
        thread = myThread(threadID, "Thread-"+str(threadID), values, expr, finalArray)
        thread.start()
        # Join the threads together when they finish.
        thread.join()
        threadID += 1
    return finalArray

# Main part of the program.
print "This program returns a Truth Table for a given expression."
print "(and = &, not = ~, or = |, implies = >>)"
while True:
    print ""
    userInput = raw_input("Enter 0 to quit. Otherwise enter a valid lowercase truth expression: ").lower()

    if userInput == "0":
        break
    try:
        # Break the input into an expression the computer can understand.
        expr = sympify(userInput)
    except:
        SyntaxError
        print "Please enter a valid expression."
        print "(and = &, not = ~, or = |, implies = >>)"
    else:
        lock = threading.Lock()
        table = rows(expr)
        # Formatting
        for x in range(0,len(table)):
            if x % 2 == 0:
                print table[x], table[x+1]
