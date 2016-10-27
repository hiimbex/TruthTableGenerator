"""This module creates a logic table from a user-given logic expression."""
import threading
from sympy import sympify, cartes
import web
from web import form

# Tell webpy where the templates are.
RENDER = web.template.render('templates/')

# The URLs for this website.
URLS = ('/', 'Index', '/table', 'Table')
APP = web.application(URLS, globals())

# Lock for threading.
LOCK = threading.Lock()

# Global table variable to pass to the truth table page.
TABLE = [[]]

# The form for submitting a truth expression.
MY_FORM = form.Form(form.Textbox("expression", form.notnull, class_="textEntry"))

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

class Index(object):

    """Creates website initial page.

    This class holds the methods for creating the intial website page via webpy. Its two
    functions, GET and POST, are used for HTTP requests.
    """

    def GET(self):
        """This function runs when the HTTP GET request for the index.html page is called."""
        return RENDER.formtest(MY_FORM)

    def POST(self):
        """This function runs when the HTTP POST request for the index.html page is called."""
        my_form = MY_FORM()
        if not my_form.validates():
            return RENDER.formtest(my_form)
        else:
            try:
                # Convert the input into SymPy internal format.
                expr = sympify(my_form['expression'].value.lower())
            except:
                return """NOT A VALID EXPRESSION.\n
                Accepted symbols: (and = &, not = ~, or = |, implies = >>)"""
            else:
                global TABLE
                TABLE = rows(expr)
                # Formatting
                raise web.seeother('/table')

class Table(object):

    """Creates webpage with truth table displayed."""

    def GET(self):
        """This function renders the truth table page when the HTTP GET request
        for truthtable.html is called."""
        return RENDER.truthtable(TABLE)

if __name__ == "__main__":
    web.internalerror = web.debugerror
    APP.run()
