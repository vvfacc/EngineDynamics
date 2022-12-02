## Kinematics of the slider-crank (piston-cylinder)

Let the crank length be r and the connecting rod length be l. The angle of the crank is theta and the angle of the connecting rod relative to the x-axis is phi. For any constant crank velocity, the equation of motion for the piston's position is defined as:
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
