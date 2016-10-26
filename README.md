# Truth Table Generator: AI Project 1

This project uses threading in Python to generate truth tables of user-driven logic expressions. 

## Introduction
Truth tables are a standard piece of computer science curriculum. While tables with only two or three variables are easy to calculate, tables with more variables than this require exponential time to construct and calculate. To give students a way to check their truth table values, we developed a python script that runs through all of the unique truth combinations for the variables and calculates the truth value of the expression based on those variabls.

## Installation
To run this program, first clone this repository. You'll also need to go to <a href="http://www.sympy.org/en/index.html">SymPy.org</a> to download their library, which is used for symbolic mathematics.
## Usage
A user enters a string of variables and operators that are interpreted as a logic expression. This input is parsed with the Python library <a href="http://www.sympy.org/en/index.html">SymPy</a> to turn the expression into a format that can be worked with. 

This expression is passed to the function `rows()`, which creates threads to calculate the ultimate truth value for each unique combination of variable truth values. Each thread takes the unique variable truth values and the logic expression given by the user and calculates the resulting truth value for the statement. Both the variables with truth values and the ultimate truth value are then placed into an array containing all of the combinations of varaible truth values.

Finally, when all of the threads have added their row to the table, the table is formatted and presented to the user.

## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request

## History
This method has been tested up to 20 unique variables, or +1 million combinations of truth values, to produce the resulting table.

This program will be tested on Zorro, a high-performance computing machine that resides in Reston, VA. 

## Credits
- Coordinator: Yan Shi
- Documentor: Sarah Hendricks
- Implementor: Bex Warner

## License
Released under the MIT License.
