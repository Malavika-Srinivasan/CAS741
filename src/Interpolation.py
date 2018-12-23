## @file Interpolation.py
#  @author Malavika Srinivasan
#  @brief This module handles the variailities in interpolation
#  @date Dec 21, 2018
from src.Input import Input
import numpy as np
from scipy.interpolate import *
class Interpolation:

    def __init__(self, t, y):
        input = Input()
        input.verifyInput(t,y)

    def interpMonomial(self, x, y):
        x = np.array(x)
        y = np.array(y)
        SIZE = len(x)

        # Initializing matrix with zeros
        A = np.zeros([SIZE, SIZE])

        # Providing values for matrix A to convert it to Ax = b form
        for i in range(SIZE):
            A[::, i] = np.power(x.T, i)  # [Doing 1 t t2...]

        b = y  # Initializing b = y

        # Solve Ax=b using python solver - Need to ask if solver has to be implemented.
        s = np.linalg.solve(A, b)

        # x = coeffs of polynomial starting from constant
        # Flip polynomial coeffs - Doing this so that I can see the polynomial if is right or wrong
        s = np.flip(s, axis=0)
        return s

    def evalMonomial(self, s, xnew):
        yfit = np.polyval(s, xnew)
        return yfit

    def interpLagrange(self, x, y):
        x = np.array(x)
        y = np.array(y)
        SIZE = len(x)

        # Initializing matrix with zeros
        A = np.zeros([SIZE, SIZE])

        # Creating unit matrix for Lagrange
        A = np.identity(SIZE)

        b = y  # Initializing b = y

        # Solve Ax=b using python solver - Need to ask if solver has to be implemented.
        s = np.linalg.solve(A, b)
        return (s)

    def evalLagrange(self, s, x, xnew):
        # This basically deals with computing the basis function for lagrange
        yfit = []
        sum = 0
        if type(x==list):
            x = np.array(x)
        if type(xnew)==list :
            xnew = np.array(xnew)
        if  type(xnew)==int or type(xnew) == float:
            xnew = np.array([xnew])
        for each in xnew:
            Lx = x
            Ly = s
            y = 0
            for k in range(len(Lx)):
                t = 1
                for j in range(len(Lx)):
                    if j != k:
                        t = t * ((each - Lx[j]) / (Lx[k] - Lx[j]))
                y += t * Ly[k]
            yfit.append(y)
        return yfit

    def interpNewton(self, x, y):
        a = []
        x = np.array(x)
        y = np.array(y)
        SIZE = len(x)

        for i in range(SIZE):
            a.append(y[i])

        for j in range(1, SIZE):
            for i in range(SIZE - 1, j - 1, -1):
                a[i] = float(a[i] - a[i - 1]) / float(x[i] - x[i - j])
        print(a)
        return a

    def evalNewton(self, a, x, xnew):
        yfit = []
        if type(x==list):
            x = np.array(x)
        if type(xnew)==list :
            xnew = np.array(xnew)
        if  type(xnew)==int or type(xnew) == float:
            xnew = np.array([xnew])
        for each in xnew:
            n = len(a) - 1
            temp = a[n]
            for i in range(n - 1, -1, -1):
                temp = temp * (each - x[i]) + a[i]
            yfit.append(temp)
        return yfit

    def interpHermiteCubic(self, x, y):
        x = np.array(x)
        y = np.array(y)
        hCubObj = PchipInterpolator(x, y)
        return (hCubObj,x)

    def evalHermiteCubic(self,xnew,h):
        if type(xnew)==list :
            xnew = np.array(xnew)
        if  type(xnew)==int or type(xnew) == float:
            xnew = np.array([xnew])
        yfit = h(xnew)
        return yfit


    def interpBSpline(self, x, y):
        x = np.array(x)
        y = np.array(y)
        tck = splrep(x,y,s=0,k=4)
        splObj = BSpline(tck[0],tck[1],tck[2], extrapolate=False)
        return (splObj,tck[1])

    def evalBSpline(self, splObj,xnew):
        if type(xnew)==list :
            xnew = np.array(xnew)
        if  type(xnew)==int or type(xnew) == float:
            xnew = np.array([xnew])
        yfit = splev(xnew,splObj)
        return yfit