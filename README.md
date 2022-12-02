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
- Geometric input parameters
![image](https://user-images.githubusercontent.com/112368478/205207378-22a21aac-4367-4ef2-a927-9569459da38b.png)
- Thermodynamic input parameters
![image](https://user-images.githubusercontent.com/112368478/205207425-3d4a21b0-09ef-4a31-a5ff-94b6fab6b779.png)
- Initial conditions  
![image](https://user-images.githubusercontent.com/112368478/205207451-9d732953-4d97-4e79-bef9-3ae6a52f19ec.png)
- Simulation parameters   
![image](https://user-images.githubusercontent.com/112368478/205207488-4c945b9b-cfff-414f-af77-4269c5667bdc.png)

After running the script, 5 plots should be created for the simulation outputs, along with a .gif animation of a single piston assembly:
![image](https://user-images.githubusercontent.com/112368478/205208082-a42cceb3-010d-4bcc-8d02-372850705339.png)
![piston_motion](https://user-images.githubusercontent.com/112368478/205208108-0fbb5e25-5023-4441-a2d3-b8c2b60b33ae.gif)


## 5. How to use: piston_kinematics.py
This script shows an investigation of the engine kinematics with an assumptions of constant velocity

Run

```
python3 pistin_kinematics.py
```
 
Input your variables for the engine properties parameters: radius of crank, length of conrod, and the engine rpm

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

 Also the acceleration:
 <div align = 'center'>

 $\ddot{x} = - \omega^{2} r \cos{\left(\omega t \right)} + \frac{\omega^{2} r^{2} \sin^{2}{\left(\omega t \right)}}{l \sqrt{1 - \frac{r^{2} \sin^{2}{\left(\omega t \right)}}{l^{2}}}} - \frac{\omega^{2} r^{2} \cos^{2}{\left(\omega t \right)}}{l \sqrt{1 - \frac{r^{2} \sin^{2}{\left(\omega t \right)}}{l^{2}}}} - \frac{\omega^{2} r^{4} \sin^{2}{\left(\omega t \right)} \cos^{2}{\left(\omega t \right)}}{l^{3} \left(1 - \frac{r^{2} \sin^{2}{\left(\omega t \right)}}{l^{2}}\right)^{\frac{3}{2}}}$

 </div>

### Output 2
This output will show the graphs of kinematic analysis of the engine via user input. 