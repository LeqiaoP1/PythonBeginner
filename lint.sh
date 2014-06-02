export PYTHONPATH=./src/learn_python_the_hard_way:$PYTHONPATH
export PYTHONPATH=./src/introduction_to_computer_science_and_programming:$PYTHONPATH

flake8 --ignore=E501,E128,E701,E261,E301,E302,E126,E127,E131,W293 $1






