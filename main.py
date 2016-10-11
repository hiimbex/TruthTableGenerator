import sys, math

def main():
    #Main stuff here

def initializeValues(numberOfVariables):
    #Initial value generation
    if numberOfVariables < 1:
        return [[]]
    subtable = initializeValues(numberOfVariables - 1)
    return [row + [v] for row in subtable for v in [True, False]]

def rows():
    #returns reults for each individual row given initial columns

print(initializeValues(3))
