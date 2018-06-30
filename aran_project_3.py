#
#Αριθμητική Ανάλυση - υποχρεωτική εργασία 2017-2018 - 3η εκφώνηση

import math
import numpy as np

def palu_gauss_method(A, b):
    n= len(A)
    #create P and L and U
    P = np.zeros(shape=(n,n))
    L = np.zeros(shape=(n,n))
    U = np.copy(A)
    for i in range(n):
        P[i,i] = 1

    #create L,U,P matrices
    for col in range(n):
        pivot = U[col][col]
        max= col
        for row in range(col, n):
            if U[row][col]> pivot:
                max= row
        if max != col:
            #swap lines for U
            temp_row= np.copy(U[col])
            #check:print(temp_row)
            U[col]= U[max]
            U[max] = temp_row
            #swap lines for P
            p_temp_row= np.copy(P[col])
            P[col]= P[max]
            P[max]= p_temp_row
            #swap lines for L
            l_temp_row = np.copy(L[col])
            L[col]= L[max]
            L[max]=l_temp_row
        #gauss method:
        for i in range(col+1,n):
            mult = U[i,col]/U[col,col]
            #change the row according to gauss
            U[i]= U[i] - mult*U[col]
            L[i,col]= mult
    for i in range(n):
        L[i,i] = 1
    print('P matrix is: \n', P)
    print('L matrix is: \n', L)
    print('U matrix is: \n', U)
    print('On to solving the system:')
    #forward substitution
    #multiply P*B
    p_b = P*b
    y= np.zeros(shape=(n,1))
    #forward substitution
    print('Solve Ly=Pb with forward substitution, y is : ')
    for i in range(n):
        rest_of_y = 0
        for j in range(i):
            rest_of_y += L[i,j]*y[j]
        y[i]= p_b[i] - rest_of_y
    print(y)
    print('Solve Ux=y with backward substitution, x is: ')
    x=np.zeros(shape=(n,1))
    for i in range(n-1,-1,-1):
        rest_of_x = 0
        for j in range(i+1,n):
            rest_of_x += U[i,j]*x[j]
        x[i]= (y[i] - rest_of_x)/U[i,i]
    print(x)
    print('Linear system is solved, x is the final solution!')

def cholesky(A):
    #https://rosettacode.org/wiki/Cholesky_decomposition - I used this formulae
    print('Cholesky decomposition:')
    n= len(A)
    L=np.zeros(shape=(n,n))
    print("Building the L matrix...")
    for i in range(n):
        for j in range(i+1):
            #use the formula for the diagonal
            if i==j:
                my_sum=0
                #counting previous elements for the formula:
                for counter in range(j):
                    my_sum += (L[i,counter])**2
                L[i,i]= np.sqrt(A[i,j] - my_sum)

            #use the formula for the elements below the diagonal:
            elif i>j:
                my_sum=0
                #counting previous elements i need for the formula:
                for counter in range(j):
                    my_sum += L[i,counter] * L[j,counter]

                L[i,j]= (1/L[j,j])*(A[i,j] - my_sum)

    print("The L matrix is:")
    print(L)
    print("The L^T matrix is:")
    print(L.transpose())





def gauss_seidel_method(n):
    print("Creating our own A, and b matrices in order to solve Ax=b")
    #n1=10,n2= 10000

    A=np.zeros(shape=(n,n))

    for i in range(n):
        for j in range(n):
            if i==j:
                A[i,j]=5
            elif j==i+1 or j==i-1:
                A[i,j]= -2

    b=np.zeros(shape=(n,1))
    for i in range(n):
        if i==0 or i==n-1:
            b[i]= 3
        else:
            b[i]= 1
    #onto the gauss seidel method:
    #x_n is the newest set of x solutions, while x is the last one,x0=(0,0...0)
    x=np.zeros(shape=(n,1))
    x_n= np.zeros(shape=(n,1))
    counter = 0

    while True:
        counter += 1
        for i in range(n):
            previous_sum = 0
            following_sum = 0
            for prev in range(i):
                previous_sum += A[i,prev]*x_n[prev]
            for next in range(i+1,n):
                following_sum += A[i,next]*x[next]
            x_n[i]= (1/A[i,i])*(b[i] - previous_sum - following_sum)
        #calculate
        difference= np.zeros(shape=(n,1))
        for i in range(n):
            difference[i]= abs(x[i]-x_n[i])
        if np.linalg.norm(difference, np.inf) <= 0.5*(10**(-4)):
            break

        x= x_n.copy()

    print('Solution:',x_n)











A = np.matrix('2 1 5; 4 4 -4 ;1 3 1')
b = np.matrix('9;2;7')
palu_gauss_method(A, b)

B =np.matrix('25 15 -5; 15 18 0; -5 0 11')
cholesky(B)
gauss_seidel_method(10)
