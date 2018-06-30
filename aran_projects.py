#Αλμήνη Μιχάλογλου -2376
#Αριθμητική Ανάλυση - υποχρεωτική εργασία 2017-2018
#εκφωνήσεις 1,2

import random
import math
import numpy
from matplotlib import pyplot as plt

def one_value(x):
    value = numpy.exp(numpy.sin(x)**3) + x**6 - 2*(x**4) - x**3 - 1
    return value
def one_der(x):
    f1 = 3 * numpy.exp(numpy.sin(x) ** 3) * numpy.cos(x) * (numpy.sin(x)) ** 2 + 6 * (x ** 5) - 8 * (x ** 3) - 3 * (
    x ** 2)
    return f1

def one_derr(x):
    value = -3*numpy.e*(numpy.sin( x )**3) + 6*numpy.e*(numpy.cos( x )**2) *numpy.sin( x ) + 30* x**4-24* x**2-6 *x
    return value
def one():
    x = numpy.arange(-2.0, 2.01, 0.01)
    f = numpy.exp(numpy.sin(x)**3) + x**6 - 2*(x**4) - x**3 - 1

    #plot f:
    plt.grid(color='#2B2B2B', linestyle='-', alpha=0.5)
    line, = plt.plot(x, f, lw=2)
    plt.show()
    #bisection
    #find N : error <= 1/2 * 10^-6
    a= -2.0
    b= 2.0
    #N = 23
    N = math.ceil(math.log(1/((1/(2*(b-a)))*10**(-6))) / math.log(2))
    print('Bisection Method:')
    for i in range(N):
        f_a = one_value(a)
        f_b = one_value(b)
        m = (a + b)/2
        value = one_value(m)
        if value == 0:
             print("Solution is :", m)
             break
        else:
            if value*f_a <0:
                b= m
            else:
                a= m
    #Newton-Raphson
    print('Newton-Raphson Method f" >= 0 according to WolframAlpha Plot :')
    x0= 0.1
    N = 0
    while True:
        N+=1
        x1= x0 - one_value(x0)/one_der(x0)
        error = abs(x1-x0)**2
        if math.sqrt(error) <= 1/2 * (10**(-6)):
            print('Found solution at :', x1, 'after ', N, 'iterations/loops')
            break
        else:
            x0= x1
    #Secant Method
    print('Secant method for x0,x1 = 2.0, 1.5')
    x0= 2.0
    x1 = 1.5
    N= 0
    while True:
        N+= 1
        x2= x1 - (one_value(x1)*(x1-x0))/(one_value(x1)-one_value(x0))
        error = abs(x2 - x1) ** 2
        if math.sqrt(error) <= 1 / 2 * (10 ** (-6)):
            print('Found solution at :', x1, 'after ', N, 'iterations/loops')
            break
        else:
            x0 = x1
            x1 = x2

#return the value of the function -2
def two_value(x):
    value =  54*(x**6) + 45*(x**5) - 102*(x**4) - 69*(x**3) + 35*(x**2) + 16*x - 4
    return value
# f' - 2
def two_der(x):
    value = 6*54*(x**5) + 5*45*(x**4) - 4*102*(x**3) - 3*69*(x**2) + 2*35*x + 16
    return value
#f'' - 2
def two_derr(x):
    value = 1620*(x**4) + 900*(x**3) - 1224*(x**2) - 414*x + 70
    return value

#2nd project
def two():
    #altered N-R
    print("Altered version of N-R:")
    x0= 2
    N=0
    while True:
        N+=1
        x1= x0 - (two_value(x0)/two_der(x0)) - 1/2 * ((two_value(x0)**2)*(two_derr(x0)))/(two_der(x0)**3)
        error = abs(x1-x0)**2
        if math.sqrt(error) <= 1/2 * (10**(-6)):
            print('Found solution at :', x1, 'after ', N, 'iterations/loops')
            break
        else:
            x0= x1
    #altered bisection method - using a random number as m
    print("Altered version of bisection method:")
    a= -2
    b= 2
    i=0
    while True:
        i+=1
        f_a = two_value(a)
        f_b = two_value(b)
        m = random.uniform(a, b)
        value = two_value(m)
        error = abs(f_a -f_b)
        if error <= (1/2)*(10**(-6)):
             print("Solution is :", m,"for",i,"steps")
             break
        else:
            if value*f_a <0:
                b= m
            else:
                a= m

    #altered secant method
    print('Altered version of the secant method:')
    x0 = 2
    x1 = 1
    x2 = 1.8
    N = 0
    while True:
        N += 1
        q = two_value(x0)/two_value(x1)
        r = two_value(x2)/two_value(x1)
        s = two_value(x2)/two_value(x0)
        x3 = x2 - (r*(r-q)*(x2 - x1)+(1-r)*s*(x2-x0))/((q-1)*(r-1)*(s-1))
        error = abs(x3 - x0) ** 2
        if math.sqrt(error) <= 1 / 2 * (10 ** (-6)):
            print('Found solution at :', x3, 'after ', N, 'iterations/loops')
            break
        else:
            x0 = x3


one()
two()


