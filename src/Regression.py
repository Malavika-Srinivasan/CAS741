## @file Regression.py
#  @author Malavika Srinivasan
#  @brief This module handles the variailities in regression
#  @date Dec 21, 2018


from src.Input import Input
import numpy as np
from scipy.linalg import lu
from numpy.linalg import inv
from numpy.linalg import qr

def div(a, b):
    if b == 0:
        ans = 0
    else:
        ans = a/b
    return ans

class Regression:

    def __init__(self, t, y, deg):
        input = Input()
        input.verifyInput(t,y)
        input.verifyDegree(deg)

    def regNormalEq(self, t, y, deg):
        x = np.array(t)
        y = np.array(y)
        SIZE = len(x)

        #Constructing A for normal equation
        A = np.zeros([SIZE, deg + 1])
        for k in range(0, deg + 1):
            if k == 0:
                A[:, k] = 1
            else:
                A[:, k] = x ** k
        c = A.T
        d = c.dot(A)
        e = c.dot(y)
        ans = np.linalg.solve(d, e)
        return ans


    def regAugSys(self, t, y, deg):
        x = np.array(t)
        y = np.array(y)
        SIZE = len(x)
        A = np.zeros([SIZE, deg + 2])
        for k in range(0, deg + 1):
            if k == 0:
                A[:, k] = 1
            if k == 1:
                A[:, k] = x ** 1
            else:
                A[:, k] = x ** k
        A[:, deg + 1] = y
        P, L, U = lu(A)
        l = len(U)
        B = U[0:deg + 1, 0:deg + 1]
        b = U[0:deg + 1, deg + 1]
        s = np.linalg.lstsq(B, b, rcond=None)[0]
        return (s)

    def regOrthogonalTn(self, t, y):
        x = np.array(t)
        y = np.array(y)
        SIZE = len(x)
        # Initializing matrix with zeros for defining matrix size
        A = np.zeros([SIZE, SIZE])
        # Providing values for matrix A to convert it to Ax = b form
        for i in range(SIZE):
            A[::, i] = np.power(x.T, i)  # [Doing 1 t t2...]
        b = y  # Initializing b = y
        # QR decomposition
        Q, R = qr(A)
        b = np.dot(Q.T, y)
        s = np.dot(inv(R), b)
        return (s)

    def evalReg(self, s, xnew):
        s = np.flip(s, axis=0)
        yfit = np.polyval(s, xnew)
        return yfit







