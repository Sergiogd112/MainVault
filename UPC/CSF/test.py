import sympy as sp
from scipy.special import erfcinv
import numpy as np

# Assign the other parameters defined in the excercisse
# Define the symbols
No, Eb, M, Gp, SIR, Tb, Tc, d, blob = sp.symbols("N_o,E_b,M,G_p,SIR,T_b,T_c,d,blob")
# define the BER
BER = 0.5 * sp.erfc(blob)

BER.simplify()
# set the BER definition to equal 3.5e-3
eq = BER - 12e-3
# Find the value of the inner part of the erfc
res = sp.solve(eq, blob)
inerfc = erfcinv(float(sp.erfc(res[0])))
a = 1 / inerfc**2
beta = 0.15
BW = 184e6
vals = {
    No: 5e-18,
}
r = 1100
L = 25 + 32 * sp.log(r, 10)
D = 12
Pt_dBm = 30
PrdBm = Pt_dBm - L + D
PrW = 10 ** ((PrdBm - 30) / 10)
act = 0.4
rb = 400e3
Tb = 1 / rb
Eb = PrW * Tb
# state the equations for Gp=Tb/Tc and BW=(1+beta)/Tc
eq2 = Gp - Tb / Tc
eq3 = (1 + beta) / Tc - BW
# state the equation for the inner part of the BER formula
eq = No / Eb + (M - 1) / Gp - a
# solve for all the unknowns
res = sp.solve([eq.subs(vals), eq2, eq3])[0]
# print the results
print(res)
print("Gp:", res[Gp])
print("M:", res[M])
print("Tc:", res[Tc])
# Compute the density of user/km^2
Mprim = np.floor(res[M] / act)
rhokm2 = np.floor(Mprim / (3.14159264 * (r / 1000) ** 2))
print("M':", Mprim)
print("density:", rhokm2, "users/km^2")
