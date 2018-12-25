## @file test_correctness.py
#  @author Malavika Srinivasan
#  @brief Test cases for Correctness, which is a non functional requirement.
#         Most of them are implemented from scratch, so they are compared against python.
#         Some of them use python libraries, for which Matlab is used to verify correctness.
#  @date 22/12/2018


from scipy import interpolate
import numpy as np
from pytest import *
from src.Interpolation import Interpolation
from src.Regression import Regression
from src.Input import Input
ADMISS_REL_ERR = 1e-1

t = [0, 1, 2, 3]
y = [0, 1, 2, 3]
interp = Interpolation(t, y)

## @brief This method takes care of division by zero
#  @details If denominator is 0, we assume div(a/b) = 0
def div(a, b):
    if b == 0:
        ans = 0
    else:
        ans = a/b
    return ans

## @brief This gives the list of test cases for Correctness.
#  @see {test_interpolation.py}
#  @return none

class Test_Correctness:

    ## @brief Test case 1 for Monomial interpolation
    #  @test A simple test case for Monomial interpolation - CFS and Python
    def test_evalMonomial1(self):

        t = [0,1,2]
        y = [0,1,2]
        interp = Interpolation(t, y)
        exp_coeff = interpolate.interp1d(t, y)
        act_coeff = np.flip(interp.interpMonomial(t,y))

        #evaluating python object
        yfit_P = exp_coeff(t)

        #evaluating CFS
        yfit = interp.evalMonomial(np.flip(act_coeff), t)

        for i in range(0,len(yfit_P)):
            a = yfit[i] - yfit_P[i]
            b = yfit[i]
            assert (div(a,b) <= ADMISS_REL_ERR)

    ## @brief Test case 2 for Monomial interpolation
    #  @test A simple test case for Monomial interpolation - CFS and Python

    def test_evalMonomial2(self):

        t = [-2, 0, 1]
        y = [-27, -1, 0]
        interp = Interpolation(t, y)
        exp_coeff = interpolate.interp1d(t, y)
        act_coeff = np.flip(interp.interpMonomial(t, y))

        # evaluating python object
        yfit_P = exp_coeff(t)

        # evaluating CFS
        yfit = interp.evalMonomial(np.flip(act_coeff), t)

        for i in range(0, len(yfit_P)):
            a = yfit[i] - yfit_P[i]
            b = yfit[i]
            assert (div(a, b) <= ADMISS_REL_ERR)

    ## @brief Test case 1 for Lagrange interpolation
    #  @test A simple test case for Lagrange interpolation - CFS and Python

    def test_evalLagrange1(self):

        t = [0, 1, 2]
        y = [0, 1, 2]
        interp = Interpolation(t, y)
        exp_coeff = interpolate.lagrange(t, y)
        act_coeff = np.flip(interp.interpLagrange(t, y))

        # evaluating python object
        yfit_P = exp_coeff(t)

        # evaluating CFS
        yfit = interp.evalLagrange(y, t, t)

        for i in range(0, len(yfit_P)):
            a = yfit[i] - yfit_P[i]
            b = yfit[i]
            assert (div(a, b) <= ADMISS_REL_ERR)


    ## @brief Test case 1 for Lagrange interpolation
    #  @test A simple test case for Lagrange interpolation - CFS and Python

    def test_evalLagrange2(self):

        t = [-2, 0, 1]
        y = [-27, -1, 0]
        interp = Interpolation(t, y)
        exp_coeff = interpolate.lagrange(t, y)
        act_coeff = np.flip(interp.interpLagrange(t, y))

        # evaluating python object
        yfit_P = exp_coeff(t)

        # evaluating CFS
        yfit = interp.evalLagrange(y, t, t)

        for i in range(0, len(yfit_P)):
            a = yfit[i] - yfit_P[i]
            b = yfit[i]
            assert (div(a, b) <= ADMISS_REL_ERR)

    ## @brief Test case 1 for Newton interpolation
    #  @test A simple test case for Newton interpolation - CFS and Matlab
    def test_evalNewton1(self):

        xarr = [0, 1, 2]
        a = [0, 1]
        t = [0,1,2]
        yMatlab = [0,1,2]
        #Tests evaluation of Newton polynomial
        yPython = interp.evalNewton(a, xarr, t)
        # Checking correctness
        for i in range(0, len(yPython)):
            a = yPython[i] - yMatlab[i]
            b = yPython[i]
            assert (div(a, b) <= ADMISS_REL_ERR)

    ## @brief Test case 2 for Newton interpolation
    #  @test A simple test case for Newton interpolation - CFS and Matlab
    def test_evalNewton2(self):
        t = [-2, 0, 1]
        y = [-27, -1, 0]
        interp = Interpolation(t, y)
        #From Matlab
        MatlabC = [-27, 13.0, -4.0]
        #Tests coefficients of Newton Polynomial
        PythonC = interp.interpNewton(t, y)
        for i in range(0, len(PythonC)):
            a = PythonC[i] - MatlabC[i]
            b = PythonC[i]
            assert (div(a, b) <= ADMISS_REL_ERR)

    ## @brief Test case for Hermite cubic interpolation
    #  @test A simple test case for Hermite cubic interpolation - CFS and Matlab
    #  @details This test case fails, but both the answers are correct.
    #           More explanation in test report.
    def test_HermiteCubic(self):

        t =  [1,2,4,5];
        y = [2,1,4,3]
        interp = Interpolation(t, y)
        #This is from Matlab
        exp_coeff = [[ 0.1667, 0.6667, -1.8333, 2.0000],[-0.7500, 2.2500, 0, 1.0000], [0.1667, -1.1667, 0, 4.0000]]
        act_coeff1, act_interval = interp.interpHermiteCubic(t, y)
        # This is done for arranging the coefficients in proper order
        act_coeff = []
        act_coeff.append([])
        act_coeff.append([])
        act_coeff.append([])
        act_coeff[0] = list(np.flip((act_coeff1[:, 0])))
        act_coeff[1] = list(np.flip((act_coeff1[:, 1])))
        act_coeff[2] = list(np.flip((act_coeff1[:, 2])))

        for i in range(0, len(act_coeff)):
            for j in range(0, len(act_coeff[i])):
                a = act_coeff[i][j] - exp_coeff[i][j]
                b = act_coeff[i][j]
                assert (div(a, b) <= ADMISS_REL_ERR)


    def test_Regression(self):

        t = [-2, 0, 1]
        y = [-27, -1, 0]
        deg = 2
        reg = Regression(t, y, deg)
        Python_coeff = np.flip(np.polyfit(t,y,deg))
        CFS_coeff_Normal = reg.regNormalEq(t, y, deg)
        CFS_coeff_AugSys = reg.regAugSys(t, y, deg)
        CFS_coeff_OrTsfn = reg.regOrthogonalTn(t, y)

        # comparing python polynomial coeff and CFS regression using Normal equation
        # CFS and Python
        for i in range(0, len(CFS_coeff_Normal)):
            a = CFS_coeff_Normal[i] - Python_coeff[i]
            b = CFS_coeff_Normal[i]
            assert (div(a, b) <= ADMISS_REL_ERR)

        # comparing python polynomial coeff and CFS regression using Augmented System
        # CFS and Python
        for i in range(0, len(CFS_coeff_AugSys)):
            a = CFS_coeff_AugSys[i] - Python_coeff[i]
            b = CFS_coeff_AugSys[i]
            assert (div(a, b) <= ADMISS_REL_ERR)

        # comparing python polynomial coeff and CFS regression using Orthogonal Transformation
        # CFS and Python
        for i in range(0, len(CFS_coeff_OrTsfn)):
            a = CFS_coeff_OrTsfn[i] - Python_coeff[i]
            b = CFS_coeff_OrTsfn[i]
            assert (div(a, b) <= ADMISS_REL_ERR)


