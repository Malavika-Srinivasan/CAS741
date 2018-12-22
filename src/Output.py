## @file Output.py
#  @author Malavika Srinivasan
#  @brief This module handles the variabilities in the output
#  @date Dec 18, 2018

import warnings

class Output(object):

    def __init__(self):
        return (None)


    def plotDataFit(self, t,y,yfit):
        #This will plot the raw data and the fit
        import matplotlib.pyplot as plt
        plt.plot(t,y,'b.',label = 'Raw data')
        plt.plot(t,yfit,'r-', label = 'Fit')
        plt.title('Data vs Fit plot')
        plt.legend()
        plt.show()


    def coeffPlotScreen(self,t,y,yfit,s):
        # This will print the coeff to the screen and plot the raw data, fit
        print('The coefficients are in ascending orders of powers of x, starting from 0')
        print(s)
        import matplotlib.pyplot as plt
        plt.plot(t, y, 'b.', label='Raw data')
        plt.plot(t, yfit, 'r-', label='Fit')
        plt.title('Data vs Fit plot')
        plt.legend()
        plt.show()


    def coeffFile(self,s):
        # This will write the coeff to a file
        with open('result.txt', 'w') as f:
            f.write("The coefficients in increasing powers of t starting from 0\n")
            for item in s:
                f.write("%f\n" % item)
        f.close()

