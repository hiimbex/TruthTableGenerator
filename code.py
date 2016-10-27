"""This module creates a logic table from a user-given logic expression."""
import threading
from sympy import sympify, cartes
import web
from web import form

# Tell webpy where the templates are.
render = web.template.render('templates/')

# The URLs for this website.
urls = (
	'/', 'index',
	'/table', 'table'
)
app = web.application(urls, globals())

LOCK = threading.Lock()
TABLE = [[]]

myform = form.Form( 
    form.Textbox("expression", 
        form.notnull,
        class_="textEntry"
        )
    )

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


class index: 
    def GET(self): 
        form = myform()
        return render.formtest(form)

    def POST(self): 
        form = myform() 
        if not form.validates(): 
            return render.formtest(form)
        else:
			try:
				# Convert the input into SymPy internal format.
				EXPR = sympify(form['expression'].value.lower())
			except:
				return "NOT A VALID EXPRESSION.\nAccepted symbols: (and = &, not = ~, or = |, implies = >>)"
			else:
				global TABLE
				TABLE = rows(EXPR)
				# Formatting
				raise web.seeother('/table')

class table:
    def GET(self):
        return render.truthtable(TABLE)


if __name__=="__main__":
    web.internalerror = web.debugerror
    app.run()