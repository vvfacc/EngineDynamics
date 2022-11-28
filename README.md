# EngineDynamics
Final Project of ME359P - Dynamics Analysis of Car Engine

## 1. Introduction
...Updating
## 2. The four-strokes engine cycle
... updating
## 3. The use of PyDy in the project
This project is just PyDy to genetate the formula of the kinamtics and dynamics analysis of the 4 strokes engine
The formula is the LATEX code output from the Python file
## 4. Kinematics of the slider-crank (piston-cylinder)

Let the crank radius be r and the conrod length be l. The angle of the crank is theta and the angle of the conrod makes with X axis is phi. For any constant crank velocity, the position of the piston, which is the equation of motions of this system is define as:
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