# Problem Set 4
# Name: 
# Collaborators: 
# Time: 

#
# Problem 1
#

def nestEggFixed(salary, save, growthRate, years):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: the annual percent increase in your investment account (an
      integer between 0 and 100).
    - years: the number of years to work.
    - return: a list whose values are the size of your retirement account at
      the end of each year.
    """
    records = [0.0 for y in range(years)]
    if (len(records) > 0):
        records[0] = salary*save*0.01
        for y in range(1, years):
            records[y] = records[y-1]*(1.0+0.01*growthRate) + salary*save*0.01

    return records


def testNestEggFixed():
    salary     = 10000
    save       = 10
    growthRate = 15
    years      = 5
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print savingsRecord
    # Output should have values close to:
    # [1000.0, 2150.0, 3472.5, 4993.375, 6742.3812499999995]

    savingsRecord = nestEggFixed(salary, save, growthRate, 0)
    print savingsRecord
    # Output should be empty list []

    savingsRecord = nestEggFixed(salary, save, 0, 2)
    print savingsRecord
    # Output should be empty list [1000.0, 2000.0]

    savingsRecord = nestEggFixed(salary, 0, 100, 2)
    print savingsRecord
    # Output should be empty list [0.0, 0.0]

#
# Problem 2
#

def nestEggVariable(salary, save, growthRates):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: a list of the annual percent increases in your investment
      account (integers between 0 and 100).
    - return: a list of your retirement account value at the end of each year.
    """
    num_years = len(growthRates)
    records = [ 0.0 for y in range(num_years) ]
    if (len(records) > 0):
        records[0] = salary*save*0.01
        for y in range(1, num_years):
            records[y] = records[y-1]*(1.0+0.01*growthRates[y]) + salary*save*0.01

    return records


def testNestEggVariable():
    salary      = 10000
    save        = 10
    growthRates = [3, 4, 5, 0, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print savingsRecord
    # Output should have values close to:
    # [1000.0, 2040.0, 3142.0, 4142.0, 5266.2600000000002]

    savingsRecord = nestEggVariable(salary, save, [])
    print savingsRecord
    # Output should be empty list []

    savingsRecord = nestEggVariable(salary, save, [3])
    print savingsRecord
    # Output should be empty list [1000.0]

#
# Problem 3
#

def postRetirement(savings, growthRates, expenses):
    """
    - savings: the initial amount of money in your savings account.
    - growthRate: a list of the annual percent increases in your investment
      account (an integer between 0 and 100).
    - expenses: the amount of money you plan to spend each year during
      retirement.
    - return: a list of your retirement account value at the end of each year.
    """
    num_years = len(growthRates)
    records = [0.0 for y in range(num_years)]
    if (num_years > 0):
        records[0] = savings*(1 + 0.01*growthRates[0]) - expenses
        for y in range(1, num_years):
            records[y] = records[y-1]*(1 + 0.01*growthRates[y]) - expenses

    return records

    

def testPostRetirement():
    savings     = 100000
    growthRates = [10, 5, 0, 5, 1]
    expenses    = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print savingsRecord
    # Output should have values close to:
    # [80000.000000000015, 54000.000000000015, 24000.000000000015,
    # -4799.9999999999854, -34847.999999999985]

    savingsRecord = postRetirement(savings, [], expenses)
    print savingsRecord


#
# Problem 4
#

def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates,
                    epsilon):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - preRetireGrowthRates: a list of annual growth percentages on investments
      while you are still working.
    - postRetireGrowthRates: a list of annual growth percentages on investments
      while you are retired.
    - epsilon: an upper bound on the absolute value of the amount remaining in
      the investment fund at the end of retirement.
    """
    if (len(postRetireGrowthRates) == 0):
        return -1 # in this case, definition "expense" has no practical meaning

    savings_records = nestEggVariable(salary, save, preRetireGrowthRates);
    total_of_savings = savings_records[-1]

    print 'total of savings:', total_of_savings

    # binary search algorithms
    # initial right end: (all savings)
    exp_right = total_of_savings
    # initial left end : 0$
    exp_left = 0.0
    
    guess = (exp_right + exp_left)/2.0

    remains = postRetirement(total_of_savings, postRetireGrowthRates, guess)
    diff = epsilon - remains[-1]
    while ( diff < 0.0 or diff >= 0.01 ): # if not limited to the upper bound
        if (diff < 0.0 ):
            exp_left = guess
        else:
            exp_right = guess

        new_guess = (exp_left + exp_right)/2.0

        if (abs(new_guess - guess) < 0.001):
            break
        else:
            guess = new_guess
            remains = postRetirement(total_of_savings, postRetireGrowthRates, guess)
            diff = epsilon - remains[-1]

    print 'remaining of fund:', remains[-1]
    return guess 
 

def testFindMaxExpenses():
    salary                = 10000
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print expenses
    # Output should have a value close to:
    # 1229.95548986

    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               [0], epsilon)
    print expenses
    # Output should be a value close to the maximal saving record


    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, 10000000)
    print expenses
    # Output should be a value close to 0.0, because the "epsilon" is set too high
