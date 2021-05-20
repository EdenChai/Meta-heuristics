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














##########################################################################################

# from math import cos, sin, sqrt, exp, e
# from numpy import pi
#
# # Search range: [-10,10]
# def Rosenbrock2D(X):
#     fx = 100 * (X[0] ** 2 - X[1]) ** 2 + (1 - X[0]) ** 2
#     return fx
#
# # Search range: [-100,100]
# # Initialization range: [-100,50]
# def Sphere(X):
#     fx = 0.0
#     for i in range(10):
#         fx += X[i] ** 2
#     return fx
#
#
# # Search range: [-2.048,2.048]
# # Initialization range: [-2.048,2.048]
# def Rosenbrock10D(X):
#     fx = 0.0
#     for i in range(9):
#         fx = + 100 * pow((pow(X[i], 2) - X[i + 1]), 2) + pow((1 - X[i]), 2)
#     return fx
#
#
# # Search range: [-32.768,32.768]
# # Initialization range: [-32.768,16]
# def Ackley(X):
#     sygma_x_2 = 0.0
#     sygma_cos = 0.0
#     for i in range(10):
#         sygma_x_2 += pow(X[i], 2)
#         sygma_cos += cos(2 * pi * X[i])
#
#     fx = -20 * exp(-0.2 * sqrt(0.1 * sygma_x_2)) - exp(0.1 * sygma_cos) + 20 + e
#     return fx
#
#
# # Search range: [-600,600]
# # Initialization range: [-600,200]
# def Griewank(X):
#     part1 = 0.0
#     part2 = 1.0
#     for i in range(10):
#         part1 += X[i] ** 2
#         part2 *= cos(float(X[i]) / sqrt(i + 1))
#     fx = (float(part1) / 4000.0) - float(part2) + 1
#     return fx
#
#
# # Search range: [-0.5,0.5]
# # Initialization range: [-0.5,0.2]
# def Weierstrass(X):
#     part1 = 0.0
#     part2 = 0.0
#     k_max = 21
#     for i in range(10):
#         for k in range(k_max):
#             part1 += pow(0.5, k) * cos(2 * pi * pow(3, k) * (X[i] + 0.5))
#     for k in range(k_max):
#         part2 += pow(0.5, k) * cos(2 * pi * pow(3, k) * 0.5)
#     fx = part1 - 10 * part2
#     return fx
#
#
# # Search range: [−5.12, 5.12]
# # Initialization range: [−5.12, 2]
# def Rastrigin(X):
#     fx = 0.0
#     for i in range(10):
#         fx += pow(X[i], 2) - 10 * cos(2 * pi * X[i])
#     return fx
#
#
# # Search range: [−5.12, 5.12]
# # Initialization range: [−5.12, 2]
# def NCRastrigin(X):
#     fx = 0.0
#     Y = [0.0]*10
#     for i in range(10):
#         if abs(X[i]) < 0.5:
#             Y[i] = X[i]
#         else:
#             Y[i] = round(2 * X[i])/2
#     for i in range(10):
#         fx += pow(Y[i], 2) - 10 * cos(2 * pi * Y[i]) + 10
#     return fx
#
#
# # Search range: [−500, 500]
# # Initialization range: [−500, 500]
# def Schwefel(X):
#     fx = 0.0
#     for i in range(10):
#         fx += X[i] * sin(sqrt(abs(X[i])))
#     fx = (-1) * fx
#     return fx
#
# # X = []
# # for i in range(10):
# #     X.append(random.randint(-500,500))
# # X = [1, 0.5, 3.8, 25.111, 5, 15.65, -20.78, 52.55, 44, 0]
# # X2 = [1, 0.5, 3.8, 25.111, 5, 15.65, -20.78, 52.55, 44, 0]
# # X3 = [1, 0.5, 3.8, 25.111, 5, 15.65, -20.78, 52.55, 44, 0]
# # X4 = [1, 0.5, 3.8, 25.111, 5, 15.65, -20.78, 52.55, 44, 0]
# # X5 = [1, 0.5, 3.8, 25.111, 5, 15.65, -20.78, 52.55, 44, 0]
# # X6 = [1, 0.5, 3.8, 25.111, 5, 15.65, -20.78, 52.55, 44, 0]
# # X7 = [1, 0.5, 3.8, 25.111, 5, 15.65, -20.78, 52.55, 44, 0]
# # X8 = [1, 0.5, 3.8, 25.111, 5, 15.65, -20.78, 52.55, 44, 0]
# # X9 = [1, 0.5, 3.8, 25.111, 5, 15.65, -20.78, 52.55, 44, 0]
# # print(X)
# # print(RosenbrockSimple(X))
# # print(Sphere(X))
# # print(Rosenbrock(X))
# # print(Ackley(X))
# # print(Griewank(X))
# # print(Weierstrass(X))
# # print(Rastrigin(X))
# # print(NCRastrigin(X))
# # print(Schwefel(X))
