#Αλμήνη Μιχάλογλου -2376
#Αριθμητική Ανάλυση - υποχρεωτική εργασία 2017-2018 - 7η εκφώνηση

import numpy as np

def least_squares_method(x_list,y_list, degree, input):
    # create A
    #print("Creating A matrix...")
    n = len(x_list)
    A = np.zeros(shape=(n, degree+1))
    b = np.zeros(shape=(n, 1))
    # fill in b matrix with y-values (f)
    for i in range(n):
        b[i] = y_list[i]
    # fill in A matrix (συντελεστές των a,b,c,ktl)
    for i in range(n):
        for j in range(degree+1):
            if j == 0:
                A[i, j] = 1
            elif j == 1:
                A[i, j] = x_list[i]
            else:
                A[i, j] = x_list[i] ** j
    #print(A)
    #print('Creating (A^T)A...')
    A_t = np.copy(A.transpose())
    A_t_A = np.dot(A_t, A)
    #print(A_t_A)
    #print("Creating A^T * b  matrix")
    A_t_b = np.dot(A_t, b)
    #print(A_t_b)
    #print("Solving in order to find a,b,c using the Gaussian method...")
    solution = np.linalg.solve(A_t_A, A_t_b)
    if degree==2:
        answer= solution[0] + solution[1]*input +solution[2]*(input**2)
    elif degree==3:
        answer = solution[0] + solution[1] * input + solution[2] * (input**2) + solution[3]*(input**3)
    elif degree==4:
        answer = solution[0] + solution[1] * input + solution[2] * (input ** 2) + solution[3] * (input**3) + solution[4]*(input**4)


    return answer


Cener_t = [0 ,1 ,2 ,3 , 4, 5, 6 , 7 , 8, 9]
Cener_y = [1.11, 1.10, 1.07, 1.05, 1.06, 1.11, 1.16, 1.22, 1.27, 1.26]

Abax_t =[0 ,1 ,2 ,3 , 4, 7, 8 , 9 , 10, 11]
Abax_y =[0.646, 0.64, 0.633, 0.618, 0.623, 0.623, 0.623, 0.643, 0.666, 0.672]

print('CENER: 18th of December for 2nd degree least squares= ', least_squares_method(Cener_t,Cener_y,2,10))
print('CENER: 18th of December for 3rd degree least squares= ', least_squares_method(Cener_t,Cener_y,3,10))
print('CENER: 18th of December for 4th degree least squares= ', least_squares_method(Cener_t,Cener_y,4,10))

print('ΑΒΑΞ: 18th of December for 2nd degree least squares= ', least_squares_method(Abax_t,Abax_y,2,10))
print('ΑΒΑΞ: 18th of December for 3rd degree least squares= ', least_squares_method(Abax_t,Abax_y,3,10))
print('ΑΒΑΞ: 18th of December for 4th degree least squares= ', least_squares_method(Abax_t,Abax_y,4,10))


print('CENER: 27th of December for 2nd degree least squares= ', least_squares_method(Cener_t,Cener_y,2,15))
print('CENER: 27th of December for 3rd degree least squares= ', least_squares_method(Cener_t,Cener_y,3,15))
print('CENER: 27th of December for 4th degree least squares= ', least_squares_method(Cener_t,Cener_y,4,15))

print('ΑΒΑΞ: 27th of December for 2nd degree least squares= ', least_squares_method(Abax_t,Abax_y,2,15))
print('ΑΒΑΞ: 27th of December for 3rd degree least squares= ', least_squares_method(Abax_t,Abax_y,3,15))
print('ΑΒΑΞ: 27th of December for 4th degree least squares= ', least_squares_method(Abax_t,Abax_y,4,15))