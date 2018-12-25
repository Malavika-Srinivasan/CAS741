import numpy as np
from Interpolation import Interpolation
from Regression import Regression
from Input import *
from Output import Output
output = Output()
print('Monomial')
t = [-2,0,1]
y = [-27,-1,0]
t = [1,2,3,4,5,6]
y = [1,2,3,4,5,6]
interp = Interpolation(t,y)
s = interp.interpMonomial(t,y)
print(s)
yfit = interp.evalMonomial(s,t)
output.plotDataFit(t,y,yfit)

print('Lagrange')
s = interp.interpLagrange(t,y)
yfit = interp.evalLagrange(s,t,t)
print(yfit)
output.plotDataFit(t,y,yfit)

print('Newton')
s = interp.interpNewton(t,y)
yfit = interp.evalNewton(s,t,t)
print(s)

print('HermiteCubic')
t = [1,2,4,5]
y = [2,1,4,3]
coeff,interval = interp.interpHermiteCubic(t,y)
yfit = interp.evalHermiteCubic(t, t, y)
print(coeff)

print('BSpline')
t = [0, 1.2, 1.9, 3.2, 4, 6.5]
y = [0, 2.3, 3.0, 4.3,2.9,3.1]
coeff = interp.interpBSpline(t,y)
print(coeff)
yfit = interp.evalBSpline(t, t, y)


#Regression
x = [1,2,3]
y = [1,3,7]
deg = 2
'''
x = [-2,0,1]
y = [-27,-1,0]
deg = 2

x = [0,1,2,3,4,5,6,7,8,9,10]
y = [0,1,2,3,4,5,6,7,8,9,10]
deg = 1
'''
print('Normal equn')
reg = Regression(x,y,deg)
s = reg.regNormalEq(x,y,deg)
yfit = reg.evalReg(s,x)
#print(yfit)
output.coeffPlotScreen(x,y,yfit,s)


print('Aug sys')
reg = Regression(x,y,deg)
s = reg.regAugSys(x,y,deg)
yfit = reg.evalReg(s,[2,3])
print(yfit)


print('QR')
reg = Regression(x,y,deg)
s = reg.regOrthogonalTn(x,y)
yfit = reg.evalReg(s,[2,3])
print(yfit)
output.coeffFile(s)