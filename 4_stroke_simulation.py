"""
Project: 4-Stroke Cycle Simulation and Animation
Section: ME 369P
Team: U20
Members:
    Bhargav Parthasarathy
    Christian Lewandowski
    Nicholas Hackworth
    Van Vo
"""
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# geometric input parameters
d_p = 0.05 # piston diameter (m)
s = 0.003 # height above TDC (m)
m_c = 1 # crank mass (kg)
l_c = 0.05 # crank length (m)
m_cs = 20 # crankshaft mass (kg)
r_cs = 0.01 # crankshaft radius (m)
l_co = 0.1 # connecting rod length (m) - relevant for animation
h_p = 0.03 # piston height (m) - relevant for animation
plot_cl = 0.01 # minimum clearance between piston assembly and plot edges - relevant for animation

# geometric calculated parameters
A_p = np.pi*(d_p/2)**2 # piston cross-sectional area (m^2)
I_c = 4/3*m_c*l_c**2 # crank MOI about crankshaft axis (kg*m^2)
I_cs = 1/2*m_cs*r_cs**2 # crankshaft MOI (kg*m^2)

# thermodynamic input parameters
P_atm = 101325 # atmospheric pressure (Pa)
T_atm = 298.15 # atmospheric temperature (K)
Cp_AF = 1005 # specific heat of constant pressure, for air-fuel mixture (J/kg*K)
Cv_AF = 718 # specific heat of constant volume, for air-fuel mixture (J/kg*K)
R = 8.3145 # molar gas constant (J/(mol*K))
AFR = 14.7 # ideal stoichiometric ratio of air to fuel
M_F = 0.1 # molar mass of fuel (kg/mol) - using gasoline
Hc_F = 47000000 # heat of combustion of fuel (J/kg) - using gasoline
M_A = 0.029 # molar mass of air (kg/mol)

# thermodynamic calculated parameters
n_AF = P_atm*A_p*(s+2*l_c)/(R*T_atm) # amount of air-fuel mixture (mol)
m_F = 1/(AFR+1)*n_AF*M_F # mass of fuel in air-fuel mixture (kg)
m_A = AFR/(AFR+1)*n_AF*M_A # mass of air in air-fuel mixture (kg)
q_cb = m_F*Hc_F # fuel combustion energy (J)
P_c_f = P_atm*((s+2*l_c)/s)**(Cp_AF/Cv_AF) # final compression pressure (Pa)
T_c_f = T_atm*P_c_f/P_atm*(s/(s+2*l_c)) # final compression temperature (K)
T_cb_f = q_cb/((m_F+m_A)*Cv_AF)+T_c_f # final combustion temperature (K)
P_cb_f = P_c_f*T_cb_f/T_c_f # final combustion pressure (Pa)

# initial conditions
theta_cs = 0 # crankshaft angle corresponding to TDC (rad)
w_cs = 2 # crankshaft angular velocity (rad/s)

# simulation parameters
theta_cs_limit = 8*np.pi # crankshaft angle iteration limit
ts = 0.0001 # time step (s)
t = 0 # total time (s)
theta_cs_list = [theta_cs] # crankshaft angle list
t_list = [t] # total time list
T_cs_list = [0] # crankshaft torque list
w_cs_list = [w_cs] # crankshaft angular velocity list
a_cs_list = [0] # crankshaft angular acceleration list
F_c_list = [0] # compression force list
F_p_list = [0] # power stroke force list

# simulation loop
while theta_cs < theta_cs_limit:
    if (theta_cs%(2*np.pi)) < np.pi: # theta_cs from 0-pi
        F_c = A_p*P_atm*((s+2*l_c)/(s+l_c+l_c*np.cos(theta_cs)))**(Cp_AF/Cv_AF) # compression force; increases from 0-pi (N)
        F_p = A_p*P_cb_f*(s/(s+l_c-l_c*np.cos(theta_cs)))**(Cp_AF/Cv_AF) # power stroke force; decreases from 0-pi (N)
    elif (theta_cs%(2*np.pi)) >= np.pi: # theta_cs from pi-2pi
        F_c = A_p*P_atm*((s+2*l_c)/(s+l_c-l_c*np.cos(theta_cs)))**(Cp_AF/Cv_AF) # compression force; increases from pi-2pi (N)
        F_p = A_p*P_cb_f*(s/(s+l_c+l_c*np.cos(theta_cs)))**(Cp_AF/Cv_AF) # power stroke force; decreases from pi-2pi (N)
    T_cs = (F_p-F_c)*l_c*abs(np.sin(theta_cs)) # crankshaft torque (Nm)
    I_d = 0 # dynamic piston assembly MOI about crankshaft axis (kg*m^2) - not yet calculated
    I = I_c+I_cs+I_d # total piston assembly MOI about crankshaft axis (kg*m^2)
    a_cs = T_cs/I # crankshaft angular accleration (rad/s^2)
    w_cs += a_cs*ts
    theta_cs += w_cs*ts+1/2*a_cs*ts**2
    t += ts
    theta_cs_list.append(theta_cs)
    t_list.append(t)
    T_cs_list.append(T_cs)
    w_cs_list.append(w_cs)
    a_cs_list.append(a_cs)
    F_c_list.append(F_c)
    F_p_list.append(F_p)

# plots
theta_range = np.arange(0, theta_cs_limit+np.pi, np.pi)
theta_ticks = [0, '??']
for a in range(2, len(theta_range)):
    theta_ticks.append(str(a)+'??')

Tavg = sum(T_cs_list)/len(T_cs_list)

