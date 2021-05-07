# Define an objective function, for example above:
# Example from the documentations on how to create a function for the model
def Fx(solution):
    fx = solution[0] ** 3 + solution[1] ** 2 + solution[2] ** 4
    return fx


# Arie's example of simple rosenbrock function
def RosenbrockSimple(solution):
    return 100 * (solution[0] ** 2 - solution[1]) ** 2 + (1 - solution[0]) ** 2


##################################################
# TODO EDEN
#########################################
def Sphere(solution):
    return


def Rosenbrock(solution):
    return


def Ackley(solution):
    return


def Griewank(solution):
    return


def Weierstrass(solution):
    return


def Rastrigin(solution):
    return


def NCRastrigin(solution):
    return


def Schwefel(solution):
    return
