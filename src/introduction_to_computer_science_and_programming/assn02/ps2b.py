###
### template of code for Problem 4 of Problem Set 2, Fall 2008
###
import ps2a

bestSoFar = 1     # variable that keeps track of largest number
                  # of McNuggets that cannot be bought in exact quantity
packages = (6,9,20)   # variable that contains package sizes


def run():
    """ only search for solutions up to size 150
        complete code here to find largest size that cannot be bought
        when done, your answer should be bound to bestSoFar
    """
    global bestSoFar
    for n in range(1, 150):   
        if not(ps2a.is_solvable(n, packages)):
            bestSoFar = n


print bestSoFar
















