import numpy as np
from Interpolation import Interpolation
from Input import *


t = [1,2,3,4,5]
y = [1,2,3,4,5]

interp = Interpolation(t,y)
s = interp.interpMonomial(t,y)
yfit = interp.evalMonomial(s,10)
print(yfit)

s = interp.interpLagrange(t,y)
yfit = interp.evalLagrange(s,t,10)
print(yfit)

s = interp.interpNewton(t,y)
yfit = interp.evalNewton(s,t,10)
print(yfit)