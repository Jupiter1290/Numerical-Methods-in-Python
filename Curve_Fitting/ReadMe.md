### Curve Fitting using Linear, Cubic, and Biquadratic Models

This Python script fits experimentally obtained data of temperature vs. specific heat (`C_p`) using three polynomial models:
- **Linear model** (1st order)
- **Cubic model** (3rd order)
- **Biquadratic model** (4th order)

The fitting is performed using SciPy’s `curve_fit()` function.  
For each model, the optimized coefficients and corresponding fitted curves are obtained and plotted alongside the actual data.

Residuals are computed and plotted to assess model accuracy and compare how well each curve represents the dataset.

**Files:**
- `data` – Input file containing temperature and specific heat values.
- `curve_fit_models.py` – Python script implementing the fitting and residual comparison.

**Outputs:**
- Fitted curves for each model.
- Residual plots comparing the linear, cubic, and biquadratic fits.