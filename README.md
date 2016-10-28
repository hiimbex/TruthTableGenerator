# Truth Table Generator: AI Project 1

This project uses threading in Python to generate truth tables of user-driven logic expressions. 

## Introduction


The table below is an example truth table of the expression **a & b**. The first two columns are the unique combination of all possible truth values of the variables used in the expression. The final column is the result of the truth values of that row placed into the expression.

| a | b | a & b |
| --- |---| ---|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |

## Installation
To run this program, first clone this repository. 

You'll also need to go to <a href="http://www.sympy.org/en/index.html">SymPy.org</a> to download their library, which is used for symbolic mathematics.

Finally, install WebPy.

`pip install web.py`

## Usage
A user enters a string of variables and operators that are interpreted as a logic expression. This input is parsed with the Python library <a href="http://www.sympy.org/en/index.html">SymPy</a> to turn the expression into a format that can be worked with. 

This expression is passed to the function `rows()`, which creates threads to calculate the ultimate truth value for each unique combination of variable truth values. Each thread takes the unique variable truth values and the logic expression given by the user and calculates the resulting truth value for the statement. Both the variables with truth values and the ultimate truth value are then placed into an array containing all of the combinations of varaible truth values.

Finally, when all of the threads have added their row to the table, the table is formatted and presented to the user.

## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Make all your awesome changes and add new features to the code!
4. Commit your changes: `git commit -m 'Add some feature'`
5. Push your branch's changes to the origin/master: `git push origin my-new-feature`
6. Open a pull request on GitHub

## History
This method has been tested up to 20 unique variables, or +1 million combinations of truth values, to produce the correct resulting table.

This program will be tested on Zorro, a high-performance computing machine that resides in Reston, VA. 

## Credits
- Coordinator: Yan Shi
- Documentor: Sarah Hendricks
- Implementor: Bex Warner

## License
Released under the MIT License.
