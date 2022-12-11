import math
import matplotlib.pyplot as plt
import sys
import numpy as np
import sympy as sp


f = open("result.txt", "w")
avergex, avergey = 0, 0
def connect_txt(file):
    inputdata = []
    data = []
    input = open(file)
    input.seek(1)
    for i in input:
        inputdata.append(input.read(3).replace(',', '.'))
        input.read(1)
        inputdata.append(input.read(2))
    for i in range(int(len(inputdata) / 2)):
        data.append([0] * 2)
    index0, index1 = 0, 0
    for i in range(int(len(inputdata))):
        if i % 2 == 0:
            data[index0][0] = float(inputdata[i])
            index0 += 1
        elif i % 2 != 0:
            data[index1][1] = int(inputdata[i])
            index1 += 1
    return data

file = input('Назва файлу:')
data = sorted(connect_txt(file))
def dataX(data):
    inputdata = []
    for i in range(len(data)):
        inputdata.append(data[i][0])
    return inputdata

def dataY(data):
    inputdata = []
    for i in range(len(data)):
        inputdata.append(data[i][1])
    return inputdata


#===========================================
def covarience(data):
    print('\nЗавдання 2')
    f.write('\nЗавдання 2')
    #averagex, averagey = 0, 0
    covarience = 0.0
    x = dataX(data)
    y = dataY(data)
    #for i in range(len(x)):
        #sumx += x[i]
        #sumy += y[i]
    #averagex = sumx / len(x)
    #averagey = sumy / len(y)
    averagex = np.mean(dataX(data))
    averagey = np.mean(dataY(data))
    print('Центр ваги для першого стовпця: ', averagex)
    print('Центр ваги для другого стовпця: ', averagey)
    f.write('Центр ваги для першого стовпця: ' + str(averagex))
    f.write('Центр ваги для другого стовпця: ' + str(averagey))
    for i in range(len(x)):
        covarience += (x[i] - averagex) * (y[i] - averagey)
    print('Коваріація: ', covarience / (len(x)-1))
    f.write('Коваріація: ' + str(covarience / (len(x) - 1)))

def correlation(data):
    print('\nЗавдання 4:')
    f.write('\nЗавдання 4:')
    x = dataX(data)
    y = dataY(data)
    sumx, sumy = sum(x), sum(y)
    correlation, sum1, sum2, sum3 = 0.0, 0.0, 0.0, 0.0
    for i in range(len(x)):
        sum1 = (x[i] - sumx) * (y[i] - sumy)
        sum2 = (x[i] - sumx) * (x[i] - sumx)
        sum3 = (y[i] - sumy) * (y[i] - sumy)
    print("Кореляція: ", sum1/math.sqrt(sum2 + (sum2 * sum3)))
    f.write("Кореляція: " + str(sum1 / math.sqrt(sum2 + (sum2 * sum3))))

def solution(data):
    print('\nЗавдання 3:')
    f.write('\nЗавдання 3:')
    x = dataX(data)
    y = dataY(data)
    global avergex, avergey
    byx, sumxy, sumx, sumy, sumx2, sumy2 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    for i in range(len(x)):
        sumx += x[i]
        sumy += y[i]
        sumxy += x[i] * y[i]
        sumx2 += x[i] * x[i]
        sumy2 += y[i] * y[i]
    byx = (len(x) * sumxy - (sumx * sumy)) / (len(x) * sumx2 - sumx2)
    x, y = sp.symbols("x, y")
    line = sp.Eq(y-sumy, byx * (x - sumx))
    print("x = ", sp.solve(line, y))
    print("y = ", sp.solve(line, x))
    f.write("x = " + str(sp.solve(line, y)))
    f.write("y = " + str(sp.solve(line, x)))
    #return sp.solve(line, x)

def diagram(data):
    print('\nЗавдання 1')
    f.write('\nЗавдання 1')
    dobXY = 0
    sumX = sum(dataX(data))
    sumY = sum(dataY(data))
    sumdobXX = 0
    X = dataX(data)
    Y = dataY(data)
    for i in range(len(data)):
        dobXY += data[i][0]*data[i][1]
        sumdobXX += data[i][0] ** 2

    b = (len(data) * dobXY - (sumX * sumY)) / ((len(data) * sumdobXX) - sumX**2)

    x = np.linspace(0, 10)
    y = b*(x - np.mean(dataX(data))) + np.mean(dataY(data))

    plt.scatter(X, Y, marker="d", s=100, color="blue")

    if max(data)==data[len(data)-1]:
        plt.title("Діаграма розкиду даних \n Тренд позитивний")
    elif min(data)==data[len(data)-1]:
        plt.title("Діаграма розкиду даних \n Тренд негативний")
    plt.xlabel("вісь X")
    plt.ylabel("вісь Y")

    plt.plot(x, y, color="green")
    plt.show()

diagram(data)
covarience(data)
solution(data)
correlation(data)

f.close()