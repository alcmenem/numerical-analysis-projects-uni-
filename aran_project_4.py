#
#Αριθμητική Ανάλυση - υποχρεωτική εργασία 2017-2018 - 4η εκφώνηση

import numpy as np
import random

def create_Google_matrix(A,q):
    """
    Calculate and create a GOOGLE matrix
    :param A: A neighbor matrix
    :param q: q parameter
    :return: G: google matrix
    """
    n=len(A)
    G= np.zeros(shape=(n,n))
    nj_list=list()
    for i in range(n):
        my_sum=0
        for j in range(n):
            my_sum+=A[i,j]
        nj_list.append(my_sum)
    #creating G matrix using the formula
    for i in range(n):
        for j in range(n):
            G[i,j] = q/n + (A[j,i]*(1-q))/nj_list[j]
    return G
def check_g(G):
    """

    :param G: my google matrix
    :return: a list of the sum of each column _i m checking if G is stochastic
    """
    my_list=list()
    for i in range(len(G)):
        sum=0
        for j in range(len(G)):
            sum+=G[j,i]
        my_list.append(sum)
    return my_list

def power_method(G):
    """
    Implementation of the power method, for a google matrix
    :param G: a google matrix
    :return: p vector
    """
    #print("I will choose a random column from the G matrix as a starting point:")
    #chose one of the columns as an initial vector
    my_roll=0
    initial=np.zeros(shape=(len(G),1))
    for i in range(len(G)):
        initial[i] = G[i,my_roll]
    #print("Initial vector is ",my_roll,"column:",initial)
    #print("Onto the steps of the power method")

    if initial[0]!=0:
        initial_l= initial[0]
    else:
        for i in range(1, len(initial)):
            if initial[i] != 0:
                initial_l = initial[i]
                break

    while True:
        next = np.copy(np.dot(G,initial))

        if next[0] != 0:
            l = next[0]

            next = np.copy((1/next[0])*next)

        else:
            for i in range(1,len(next)):

                if next[i] != 0:
                    l = next[i]
                    next = np.copy((1 / next[i]) * next)
                    break

        difference = abs(initial_l -l)
        if difference<= (1/2)*10**(-7):
            my_p = np.copy(next)
            break
        initial=np.copy(next)
        initial_l = l
    sum = 0
    for i in range(len(my_p)):
        sum+=my_p[i]
    for i in range(len(my_p)):
        my_p[i]=my_p[i]/sum

    return my_p




A= np.matrix('0 1 0 0 0 0 0 0 1 0 0 0 0 0 0; 0 0 1 0 1 0 1 0 0 0 0 0 0 0 0;0 1 0 0 0 1 0 1 0 0 0 0 0 0 0;0 0 1 0 0 0 0 0 0 0 0 1 0 0 0; 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0;0 0 0 0 0 0 0 0 0 1 1 0 0 0 0;0 0 0 0 0 0 0 0 0 1 1 0 0 0 0;0 0 0 1 0 0 0 0 0 0 1 0 0 0 0;0 0 0 0 1 1 0 0 0 1 0 0 0 0 0;0 0 0 0 0 0 0 0 0 0 0 0 1 0 0;0 0 0 0 0 0 0 0 0 0 0 0 0 0 1;0 0 0 0 0 0 1 1 0 0 1 0 0 0 0;0 0 0 0 0 0 0 0 1 0 0 0 0 1 0;0 0 0 0 0 0 0 0 0 1 1 0 1 0 1;0 0 0 0 0 0 0 0 0 0 0 1 0 1 0')
q=0.15
G =create_Google_matrix(A,q)
#print(G)
p= power_method(G)
print("Checking G:",check_g(G))
print('P vector i found for page-ranks for ORIGINAL A:\n',p.transpose())
myA=np.copy(A)
#3rd question: My changes : link 1.2.3 to 11. Unlink 11 from 15. Link 11 to 1.
for i in range(3):
    myA[i,10]=1
myA[10,14]=0
myA[10,0]=1
#print("I created a new version of A in order to increase the rank of page 11: \n",myA)
my_G= create_Google_matrix(myA,q)
my_p= power_method(my_G)
print('P vector i found for my page-rank -3rd question:\n',my_p.transpose())
#4th question q1,q2
q1 = 0.02
q2 = 0.6
G1 = create_Google_matrix(myA,q1)
p1= power_method(G1)

G2= create_Google_matrix(myA, q2)

p2 = power_method(G2)

#print("First p \n",my_p)
print("Q= 0.02: \n", p1.transpose())
print("Q= 0.6: \n", p2.transpose())
#fifth question for original A matrix
A_5 = np.copy(A)
A_5[7,10]=3
A_5[11,10]=3
G_5 =create_Google_matrix(A_5,q)
p_5 = power_method(G_5)
print('P vector i found for page-ranks question 5:\n', p_5.transpose())
# sixth question, deleting row,column 9 from A in  order for page 10 to have zero influence
A_6= np.zeros(shape=(14,14))
for i in range(15):
    for j in range(15):
        if i < 9:
            row = i
        elif i > 9:
            row = i-1
        if j < 9:
            col = j
        elif j > 9:
            col = j -1
        if i != 9 and j != 9:
            A_6[row,col] = A[i,j]
#print(A_6)
G_6=create_Google_matrix(A_6,q)
p_6= power_method(G_6)
print('P vector i found for page-ranks for A_6 without the 10th page:\n',p_6.transpose())
