from Input import *
import numpy as np

class Interpolation:
    global x, y

    def __init__(self,t,y):
        print('I am at Interpolation init')
        input = Input(t, y)
        input.verifyInput()




    def interpMonomial(self, x, y):
        x = np.array(x)
        y = np.array(y)
        print('I am at Monomial')
        SIZE = len(x)
        # Initializing matrix with zeros
        A = np.zeros([SIZE, SIZE])

        # Providing values for matrix A to convert it to Ax = b form
        for i in range(SIZE):
            A[::, i] = np.power(x.T, i)  # [Doing 1 t t2...]
        b = y  # Initializing b = y

        # Solve Ax=b using python solver - Need to ask if solver has to be implemented.
        s = np.linalg.solve(A, b)
        # x = coeffs of polynomial starting from constant
        # Flip polynomial coeffs - Doing this so that I can see the polynomial if is right or wrong
        s = np.flip(s, axis=0)
        print('-----------------------------------------------')
        print('Monomial Coefficients')
        print(np.poly1d(s))
        return s

    def evalMonomial(self, s, xnew):
        yfit = np.polyval(s, xnew)
        return yfit

    def interpLagrange(self, x, y):

        x = np.array(x)
        y = np.array(y)

        SIZE = len(x)
        # Initializing matrix with zeros
        A = np.zeros([SIZE, SIZE])

        # Creating unit matrix for Lagrange
        A = np.identity(SIZE)

        b = y  # Initializing b = y

        # Solve Ax=b using python solver - Need to ask if solver has to be implemented.
        s = np.linalg.solve(A, b)
        # numpy.linalg.inv()
        # Print polynomial coeffs
        # print (s)
        print('-----------------------------------------------')
        print('Lagrange Coefficients')
        print(np.poly1d(s)) #To check working - Can be removed later.
        return (s)

    # Evaluate polynomial at given xarray
    def evalLagrange(self, s, x, xnew):
        # This basically deals with computing the basis function for lagrange
        yfit = []
        sum = 0
        if type(xnew==int):
            xnew = [xnew]
        for k in range(0, len(xnew)):
            sum = 0
            each = xnew[k]
            for i in range(1, len(x)):
                u = 1
                l = 1
                for j in range(1, len(x)):
                    if j != i:
                        u = u * (each - x[j])
                        l = l * (x[i] - x[j])
                sum = sum + u / l * s[i]
            yfit.append(sum)
        return yfit

    def interpNewton(self, x, y):

        x = np.array(x)
        y = np.array(y)
        SIZE = len(x)
        # Initializing matrix with zeros
        A = np.ones([SIZE, SIZE])
        for i in range(0, len(x)):
            for j in range(0, len(x)):
                # print (j)
                if (j == 0):
                    A[i, j] = 1
                else:
                    p = []
                    for k in range(0, j):
                        p.append(x[i] - x[k])

                    A[i][j] = np.prod(p)
            # print ('A[%d,%d] = %f' %(i,j,A[i][j]))
        # print ('*******************')

        # print (A)

        b = y  # Initializing b = y
        # Solve Ax=b using python solver - Need to ask if solver has to be implemented.
        s = np.linalg.solve(A, b)
        # Making the coefficients < 1e-5 as zero for the betterment of readability. Otherwise it will give very small values in the coefficients which will be the length of data
        for i in range(0, len(s)):
            if s[i] < 1e-5:
                s[i] = 0

        print('-----------------------------------------------')
        print('Newton Coefficients')
        print(np.poly1d(s))
        return s

    # **********************************************

    def evalNewton(self, s, x, xnew, ):

        n = len(x) - 1  # Degree of polynomial
        p = s[n]
        for k in range(1, n + 1):
            p = s[n - k] + (xnew - x[n - k]) * p
        return p
