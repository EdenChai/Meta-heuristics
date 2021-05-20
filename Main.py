from mealpy.math_based.HC import BaseHC
from mealpy.physics_based.SA import BaseSA
from mealpy.swarm_based.ABC import BaseABC
from mealpy.swarm_based.EHO import BaseEHO
from mealpy.swarm_based.GWO import BaseGWO
from mealpy.swarm_based.PSO import BasePSO
from mealpy.swarm_based.WOA import BaseWOA
import Functions

function = Functions.Rosenbrock2D       # This objective function come from "opfunu" library.
verbose = True                          # Print out the training results
epoch = 10                              # Number of iterations / epochs
populationSize = 10                     # Populations size (Number of individuals / Number of solutions)
problemSize = 2                         # Number of dimensions
lowerBound = [-10]                      # The lower bound of the function
upperBound = [10]                       # The upper bound of the function

model = BaseHC(function, lowerBound, upperBound, verbose, epoch, populationSize, problem_size = problemSize)
best_pos, best_fit, list_loss = model.train()

"""" Stage 1-b """

# Run HC first time
print("Run HC first time on 2D Rosenbrock")
print(model.solution[1])
print(model.loss_train)

# Run HC second time
print("\nRun HC second time on 2D Rosenbrock")
model.train()
print(model.solution[1])

##################################################################

"""" Stage 1-c """

# Run GWO first time
print("\nRun GWO first time on 2D Rosenbrock")
model = BaseGWO(function, lowerBound, upperBound, verbose, epoch, populationSize, problem_size = problemSize)
model.train()
print(model.solution[1])

# Run GWO second time
print("\nRun GWO second time on 2D Rosenbrock")
model.train()
print(model.solution[1])

#################################################################

"""" Stage 1-d """

# Run both HC and GWO on 10D problem 50 times with different bounds

function = Functions.Rosenbrock10D      # This objective function come from "opfunu" library.
verbose = True                          # Print out the training results
epoch = 50                              # Number of iterations / epochs
populationSize = 10                     # Populations size (Number of individuals / Number of solutions)
problemSize = 10                        # Number of dimensions
lowerBound = [-2.048]                   # The lower bound of the function
upperBound = [2.048]                    # The upper bound of the function

# Run HC
print("\nRun HC on 10D Rosenbrock")
model = BaseHC(function, lowerBound, upperBound, verbose, epoch, populationSize, problem_size = problemSize)
model.train()
print(model.solution[1])

# Run GWO
print("\nRun GWO on 10D Rosenbrock")
model = BaseGWO(function, lowerBound, upperBound, verbose, epoch, populationSize, problem_size = problemSize)
model.train()
print(model.solution[1])


#################################################################

"""" Stage 2-b """

def runAlgorithms(func, lower, upper):
    function = func
    verbose = True
    epoch = 10
    populationSize = 10
    problemSize = 10
    lowerBound = lower
    upperBound = upper
    
    # Run HC
    model1 = BaseHC(function, lowerBound, upperBound, verbose, epoch, populationSize, problem_size = problemSize)
    model1.train()
    print(model1.solution[1])
    
    # Run SA
    model2 = BaseSA(function, lowerBound, upperBound, verbose, epoch, populationSize, problem_size = problemSize)
    model2.train()
    print(model2.solution[1])
    
    # Run PSO
    model3 = BasePSO(function, lowerBound, upperBound, verbose, epoch, populationSize, problem_size = problemSize)
    model3.train()
    print(model3.solution[1])
    
    # Run EHO
    model4 = BaseEHO(function, lowerBound, upperBound, verbose, epoch, populationSize, problem_size = problemSize)
    model4.train()
    print(model4.solution[1])
    
    # Run WOA
    model5 = BaseWOA(function, lowerBound, upperBound, verbose, epoch, populationSize, problem_size = problemSize)
    model5.train()
    print(model5.solution[1])
    
    # Run GWO
    model6 = BaseGWO(function, lowerBound, upperBound, verbose, epoch, populationSize, problem_size = problemSize)
    model6.train()
    print(model6.solution[1])
    
    # Run ABC
    model7 = BaseABC(function, lowerBound, upperBound, verbose, epoch, populationSize, problem_size = problemSize)
    model7.train()
    print(model7.solution[1])

# runAlgorithms( Functions.Sphere, -100, 100 )
# runAlgorithms( Functions.Rosenbrock10D, -2.048, 2.048 )
# runAlgorithms( Functions.Ackley, -32.768, 32.76 )
# runAlgorithms( Functions.Griewank, -600, 600 )
# runAlgorithms( Functions.Weierstrass, -0.5, 0.5 )
# runAlgorithms( Functions.Rastrigin, -5.12, 5.12 )
# runAlgorithms( Functions.NCRastrigin, -5.12, 5.12 )
# runAlgorithms( Functions.Schwefel, -500, 500 )

# b = 10;
# f = lambda x,y: (x-1)**2 + b*(y-x**2)**2;
# # Initialize figure
# figRos = plt.figure(figsize=(12, 7))
# axRos = figRos.gca(projection='3d')
#
# # Evaluate function
# X = np.arange(-10, 10, 0.15)
# Y = np.arange(-10, 10, 0.15)
# X, Y = np.meshgrid(X, Y)
# Z = f(X,Y)
#
# # Plot the surface
# surf = axRos.plot_surface(X, Y, Z, cmap=cm.gist_heat_r,
#                        linewidth=0, antialiased=False)
# axRos.set_zlim(0, 200)
# figRos.colorbar(surf, shrink=0.5, aspect=10)
# plt.show()
