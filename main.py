#Found online but understand and good example
def tablize(n, truths=[]):
    if not n:
        print truths
    else:
        for i in [True, False]:
            tablize(n - 1, truths+[i])

tablize(20)


def main():
    #Main stuff here

def initializeValues():
    #Initial value generation

def rows():
    #returns reults for each individual row given initial columns
