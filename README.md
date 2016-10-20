# TruthTableGenerator
Artificial Intelligence Project 1

This project uses threading in Python to generate truth tables of various logic expressions. 

Method:
A user enters a string of variables and operators that are interpreted as a logic expression. This input is parsed with the Python library <a href="http://www.sympy.org/en/index.html">SymPy</a>, which is used for symbolic mathematics, to turn the expression into a format that can be worked with. This expression is passed to the function **rows()**, which 

This method has been tested up to 20 unique variables, or +1 million combinations of truth values, to produce the resulting table.
