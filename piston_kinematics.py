from sympy import *
from numpy import linspace
import matplotlib.pyplot as  plt
from sympy import lambdify
import math as m

# time variable //GLOBAL VARIABLES
t = symbols('t')
# Angular velocity of crank
omega = symbols('omega')
# length of crank
r = symbols('r')
# length of connecting rod
l = symbols('l')

def calculation_formula(t, omega, r, l):
    # Angular position of crank
    theta = omega * t
    
    # sin(phi)
    sPhi = r / l * sin(omega * t)

    # cos(phi)
    cPhi = sqrt(1 - sPhi ** 2)

    # Position of the piston
    x = r * cos(theta) + l * cPhi
    
    # Velocity of the piston
    xdot = diff(x, t)
    
    # Acceleration of the piston
    xddot = diff(xdot, t)
    
    print("------------------------")
    print("The mathematical formula of the kinematic analysis in LATEX form: \n")
    print(f"Formula of the equation of position in LATEX form: {latex(x)}")
    print(f"Formula of the equation of velocity in LATEX form: {latex(xdot)}")
    print(f"Formula of the equation of acceleration in LATEX form: {latex(xddot)}")
    print("------------------------\n")
    
    return [x, xdot, xddot]

## This function generates the kinematic analysis based on inputs related to the engine properties
def kinematics():
    print("\nTo perform the kinematic analysis, please input your engine properties at the exact motor speed (The motor speed increases when accelerating and decreases when decelerating): \n")
    rV = float(input("Please enter the length of the crank (in): "))
    lV = float(input("Please enter length of connecting rod (in): "))
    omegaRpm = float(input("Please enter the angular velocity of the engine (rpm): "))   
    omegaRad = omegaRpm * 2 * m.pi / 60
    vars = {r: rV, l: lV, omega: omegaRad}
    
    result = calculation_formula(t, omega, r, l)
    
    # Position
    x = result[0]
    x = x.subs(vars)
    
    lam_x = lambdify(t, x, modules=['numpy'])
    
    # Velocity
    xdot = result[1]
    xdot = xdot.subs(vars)
    lam_xdot = lambdify(t, xdot, modules=['numpy'])
    
    # Acceleration
    xddot = result[2]
    xddot = xddot.subs(vars)
    lam_xddot = lambdify(t, xddot, modules=['numpy'])
    
    ## Generating kinamatics analysis plot
    ## We plot the x, xdot, and xddot in 2 time periods of rotation in second:
    timePeriod = 60 / (omegaRpm)
    t_vals = linspace(0, timePeriod * 2, 720)
    
    x_vals = lam_x(t_vals)
    xdot_vals = lam_xdot(t_vals)
    xddot_vals = lam_xddot(t_vals)
    
    # Plotting
    figure, axis = plt.subplots(3, figsize = (10, 6))
    figure.suptitle("Kinematic Analysis of Engine")
    
    plt.tight_layout()
    engineInfo = f"Engine Infomation: \nCrank length: {rV} in\nConrod length: {lV} in\nEngine speed: {omegaRpm} rpm"
    plt.gcf().text(0.01, 0.5, engineInfo, fontsize = 10)
    plt.subplots_adjust(left = 0.25)
    
    axis[0].plot(t_vals, x_vals)
    axis[0].set_title("Position Analysis")
    axis[0].set(xlabel = "Time (s)", ylabel = "Position (in)")
    
    axis[1].plot(t_vals, xdot_vals)
    axis[1].set_title("Velocity Analysis")
    axis[1].set(xlabel = "Time (s)", ylabel = "Velocity (in/s)")
    
    axis[2].plot(t_vals, xddot_vals)
    axis[2].set_title("Acceleration Analysis")
    axis[2].set(xlabel = "Time (s)", ylabel = "Acceleration (in/s^2)")
    
    plt.show()

def main():
    calculation_formula(t, omega, r, l)
    kinematics()
    
if __name__ == "__main__":
    main()