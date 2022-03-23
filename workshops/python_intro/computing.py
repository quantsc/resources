# import random

# random.seed(10)
# print('Uniform random variable in (0,1)', random.random())
# print(random.random())
# print(random.random())
# print(random.random())

# print('\nUniform RV in (1,5): ', random.uniform(1,5))

#######

import numpy as np
import matplotlib.pyplot as plt

# mean = 1.5
# standard_deviation = 2
# total_samples = 1000

# samples = np.random.normal(mean, standard_deviation, total_samples)
# print('random variables: ', samples, '\n')
# plt.title("100 Normal RVs.")
# plt.xlabel("Variable Value")
# plt.ylabel("Frequency")
# count, bins, ignored = plt.hist(samples, 28, (-4, 10))
# plt.savefig('randomNormalVariables.png')

#######

import math

# print(math.pow(2,0.5) / 2)
# print(np.sin(math.pi/4))
# print(np.sin(math.pi/2))

# x = np.linspace(0,1,20)
# print('linSpace: ', x, '\n')
# print(np.sin(math.pow(math.factorial(1), 2)*x) / math.factorial(1))
# print(np.sin(math.pow(math.factorial(1), 2)*x) / math.factorial(1) + np.sin(math.pow(math.factorial(2), 2)*x) / math.factorial(2))

# def draw_graph(x_start, x_end):
#     # 1000 linearly spaced numbers
#     x = np.linspace(x_start,x_end,1000)

#     y = 0
#     for i in range(1,10):
#         kFact = math.factorial(i)
#         kFactSq = math.pow(kFact, 2)
#         y += np.sin(kFactSq*x) / kFact

#     # setting the axes at the centre
#     fig = plt.figure()
#     ax = fig.add_subplot(1, 1, 1)

#     ax.spines['right'].set_color('none')
#     ax.spines['top'].set_color('none')

#     ax.xaxis.set_ticks_position('bottom')
#     ax.spines['bottom'].set_position(('data',0))

#     ax.yaxis.set_ticks_position('left')
#     ax.spines['left'].set_position(('data',0))

#     ax.title.set_text(f'h(x): a finite Fourier expansion with x in [{x_start},{x_end}]')
#     ax.set_xlabel('x')
#     ax.set_ylabel('h(x)')
#     # plot the function
#     plt.plot(x,y, 'b')

#     # show the plot
#     plt.savefig('sumOfSines.png')

# draw_graph(0,1)

#######

# from scipy import integrate
# # Note: the Cauchy probability density function is of the form 1/((pi*gamma)*(1+((x-x0)^2))/gamma)
# # See cauchyPdf.png for graph
# cauchy = lambda x: 1 / (math.pi * (1 + x**2)) # Cauchy pdf with gamma = 1, x0 = 0
# # Note: integrate.quad uses a fortran integration functionality called quadpack
# print("Theoretical probability of a cauchy random variable being between ±(1.5^.5): ", integrate.quad(cauchy, -math.sqrt(1.5), math.sqrt(1.5))[0])

# #######

from sklearn.linear_model import LinearRegression

# creating data (2 independent variables, 1 dependent variable)
X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
# y = x0 + 2*x1 + 3
y = np.dot(X, np.array([1, 2])) + 3

# creating an actual model
reg = LinearRegression().fit(X, y)

print('\n\n')
print('correlation score: ', reg.score(X, y))
print('regression coefficients: ', reg.coef_)
print('regression intercept: ', reg.intercept_)
print("model's prediction for the value of y(3,5): ", reg.predict(np.array([[3, 5]])))



