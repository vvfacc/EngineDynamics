from kin import *

# a, b: coefficient in gas pressure function
init_printing(pretty_print=True)
a = symbols('a')
b = symbols('b')
c = symbols('c')
d = symbols('d')

# Bore of cylinder
Bo = symbols('B')


Pg = a + b * exp(-(theta - c) / d)
# Gas pressure funtion
#print(latex(Pg))

# Force of gas pressure
Fg = -pi/4 * Pg * (Bo ** 2) 
print(latex(Fg))