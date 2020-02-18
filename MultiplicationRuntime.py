######################################################
# Jacob Montenieri
# Introduction To Algorithms
# Lab 2
# This lab goes over different methods of multiplying
# binary numbers and goes over the importance of efficiency
# and run time for each method.
######################################################
import random
import timeit
import math


def decimult(a, b):
    return a*b
#Basic Method of Multiplication


def method1(a, b):
    j = 1
    t = 0
    l = len(bin(b)) - 2  # THIS IS IMPORTANT, HOW TO FIND SIZE OF BINARY
    #print("Length of Y: " + str(l))
    for j in range(0, l):
        h1 = b & 1
        #print("H1 value is: " + str(h1))
        t = t + (a * h1)
        b = b >> 1
        a = a << 1
    print("Total after Method 1: " + str(t))
    return


def method2(a, b):
    if b == 0:
        return 0
    t = method2(a, math.floor((b >> 1)))
    if (a * b) == ((a*(math.floor(b >> 1))) << 1):
        #print("Y is Even")
        return t << 1
    else:
        #print("Y is Odd")
        return a + (t << 1)


def method3(a, b):
    if a.bit_length() > b.bit_length():
        n = a.bit_length()
    else:
        n = b.bit_length()
    #print("Largest N bit is: " + str(n))
    if n <= 1:
        return a * b
    #print("N value: " + str(n))
    #print("Number of bits for n: " + str(math.ceil(n/2)))
    al = a >> math.floor(n >> 1)
    ar = a & (a-(al << math.floor(n >> 1)))
    bl = b >> math.floor(n >> 1)
    br = b & (b - (bl << math.floor(n >> 1)))
    p1 = method3(al, bl)
    p2 = method3(ar, br)
    p3 = method3((al + ar), (bl + br))
    return (p1 << ((math.floor(n >> 1)) << 1)) + ((p3-p1-p2) << (math.floor(n >> 1))) + p2
    #return p1 * 2**((math.floor(n >> 1)) << 1) + (p3-p1-p2) * 2**math.floor(n >> 1) + p2



i = 1
totalTime1 = 0
totalTime2 = 0
totalTime3 = 0
#print("Random number X equals: " + str(x))
#z = decimult(x, y)
#print("Z equals " + str(z))

#print("BINARY X: " + bin(x))
#print("BINARY Y: " + bin(y))
#method1(x, y)
#total2 = method2(x, y)#
#print("Total after method2: " + str(total2))
#total3 = method3(x, y)
#print("Total after method3: " + str(total3))


print("Enter the length of the digits you'd like to multiply: ")
d = input()
d = int(d)
for r in range(0, 1):
    x = random.randint(1, 9)
    for i in range(1, d):
        f = random.randrange(10)
        x = int(str(x) + str(f))

    y = random.randint(1, 9)
    for i in range(1, d):
        f = random.randrange(10)
        y = int(str(y) + str(f))
    print("X value: " + str(x))
    print("Y valueL " + str(y))
    total2 = method2(x, y)
    print("Total after Method 2: " + str(total2))
    total3 = method3(x, y)
    print("Total after Method 3: " + str(total3))
    t1 = timeit.Timer('method1(x, y)', 'from __main__ import method1, x, y')
    elapsed1 = t1.timeit(number=1)
    totalTime1 = totalTime1 + elapsed1
    #print("Method1 takes this long to multiply: ", elapsed1)

    #t2 = timeit.Timer('method2(x, y)', 'from __main__ import method2, x, y')
    #elapsed2 = t2.timeit(number=1)
    #totalTime2 = totalTime2 + elapsed2
    #print("Method2 takes this long to multiply: ", elapsed2)

    t3 = timeit.Timer('method3(x, y)', 'from __main__ import method3, x, y')
    elapsed3 = t3.timeit(number=1)
    totalTime3 = totalTime3 + elapsed3
    #print("Method3 takes this long to multiply: ", elapsed3)

print("Method 1 takes an average of " + str(totalTime1/10) + " seconds.")
print("Method 2 takes an average of " + str(totalTime2/10) + " seconds.")
print("Method 3 takes an average of " + str(totalTime3/10) + " seconds.")
