import numpy as np

r = [
    0.8 - 0.2j,
    -0.1 + 0.6j,
    0.3 + 0.6j,
    0.8 - 0.2j,
    -0.3 + 0.1j,
    -0.03 - 0.1j,
    -0.6 - 1j,
    -0.3 + 0.1j,
    0.3 + 0.04j,
    0.1 - 0.6j,
    -0.5 - 0.8j,
    0.3 + 0.04j,
    -0.3 + 0.1j,
    -0.03 - 0.1j,
    -0.6 - 1j,
    -0.3 + 0.1j,
    -0.8 + 0.2j,
    0.1 - 0.6j,
    -0.3 - 0.6j,
    -0.8 + 0.2j,
    0.8 - 0.2j,
    -0.1 + 0.6j,
    0.3 + 0.6j,
    0.8 - 0.2j,
]

y = [
    0.35 + 0.35j,
    -0.5 + 0j,
    0 + 0.25j,
    -0.35 - 0.35j,
    0.5 - 0j,
    -0.17 + 0.17j,
    0 - 0.5j,
    0.35 - 0.35j,
    -0.17 + 0.17j,
    -0.35 - 0.35j,
    0.5 - 0j,
    -0.17 + 0.17j,
    -0.35 - 0.35j,
    0.5 + 0j,
    -0.25j,
    0.35 + 0.35j,
    -0.5 + 0j,
    0 + 0.25j,
]

rb = 24e6

k = 0
for i in range(1, len(r)):
    if r[i] == r[0]:
        for j in range(i + 1, len(r)):
            if r[j] != r[j - i]:
                k = j
                break
        break

N = i
M = k

nsyms = 16
nbits = np.log2(nsyms)
rs_eff = rb / nbits
print(f"rs={rs_eff}")
rs = rs_eff / (N / M)
print(f"rs_eff={rs}")
Bt = (N + 1) * rs / N
print(f"Bt={Bt}")
