# TruthTableGenerator
Artificial Intelligence Project 1
Coordinator: Yan Shi
Documentor: Sarah Hendricks
Implementor: Bex Warner

This project uses threading in Python to generate truth tables of various logic expressions. 

Requirements:
Python 3.0
SymPy library

Method:
A user enters a string of variables and operators that are interpreted as a logic expression. This input is parsed with the Python library <a href="http://www.sympy.org/en/index.html">SymPy</a>, which is used for symbolic mathematics, to turn the expression into a format that can be worked with. 
This expression is passed to the function **rows()**, which creates threads to calculate the ultimate truth value for each unique combination of variable truth values. Each thread takes the unique variable truth values and the logic expression given by the user and calculates the resulting truth value for the statement. Both the variables with truth values and the ultimate truth value are then placed into an array containing all of the combinations of varaible truth values.
Finally, when all of the threads have added their row to the table, the table is formatted and presented to the user.

This method has been tested up to 20 unique variables, or +1 million combinations of truth values, to produce the resulting table.

Future:
This program will be tested on Zorro, a high-performance computing machine that resides in Reston, VA. 
