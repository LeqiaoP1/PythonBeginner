import random

#problem 5 -- merge sort
def merge_two_lists(L1, L2):
    ''' both list are already sorted '''
    #print "try to merge two lists: ", L1, L2
    L = []
    if len(L1) == 0:
        return L2
    else:
        pos1 = 0 # not inserted position in List1
        for e in L2:
            if pos1 < len(L1):
                while L1[pos1] < e:
                    L.append(L1[pos1])
                    pos1 += 1
                    if pos1 == len(L1):
                        break
            
            L.append(e)
            
        return L + L1[pos1:]


def merge_sort(L):
    if len(L) <= 1:
        return L
    else:
        #divide two subsets
        L1 = merge_sort( L[0 : len(L)/2] )
        L2 = merge_sort( L[len(L)/2 : ] )

        #merge two sorted lists
        return merge_two_lists(L1, L2)


def test1():
    L1 = [2, 5]
    L2 = [3, 4]
    print merge_two_lists(L1, L2)
    L3 = [4]
    L4 = []
    print merge_two_lists(L3, L4)
    print merge_sort([1, 3, 4, 2, 0])


#problem 6 -- find number
def findNumber(maxVal):
    target_val = 0

    def cmpGuess(guess):
        if guess == target_val:
            return 0
        else:
            return 1 if guess > target_val else -1

    if maxVal > 0:
        target_val = random.randint(0, maxVal-1)
        print "DEBUG only: target value ", target_val
        got_answer = False
        while not got_answer:
            user_guess = int(raw_input("Give your guess (value between 0 and %d):"%maxVal))
            res = cmpGuess(user_guess)
            if  res == 0:
                got_answer = True
            elif res > 0:
                print "Too large.. try again"
            else:
                print "Too small.. try again"

        print "You got it! Congratulation!"
    else:
        raise ValueError



