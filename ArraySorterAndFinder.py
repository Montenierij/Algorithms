######################################################
# Jacob Montenieri
# Introduction To Algorithms
# Lab 4
# This lab creates an array of N random integers up to
# a given number and then finds the n'th smallest value
# after sorting the array from smallest to largest.
######################################################
import numpy as np


def selection(a, b):
    al = []
    av = []
    ar = []
    v = np.random.choice(a=a)
    for i in range(0, np.size(a)):
        if a[i] < v:
            al.append(a[i])
            #print("small")
        elif a[i] == v:
            av.append(a[i])
            #print("same")
        elif a[i] > v:
            ar.append(a[i])
            #print("big")
    if b <= len(al):
        return selection(al, b)
    elif len(al) < b <= (len(al) + len(av)):
        return v
    elif b > (len(al) + len(av)):
        return selection(ar, (b-(len(al) + len(av))))


print("Enter N")
n = input()
print("Enter K")
k = input()
sizeOfInput = 10
array = np.random.randint(int(sizeOfInput), size=int(n))
print(str(len(array)))
print(array)
print(np.sort(array))
answer = selection(array, int(k))
print("The " + str(k) + " smallest input is: " + str(answer))


