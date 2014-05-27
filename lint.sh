export PYTHONPATH=./src/learn_python_the_hard_way:$PYTHONPATH

flake8 --ignore=E501,E128,E701,E261,E301,E126,E127,E131 test/
flake8 --ignore=E501,E128,E701,E261,E301,E126,E127,E131 src/



