## @file test_interpolation.py
#  @author Malavika Srinivasan
#  @brief Test cases for Interpolation module
#  @date 21/12/2018

import numpy as np
from pytest import *
from src.Interpolation import Interpolation
from src.Input import Input
ADMISS_REL_ERR = 1e-2

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

## @brief This gives the list of test cases for Interpolation module.
#  @details Contains list of known solutions and checks if interpolation module produces the same solution.
#  @param none
#  @exception none
#  @see {Interpolation.py}
#  @return none

class Test_Interpolation:

    ## @brief Test case 1 for Monomial interpolation
    #  @test A simple test case for Monomial interpolation - TC4
    def test_Monomial1(self):

        t = [0,1,2]
        y = [0,1,2]
        interp = Interpolation(t, y)
        exp_coeff = [0,1,0]
        act_coeff = np.flip(interp.interpMonomial(t,y))
        for i in range(0,len(act_coeff)):
            a = exp_coeff[i] - act_coeff[i]
            b = exp_coeff[i]
            assert (div(a,b) <= ADMISS_REL_ERR)

    ## @brief Test case 2 for Monomial interpolation
    #  @test A simple test case for Monomial interpolation - TC5
    def test_Monomial2(self):
        t = [-2, 0, 1]
        y = [-27, -1, 0]
        interp = Interpolation(t, y)
        exp_coeff = [-1, 5, -4]
        act_coeff = np.flip(interp.interpMonomial(t, y))
        print(act_coeff)
        for i in range(0, len(act_coeff)):
            a = exp_coeff[i] - act_coeff[i]
            b = exp_coeff[i]
            assert (div(a, b) <= ADMISS_REL_ERR)

    ## @brief Test case 1 for Lagrange interpolation
    #  @test A simple test case for Lagrange interpolation - TC6
    def test_Lagrange1(self):

        t = [0,1,2]
        y = [0,1,2]
        interp = Interpolation(t, y)
        exp_coeff = [0,1,2]
        act_coeff = interp.interpLagrange(t,y)
        for i in range(0,len(act_coeff)):
            a = exp_coeff[i] - act_coeff[i]
            b = exp_coeff[i]
            assert (div(a,b) <= ADMISS_REL_ERR)


    ## @brief Test case 2 for Lagrange interpolation
    #  @test A simple test case for Lagrange interpolation - TC7
    def test_Lagrange2(self):
        t = [-2, 0, 1]
        y = [-27, -1, 0]
        interp = Interpolation(t, y)
        exp_coeff = [-27, -1, 0]
        act_coeff = interp.interpLagrange(t, y)
        print(act_coeff)
        for i in range(0, len(act_coeff)):
            a = exp_coeff[i] - act_coeff[i]
            b = exp_coeff[i]
            assert (div(a, b) <= ADMISS_REL_ERR)

    ## @brief Test case 1 for Newton interpolation
    #  @test A simple test case for Newton interpolation - TC8
    def test_Newton1(self):
        t = [0,1,2]
        y = [0,1,2]
        interp = Interpolation(t, y)
        exp_coeff = [0,1,0]
        act_coeff = interp.interpNewton(t,y)
        for i in range(0,len(act_coeff)):
            a = exp_coeff[i] - act_coeff[i]
            b = exp_coeff[i]
            assert (div(a,b) <= ADMISS_REL_ERR)


    ## @brief Test case 2 for Newton interpolation
    #  @test A simple test case for Newton interpolation - TC9
    def test_Newton2(self):
        t = [-2, 0, 1]
        y = [-27, -1, 0]
        interp = Interpolation(t, y)
        exp_coeff = [-1, 5, -4]
        act_coeff = interp.interpNewton(t, y)
        print(act_coeff)
        for i in range(0, len(act_coeff)):
            a = exp_coeff[i] - act_coeff[i]
            b = exp_coeff[i]
            assert (div(a, b) <= ADMISS_REL_ERR)

    ## @brief Test case 1 for Hermite Cubic interpolation
    #  @test A simple test case for Hermite Cubic interpolation - TC10
    def test_HermiteCubic1(self):
        t = [1,3]
        y = [2,1]
        interp = Interpolation(t, y)
        exp_coeff = [2, 1.67, 1.33, 1.0]
        exp_interval = [1,3]
        act_coeff,act_interval = interp.interpHermiteCubic(t, y)
        #Checking the coefficients
        for i in range(0, len(act_coeff.c)):
            a = exp_coeff[i] - act_coeff.c[i]
            b = exp_coeff[i]
            assert (div(a, b) <= ADMISS_REL_ERR)
        #Checking interval information
        for i in range(0, len(act_interval)):
            a = exp_interval[i] - act_interval[i]
            b = exp_interval[i]
            assert (div(a, b) <= ADMISS_REL_ERR)

   ## @brief Test case 2 for Hermite Cubic interpolation
    #  @test A simple test case for Hermite Cubic interpolation - TC11
    def test_HermiteCubic2(self):
        t = [1,2,4,5]
        y = [2,1,4,3]
        interp = Interpolation(t, y)
        exp_coeff = [ [1.0,1.0, 1.38888889, 2.0], [4.0, 4.0, 1.0, 1.0], [3.0, 3.61111111, 4.0, 4.0]]
        exp_interval = [1,2,4,5]
        act_coeff1,act_interval = interp.interpHermiteCubic(t, y)
        #This is done for arranging the coefficients in proper order
        act_coeff = []
        act_coeff.append([])
        act_coeff.append([])
        act_coeff.append([])
        act_coeff[0] = list(np.flip((act_coeff1.c[:, 0])))
        act_coeff[1] = list(np.flip((act_coeff1.c[:, 1])))
        act_coeff[2] = list(np.flip((act_coeff1.c[:, 2])))
        #Checking coefficients
        for i in range(0, len(act_coeff)):
            for j in range(0,len(act_coeff[i])):
                a = exp_coeff[i][j] - act_coeff[i][j]
                b = exp_coeff[i][j]
                assert (div(a, b) <= ADMISS_REL_ERR)
        #checking interval
        for i in range(0, len(act_interval)):
            a = exp_interval[i] - act_interval[i]
            b = exp_interval[i]
            assert (div(a, b) <= ADMISS_REL_ERR)

    ## @brief Test case 1 for BSpline interpolation
    #  @test A simple test case for BSpline interpolation - TC12
    def test_BSpline(self):
        t = [0.0, 1.2, 1.9, 3.2, 4.0, 6.5]
        y = [0.0, 2.3, 3.0, 4.3, 2.9, 3.1]
        exp_coeff = [0, 2.987, -0.574, 14.670,-10.325, 3.1, 0, 0, 0, 0, 0]
        interp = Interpolation(t, y)
        splObj,act_coeff = interp.interpBSpline(t, y)
        #Checking the coefficients
        for i in range(0, len(act_coeff)):
            a = exp_coeff[i] - act_coeff[i]
            b = exp_coeff[i]
            assert (div(a, b) <= ADMISS_REL_ERR)

    ## @brief Test case 1 for evalMonomial
    #  @test A simple test case for checking evalMonomial - TC13
    def test_evalMonomial1(self):
        coeff = [0,1]
        t = [2]
        y = [2]
        yfit = interp.evalMonomial(np.flip(coeff), t)
        # Checking the fit
        for i in range(0, len(yfit)):
            a = y[i] - yfit[i]
            b = y[i]
            assert (div(a, b) <= ADMISS_REL_ERR)

    ## @brief Test case 2 for evalMonomial
    #  @test A simple test case for checking evalMonomial - TC14
    def test_evalMonomial2(self):
        coeff = [-1,5,-4]
        t = [-2]
        y = [-27]
        yfit = interp.evalMonomial(np.flip(coeff), t)
        # Checking the fit
        for i in range(0, len(yfit)):
            a = y[i] - yfit[i]
            b = y[i]
            assert (div(a, b) <= ADMISS_REL_ERR)

    ## @brief Test case 1 for evalLagrange
    #  @test A simple test case for checking evalLagrange - TC15
    def test_evalLagrange1(self):
        xarr = [0,1,2]
        yarr = [0,1,2]
        t = [2]
        y = [2]
        yfit = interp.evalLagrange(yarr, xarr , t)
        # Checking the fit
        for i in range(0, len(yfit)):
            a = y[i] - yfit[i]
            b = y[i]
            assert (div(a, b) <= ADMISS_REL_ERR)

    ## @brief Test case 2 for evalLagrange
    #  @test A simple test case for checking evalLagrange - TC16
    def test_evalLagrange2(self):
        xarr = [-2, 0, 1]
        yarr = [-27, -1, 0]
        t = [-2]
        y = [-27]
        yfit = interp.evalLagrange(yarr, xarr , t)
        # Checking the fit
        for i in range(0, len(yfit)):
            a = y[i] - yfit[i]
            b = y[i]
            assert (div(a, b) <= ADMISS_REL_ERR)

    ## @brief Test case 1 for evalNewton
    #  @test A simple test case for checking evalNewton - TC17
    def test_evalNewton1(self):
        xarr = [0,1,2]
        a = [0,1]
        t = [2]
        y = [2]
        yfit = interp.evalNewton(a, xarr , t)
        # Checking the fit
        for i in range(0, len(yfit)):
            a = y[i] - yfit[i]
            b = y[i]
            assert (div(a, b) <= ADMISS_REL_ERR)

    ## @brief Test case 2 for evalNewton
    #  @test A simple test case for checking evalNewton - TC18
    def test_evalNewton2(self):
        xarr = [-2, 0, 1]
        a = [-27, 13.0, -4.0]
        t = [-2]
        y = [-27]
        yfit = interp.evalNewton(a, xarr , t)
        # Checking the fit
        for i in range(0, len(yfit)):
            a = y[i] - yfit[i]
            b = y[i]
            assert (div(a, b) <= ADMISS_REL_ERR)

    ## @brief Test case 1 for evalHermiteCubic
    #  @test A simple test case for checking evalHermiteCubic - TC19
    def test_evalHermiteCubic1(self):
        xarr = [1,3]
        yarr = [2,1]
        y = [2,1]
        xnew = [1, 3]
        h,v = interp.interpHermiteCubic(xarr,yarr)
        yfit = interp.evalHermiteCubic(xnew,h)
        # Checking the fit
        for i in range(0, len(yfit)):
            a = y[i] - yfit[i]
            b = y[i]
            assert (div(a, b) <= ADMISS_REL_ERR)

    ## @brief Test case 2 for evalHermiteCubic
    #  @test A simple test case for checking evalHermiteCubic - TC20
    def test_evalHermiteCubic2(self):
        xarr = [1, 2, 4, 5]
        yarr = [2, 1, 4, 3]
        xnew = [1,2,4,5]
        y = [2,1,4,3]
        h, v = interp.interpHermiteCubic(xarr, yarr)
        yfit = interp.evalHermiteCubic(xnew, h)
        # Checking the fit
        for i in range(0, len(yfit)):
            a = y[i] - yfit[i]
            b = y[i]
            assert (div(a, b) <= ADMISS_REL_ERR)

   ## @brief Test case 1 for evalHermiteCubic
    #  @test A simple test case for checking evalHermiteCubic - TC21
    def test_evalBSpline(self):
        t = [0.0, 1.2, 1.9, 3.2, 4.0, 6.5]
        y = [0.0, 2.3, 3.0, 4.3, 2.9, 3.1]
        xnew = [0.0, 1.2, 1.9, 3.2, 4.0, 6.5]
        splObj, act_coeff = interp.interpBSpline(t, y)
        yfit = interp.evalBSpline(splObj, xnew)
        # Checking the fit
        for i in range(0, len(yfit)):
            a = y[i] - yfit[i]
            b = y[i]
            assert (div(a, b) <= ADMISS_REL_ERR)

