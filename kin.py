from sympy import *

## Write result to an output file
## Python calculation based on diagram

#time
t = symbols('t')
# Angular velocity of crank
omega = symbols('\omega')
# radius of crank
r = symbols('r')
# length of conrod
l = symbols('l')

# Angular position of crank
theta = omega * t

# sin(phi)
sPhi = r / l * sin(omega * t)

# cos(phi)
cPhi = sqrt(1 - sPhi ** 2)

# Position of the slider (piston)
x = r * cos(theta) + l * cPhi

# Velocity of the slider
xdot = diff(x, t)
#print(latex(xdot))

# acceleration
xddot = diff(xdot, t)
#print(latex(xddot))