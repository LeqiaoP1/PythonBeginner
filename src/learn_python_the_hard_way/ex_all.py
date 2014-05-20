
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
    

