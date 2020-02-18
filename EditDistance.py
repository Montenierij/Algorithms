######################################################
# Jacob Montenieri
# Introduction To Algorithms
# Lab 7
# This lab goes over a dynamic programming algorithm
# to computer the necessary edit distance between two
# strings.
######################################################
def diff(str1, str2, a, b):
    if str1[a-1] == str2[b-1]:
        return 0
    else:
        return 1


total = 1E6
newString1 = ""
newString2 = ""
string1 = "exponential"
string2 = "polynomial"
len1 = len(string1)
len2 = len(string2)
E = []  #My list
for i in range(len1 + 1):
    E.append([0]*(len2 + 1))

for i in range(len1 + 1):
    E[i][0] = i

for j in range(1, len2 + 1):
    E[0][j] = j

for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        E[i][j] = min(E[i-1][j] + 1, E[i][j-1] + 1, E[i-1][j-1] + diff(string1, string2, i, j))
for l in E:
    print(l)
total = E[len1-1][len2-1]
i = len1
j = len2
while i > 0 and j >= 0:
    if E[i][j] == E[i-1][j] + 1:
        newString2 = "-" + newString2
        newString1 = string1[i-1] + newString1
        i -= 1
    elif E[i][j] == E[i][j-1] + 1:
        newString1 = "-" + newString1
        newString2 = string2[j-1] + newString2
        j -= 1
    else:
        newString2 = string2[j-1] + newString2
        newString1 = string1[i-1] + newString1
        i -= 1
        j -= 1
print(newString1)
print(newString2)
