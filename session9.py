from functools import wraps
from datetime import datetime
import time


count_dic = {}


def counter(func):
    '''
    A function named counter to count the number of times a function is called.
    And attached the nested function(inner) to input function name without losing existing function identity.
    Input : a function name
    Output : Attach nested function(inner) to input function using the concept of closures.
    '''
    count = 0
    @wraps(func)
    def inner(*args):
        nonlocal count
        count += 1
        count_dic[func.__name__] = count
        func(*args),
        return count_dic
    return inner


@counter
def add(*args):
    '''
    Sum function to return the sum of input numbers.
    Input : n Number from *args
    Output = sum of all passed numbers.
    '''
    return sum(args)


@counter
def calc_min(*args):
    '''
    A function "calc_min" to return the min of all the numbers.
    '''
    return min(args)


@counter
def calc_max(*args):
    '''
    A function "calc_min" to return the min of all the numbers.
    '''
    return max(args)



def print_func(func,sec):
    '''
    A funcction to call the function on every odd seconds continuously for n sceonds.
    '''
    for _ in range(sec):
        dt = datetime.now().second
        if dt%2 != 0:
            print(func(5,8))
            time.sleep(1)
        else:
            time.sleep(1)


print_func(add,10)
print_func(calc_min,6)
print_func(calc_max,4)
print(count_dic)