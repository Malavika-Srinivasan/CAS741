## @file test_regression.py
#  @author Malavika Srinivasan
#  @brief Test cases for Regression module
#  @date 21/12/2018

import numpy as np
from pytest import *
from src.Regression import Regression
from src.Input import Input
ADMISS_REL_ERR = 1e-2



## @brief This method takes care of division by zero
#  @details If denominator is 0, we assue div(a/b) = 0
def div(a, b):
    if b == 0:
        ans = 0
    else:
        ans = a/b
    return ans

## @brief This gives the list of test cases for Regression module.
#  @details Contains list of known solutions and checks if regression module produces the same solution.
#  @param none
#  @exception none
#  @see {Regression.py}
#  @return none

class Test_Regression:

    ## @brief Test case 1 for Normal Equation
    #  @test A simple test case for Normal Equation - TC22
    def test_NormalEquation1(self):

        t = [0,1,2,3,4,5,6,7,8,9,10]
        y = [0,1,2,3,4,5,6,7,8,9,10]
        deg = 1
        reg = Regression(t, y, deg)
        exp_coeff = [0,1]
        act_coeff = reg.regNormalEq(t, y, deg)
        for i in range(0,len(act_coeff)):
            a = exp_coeff[i] - act_coeff[i]
            b = exp_coeff[i]
            assert (div(a,b) <= ADMISS_REL_ERR)

    ## @brief Test case 2 for Normal Equation
    #  @test A simple test case for Normal Equation - TC23
    def test_NormalEquation2(self):

        t = [1,2,3]
        y = [1,3,7]
        deg = 1
        reg = Regression(t, y, deg)
        exp_coeff = [-2.3333,3]
        act_coeff = reg.regNormalEq(t, y, deg)
        for i in range(0,len(act_coeff)):
            a = exp_coeff[i] - act_coeff[i]
            b = exp_coeff[i]
            assert (div(a,b) <= ADMISS_REL_ERR)

    ## @brief Test case 3 for Normal Equation
    #  @test A simple test case for Normal Equation - TC24
    def test_NormalEquation3(self):

        t = t = [0,200,400,600,800]
        y = [0.0010, 0.0015, 0.0021, 0.0051,0.0094]
        deg = 2
        reg = Regression(t, y, deg)
        exp_coeff = [0.00116857142857, -0.00000408571429, 0.00000001785714]
        act_coeff = reg.regNormalEq(t, y, deg)
        for i in range(0,len(act_coeff)):
            a = exp_coeff[i] - act_coeff[i]
            b = exp_coeff[i]
            assert (div(a,b) <= ADMISS_REL_ERR)

    ## @brief Test case 1 for Augmented System
    #  @test A simple test case for Augmented System - TC25
    def test_AugmentedSystem1(self):

        t = [0,1,2,3,4,5,6,7,8,9,10]
        y = [0,1,2,3,4,5,6,7,8,9,10]
        deg = 1
        reg = Regression(t, y, deg)
        exp_coeff = [0,1]
        act_coeff = reg.regAugSys(t, y, deg)
        for i in range(0,len(act_coeff)):
            a = exp_coeff[i] - act_coeff[i]
            b = exp_coeff[i]
            assert (div(a,b) <= ADMISS_REL_ERR)

    ## @brief Test case 2 for Augmented System
    #  @test A simple test case for Augmented System - TC26
    def test_AugmentedSystem2(self):

        t = [1,2,3,4]
        y = [5,3,2,1]
        deg = 1
        reg = Regression(t, y, deg)
        exp_coeff = [6,-1.3]
        act_coeff = reg.regAugSys(t, y, deg)
        print (act_coeff)
        for i in range(0,len(act_coeff)):
            a = exp_coeff[i] - act_coeff[i]
            b = exp_coeff[i]
            assert (div(a,b) <= ADMISS_REL_ERR)

    ## @brief Test case 1 for Orthogonal Transformation
    #  @test A simple test case for Orthogonal Transformation - TC27
    def test_OrthoTrans1(self):
        t = [0,1,2,3,4,5,6,7,8,9,10]
        y = [0,1,2,3,4,5,6,7,8,9,10]
        deg = 1
        reg = Regression(t, y, deg)
        exp_coeff = [0,1,0,0,0,0,0,0,0,0,0]
        act_coeff = reg.regOrthogonalTn(t, y)
        print(act_coeff)
        for i in range(0,len(act_coeff)):
            a = exp_coeff[i] - act_coeff[i]
            b = exp_coeff[i]
            assert (div(a,b) <= ADMISS_REL_ERR)

    ## @brief Test case 2 for Orthogonal Transformation
    #  @test A simple test case for Orthogonal Transformation - TC28
    def test_OrthoTrans2(self):
        t = [1,2,3,4]
        y = [5,3,2,1]
        deg = 3
        reg = Regression(t, y, deg)
        exp_coeff = [9, -5.3333, 1.5, -0.1667]
        act_coeff = reg.regOrthogonalTn(t, y)
        print (act_coeff)
        for i in range(0,len(act_coeff)):
            a = exp_coeff[i] - act_coeff[i]
            b = exp_coeff[i]
            assert (div(a,b) <= ADMISS_REL_ERR)