plt.figure()
plt.plot(theta_cs_list, T_cs_list, label='Simulated Torque')
plt.axhline(y=Tavg, color='r', linestyle='-', label='Average Torque')
plt.xticks(theta_range, theta_ticks)
plt.ylabel('Crankshaft Torque (Nm)')
plt.xlabel('Crankshaft Angle (rad)')
plt.title('Crankshaft Torque vs Angle')
plt.grid()
plt.legend(loc='upper right')

plt.figure()
plt.plot(theta_cs_list, w_cs_list)
plt.xticks(theta_range, theta_ticks)
plt.ylabel('Crankshaft Angular Velocity (rad/s)')
plt.xlabel('Crankshaft Angle (rad)')
plt.title('Crankshaft Angular Velocity vs Angle')
plt.grid()

plt.figure()
plt.plot(theta_cs_list, a_cs_list)
plt.xticks(theta_range, theta_ticks)
plt.ylabel('Crankshaft Angular Acceleration (rad/s^2)')
plt.xlabel('Crankshaft Angle (rad)')
plt.title('Crankshaft Angular Acceleration vs Angle')
plt.grid()

plt.figure()
plt.plot(theta_cs_list, F_c_list)
plt.xticks(theta_range, theta_ticks)
plt.ylabel('Piston Compression Force (N)')
plt.xlabel('Crankshaft Angle (rad)')
plt.title('Piston Compression Force vs Angle')
plt.grid()

plt.figure()
plt.plot(theta_cs_list, F_p_list)
plt.xticks(theta_range, theta_ticks)
plt.ylabel('Piston Combustion Force (N)') # technically this is combustion + power-stroke force, but this stage is commonly referred to as the combustion stage, so calling it that
plt.xlabel('Crankshaft Angle (rad)')
plt.title('Piston Combustion Force vs Angle')
plt.grid()

# animation setup
cylinder_top_y = l_c+l_co+h_p+s # y-coordinate for top of cylinder (m)

fig = plt.figure()
# fig.set_dpi(80)
# fig.set_size_inches(7, 6.5)
ax = plt.axes(xlim = (-l_c-plot_cl,l_c+plot_cl), ylim = (-l_c-plot_cl, l_c+l_co+h_p+s+plot_cl))
plt.axis('scaled')
plt.xlabel('Intake')

# object creation and starting positions
gas = plt.Rectangle((-d_p/2, l_c+l_co+h_p), d_p, s, fc = 'c')
circle = plt.Circle((0, 0), radius=r_cs, fc='k')
piston = plt.Rectangle((-d_p/2, l_c+l_co), d_p, h_p, fc='k')
crank = plt.Line2D((0, 0), (0, l_c), lw=5,
                          marker='.', 
                          markersize=10, 
                          markerfacecolor='m', 
                          markeredgecolor='m', 
                          alpha=0.5)
conrod = plt.Line2D((0, 0), (l_c, l_c+l_co), lw=5,
                          marker='.', 
                          markersize=10, 
                          markerfacecolor='m', 
                          markeredgecolor='m', 
                          alpha=0.5)
cylinder_left = plt.Line2D((-d_p/2, -d_p/2), (l_co-l_c, cylinder_top_y), lw=2)
cylinder_right = plt.Line2D((d_p/2, d_p/2), (l_co-l_c, cylinder_top_y), lw=2)
cylinder_top = plt.Line2D((-d_p/2, d_p/2), (cylinder_top_y, cylinder_top_y), lw=2)

# plot objects in figure to initialize
def init():
    plt.gca().add_line(crank)
    plt.gca().add_line(conrod)
    plt.gca().add_patch(circle)
    plt.gca().add_patch(piston)
    plt.gca().add_patch(gas)
    plt.gca().add_line(cylinder_left)
    plt.gca().add_line(cylinder_right)
    plt.gca().add_line(cylinder_top)
    return crank, conrod, circle, piston, gas, cylinder_left, cylinder_right, cylinder_top

def animate(i):
    # calculate next object position
    crank_x = l_c*np.sin(i)
    crank_y = l_c*np.cos(i)
    piston_y = l_c*np.cos(i)+l_co
    gas_y = piston_y+h_p
    gas_h = cylinder_top_y-gas_y

    # set new object position
    crank.set_xdata([0, crank_x])
    crank.set_ydata([0, crank_y])
    piston.set_y(piston_y)
    conrod.set_xdata([crank_x, 0])
    conrod.set_ydata([crank_y, piston_y])
    gas.set_y(gas_y)
    gas.set_height(gas_h)
    
    # gas color-coding for 4-stroke cycle
    if np.pi < i <= 2*np.pi:
        gas.set_facecolor("y")
        plt.xlabel('Compression')
    elif 2*np.pi < i <= 3*np.pi:
        gas.set_facecolor('r')
        plt.xlabel('Combustion')
    elif 3*np.pi < i <= 4*np.pi:
        gas.set_facecolor('b')
        plt.xlabel('Exhaust')
    elif 4*np.pi < i <= 5*np.pi:
        gas.set_facecolor("c")
        plt.xlabel('Intake')
    elif 5*np.pi < i <= 6*np.pi:
        gas.set_facecolor('y')
        plt.xlabel('Compression')
    elif 6*np.pi < i <= 7*np.pi:
        gas.set_facecolor('r')
        plt.xlabel('Combustion')
    elif 7*np.pi < i <= 8*np.pi:
        gas.set_facecolor('b')
        plt.xlabel('Exhaust')
    return crank, conrod, piston, gas

# create and save animation
anim = animation.FuncAnimation(fig, animate, 
                                init_func=init, 
                                frames=theta_cs_list, 
                                interval= 200,
                                blit=True)

anim.save('piston_motion.gif', fps = 60, dpi=80, writer='pillow')
