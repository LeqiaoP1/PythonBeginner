#PYTHONPATH=src python -m unittest discover -s ./test/ -p 'test_*.py' -v
export PYTHONPATH=./src/learn_python_the_hard_way/:$PYTHONPATH

nosetests -v -s -w./test $1;echo "argument: " $1




















