#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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


#animation
#create objects to populate animation
fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(7, 6.5)
ax = plt.axes(xlim = (-0.06,0.06), ylim = (-0.06, 0.26))


gas = plt.Rectangle((-d_p/2, l_c + 2* r_cs), d_p, s, fc = 'c')
circle = plt.Circle((0, 0), radius=r_cs, fc='y')
piston = plt.Rectangle((-d_p/2, l_c + r_cs), d_p, r_cs, fc='k')
crankshaft = plt.Line2D((0, 0), (0, r_cs), lw=5, 
                         marker='.', 
                         markersize=10, 
                         markerfacecolor='r', 
                         markeredgecolor='r', 
                         alpha=0.5)
crank = plt.Line2D((0, 0), (r_cs, r_cs + l_c), lw=5, 
                         marker='.', 
                         markersize=10, 
                         markerfacecolor='r', 
                         markeredgecolor='r', 
                         alpha=0.5)

plt.axis('scaled')

#put objects on figure to initialize
def init():
    plt.gca().add_line(crankshaft)
    plt.gca().add_line(crank)
    plt.gca().add_patch(circle)
    plt.gca().add_patch(piston)
    plt.gca().add_patch(gas)
    return crankshaft, crank, circle, piston, gas

#
def animate(i):
    
    #get current object positions
    x, y = tuple(crankshaft.get_xydata()[1])
    h_piston = piston.get_y()
    gas_y = gas.get_y()
    top_of_cylinder = l_c + 2* r_cs + s
    
    #calculate next object position
    x = r_cs * np.sin(i)
    y = r_cs * np.cos(i)
    h_piston = l_c + r_cs * np.cos(i)
    gas_y = h_piston + r_cs
    height_gas = top_of_cylinder - gas_y

    #set new object position
    crankshaft.set_xdata([0, x])
    crankshaft.set_ydata([0, y])
    piston.set_y(h_piston)
    crank.set_xdata([x, 0])
    crank.set_ydata([y, h_piston])
    gas.set_y(gas_y)
    gas.set_height(height_gas)
    if i <= m.pi:
        pass
    elif m.pi < i <= 2*m.pi:
        gas.set_facecolor("g")
    elif 2*m.pi < i <= 3*m.pi:
        gas.set_facecolor('r')
    elif 3*m.pi < i <= 4*m.pi:
        gas.set_facecolor('b')
    elif 4*m.pi < i <= 5*m.pi:
        gas.set_facecolor("c")
    elif 5*m.pi < i <= 6*m.pi:
        gas.set_facecolor('g')
    elif 6*m.pi < i <= 7*m.pi:
        gas.set_facecolor('r')
    elif 7*m.pi < i <= 8*m.pi:
        gas.set_facecolor('b')
    return crankshaft, crank, piston, gas

#create and save animation
anim = animation.FuncAnimation(fig, animate, 
                               init_func=init, 
                               frames=theta_cs_list, 
                               interval= 200,
                               blit=True)

anim.save('piston_test.gif', fps = 60, dpi=80, writer='pillow')
