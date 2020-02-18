file1 = open(r"Lab1Data2.txt")
filew = open("Lab1Data2Formalized.txt", "w")
x = 0
counter = 0
for i in range(0, file1.__sizeof__()):
    y = file1.readline()
    y = y.splitlines()
    x = y[0].split(" ")
    print(x[0])
    #plt.plot(x[0], x[1])
    #print(x[0])
    #print(x[1])
    #if i % 14 == 13:          #THIS WILL DO EVERY 14 LOGS
   # filew.write(str(x[0]) + "," + str(x[1]) + "\n")
filew.close()
