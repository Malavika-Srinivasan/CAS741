## @file Input.py
#  @author Malavika Srinivasan
#  @brief This module stores the input information
#  @date Dec 6, 2018

import numpy as np
import warnings

class Input:
    def __init__(self):
        return None

    def verifyInput(self,t,y):
        #To verify if len(t) == len(y)
        if (len(t) == len(y)):
            pass
        else:
            raise Exception('Length mismatch, Length of input arrays must be same....')

        #To verify if len(t) > 1
        if (len(t) > 1):
            pass
        else:
            raise Exception('Length mismatch, Please enter atleast two numbers.')

        #To verify if there is an wrong type of data in t array
        for each in t:
            if (type(each)==float or type(each)==int):
                pass
            else:
                raise Exception('Type mismatch, Please enter only numbers')

        # To verify if there is an wrong type of data in t array
        for each in y:
            if (type(each)==float or type(each)==int):
                pass
            else:
                raise Exception('Type mismatch, Please enter only numbers')

        # To verify if t array is ascending
        b = np.array(np.sort(t))
        if np.array_equal(b,t):
            pass
        else:
            raise Exception('x array must be sorted')


    def verifyDegree(self, deg):
        if deg > 0 and type(deg)==int:
            pass
        else:
            raise Exception('Value Error, Degree can only be a natural number')