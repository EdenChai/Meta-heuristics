# import pip
#
# package_names=['mealpy'] #packages to install
# pip.main(['install'] + package_names + ['--upgrade'])
# # --upgrade to install or update existing packages
#################################################################
# Imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
from mpl_toolkits.mplot3d import Axes3D
from sklearn import preprocessing

# # Data
# x = np.linspace(-10, 10, 20)
# y = np.linspace(-10, 10, 20)
# X, Y = np.meshgrid(x,y)
#
# # Multivariate Normal
# mu_x = np.mean(x)
# sigma_x = np.std(x)
# mu_y = np.mean(y)
# sigma_y = np.std(y)
#
#
# rv = multivariate_normal([mu_x, mu_y], [[sigma_x, 0], [0, sigma_y]])
#
# normalized = preprocessing.normalize(rv.pdf)
# # Probability Density
# pos = np.empty(X.shape + (2,))
# pos[:, :, 0] = X
# pos[:, :, 1] = Y
# pd = rv.pdf(pos)
#
# # Plot
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# ax.plot_surface(X, Y, pd, cmap='viridis', linewidth=0)
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Probability Density')
# plt.title("Multivariate Normal Distribution")
# plt.show()
#####################################################################################
from opfunu.cec_basic.cec2014_nobias import *
from opfunu.cec_basic.cec2014_nobias import *
from mealpy.math_based.HC import OriginalHC, BaseHC
from mealpy.swarm_based.GWO import BaseGWO, RW_GWO
import Functions
###############################################
#TODO ARIE

# Setting parameters
# obj_func = F5       # This objective function come from "opfunu" library. You can design your own objective function like above
# verbose = False     # Print out the training results
# epoch = 500         # Number of iterations / generations / epochs
# pop_size = 50       # Populations size (Number of individuals / Number of solutions)
obj_func = Functions.RosenbrockSimple
verbose = False
epoch = 10
pop_size = 100

problemSize = 2
lb2 = -10
ub2 = 10
#Remember the keyword "problem_size"
# md2 = BaseHC(obj_func, lb2, ub2, verbose, epoch, pop_size,problem_size=problemSize)
# best_pos1, best_fit1, list_loss1 = md2.train()
# print(md2.solution[1])

md2 = BaseGWO(obj_func, lb2, ub2, verbose, epoch, pop_size, problem_size=problemSize)
best_pos1, best_fit21, list_loss1 = md2.train()
print(md2.solution[1])