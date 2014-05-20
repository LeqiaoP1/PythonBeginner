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

   
if __name__ == '__main__':
    import sys
    import nose
    print "Arguments are: ", str(sys.args[0])
    nose.main()
