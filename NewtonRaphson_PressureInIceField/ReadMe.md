### Newton–Raphson Method – Pressure in Ice Field

This program applies the **Newton–Raphson method** to determine the minimum cushion pressure in an ice field as a function of ice thickness.

**Given:**
- β = 0.5, r = 40 ft, σ = 150 psi (converted to pounds/ft² internally)

**Tasks:**
1. Compute pressure for h = 0.6 ft.  
2. Find the optimal relaxation factor using a convergence plot.  
3. Tabulate minimum pressures for h = [0.6, 1.2, 1.8, 2.4, 3.0, 3.6, 4.2].

**Outputs:**
- Iterations vs Relaxation Factor plot
- Minimum Pressure vs Height plot

**Methodology:**
Uses iterative root-finding with controlled tolerance and convergence monitoring.
