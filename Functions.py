from math import cos, sin, sqrt, exp, e
from numpy import pi

""" This class contains all functions from the article """

def Rosenbrock2D(X):
    fx = 100 * (X[0] ** 2 - X[1]) ** 2 + (1 - X[0]) ** 2
    return fx

def Sphere(X):
    fx = 0.0
    for i in range(10):
        fx += X[i] ** 2
    return fx

def Rosenbrock10D(X):
    fx = 0.0
    for i in range(9):
        fx += 100 * pow((pow(X[i], 2) - X[i + 1]), 2) + pow((1 - X[i]), 2)
    return fx

def Ackley(X):
    sygma_x_2 = 0.0
    sygma_cos = 0.0
    for i in range(10):
        sygma_x_2 += pow(X[i], 2)
        sygma_cos += cos(2 * pi * X[i])
    
    fx = -20 * exp(-0.2 * sqrt(0.1 * sygma_x_2)) - exp(0.1 * sygma_cos) + 20 + e
    return fx

def Griewank(X):
    part1 = 0.0
    part2 = 1.0
    for i in range(10):
        part1 += X[i] ** 2
        part2 *= cos(float(X[i]) / sqrt(i + 1))
    fx = (float(part1) / 4000.0) - float(part2) + 1
    return fx

def Weierstrass(X):
    part1 = 0.0
    part2 = 0.0
    k_max = 21
    for i in range(10):
        for k in range(k_max):
            part1 += pow(0.5, k) * cos(2 * pi * pow(3, k) * (X[i] + 0.5))
    for k in range(k_max):
        part2 += pow(0.5, k) * cos(2 * pi * pow(3, k) * 0.5)
    fx = part1 - 10 * part2
    return fx

def Rastrigin(X):
    fx = 0.0
    for i in range(10):
        fx += pow(X[i], 2) - 10 * cos(2 * pi * X[i])
    return fx

def NCRastrigin(X):
    fx = 0.0
    Y = [0.0] * 10
    for i in range(10):
        if abs(X[i]) < 0.5:
            Y[i] = X[i]
        else:
            Y[i] = round(2 * X[i]) / 2
    for i in range(10):
        fx += pow(Y[i], 2) - 10 * cos(2 * pi * Y[i]) + 10
    return fx

def Schwefel(X):
    fx = 0.0
    for i in range(10):
        fx += X[i] * sin(sqrt(abs(X[i])))
    fx = (-1) * fx
    return fx