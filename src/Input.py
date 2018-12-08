## @file Input.py
#  @author Malavika Srinivasan
#  @brief This module stores the input information
#  @date Dec 6, 2018

import numpy as np
import warnings

class Input(object):
    global t,y
    def __init__(self, t, y):
        print('I am at Input init')
        self.t = t
        self.y = y

    def verifyInput(self):
        #To verify if len(t) == len(y)
        if (len(self.t) == len(self.y)):
            pass
        else:
            raise Exception('Length mismatch, len of input arrays must be same.')

        #To verify if len(t) > 1
        if (len(self.t) > 1):
            pass
        else:
            raise Exception('Length mismatch, Please enter atleast two numbers.')

        #To verify if there is an wrong type of data in t array
        for each in self.t:
            if (type(each)==float or type(each)==int):
                pass
            else:
                raise Exception('Type mismatch, Please enter only numbers')
        # To verify if there is an wrong type of data in t array
        for each in self.y:
            if (type(each)==float or type(each)==int):
                pass
            else:
                raise Exception('Type mismatch, Please enter only numbers')

    def verifyDegree(self, deg):
        if deg > 0 and type(deg)==int:
            pass
        else:
            raise Exception('Value Error, Degree can only be a natural number')