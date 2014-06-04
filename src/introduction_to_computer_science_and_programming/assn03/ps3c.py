from string import *

def constrainedMatchPair(firstMatch, secondMatch, length):
    """
    Args:
        firstMatch: a tuple representing starting points for the first substring
        secondMatch: a tuple representing starting points for the second substring
        length: the length of the first substring
    
    Return:
        a tuple of all members (call it n) of the first tuple for which is an element 
        in the second tuple (call in k), such that n+m+1 = k, where m is the length of 
        the first substring
    """
    tp_pairs = ()
    for n in firstMatch:
        for k in secondMatch:
            if ((n + length + 1) == k):
                tp_pairs = tp_pairs + ((n, k),)
    
    return tp_pairs
