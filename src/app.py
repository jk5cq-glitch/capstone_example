import math

def add(a, b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    return a/b

def log(a):
    return math.log(a)

def squ(a):
    return a ** 2

def sin(a):
    return math.sin(a)

def cos(a):
    return math.cos(a)

def root(a):
    if (a) >= 0:
        return math.sqrt(a)
    else:
        return ("Invalid number")

def perc(a, b):
    if ((a / abs(a) == -1) or (b == 0)):
        return "Invalid"
    else:
        return (a / b) * 100  