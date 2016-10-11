#Found online but understand and good example
def tablize(n, truths=[]):
    if not n:
        print truths
    else:
        for i in [True, False]:
            tablize(n - 1, truths+[i])

tablize(20)

# This function is the first function of the program to run. 
# Input: takes in the text of the truth function that the user wants generated.
# Output: a truth table that contains the truth values of the intial variables and the ultimate expression.
def main():
    #Main stuff here

# This function creates the intial combinations of possible truth values for the variables.
# Input: the set of variables that are used in the final equation
# Output: the columns of initial truth values
def initializeValues():
    #Initial value generation

# This function determines the truth value of the ultimate expression based on the inital truth values for that row
# Input: the array of truth values and the ultimate expression
# Output: the truth value for a the ultimate expression
def rows():
    #returns reults for each individual row given initial columns
