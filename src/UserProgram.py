import numpy as np
from Interpolation import Interpolation
from Regression import Regression
from Input import *
from Output import Output
output = Output()

t = [-2,0,1]
y = [-27,-1,0]
interp = Interpolation(t,y)
s = interp.interpMonomial(t,y)
yfit = interp.evalMonomial(s,t)
print(yfit)
output.plotDataFit(t,y,yfit)


s = interp.interpLagrange(t,y)
yfit = interp.evalLagrange(s,t,t)
print(yfit)
output.plotDataFit(t,y,yfit)


s = interp.interpNewton(t,y)
yfit = interp.evalNewton(s,t,t)
print(yfit)

t = [1,2,4,5]
y = [2,1,4,3]
hCubObj = interp.interpHermiteCubic(t,y)
print(hCubObj.c)
yfit = interp.evalHermiteCubic(hCubObj,1)
print(yfit)

t = [0, 1.2, 1.9, 3.2, 4, 6.5]
y = [0, 2.3, 3.0, 4.3,2.9,3.1]

splObj = interp.interpBSpline(t,y)
print(splObj.c)
yfit = interp.evalBSpline(splObj,10)
print(yfit)

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
s = reg.regOrthogonalTn(x,y,deg)
yfit = reg.evalReg(s,[2,3])
print(yfit)
output.coeffFile(s)