# EngineDynamics
ME 369P Final Project - 4-Stroke Cycle Simulation, Animation, and Kinematic Analysis

## 1. Objective
Model the basic dynamics of an ideal 4-stroke cycle piston assembly, and animate a single piston assembly

## 2. Requirements
- Define and implement forcing function
- Derive EOM for single piston assembly
- Plot torque and angular velocity about crankshaft

## 3. Required packages
Matplotlib:
```
python -m pip install -U pip
python -m pip install -U matplotlib
conda install matplotlib
```

Sympy:
```
pip install sympy
conda install -c anaconda sympy
```

Numpy:
```
pip install numpy
conda install numpy
```

## 4. How to use: 4_stroke_simulation.py
This script simulates an ideal 4-stroke cycle for a 4-piston assembly, plots ouputs such as crankshaft torque and angular velocity, and animates a single piston assembly.

User inputs can be provided in the following sections:
- Geometric input parameters:
```
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
```
- Thermodynamic input parameters:
```
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
```
- Initial conditions:
```
# initial conditions
theta_cs = 0 # crankshaft angle corresponding to TDC (rad)
w_cs = 2 # crankshaft angular velocity (rad/s)
```
- Simulation parameters:
```
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
```

After running the script, 5 plots should be created for the simulation outputs, along with a .gif animation of a single piston assembly:
![image](https://user-images.githubusercontent.com/112368478/205208082-a42cceb3-010d-4bcc-8d02-372850705339.png)
![piston_motion](https://user-images.githubusercontent.com/112368478/205208108-0fbb5e25-5023-4441-a2d3-b8c2b60b33ae.gif)


## 5. How to use: piston_kinematics.py
This script shows an investigation of engine kinematics with constant velocity and geometric inputs

Run

```
python3 piston_kinematics.py
```
 
Input your variables for the engine properties parameters: crank length, connecting rod length, and the engine rpm

Example: 

```
Please enter the length of the crank (in): 10
Please enter length of connecting rod (in): 35
Please enter the angular velocity of the engine (rpm): 5000
```

### Output 1:
This output will show the general formula of the piston motion in LATEX format.

Formula of the equation of position in LATEX form:

<div align='center'>

 $x = l \sqrt{1 - \frac{r^{2} \sin^{2}{\left(\omega t \right)}}{l^{2}}} + r \cos{\left(\omega t \right)}$

 </div>

 The velocity of piston is obtained by differentiated position versus time:
 <div align = 'center'>

 $\dot{x} = - \omega r \sin{\left(\omega t \right)} - \frac{\omega r^{2} \sin{\left(\omega t \right)} \cos{\left(\omega t \right)}}{l \sqrt{1 - \frac{r^{2} \sin^{2}{\left(\omega t \right)}}{l^{2}}}}$

 </div>

 And similarly for acceleration:
 <div align = 'center'>

 $\ddot{x} = - \omega^{2} r \cos{\left(\omega t \right)} + \frac{\omega^{2} r^{2} \sin^{2}{\left(\omega t \right)}}{l \sqrt{1 - \frac{r^{2} \sin^{2}{\left(\omega t \right)}}{l^{2}}}} - \frac{\omega^{2} r^{2} \cos^{2}{\left(\omega t \right)}}{l \sqrt{1 - \frac{r^{2} \sin^{2}{\left(\omega t \right)}}{l^{2}}}} - \frac{\omega^{2} r^{4} \sin^{2}{\left(\omega t \right)} \cos^{2}{\left(\omega t \right)}}{l^{3} \left(1 - \frac{r^{2} \sin^{2}{\left(\omega t \right)}}{l^{2}}\right)^{\frac{3}{2}}}$

 </div>

### Output 2:
This output will show the graphs of kinematic analysis of the engine via user input:
![piston_kinematics_plots](https://user-images.githubusercontent.com/112368478/205214328-f4144104-a2aa-43c6-8a68-52199c052c7d.jpeg)
