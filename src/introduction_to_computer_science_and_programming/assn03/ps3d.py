from string import *
from ps3b import subStringMatchExact
from ps3_template import subStringMatchOneSub


def subStringMatchExactlyOneSub(target, key):
    """ find those matched and with only substitution in target 
        return:
                a tuple contains the starting positions of substring in target, which can
                matchs the key string except for exactly one char
    """
    tuple_pairs = subStringMatchOneSub(key, target)
    print "all pairs: ", tuple_pairs
    fully_matched_pos = subStringMatchExact(target, key)
    print "matched_pos:", fully_matched_pos
    answer = ()
    for tuple_pair in tuple_pairs:
        start = list(tuple_pair).pop(0)
        if start in fully_matched_pos: 
            pass
        else:
            answer = answer + (start,)

    return answer


