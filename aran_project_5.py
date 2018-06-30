#Αλμήνη Μιχάλογλου -2376
#Αριθμητική Ανάλυση - υποχρεωτική εργασία 2017-2018 - 5η εκφώνηση

import numpy as np
import random


def find_random_set(n):
    """

    :param n: how many data points i need
    :return: an ordered list of said points
    """
    x_list = list()
    for i in range (n):
        #random x points in (-π,π)
        x = random.uniform(-np.pi,np.pi)
        x_list.append(x)
    #sort my points, as it is necessary for the methods i 'm going to use
    x_list.sort()
    return x_list
def random_set_values(x_list):
    """
    i chose to do this using random points
    :param x_list: ordered points
    :return: their f values
    """
    n= len(x_list)
    y_list=list()
    for i in range (n):
        my_x = x_list[i]
        y= np.sin(my_x)
        y_list.append(y)
    return y_list


def lagrange_pol(x_list,y_list, input):
    """

    :param x_list: ordered list of points
    :param y_list: list of the values of said points
    :return:
    """
    #number of Li I'll need
    n = len(x_list)
    L_list=list()
    for i in range(n):
        #Li
        L = 1
        for j in range(n):
            if i != j:
                L *= (input - x_list[j])/(x_list[i]-x_list[j])
        L_list.append(L)
    my_sum=0
    for i in range(n):
        my_sum += y_list[i]*L_list[i]
    return my_sum

def cubic_splines():
    return 0
def least_squares(x_list,y_list, input):
    print("Least squares method for a curve in the form of : a +bt +c(t^2)")
    #create A
    print("Creating A matrix...")
    n=len(x_list)
    A= np.zeros(shape=(n,3))
    b= np.zeros(shape=(n,1))
    #fill in b matrix with y-values (f)
    for i in range(n):
        b[i] = y_list[i]
    #fill in A matrix (συντελεστές των a,b,c = 1,t,t^2)
    for i in range(n):
        for j in range(3):
            if j==0:
                A[i,j]=1
            elif j==1:
                A[i,j]= x_list[i]
            else:
                A[i,j]= x_list[i]**2
    print(A)
    print('Creating (A^T)A...')
    A_t = np.copy(A.transpose())
    A_t_A= np.dot(A_t,A)
    print(A_t_A)
    print("Creating A^T * b  matrix")
    A_t_b = np.dot(A_t,b)
    print(A_t_b)
    print("Solving in order to find a,b,c using the Gaussian method...")
    solution = np.linalg.solve(A_t_A,A_t_b)
    print("Solution is : {} + {} t + {} t^2".format( solution[0],solution[1],solution[2]))
    print("Calculatin errors...")
    x= np.dot(A,solution)
    r= b - x
    r_n = np.linalg.norm(r)
    print("error-norm:",r_n)
    print("Solution for my input =",input)
    answer = solution[0] + solution[1]*input + solution[2]*(input**2)
    print("My answer is ",answer)
    return r_n

x_list= find_random_set(10)
y_list = random_set_values(x_list)
print(lagrange_pol(x_list,y_list,np.pi/2))
x= [- np.pi, -np.pi/4, -np.pi/12, 0, -np.pi*0.21, np.pi/10, np.pi/2, 2*np.pi/2, np.pi/6, np.pi]
y= random_set_values(x)
least_squares(x_list,y_list,np.pi/4)

