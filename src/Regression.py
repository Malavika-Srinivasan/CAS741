
import pandas as pd
from Input import *
import numpy as np
class Regression:

    global x, y

    def __init__(self ,t ,y, deg):
        print('I am at Regression init')
        input = Input(t, y)
        input.verifyInput()
        input.verifyDegree(deg)

    def regNormalEq(self,x,y,deg):

        x = np.array(x)
        y = np.array(y)
        SIZE = len(x)
        A = np.zeros([SIZE, deg + 1])
        print(A)
        for k in range(0, deg + 1):
            print(k)
            if k == 0:
                A[:, k] = 1
            else:
                A[:, k] = x ** k
            print(A)
        print(A)
        ATranspose = A.T
        print(ATranspose)
        ATransposeDotA = ATranspose.dot(A)
        print(ATransposeDotA)
        print(y)
        ATranspose_d = ATranspose.dot(y)
        print(ATranspose_d)
        ans = np.linalg.solve(ATransposeDotA, ATranspose_d)
        print(ans)
        return ans

    def regAugSys(self, t, y):
        print('Augmented system')

    def regOrthogonalTn(self,t,y):
        print('Orthogonal Transformation')

    def evalReg(self,s,xnew):
        print('Inside eval Reg')
        s = np.flip(s, axis=0)
        yfit = np.polyval(s,xnew)
        return yfit

