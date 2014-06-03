import sys
from unittest import TestCase
from StringIO import StringIO

from src.introduction_to_computer_science_and_programming.assn00 import *
class TestAssn00(TestCase):
    """ test class for the assignment 00 """
    def setUp(self):
        print '\n*** Setup & Run Test for "Assn00" ***\n'
        self.heldout = sys.stdout
        sys.stdout = StringIO()
       
    def tearDown(self):
        sys.stdout = self.heldout
        print '\n*** Done with testing "Assn00" ***\n'

    def test_problem1(self):
        ps0.run_problem1(lambda x:"peng", lambda x:"leqiao")        
        lines = sys.stdout.getvalue().splitlines()
        self.assertEquals(lines[2], "leqiao")
        self.assertEquals(lines[3], "peng")
       


from src.introduction_to_computer_science_and_programming.assn01 import *
class TestAssn01(TestCase):
    """ Testcases for the assignment 01 """
    def test_problem1(self):
        self.assertEquals(ps1a.Prime.get_nth_prime(1), 2)
        self.assertEquals(ps1a.Prime.get_nth_prime(1000), 7919)

    def test_problem2(self):
        self.assertEquals(ps1b.get_ratio(1) < ps1b.get_ratio(10), True)
        self.assertEquals(ps1b.get_ratio(10) < ps1b.get_ratio(30), True)
        self.assertEquals(ps1b.get_ratio(30) < ps1b.get_ratio(100), True)




if __name__ == '__main__':
    import nose
    print "Arguments are: ", str(sys.args[0])
    nose.main()
