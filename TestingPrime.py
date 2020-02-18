######################################################
# Jacob Montenieri
# Introduction To Algorithms
# Lab 3
# This lab goes over primeality testing and how to
# test using an algorithm that is efficient but also
# doesn't have a 100 percent success rate, showing
# tradeoffs of accuracy vs. speed
######################################################
import random
import timeit
import math


def modexp(x, y, n):
    if y <= 0:
        return 1
    z = modexp(x, math.floor(y >> 1), n)
    if (x * y) == ((x*(math.floor(y >> 1))) << 1):
        return (z**2) % n
    else:
        return (x * z**2) % n


def primeality2(n):
    primetest = 0
    for i in range(0, 1):
        p = random.randint(1, n-1)
        if (p**(n-1) % n) != 1:
            primetest = 1   #NO LONGER PRIME
    return primetest


#print("Enter X")
#a = input()
#a = int(a)
#print("Enter Y")
#b = input()
#b = int(b)
print("Enter N")
counter = 0
c = input()
c = int(c)
#total = modexp(a, b, c)
#print("X^Y mod N equals:" + str(((a**b) % c)))
#print("X^Y mod N equals " + str(total) + " From modexp")
for j in range(0, 1000):
    prime = primeality2(c)
    if prime == 0:#Prime
        counter += 1
print("Number returned prime " + str(counter) + " times in 1000 trials.")



