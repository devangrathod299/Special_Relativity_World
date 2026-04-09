# Special_Relativity_World
This is a small-scaled pygame simulation of Lorentz transformation and shift in world lines with respect to change in the velocity of the body moving in a straight line.

# What does this project do?
This takes a given Relativistic velocity (in fraction of speed of light (c)) and displays:
- **Length Contraction** - How much the distance shrinks in the direction of motion.
- **Time Dilation** - How time slows down for a moving observer.
- **Lorentz Factor** - By what factor the length contraction and time dilation takes place.
- **Shift in World Lines** - How the axes of space and time transform.
  
# Mathematics involved:
Simple equations of length contraction and time dilation derived in famous "On the Electrodynamics of Moving Bodies"(1906) paper by Einstein. In the theory, an object moving at velocity **v** relative to an observer experiences:
- **Length Contraction:**
  $$x_r = \gamma(x - (vt)) $$
  
- **Time Dilation:**
  $$t_r = \gamma(t - (\frac{vx}{c^2})) $$

- **Lorentz Factor:**
  $$\gamma = \frac{1}{\sqrt{{c^2} - {v^2}}} $$ 
  
where **c** is the speed of light.

**Plotting of World Lines**
The World lines are plotted using:
$$x' = tan(\beta) * (x) $$
