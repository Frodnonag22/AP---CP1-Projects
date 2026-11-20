# AP Flexible Calculator

def sum(*args):
    """Calculates the Sum"""
    total = 0
    for arg in args:
        total += arg
    return total

def average(decimal=2, *args):
    """Calculates the avarage"""
    total = 0
    for arg in args:
        total += arg
    amount = 0
    for arg in args:
        amount += 1
    average = total/amount
    return round(average, decimal)

def max(*args):
    """Calculates the Max"""
    for arg in args:
        largest = arg
    for arg in args:
        if largest < arg:
            largest = arg
    return largest

def min(*args):
    """Calculates the Min"""
    for arg in args:
        smallest = arg
    for arg in args:
        if smallest > arg:
            smallest = arg
    return smallest

def product(*args):
    """Calculates the Product"""
    product = 1
    for arg in args:
        product *= arg
    return product

