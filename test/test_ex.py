import sys
import unittest
from StringIO import StringIO

from src.learn_python_the_hard_way import ex_all


def test_ex01():
    print '\n*** Run the "Ex. 1" ***\n'
    ex_all.ex01()


def test_ex02():
    print '\n*** Run the "Ex. 2" ***\n'
    ex_all.ex02()



def test_ex03():
    print '\n*** Run the "Ex. 3" ***\n'
    ex_all.ex03()


def test_ex10():
    print '\n*** Run the "Ex. 10" ***\n'
    ex_all.ex10()


def test_ex11():
    print '\n*** Run the "Ex. 11" ***\n'
    ex_all.ex11()


def test_ex13():
    print '\n*** Run the "Ex. 13" ***\n'
    ex_all.ex13()


def test_ex15():
    print '\n*** Run the "Ex. 15" ***\n'
    ex_all.ex15()

def test_ex21():
    print '\n*** Run the "Ex. 21" ***\n'
    assert(ex_all.ex21_add(-1, 1) == 0)
    assert(ex_all.ex21_divide(3, 2) == 1)
       

class TestEx26(unittest.TestCase):

    def setUp(self):
        print '\n*** Run the "Ex. 26" ***\n'
        self.held = sys.stdout
        sys.stdout = StringIO()
        

    def tearDown(self):
        sys.stdout = self.held
        print '\n*** Done with "Ex.26" ***\n'
        

    def test_ex26(self):                  
        sentence = "All god\tthings come to those who weight."
        words = ex_all.Ex26.break_words(sentence)
        sorted_words = ex_all.Ex26.sort_words(words)
        ex_all.Ex26.print_first_word(words)        
        ex_all.Ex26.print_last_word(words)
        ex_all.Ex26.print_first_word(sorted_words)
        ex_all.Ex26.print_last_word(sorted_words)
        '''      
        sorted_words = ex_all.Ex26.sort_sentence(sentence)
        print sorted_words
        
        ex_all.Ex26.print_first_and_last(sentence)
        ex_all.Ex26.print_first_and_last_sorted(sentence)
        '''     
        lines = sys.stdout.getvalue().splitlines()
        self.assertEquals(lines[0], "All")
        self.assertEquals(lines[1], "weight.")
        self.assertEquals(lines[2], "All")
        self.assertEquals(lines[3], "who")


class TestEx40(unittest.TestCase):

    def setUp(self):
        print '\n*** Run the "Ex. 40" ***\n'
        self.held = sys.stdout
        sys.stdout = StringIO()
        

    def tearDown(self):
        sys.stdout = self.held
        print '\n*** Done with "Ex.40" ***\n'
        

    def test_ex40(self):                  
        cities = {'CA':'San Francisco', 'MI': 'Detroit', 'FL':'Jacksonville'}
        cities['NY'] = 'New York'
        cities['OR'] = 'Portland'
    
        ex_all.Ex40.find_city(cities, 'CA')
        ex_all.Ex40.find_city(cities, 'NY')
        ex_all.Ex40.find_city(cities, 'DE')

        lines = sys.stdout.getvalue().splitlines()
        
        self.assertEquals(lines[0], "San Francisco")
        self.assertEquals(lines[1], "New York")
        self.assertEquals(lines[2], "Not found")


from src.learn_python_the_hard_way.ex_all import Ex42
class TestEx42(unittest.TestCase):
    def test_ex42(self):
        print '\n*** Run the "Ex. 42" ***\n'
        myEx42 = Ex42(2, 3)
        self.assertEquals(myEx42.do_task(), 2*3)




from nose.tools import *
from src.learn_python_the_hard_way.ex_all import lexicon
class TestEx48(unittest.TestCase):

    def test_directions(self):
        assert_equal(lexicon.scan("north"), [('direction', 'north')])
        result = lexicon.scan("north south east")
        assert_equal(result, [('direction', 'north'),
                              ('direction', 'south'),
                              ('direction', 'east')])

    def test_verbs(self):
        assert_equal(lexicon.scan("go"), [('verb', 'go')])
        result = lexicon.scan("go kill eat")
        assert_equal(result, [('verb', 'go'),
                              ('verb', 'kill'),
                              ('verb', 'eat')])


    def test_stops(self):
        assert_equal(lexicon.scan("the"), [('stop', 'the')])
        result = lexicon.scan("the in of")
        assert_equal(result, [('stop', 'the'),
                              ('stop', 'in'),
                              ('stop', 'of')])


    def test_nouns(self):
        assert_equal(lexicon.scan("bear"), [('noun', 'bear')])
        result = lexicon.scan("bear princess")
        assert_equal(result, [('noun', 'bear'),
                              ('noun', 'princess')])

    def test_numbers(self):
        assert_equal(lexicon.scan("1234"), [('number', 1234)])
        result = lexicon.scan("3 91234")
        assert_equal(result, [('number', 3),
                              ('number', 91234)])


    def test_errors(self):
        assert_equal(lexicon.scan("ASDFADFASDF"), [('error', 'ASDFADFASDF')])
        result = lexicon.scan("bear IAS princess")
        assert_equal(result, [('noun', 'bear'),
                              ('error', 'IAS'),
                              ('noun', 'princess')])



from src.learn_python_the_hard_way.ex_all import Parser
from src.learn_python_the_hard_way.ex_all import Sentence
class TestParser(unittest.TestCase):

    def test_1(self):
        words_list = lexicon.scan("eat the bear")
        sent = Parser.parse_sentence(words_list)
        assert_equal(sent.subject, 'player')
        assert_equal(sent.verb, 'eat')
        assert_equal(sent.object, 'bear')

    def test_2(self):
        words_list = lexicon.scan("he kill the bear")
        sent = Parser.parse_sentence(words_list)
        assert_equal(sent.subject, 'VIP_P1')
        assert_equal(sent.verb, 'kill')
        assert_equal(sent.object, 'bear')



if __name__ == '__main__':
    import sys
    import nose
    print "Arguments are: ", str(sys.args[0])
    nose.main()
