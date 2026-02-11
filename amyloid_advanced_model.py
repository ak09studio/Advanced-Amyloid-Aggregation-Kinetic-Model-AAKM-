Advanced Amyloid Aggregation Simulator
Primary + Secondary Nucleation + Fragmentation
Global Optimization Framework


import numpy as np
import pandas as pd
from scipy.integrate import solve_ivp
from scipy.optimize import differential_evolution
import matplotlib.pyplot as plt
from datetime import datetime

CREATOR_SIGNATURE = "ak09.studio"

-------------------------------
GLOBAL CONSTANTS
-------------------------------

R = 8.314  # Gas constant (J/mol/K)

M0 = 100.0
P0 = 0.0
n = 2

T_ref = 298
T_sim = 310

Ea_kn = 40000
Ea_ke = 30000
Ea_k2 = 35000
Ea_kf = 25000

-------------------------------
ARRHENIUS FUNCTION
-------------------------------

def arrhenius(k_ref, Ea, T):
    return k_ref * np.exp((-Ea / R) * (1 / T - 1 / T_ref))

-------------------------------
ODE SYSTEM
-------------------------------

def aggregation_odes(t, y, kn, ke, k2, kf):

    M, P = y

    primary = kn * M**n
    elongation = ke * M * P
    secondary = k2 * M**2 * P
    fragmentation = kf * P

    dMdt = -primary - elongation - secondary
    dPdt = primary + elongation + secondary - fragmentation

    return [dMdt, dPdt]

-------------------------------
SIMULATION WRAPPER
-------------------------------

def run_simulation(params, t_eval):

    kn_ref, ke_ref, k2_ref, kf_ref = params

    kn = arrhenius(kn_ref, Ea_kn, T_sim)
    ke = arrhenius(ke_ref, Ea_ke, T_sim)
    k2 = arrhenius(k2_ref, Ea_k2, T_sim)
    kf = arrhenius(kf_ref, Ea_kf, T_sim)

    sol = solve_ivp(
        aggregation_odes,
        (0, max(t_eval)),
        [M0, P0],
        t_eval=t_eval,
        args=(kn, ke, k2, kf),
        method="LSODA",
        rtol=1e-8,
        atol=1e-10
    )

    return sol.y[1]

-------------------------------
SYNTHETIC EXPERIMENTAL DATA
-------------------------------

time_exp = np.linspace(0, 200, 80)

true_params = [1e-4, 1e-2, 5e-5, 1e-3]

fluorescence_true = run_simulation(true_params, time_exp)
noise = np.random.normal(0, 1.5, size=len(fluorescence_true))
fluorescence_exp = fluorescence_true + noise

-------------------------------
OBJECTIVE FUNCTION
-------------------------------

def objective_function(params):
    model_pred = run_simulation(params, time_exp)
    residuals = fluorescence_exp - model_pred
    return np.sum(residuals**2)

-------------------------------
GLOBAL OPTIMIZATION
-------------------------------

bounds = [
    (1e-6, 1e-2),
    (1e-5, 1e-1),
    (1e-6, 1e-2),
    (1e-5, 1e-1)
]

result = differential_evolution(
    objective_function,
    bounds,
    strategy="best1bin",
    maxiter=60,
    popsize=20,
    tol=1e-7
)

fitted_params = result.x

-------------------------------
MODEL VALIDATION METRICS
-------------------------------

fluorescence_fit = run_simulation(fitted_params, time_exp)

residuals = fluorescence_exp - fluorescence_fit
ss_res = np.sum(residuals**2)
ss_tot = np.sum((fluorescence_exp - np.mean(fluorescence_exp))**2)

r_squared = 1 - (ss_res / ss_tot)
rmse = np.sqrt(np.mean(residuals**2))

-------------------------------
EXPORT PARAMETERS
-------------------------------

param_df = pd.DataFrame({
    "Parameter": ["kn", "ke", "k2", "kf"],
    "Fitted_Value": fitted_params
})

param_df.to_csv("fitted_parameters.csv", index=False)

-------------------------------
PLOT RESULTS
-------------------------------

time_smooth = np.linspace(0, 200, 500)
fluorescence_smooth = run_simulation(fitted_params, time_smooth)

plt.figure()
plt.scatter(time_exp, fluorescence_exp, label="Experimental Data")
plt.plot(time_smooth, fluorescence_smooth, label="Optimized Model")
plt.xlabel("Time")
plt.ylabel("Fluorescence (a.u.)")
plt.title("Advanced Amyloid Aggregation Model")
plt.legend()

plt.savefig("advanced_aggregation_fit.png", dpi=300)
plt.close()

-------------------------------
EXPORT REPORT
-------------------------------

with open("simulation_report.txt", "w") as f:
    f.write("Advanced Amyloid Aggregation Simulation\n")
    f.write(f"Generated: {datetime.now()}\n\n")
    f.write("Fitted Parameters:\n")
    for name, val in zip(["kn", "ke", "k2", "kf"], fitted_params):
        f.write(f"{name} = {val:.4e}\n")
    f.write(f"\nR-squared: {r_squared:.6f}\n")
    f.write(f"RMSE: {rmse:.6f}\n\n")
    f.write(f"Signature: {CREATOR_SIGNATURE}\n")

print("Simulation complete.")
print("Creator:", CREATOR_SIGNATURE)
print("R² =", r_squared)
print("RMSE =", rmse)
print("Exported files:")
print("- advanced_aggregation_fit.png")
print("- fitted_parameters.csv")
print("- simulation_report.txt")|



WHOA A BLACKHOLE??

                     .       .       .
               .                           .
           .                                   .
        .                                         .
      .                                             .
     .               ***************                 .
    .            ***********************              .
    .          ***************************             .
    .         *****************************             .
    .          ***************************             .
     .            ***********************              .
      .               ***************                 .
        .                                         .
           .                                   .
               .                           .
                     .       .       .


                           ^
                          / \
                         /___\
                          | |
                          | |
                         /   \
                        /_____\
                           |
                           |
                           |
                          / \
                         /___\
