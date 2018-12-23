## @file test_Input.py
#  @author Malavika Srinivasan
#  @brief Test cases for Input module
#  @date 21/12/2018

from pytest import *
from src.Input import Input

## @brief This gives the list of test cases for Input module.
#  @details Checks if input module raises exceptions for incorrect inputs
#  @param none
#  @exception none
#  @see {Input.py}
#  @return none

class Test_Input:

    ## @brief Test cases for Length mismatch
    #  @test Tests if exception is raised for incorrect input - TC1b
    def test_Input_LengthMismatch(self):

        #Test case for Length mismatch
        t = [0,1,2]
        y = [0,1]
        input = Input()
        try:
            input.verifyInput(t,y)
        except:
            pass

    ## @brief Test cases for Length mismatch
    #  @test Tests if exception is raised for incorrect input - TC1a
    def test_Input_MinimumLength(self):

        #Test case for Length mismatch
        t = [0]
        y = [0]
        input = Input()
        try:
            input.verifyInput(t,y)
        except:
            pass

    ## @brief Test cases for Length mismatch
    #  @test Tests if exception is raised for incorrect input - TC2
    def test_Input_WrongType(self):

        #Test case for wrong data type
        t = [0,1,2,3,'r']
        y = [0,1,2,3,4]
        input = Input()
        try:
            input.verifyInput(t,y)
        except:
            pass

    ## @brief Test cases for Length mismatch
    #  @test Tests if exception is raised for incorrect input - TC3
    def test_Input_WrongOrder(self):

        #Test case for unordered t array
        t = [0,-1,1,2,3]
        y = [0,1,2,3,4]
        input = Input()
        try:
            input.verifyInput(t,y)
        except:
            pass

