#
#Αριθμητική Ανάλυση - υποχρεωτική εργασία 2017-2018 - 6η εκφώνηση

import math
import numpy as np

def create_data_set(a,b,N):
    x_list=list()
    for i in range(N+1):
        my_x= a + i*((b-a)/N)
        x_list.append(my_x)
    return x_list

def Trap_method(x,a,b):
    """

    :param x: given data set of x
    :return: integral of sin(x) for my data set
    """

    n= len(x) -1
    my_sum=0
    #I want to firtly calculate the sum we use in the trapezoid method, then do the rest of the calculations
    for i in range(1,n):
        my_sum+=np.sin(x[i])
    integral= ((b-a)/(2*n))*(np.sin(x[0]) + np.sin(x[n]) + 2*my_sum)
    return integral

def Simpson_method(x,a,b):
    """

    :param x: given data set of x (N- even number)
    :param a: limit
    :param b: limit
    :return: integral according to simpson method for sin(x)
    """
    n= len(x) -1
    #firstly i need to calculate two sums needed for the simpson method, then do the rest:
    sum_1 = 0
    sum_2 = 0
    for i in range(1,int(n/2)):
        sum_1 += np.sin(x[2*i])
    for i in range(1,int(n/2) +1):
        sum_2 += np.sin(x[2*i -1])
    integral = ((b-a)/(3*n))*(np.sin(x[0]) + np.sin(x[n]) + 2*sum_1 + 4*sum_2)
    return integral
def calculate_error(x):
    """

    :param x: the result of one of the methods
    :return: |real-estimation|
    """

    error=abs(1-x)
    return error

uniform_x = create_data_set(0,np.pi/2,10)
test_x = [0,np.pi/10,np.pi/6,np.pi/5,np.pi/2]
t=Trap_method(uniform_x,0,np.pi/2)
s=Simpson_method(uniform_x,0,np.pi/2)
print("Trapezoid method result:",t)
print("Simpson method result:",s)
print("Error for trapezoid method  {0:.15f}".format(calculate_error(t)))
print("Error for simpson method  {0:.15f}".format(calculate_error(s)))
print("let's use some non uniform intervals - some taken from project 5.")
print(test_x)
print("let's check the methods now for [0, π/2]")
test_t = Trap_method(test_x,0,np.pi/2)
test_s = Simpson_method(test_x,0,np.pi/2)
print("Trapezoid method result:",test_t)
print("Simpson method result:",test_s)
print("Error for trapezoid method  {0:.15f}".format(calculate_error(test_t)))
print("Error for simpson method  {0:.15f}".format(calculate_error(test_s)))
