from string import *

def subStringMatchExact(target, key):
    """ return a tuple of the starting points of matches of the key string
        int the target string
    """
    tp_pos = ()
    pos = 0
    while (pos <= len(target)-len(key)):
        if (target[pos:pos+len(key)] == key):
                tp_pos = tp_pos + (pos,)
        pos = pos + 1

    return tp_pos

