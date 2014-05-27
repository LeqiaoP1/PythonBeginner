
def ex01():
    print "Hello World!"
    print "Hello Again!"
    print "I'd much rather you 'not'."
    print 'I "said" do not touch this.'

    return None


def ex02():
    # A comment, this is so you can read your program later.
    # Anything after the # is ignored by python.   
    print "I could have code like this." # and the comment after is ignored    
    # You can also use a comment to "disable" or comment out a piece of code:
    # print "This was't run."
    print "This will run."
    return None


def ex03():
    print "I will now count my chickens:"
    print "Hens", 25 + 30 / 6
    print "Roosters", 100 - 25 * 3 % 4
    print "Now I will count the eggs:"
    print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
    print "Is it true that 3 + 2 < 5 - 7?"
    print 3 + 2 < 5 - 7
    print "What is 3 + 2?", 3 + 2
    print "What is 5 - 7?", 5 - 7
    print "Oh, that's why it's False."
    print "How about some more."
    print "Is it greater?", 5 > -2
    print "Is it greater or equal?", 5 >= -2
    print "Is it less or equal?", 5 <= -2
    return None


def ex10():
    tabby_cat = "\tI'm tabbed in."
    persian_cat = "I'm split\non a line."
    backslash_cat = "I'm \\ a \\ cat."
    fat_cat = '''
    I'll do a list:
    \t* Cat food
    \t* Fishies
    \t* Catnip\n\t* Grass
    '''
    print tabby_cat
    print persian_cat
    print backslash_cat
    print fat_cat
    return None


def ex11():
    print "How old are you?",
    age = raw_input()
    print "How tall are you?",
    height = raw_input()
    print "How much do you weigh?",
    weight = raw_input()
    print "So, you're %s old, %r tall and %r heavy." %(age, height, weight)
    
    
def ex13():
    from sys import argv
    script, first, second, third, fourth = argv
    print "The script is called:", script
    print "Your first variable is:", first
    print "Your second variable is:", second
    print "Your third variable is:", third
    print "Your fourth variable is:", fourth

    
def ex15():
    from sys import argv
    """script, filename = argv
    txt = open(filename)
    print "Here's your file %r:" % filename
    print txt.read()
    """
    print "Type the filename again:"
    file_again = raw_input("> ")
    txt_again = open(file_again)
    
    print txt_again.read()
    txt_again.close()


def ex21_add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b


def ex21_subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b


def ex21_multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b


def ex21_divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b


class Ex26(object):
    """ statish methods
    """
    def break_words(stuff):
        """This function will break up words for us."""
        words = stuff.split(' ')
        return words

    def sort_words(words):
        """Sorts the words."""
        return sorted(words)

    def print_first_word(words):
        """Prints the first word after popping it off."""
        word = words.pop(0)
        print word

    def print_last_word(words):
        """Prints the last word after popping it off."""
        word = words.pop(-1)                      
        print word

    def sort_sentence(sentence):
        """Takes in a full sentence and returns the sorted words."""
        words = Ex26.break_words(sentence)
        return Ex26.sort_words(words)
    
    def print_first_and_last(sentence):
        """Prints the first and last words of the sentence."""
        words = Ex26.break_words(sentence)
        Ex26.print_first_word(words)
        Ex26.print_last_word(words)

    def print_first_and_last_sorted(sentence):
        """Sorts the words then prints the first and last one."""
        words = Ex26.sort_sentence(sentence)
        Ex26.print_first_word(words)
        Ex26.print_last_word(words)

    break_words = staticmethod(break_words)
    sort_words = staticmethod(sort_words)
    print_first_word = staticmethod(print_first_word)
    print_last_word = staticmethod(print_last_word)
    sort_sentence = staticmethod(sort_sentence)
    print_first_and_last = staticmethod(print_first_and_last)
    print_first_and_last_sorted = staticmethod(print_first_and_last_sorted)


class Ex40(object):
    """ dictionary lookup"""
    @staticmethod
    def find_city(themap, state):
        if state in themap:
            print themap[state]
        else:
            print "Not found"


class Ex42(object):
    """ two nested classes """
    class TheThing(object):
        def __init__(self):
            self.number = 0


        def add_me_up(self, more):
            self.number += more
            return self.number


    class TheMultiplier(object):
        def __init__(self, base):
            self.base = base
        
        def do_it(self, m):
            return m * self.base
    
    """ main class """   
    def __init__(self, op1, op2):
        self.thingA = self.TheThing()
        self.thingA.add_me_up(op1)
        self.thingB = self.TheThing()
        self.thingB.add_me_up(op2)

    def do_task(self):
        return self.TheMultiplier(self.thingA.number).do_it(self.thingB.number)



class lexicon(object):
    """ for exercise 48. """
    directions = "north south east west down up left right back"
    verbs = "go stop kill eat"
    stops = "the in of"
    nouns = "door bear princess cabinet VIP_P1"
    
    @staticmethod
    def scan(input_str):
        words = input_str.split()
        ret_list = []
        for w in words:
            if w in lexicon.directions.split():
                ret_list.append(('direction', w))
            elif w in lexicon.verbs.split():
                ret_list.append(('verb', w))
            elif w in lexicon.nouns.split():
                ret_list.append(('noun', w))
            elif w in lexicon.stops.split():
                ret_list.append(('stop', w))
            elif w.isdigit():
                ret_list.append(('number', int(w)))
            else:
                ret_list.append(('error', w))

        return ret_list
                
    
class ParserError(Exception):
    pass


class Sentence(object):

    def __init__(self, subject, verb, object):
        # remember we take ('noun','princess') tuples and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = object[1]


class Parser(object):
    """ for ex.49  """
    @staticmethod
    def peek(word_list):  # tuple list
        if word_list:
            word = word_list[0] # get the first one but not pop it up
            return word[0]
        else:
            return None

    @staticmethod
    def match(word_list, expecting): # tuple list
        if word_list:
            word = word_list.pop(0) # pop the head tuple

            if word[0] == expecting:
                return word
            else:
                return None
        else:
            return None

    @staticmethod
    def skip(word_list, word_type):  # tuple list
        # loop until empty list or first non-matched word-type
        while Parser.peek(word_list) == word_type: 
            Parser.match(word_list, word_type)

    @staticmethod
    def parse_verb(word_list):
        Parser.skip(word_list, 'stop')

        if Parser.peek(word_list) == 'verb':
            return Parser.match(word_list, 'verb')
        else:
            raise ParserError("Expected a verb next.")

    @staticmethod
    def parse_object(word_list):
        Parser.skip(word_list, 'stop')
        next = Parser.peek(word_list)

        if next == 'noun':
            return Parser.match(word_list, 'noun')
        if next == 'direction':
            return Parser.match(word_list, 'direction')
        else:
            raise ParserError("Expected a noun or direction next.")

    @staticmethod
    def parse_subject(word_list, subj): # "subj" is already extracted
        verb = Parser.parse_verb(word_list)
        obj = Parser.parse_object(word_list)

        return Sentence(subj, verb, obj)

    @staticmethod
    def parse_sentence(word_list):
        Parser.skip(word_list, 'stop')
        start = Parser.peek(word_list)

        if start == 'noun':
            subj = Parser.match(word_list, 'noun')
            return Parser.parse_subject(word_list, subj)
        elif start == 'verb':
            # assume the subject is the player then
            return Parser.parse_subject(word_list, ('noun', 'player'))
        else:
            raise ParserError("Must start with subject, object, or verb not: %s" % start)







