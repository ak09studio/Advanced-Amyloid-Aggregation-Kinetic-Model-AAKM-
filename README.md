Advanced Amyloid Aggregation Kinetic Model

This project implements a temperature-dependent amyloid aggregation model incorporating primary nucleation, elongation, secondary nucleation, and fragmentation dynamics. The system is solved numerically and parameters are globally optimized using differential evolution
​
Perfect.
Below is a research-grade, detailed README.md you can directly paste into your GitHub repository.

This is structured like something a computational biophysics lab would publish.

🧬 Advanced Amyloid Aggregation Kinetic Model
Multi-Pathway Temperature-Dependent Simulation Framework
📌 Overview

This repository implements a computational model of amyloid protein aggregation incorporating:

Primary nucleation

Secondary nucleation

Elongation

Fragmentation

Temperature-dependent Arrhenius scaling

Global parameter optimization

Statistical validation (R² and RMSE)

The system of coupled nonlinear differential equations is solved using an adaptive stiff solver (LSODA), and model parameters are estimated via global optimization using Differential Evolution.

This framework is designed for quantitative kinetic analysis of protein aggregation systems and fluorescence-based experimental fitting.

🔬 Scientific Background

Amyloid aggregation is a multi-step, nonlinear kinetic process involving competing molecular pathways. This model incorporates mechanistic pathways relevant to in vitro aggregation systems.

Governing Equations

Monomer concentration:

𝑑
𝑀
𝑑
𝑡
=
−
𝑘
𝑛
𝑀
𝑛
−
𝑘
𝑒
𝑀
𝑃
−
𝑘
2
𝑀
2
𝑃
dt
dM
	​

=−k
n
	​

M
n
−k
e
	​

MP−k
2
	​

M
2
P

Aggregate concentration:

𝑑
𝑃
𝑑
𝑡
=
𝑘
𝑛
𝑀
𝑛
+
𝑘
𝑒
𝑀
𝑃
+
𝑘
2
𝑀
2
𝑃
−
𝑘
𝑓
𝑃
dt
dP
	​

=k
n
	​

M
n
+k
e
	​

MP+k
2
	​

M
2
P−k
f
	​

P

Where:

𝑀
M = Monomer concentration

𝑃
P = Aggregate concentration

𝑘
𝑛
k
n
	​

 = Primary nucleation rate constant

𝑘
𝑒
k
e
	​

 = Elongation rate constant

𝑘
2
k
2
	​

 = Secondary nucleation rate constant

𝑘
𝑓
k
f
	​

 = Fragmentation rate constant

𝑛
n = Reaction order

Fluorescence intensity is assumed proportional to aggregate concentration:

𝐹
(
𝑡
)
∝
𝑃
(
𝑡
)
F(t)∝P(t)
🌡 Temperature Dependence

All kinetic rate constants are scaled using Arrhenius kinetics:

𝑘
(
𝑇
)
=
𝑘
𝑟
𝑒
𝑓
exp
⁡
[
−
𝐸
𝑎
𝑅
(
1
𝑇
−
1
𝑇
𝑟
𝑒
𝑓
)
]
k(T)=k
ref
	​

exp[
R
−E
a
	​

	​

(
T
1
	​

−
T
ref
	​

1
	​

)]

Where:

𝐸
𝑎
E
a
	​

 = Activation energy

𝑅
R = Gas constant

𝑇
T = Simulation temperature

This allows thermodynamic comparison between physiological and non-physiological conditions.

⚙ Numerical Implementation
ODE Solver

scipy.integrate.solve_ivp

Method: LSODA

Automatically handles stiff and non-stiff transitions

Tight tolerances for numerical stability

Optimization Strategy

scipy.optimize.differential_evolution

Global search algorithm

Avoids local minima trapping

Parameter bounds applied for physical realism

📊 Model Validation

After fitting:

Residual Sum of Squares (RSS) computed

Coefficient of Determination (R²) calculated

Root Mean Square Error (RMSE) reported

These metrics quantify model-data agreement.
