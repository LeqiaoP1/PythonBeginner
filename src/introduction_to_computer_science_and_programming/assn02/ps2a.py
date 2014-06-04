

def max_not_solvable():
    """find the largest number of McNuggest that cannot be bought in exact quantity
       package = [6, 9, 20] by McDonald  
    """
    solvables = [] # continous
    d = 1
    max_unsolvable = 1
    while (len(solvables) < 6):
        d = d + 1
        if (is_solvable(d, [6, 9, 20])):
            solvables.append(d)
        else:
            max_unsolvable = d
            solvables = []

    return max_unsolvable
            

def is_solvable(n, package):
    """ check if the "n" can be assembled in combinations of items in given "package"
        recursive method
    """
    if (n == 0):
        return True  
    elif ( (n < 0) or (len(package) == 0) ):
        return False
    else:
        return is_solvable(n, package[1:]) or is_solvable(n-package[0], package)






            
            
            
