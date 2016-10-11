import sys, math

# This is the first function of the program to run.
def main():
    # get input of truth expression from user
    # find the number of variables in the expression
    # initialize the values
    # in a loop, calculate the truth variable for each row
    # print the resulting table


# This function creates the intial combinations of possible truth values for the variables.
# Input: the set of variables that are used in the final equation
# Output: the columns of initial truth values
def initializeValues(numberOfVariables):
    if numberOfVariables < 1:
        return [[]]
    subtable = initializeValues(numberOfVariables - 1)
    return [row + [v] for row in subtable for v in [True, False]]


# This function determines the truth value of the ultimate expression based on the inital truth values for that row
# Input: the array of truth values and the ultimate expression
# Output: the truth value for a the ultimate expression
def rows():
    #returns reults for each individual row given initial columns

print(initializeValues(3))
