"""This module creates a logic table from a user-given logic expression."""
import threading

import cgi
import cgitb; cgitb.enable()
from sympy import sympify, cartes

class MyThread(threading.Thread):

    """Creates unique thread.

    This class modifies the existing threading module. Threads in this class
    are given the variables and a unique combination of their truth values,
    as well as the given logic expression, to determine the ultimate truth
    value for that unique combination.
    """

    def __init__(self, thread_id, values, expression, final_array):
        """Creates a thread."""
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.values = values
        self.expression = expression
        self.final_array = final_array
    def run(self):
        """Calculates the ultimate truth value from the variables and adds both to the table."""
        # Get the list of variables and their truth values
        variables = self.values.items()
        # Calculate the result of the expression from the variables
        result = self.expression.subs(self.values)
        # Lock the array so we can alter it
        LOCK.acquire()
        try:
            # Append the variable truth values for that row
            self.final_array.append(variables)
            # Append the ultimate result of the expression for that row in the truth table
            self.final_array.append(result)
        finally:
            LOCK.release()

def rows(expression):
    """This function creates the final table of truth values with the variables and the final
        expression for each row.
        params: the preformatted logic expression
        returns: the final array
    """
    final_array = []
    thread_id = 1
    # Get the variables out of the expression
    variables = expression.free_symbols
    # Go through the initial generation of the truth values
    for truth_row in cartes([True, False], repeat=len(variables)):
        # Pair each individual variable with its truth value and add to dictionary
        values = dict(zip(variables, truth_row))
        # Start a unique thread for each row
        thread = MyThread(thread_id, values, expression, final_array)
        thread.start()
        # Join the threads together when they finish.
        thread.join()
        thread_id += 1
    return final_array

form = cgi.FieldStorage()
html = """
<html>
<head>
</head>
<body>
<form action="index.py" name="myform" method="GET">
        Enter length:  <input type="text" name="length"><br />
        Enter width: <input type="text" name="width"><br />
        <input type="submit" value="submit">
</form>
</body>
</html>
"""

print "This program returns a Truth Table for a given expression."
print "(and = &, not = ~, or = |, implies = >>)"
while True:
    print ""
    print "Enter 0 to quit."
    USER_INPUT = raw_input("Enter a valid lowercase truth expression: ").lower()

    if USER_INPUT == "0":
        break
    try:
        # Break the input into an expression the computer can understand.
        EXPR = sympify(USER_INPUT)
    except:
        print "NOT A VALID EXPRESSION."
        print "Accepted symbols: (and = &, not = ~, or = |, implies = >>)"
    else:
        LOCK = threading.Lock()
        TABLE = rows(EXPR)
        # Formatting
        for x in range(0, len(TABLE)):
            if x % 2 == 0:
                print TABLE[x], TABLE[x+1]

