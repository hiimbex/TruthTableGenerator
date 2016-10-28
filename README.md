# Truth Table Generator: AI Project 1

This project uses threading in Python to generate truth tables of user-driven logic expressions. 

## Introduction
This project has two main files: main.py, which runs solely in the command line, and code.py, which uses a webpy server to display information in the browser. Images of these two programs can be found in the Wiki.

The table below is an example truth table of the expression **a & b**. The first two columns are the unique combination of all possible truth values of the variables used in the expression. The final column is the result of the truth values of that row placed into the expression.

| a | b | a & b |
| --- |---| ---|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |

## Installation
To run this program, first clone this repository. 

<a href="http://www.sympy.org/en/index.html">SymPy.org</a> is needed for this project, through Anaconda or <a href="http://conda.pydata.org/docs/install/quick.html">Miniconda</a>. Installing <a href="http://conda.pydata.org/docs/install/quick.html">Miniconda</a> will make installing SymPy much easier; simply click on the link to download the package manager and follow the installation tutorial.
(<a href="http://conda.pydata.org/docs/install/quick.html">Miniconda</a> is preferred, since it is a smaller package.) 
Once you have Anaconda or <a href="http://conda.pydata.org/docs/install/quick.html">Miniconda</a>, you can check if you have SymPy by running the command `from sympy import *`. If there is an error or you do not have Sympy, install SymPy using the command `conda install sympy`.

Finally, install WebPy if you want to run the program in the browser by issuing the command `pip install web.py`. This is necessary to run `code.py`. However, if you just wish to run the code through a command line or IDE interface, simply run `main.py`.

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

This program has also been tested on Zorro, a high-performance computing machine that resides in Reston, VA. 

## Credits
- Coordinator: Yan Shi
- Documentor: Sarah Hendricks
- Implementor: Bex Warner

## License
Released under the MIT License.
