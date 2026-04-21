# Special_Relativity_World
This is a small-scaled pygame simulation of Lorentz transformation and shift in world lines with respect to change in the velocity of the body moving in a straight line.

# About:

Visualizing difficult concepts is very fascinating, especially those which you do not observe so easily like special relativity. This simulation brings Einstein's Special Relativity to life showcasing how does space-time system transforms for a moving observer using Lorentz transformation and Minkowski diagrams.

# What does this project do?
This takes a given Relativistic velocity (in fraction of speed of light (c)) and displays:

- **Lorentz Transformation** - How the space and time changes for a moving body.
- **Length Contraction** - How much the distance shrinks in the direction of motion.
- **Time Dilation** - How time slows down for a moving observer.
- **Lorentz Factor** - By what factor the length contraction and time dilation takes place.
- **Shift in World Lines** - How the axes of space and time transform.
- **Breaking Simultaneity** - How events are seem to occur simultaneous in one frame no longer seem simultaneous in another frame moving with respect to the reference frame.
  
# Mathematics involved:
Simple equations of length contraction and time dilation derived in famous "On the Electrodynamics of Moving Bodies"(1906) paper by Einstein. In the theory, an object moving at velocity **v** relative to an observer experiences:
- **Lorentz Transformation of Space:**
  $$x_r = \gamma(x - (vt)) $$
  
- **Lorentz Transformation of Time:**
  $$t_r = \gamma(t - (\frac{vx}{c^2})) $$

- **Lorentz Factor:**
  $$\gamma = \frac{1}{\sqrt{{c^2} - {v^2}}} $$
  
where **c** is the speed of light.

- **Length Contraction:**
  $$L = \frac{L_0}{\gamma} $$

- **Time Dilation:**
  $$T = \gamma * T_0 $$

  where L_0 and T_0 space and time intervals in rest frames. 

- **Plotting of World Lines**

The World lines are plotted using:
- $$x' = tan(\beta) * (x) $$

- $$ct' = tan(\beta) * (ct) $$

- $$\beta = \frac{v}{c}$$

where (x,t) is rest frame observers coordinate system, (x',t') is moving body's coordinate system observed from rest frame.

## Road map:
- Introducing multiple frames with different velocities.
- Adding different types of motion and acceleration to frames.
- Answering 'What if beyond c?'

## Built With

- **Python** - Programming language
- **Pygame** - Graphics and simulation rendering

## Download & Run
Go to the [Releases](https://github.com/devangrathod299/Special_Relativity_World/releases) page and download the latest `.exe`
