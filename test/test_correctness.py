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
#  @details If denominator is 0, we assue div(a/b) = 0
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
    #  @test A simple test case for Monomial interpolation - TC4
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
    #  @test A simple test case for Monomial interpolation - TC4

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

    ## @brief Test case 1 for Monomial interpolation
    #  @test A simple test case for Monomial interpolation - TC4

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


    ## @brief Test case 1 for Monomial interpolation
    #  @test A simple test case for Monomial interpolation - TC4

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
        for i in range(0, len(CFS_coeff_Normal)):
            a = CFS_coeff_Normal[i] - Python_coeff[i]
            b = CFS_coeff_Normal[i]
            assert (div(a, b) <= ADMISS_REL_ERR)

        # comparing python polynomial coeff and CFS regression using Augmented System
        for i in range(0, len(CFS_coeff_AugSys)):
            a = CFS_coeff_AugSys[i] - Python_coeff[i]
            b = CFS_coeff_AugSys[i]
            assert (div(a, b) <= ADMISS_REL_ERR)

        # comparing python polynomial coeff and CFS regression using Orthogonal Transformation
        for i in range(0, len(CFS_coeff_OrTsfn)):
            a = CFS_coeff_OrTsfn[i] - Python_coeff[i]
            b = CFS_coeff_OrTsfn[i]
            assert (div(a, b) <= ADMISS_REL_ERR)


