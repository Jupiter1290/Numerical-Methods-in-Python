### Engine Data Analysis and Power Estimation

This Python script processes experimental engine data stored in `engine_data.out` to compute key performance parameters using numerical integration.

**Features:**
- Verifies input file structure and compatibility.
- Visualizes parameter relationships (e.g., `Pressure vs Volume`, `Volume vs Pressure`).
- Calculates area under the `P–V` curve using the trapezoidal rule.
- Estimates **power output** and **specific fuel consumption (SFC)**.

**Libraries Used:** `scipy.integrate`, `matplotlib`, `sys`

**Outputs:**
- Graphs of selected variable pairs.
- Printed power output and SFC in engineering units.
