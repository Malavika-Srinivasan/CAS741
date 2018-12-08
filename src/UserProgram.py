import numpy as np
from Interpolation import Interpolation
from Regression import Regression
from Input import *


#t = [1,2,3,4,5]
#y = [1,2,3,4,5]
t = [-2,0,1]
y = [-27,-1,0]
interp = Interpolation(t,y)
s = interp.interpMonomial(t,y)
yfit = interp.evalMonomial(s,[5,10])
print(yfit)

s = interp.interpLagrange(t,y)
yfit = interp.evalLagrange(s,t,[5,10])
print(yfit)

s = interp.interpNewton(t,y)
yfit = interp.evalNewton(s,t,[5,10])
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

x = [0,1,2,3,4,5,6,7,8,9,10]
y = [0,1,2,3,4,5,6,7,8,9,10]
deg = 1

x = [1,2,3]
y = [1,3,7]
deg = 1

x = [-2,0,1]
y = [-27,-1,0]
deg = 2

reg = Regression(x,y,deg)
s = reg.regNormalEq(x,y,deg)
yfit = reg.evalReg(s,[-2,0])
print(yfit)

reg = Regression(x,y,deg)
s = reg.regAugSys(x,y,deg)
yfit = reg.evalReg(s,[-2,0])
print(yfit)
