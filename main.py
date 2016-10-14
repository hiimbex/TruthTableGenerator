import sys, math, threading, pprint, string
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
    for truth_values in cartes([True, False], repeat=len(variables)):
        # Pair each individual variable with its truth value and add to dictionary
        values = dict(zip(variables, truth_values))
        # Start a unique thread for each row
        thread = myThread(threadID, "Thread-"+str(threadID), values, expr, finalArray)
        thread.start()
        # Add each thread to a list so that we can join them later
        threads.append(thread)
        threadID += 1
    # Join the finished threads together
    for t in threads:
        t.join()
    return finalArray

# Main part of the program
keepRunning = True
print "This program returns a Truth Table for a given expression."
while keepRunning:
    userInput = raw_input("Enter 0 to quit. Otherwise enter a valid lowercase truth expression: ").lower()
    try:
        expr = sympify(userInput)
    except:
        SyntaxError
    else:
        if userInput == "0":
            keepRunning = False
        else:
            lock = threading.Lock()
            table = rows(expr)
            # Formatting
            for x in range(0,len(table)):
                if x % 2 == 0:
                    print table[x], table[x+1]
