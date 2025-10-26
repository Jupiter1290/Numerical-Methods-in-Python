### Modelling a Damped Pendulum using ODE Integration

This script models the motion of a damped pendulum using the coupled second-order differential equations of motion.

**Equation:**
\[
\frac{d^2\theta}{dt^2} + \frac{b}{m}\frac{d\theta}{dt} + \frac{g}{l}\sin(\theta) = 0
\]

**Method:**
- Uses `scipy.integrate.odeint()` to numerically solve for angular displacement and velocity.
- Visualizes the time evolution of both parameters.

**Inputs:**
- Damping constant `b = 0.05`, length `l = 1 m`, mass `m = 0.1 kg`, initial angular velocity = 3 rad/s

**Outputs:**
- Time-series plots showing the decay of oscillations due to damping.

