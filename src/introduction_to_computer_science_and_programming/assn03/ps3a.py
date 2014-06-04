from string import *

def countSubStringMatch(target, key):
    """ iteratively count the number of instances of the key in the target string """
    cnt_instances = 0
    pos = 0
    while (pos <= len(target)-len(key)):
        if (target[pos:pos+len(key)] == key):
                cnt_instances = cnt_instances + 1
        pos = pos + 1

    return cnt_instances
        

def countSubStringMatchRecursive(target, key):
    """ recursively count the number of instances of the key in the target string """
    if ( (len(target) == 0) or (len(target) < len(key)) ):
        return 0
    elif ( target[0:len(key)] == key ):
        return 1 + countSubStringMatchRecursive( target[1:], key )
    else:
        return countSubStringMatchRecursive( target[1:], key )

            


    
