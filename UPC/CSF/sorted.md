## A digital mobile communications system transmits at a rate of 500kbps. The wireless channel presents fast Rayleigh type time domain variations. An interleaving mechanism has been introduced to break the bursts of errors, assuring that no consecutive error bits are delivered in the same codeword at destination. The interleaving matrix has been designed assuming that the mobile node moves at 90 km/h and that the delay introduced by the interleaving mechanism does not exceed 200ms. Codewords are of 350 bits and each codeword is written in a row of the interleaving matrix. Calculate the maximum possible carrier frequency (Hz) of the wireless signal.

Note: You can use Hz, kHz, MHz or GHz, just write the units after the number

- 10.25 GHz
## A digital mobile communications system uses a carrier frequency of 2.4GHz and transmits at a rate of 1Mbps. The wireless channel presents fast Rayleigh type time domain variations. An interleaving mechanism has been introduced to break the bursts of errors, assuring that there are no more than two consecutive bits are delivered in the same codeword at destination. The interleaving matrix has been designed assuming that the channel coherence time is 1ms and the delay introduced by the interleaving mechanism must not exceed 300ms. Calculate the maximum size (bits) of the codewords assuming that one codeword is written in each row of the matrix and bits are read in columns.

- 300 bits
## A wireless digital transmission system is based on OFDM. All carriers are modulated with 16-QAM. The noise power is negligible. Assuming perfect synchronism, the samples of the received signal are:

```Python
r = [
    -0.5 - 0.1j,
    0.7 - 0.1j,
    0.3 + 0.6j,
    0.8 - 0.2j,
    -0.3 + 0.1j,
    -0.03 - 0.1j,
    -0.5 - 0.1j,
    0.7 - 0.1j,
    -0.6 - 1j,
    -0.3 - 0.1j,
    -0.5 - 0.8j,
    0.3 + 0.04j,
    -0.3 + 0.1j,
    -0.03 - 0.1j,
    -0.6 - 1j,
    -0.3 - 0.1j,
    0.3 + 0.6j,
    0.8 - 0.2j,
    -0.3 - 0.6j,
    -0.8 + 0.2j,
    0.8 - 0.2j,
    -0.1 + 0.6j,
    0.3 + 0.6j,
    0.8 - 0.2j,
]
```

The output of the receiver, once the cyclic prefix has been eliminated and before equalising is:

```Python
y = [
    0 - 0.2j,
    -0.084 + 0.084j,
    0.122 + 0.367j,
    -0.48 - 0.16j,
    0.197 - 0.197j,
    0.707 + 0.707j,
    0.2 + 0j,
    0.254 - 0.084j,
    -0.367 + 0.363j,
    -0.16 - 0.48j,
    0.197 - 0.593j,
    -0.707 + 0.703,
    0.2 - 0j,
    0.254 + 0.254,
    0.367 - 0.123j,
    0.48 + 0.48j,
    -0.593 + 0.593j,
    0 + 1j,
]
```

The first and the last carriers are pilots of unitary amplitude. Calculate the channel coefficient (amplitude) for the third carrier, applying a linear interpolation in the frequency domain.
![[Pasted image 20240613121907.png]]
![[Pasted image 20240613121928.png]]

Solution in Python:

```Python
import numpy as np

r = [
    -0.5 - 0.1j,
    0.7 - 0.1j,
    0.3 + 0.6j,
    0.8 - 0.2j,
    -0.3 + 0.1j,
    -0.03 - 0.1j,
    -0.5 - 0.1j,
    0.7 - 0.1j,
    -0.6 - 1j,
    -0.3 - 0.1j,
    -0.5 - 0.8j,
    0.3 + 0.04j,
    -0.3 + 0.1j,
    -0.03 - 0.1j,
    -0.6 - 1j,
    -0.3 - 0.1j,
    0.3 + 0.6j,
    0.8 - 0.2j,
    -0.3 - 0.6j,
    -0.8 + 0.2j,
    0.8 - 0.2j,
    -0.1 + 0.6j,
    0.3 + 0.6j,
    0.8 - 0.2j,
]

y = [
    0 - 0.2j,
    -0.084 + 0.084j,
    0.122 + 0.367j,
    -0.48 - 0.16j,
    0.197 - 0.197j,
    0.707 + 0.707j,
    0.2 + 0j,
    0.254 - 0.084j,
    -0.367 + 0.363j,
    -0.16 - 0.48j,
    0.197 - 0.593j,
    -0.707 + 0.703,
    0.2 - 0j,
    0.254 + 0.254,
    0.367 - 0.123j,
    0.48 + 0.48j,
    -0.593 + 0.593j,
    0 + 1j,
]

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

M1 = np.abs(y[0])
M6 = np.abs(y[5])
M3 = np.abs(y[2])
Delta=(M6-M1)/(N-1)
print(Delta)
coeff=M3+Delta
print(coeff)
```

- 0.52
## A wireless digital transmission system is based on OFDM. All carriers are modulated with 16-QAM. The noise power is negligible. Assuming perfect synchronism, the samples of the received signal are:

```Python
r=[-0.5-0.1j, 0.7-0.1j, 0.3+0.6j, 0.8-0.2j, -0.3+0.1j, -0.03-0.1j, -0.5-0.1j, 0.7-0.1j, -0.6-1j, -0.3-0.1j, -0.5-0.8j, 0.3+0.04j, -0.3+0.1j, -0.03-0.1j, -0.6-1j, -0.3-0.1j, 0.3+0.6j, 0.8-0.2j, -0.3-0.6j, -0.8+0.2j, 0.8-0.2j, -0.1+0.6j, 0.3+0.6j, 0.8-0.2j]
```

The output of the receiver, once the cyclic prefix has been eliminated and before equalising is:

```Python
y=[0-0.2j, -0.360+0.360j, 0.122+0.367j, -0.48-0.16j, 0.197-0.197j, 0.707+0.707j, 0.2+0j, 1.080-0.360j, -0.367+0.367j, -0.16- 0.48j, 0.197-0.593j, -0.707+0.707j, 0.2-0j, 1.080+0.360j, 0.367-0.122j, 0.48+0.48j, -0.593+0.593j, 0+1j]
```

The first and the last carriers are pilots of unitary amplitude.
With the following table for the modulation, equalise the signal and calculate the bits received through the second carrier

| Bits   | Value |
| ------ | ----- |
| "0000" | 3+1j  |
| "0001" | -1+3j |
| "0010" | 1+1j  |
| "0011" | -1-1j |
| "0100" | -3-3j |
| "0101" | -3+1j |
| "0110" | 1-3j  |
| "0111" | 3-1j  |
| "1000" | 3-3j  |
| "1001" | 3+3j  |
| "1010" | -1+1j |
| "1011" | -1-3j |
| "1100" | 1+3j  |
| "1101" | 1-1j  |
| "1110" | -3-1j |
| "1111" | -3+3j |

- 101001110000
## A wireless digital transmission system is based on OFDM. All carriers are modulated with 16-QAM. The noise power is negligible. Assuming perfect synchronism, the samples of the received signal are:

```Python
r=[-0.5-0.1j, 0.7-0.1j   0.3+0.6j,   0.8-0.2j   -0.3+0.1j   -0.03-0.1j,   -0.5-0.1j, 0.7-0.1j   -0.6-1j   -0.3-0.1j,   -0.5-0.8j   0.3+0.04j, -0.3+0.1j   - 0.03-0.1j,   -0.6-1j,   -0.3-0.1j   0.3+0.6j   0.8-0.2j   -0.3-0.6j,   -0.8+0.2j    0.8-0.2j   -0.1+0.6j   0.3+0.6j,   0.8-0.2j]
```

The output of the receiver, once the cyclic prefix has been eliminated and before equalising is:

```Python
y=[0-0.2j    -0.084+0.084j   0.122+0.367j   -0.48-0.16j    0.197-0.197j    0.707+0.707j    0.2+0j   0.254-0.084j   -0.367+0.367j, -0.16- 0.48j    0.197-0.593j    -0.707+0.707j, 0.2-0j    0.254+0.254j   0.367-0.122j    0.48+0.48j, -0.593+0.593j   0+1j]
```

The first and the last carriers are pilots of unitary amplitude. Calculate the channel coefficient (amplitude) for the second carrier, applying a linear interpolation in the frequency domain.

- 0.36
## A wireless digital transmission system is based on OFDM. All carriers are modulated with 16-QAM. The noise power is negligible. Assuming perfect synchronism, the samples of the received signal are:

```Python
r=[1.06-0.5j, -0.06+0.02j, -0.44-0.94j, 1.16+1.16j, 0.49-0.35j, -1.16+0.31j, 1.06-0.5j, -0.06+0.02j, -0.44-0.94j, -0.16-0.83j, 0.03-0.38j, 0.29-0.47j, 0.5+0.83j, 0.87-0.18j, -0.53+1.05j, -0.16-0.83j, 0.03-0.38j, 0.29-0.47j, 0.16-0.16j, -0.37+0.38j, 0.7-0.67j, 0.16+0.16j, 0.12+1.34j, 0.2-1.05j, 0.16-0.16j, -0.37+0.38j, 0.7-0.67j]
```

The output of the receiver, once the cyclic prefix has been eliminated and before equalising is:

```Python
y=[0+0.1j, 0.6+0.6j, 0.9-0.3j, -0.4+1.2j, 1.5+1.5j, 0+0.6j, 0.1+0j, 0.6+0.2j, -0.3-0.3j, -0.4+1.2j, 0.5+0.5j, 0+0.6j, -0.1+0j, 0.2+0.2j, 0.9+0.3j, -0.4-0.4j, -1.5-0.5j, 0+0.6j]
```

The first and the last carriers are pilots of unitary amplitude.
With the following table for the modulation, equalise the signal and calculate the bits received through the third carrier.

| Bits | Value |
| ---- | ----- |
| 0000 | 3+1j  |
| 0001 | -1+3j |
| 0010 | 1+1j  |
| 0011 | -1-1j |
| 0100 | -3-3j |
| 0101 | -3+1j |
| 0110 | 1-3J  |
| 0111 | 3-1j  |
| 1000 | 3-3J  |
| 1001 | 3+3j  |
| 1010 | -1+1j |
| 1011 | -1-3j |
| 1100 | 1+3j  |
| 1101 | 1-1j  |
| 1110 | -3-1j |
| 1111 | -3+3j |

Solution in Python:

```Python
import numpy as np
import matplotlib.pyplot as plt
import itertools
```

convert the table to a dictionary and then use it to convert the symbols to bits.

```Python
mod={
    (0,0,0,0): 3+1j,
    (0,0,0,1): -1+3j,
    (0,0,1,0): 1+1j,
    (0,0,1,1): -1-1j,
    (0,1,0,0): -3-3j,
    (0,1,0,1): -3+1j,
    (0,1,1,0): 1-3j,
    (0,1,1,1): 3-1j,
    (1,0,0,0): 3-3j,
    (1,0,0,1): 3+3j,
    (1,0,1,0): -1+1j,
    (1,0,1,1): -1-3j,
    (1,1,0,0): 1+3j,
    (1,1,0,1): 1-1j,
    (1,1,1,0): -3-1j,
    (1,1,1,1): -3+3j,
}

demod = {v: k for k, v in mod.items()}

syms=np.array([sym for sym in mod.values()])
```

Compute the number of carriers by finding the where the cyclic prefix repeats

```Python
cp0 = r[0]

for i in range(1, len(r)):
    if r[i] == cp0:
        break
print(f"Number of carriers: {i}")
N=i
```

Get the third carrier

```Python
y_3=np.array([y[i] for i in range(2, len(y), N)])
```

Compute the modulus element-wise

```Python
modulus = np.abs(y_3)
```

Find the maximum index modulus

```Python
max_index = np.argmax(modulus)
```

Compute the phase of the maximum index

```Python
phase = np.angle(y_3[max_index])
```

Find the candidate symbols with the same phase

```Python
cand_sym = [sym for sym in syms if np.angle(sym) == phase]
```

Find the symbol with the maximum modulus

```Python
max_sym = cand_sym[np.argmax([np.abs(sym) for sym in cand_sym])]
```

compute the ratio

```Python
ratio = y_3[max_index] / max_sym
```

Rescale the carrier

```Python
y_3 /= ratio
```

Demodulate the carrier

```Python
bits = [demod[sym] for sym in y_3]
bits=list(itertools.chain(*bits))
print(''.join([str(bit) for bit in bits]))
```

- 011100110000
  Complete solution in Python:

```Python
import numpy as np
import matplotlib.pyplot as plt
import itertools

r=[1.06-0.5j, -0.06+0.02j, -0.44-0.94j, 1.16+1.16j, 0.49-0.35j, -1.16+0.31j, 1.06-0.5j, -0.06+0.02j, -0.44-0.94j, -0.16-0.83j, 0.03-0.38j, 0.29-0.47j, 0.5+0.83j, 0.87-0.18j, -0.53+1.05j, -0.16-0.83j, 0.03-0.38j, 0.29-0.47j, 0.16-0.16j, -0.37+0.38j, 0.7-0.67j, 0.16+0.16j, 0.12+1.34j, 0.2-1.05j, 0.16-0.16j, -0.37+0.38j, 0.7-0.67j]

y=[0+0.1j, 0.6+0.6j, 0.9-0.3j, -0.4+1.2j, 1.5+1.5j, 0+0.6j, 0.1+0j, 0.6+0.2j, -0.3-0.3j, -0.4+1.2j, 0.5+0.5j, 0+0.6j, -0.1+0j, 0.2+0.2j, 0.9+0.3j, -0.4-0.4j, -1.5-0.5j, 0+0.6j]

mod={
    (0,0,0,0): 3+1j,
    (0,0,0,1): -1+3j,
    (0,0,1,0): 1+1j,
    (0,0,1,1): -1-1j,
    (0,1,0,0): -3-3j,
    (0,1,0,1): -3+1j,
    (0,1,1,0): 1-3j,
    (0,1,1,1): 3-1j,
    (1,0,0,0): 3-3j,
    (1,0,0,1): 3+3j,
    (1,0,1,0): -1+1j,
    (1,0,1,1): -1-3j,
    (1,1,0,0): 1+3j,
    (1,1,0,1): 1-1j,
    (1,1,1,0): -3-1j,
    (1,1,1,1): -3+3j,
}

demod = {v: k for k, v in mod.items()}

syms=np.array([sym for sym in mod.values()])

cp0 = r[0]

for i in range(1, len(r)):
    if r[i] == cp0:
        break
print(f"Number of carriers: {i}")
N=i

y_3=np.array([y[i] for i in range(2, len(y), N)])

max_index = np.argmax(modulus)
phase = np.angle(y_3[max_index])
cand_sym = [sym for sym in syms if np.angle(sym) == phase]
max_sym = cand_sym[np.argmax([np.abs(sym) for sym in cand_sym])]
ratio = y_3[max_index] / max_sym

y_3 /= ratio

bits = [demod[sym] for sym in y_3]
bits=list(itertools.chain(*bits))
print(''.join([str(bit) for bit in bits]))
```
## A wireless digital transmission system is based on OFDM. All carriers are modulated with 16-QAM. The noise power is negligible. Assuming perfect synchronism, the samples of the received signal are:

```Python
r=[1.16-0.5j, -0.006+0.02j, -0.66-0.64j, 1.16+1.16j, 0.49-0.35j, -1.16+0.31j, 1.16-0.5j, -0.006+0.02j, -0.66-0.64j, -0.16-0.83j, 0.03-0.38j, 0.29-0.47j, 0.5+0.83j, 0.87-0.18j, -0.53+1.05j, -0.16-0.83j, 0.03-0.38j, 0.29-0.47j, 0.16-0.16j, -0.37+0.38j, 0.7-0.67j, 0.16+0.16j, 0.12+1.34j, 0.2-1.05j, 0.16-0.16j, -0.37+0.38j, 0.7-0.67j]
```

The output of the receiver, once the cyclic prefix has been eliminated and before equalising is:

```Python
y=[0.1+0j, 0.2+0.2j, 0.9-0.3j, -0.4+1.2j, 1.5+1.5j, 0+0.6j, 0.1+0j, 0.6+0.2j, -0.3-0.3j, -0.4+1.2j, 0.5+0.5j, 0+0.6j, 0.1+0j, 0.2+0.2j, 0.9+0.3j-0.4-0.4j, -1.5-0.5j, 0+0.6j]
```

Calculate the total transmitted bandwidth (MHz) if we want to have an effective transmission rate of 24Mbps.
![[Pasted image 20240613121544.png]]
![[Pasted image 20240613121613.png]]

Solution in Python:

```Python
import numpy as np

r = [
    1.16 - 0.5j,
    -0.006 + 0.02j,
    -0.66 - 0.64j,
    1.16 + 1.16j,
    0.49 - 0.35j,
    -1.16 + 0.31j,
    1.16 - 0.5j,
    -0.006 + 0.02j,
    -0.66 - 0.64j,
    -0.16 - 0.83j,
    0.03 - 0.38j,
    0.29 - 0.47j,
    0.5 + 0.83j,
    0.87 - 0.18j,
    -0.53 + 1.05j,
    -0.16 - 0.83j,
    0.03 - 0.38j,
    0.29 - 0.47j,
    0.16 - 0.16j,
    -0.37 + 0.38j,
    0.7 - 0.67j,
    0.16 + 0.16j,
    0.12 + 1.34j,
    0.2 - 1.05j,
    0.16 - 0.16j,
    -0.37 + 0.38j,
    0.7 - 0.67j,
]

y = [
    0.1 + 0j,
    0.2 + 0.2j,
    0.9 - 0.3j,
    -0.4 + 1.2j,
    1.5 + 1.5j,
    0 + 0.6j,
    0.1 + 0j,
    0.6 + 0.2j,
    -0.3 - 0.3j,
    -0.4 + 1.2j,
    0.5 + 0.5j,
    0 + 0.6j,
    0.1 + 0j,
    0.2 + 0.2j,
    0.9 + 0.3j - 0.4 - 0.4j,
    -1.5 - 0.5j,
    0 + 0.6j,
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
```

- 10.5 MHz
## A wireless digital transmission system is based on OFDM. All carriers are modulated with 16-QAM. The noise power is negligible. Assuming perfect synchronism, the samples of the received signal are:

```Python
r=[1.16-0.5j, -0.006+0.02j, -0.66-0.64j, 1.16+1.16j, 0.49-0.35j, -1.16+0.31j, 1.16-0.5j, -0.006+0.02j, -0.66-0.64j, -0.16-0.83j, 0.03-0.38j, 0.29-0.47j, 0.5+0.83j, 0.87-0.18j, -0.53+1.05j, -0.16-0.83j, 0.03-0.38j, 0.29-0.47j, 0.16-0.16j, -0.37+0.38j, 0.7-0.67j, 0.16+0.16j, 0.12+1.34j, 0.2-1.05j, 0.16-0.16j, -0.37+0.38j, 0.7-0.67j]
```

The output of the receiver, once the cyclic prefix has been eliminated and before equalising is:

```Python
y=[0.1+0j, 0.2+0.2j, 0.9-0.3j, -0.4+1.2j, 1.5+1.5j, 0+0.6j, 0.1+0j, 0.6+0.2j, -0.3-0.3j, -0.4+1.2j, 0.5+0.5j, 0+0.6j, 0.1+0j, 0.2+0.2j, 0.9+0.3j-0.4-0.4j, -1.5-0.5j, 0+0.6j]
```

The first and the last carriers are pilots of unitary amplitude.
Calculate the number of transmitted OFDM symbols
Solution in Python:
Compute the number of carriers by finding the where the cyclic prefix repeats

```Python
cp0 = r[0]

for i in range(1, len(r)):
    if r[i] == cp0:
        break
print(f"Number of carriers: {i}")
N=i
```

Compute the number of transmitted OFDM symbols

```Python
n_symbols = len(y) // N
print(f"Number of transmitted OFDM symbols: {n_symbols}")
```

- 3
## A wireless digital transmission system is based on OFDM. All carriers are modulated with 8-DPSK and unitary amplitude. The noise power is negligible. Assuming perfect synchronism, the samples of the received signal are:

```Python
r=[0.3+0.6j, 0.8-0.2j, -0.1+0.6j   0.3+0.6j   0.8-0.2j, -0.6-1j, -0.3+0.1j, -0.03-0.1j, -0.6-1j   -0.3+0.1j, -0.5-0.8j, 0.3+0.04j   0.1-0.6j   -0.5- 0.8j   0.3+0.04j, -0.6-1j, -0.3+0.1j, -0.03-0.1j, -0.6-1j   -0.3+0.1j, -0.3-0.6j, -0.8+0.2j   0.1-0.6j   -0.3-0.6j   -0.8+0.2j, 0.3+0.6j, 0.8-0.2j   - 0.1+0.6j   0.3+0.6j   0.8-0.2j, -0.5-0.8j,   0.3+0.04j   0.1-0.6j   -0.5-0.8j   0.3+0.04j]
```

The output of the receiver, once the cyclic prefix has been eliminated and before equalising is:

```Python
y=[0.35+0.35j    -0.5+0j   0+0.25j   -0.35-0.35j    0.5-0j    -0.17+0.17j    0-0.5j    0.35-0.35j   -0.17+0.17j    -0.35-0.35j    0.5-0j    - 0.17+0.17j   -0.35-0.35j    +0.5+0j   -0.25j    0.35+0.35j    -0.5+0j   0+0.25j, 0-0.5j    0.35-0.35j   -0.17+0.17j]
```

Calculate the total transmitted bandwidth (MHz) if we want to have an effective transmission rate of 27Mbps.

- 20 MHz
## A wireless digital transmission system is based on OFDM. All carriers are modulated with 8-DPSK and unitary amplitude. The noise power is negligible. Assuming perfect synchronism, the samples of the received signal are:

```python
r = [0.8-0.2j, -0.1+0.6j, 0.3+0.6j, 0.8-0.2j, -0.3+0.1j, -0.03-0.1j, -0.6-1j, -0.3+0.1j, 0.3+0.04j, 0.1-0.6j, -0.5-0.8j, 0.3+0.04j, -0.3+0.1j, -0.03-0.1j, -0.6-1j, -0.3+0.1j, -0.8+0.2j, 0.1-0.6j, -0.3-0.6j, -0.8+0.2j, 0.8-0.2j, -0.1+0.6j, 0.3+0.6j, 0.8-0.2j]
```

The output of the receiver, once the cyclic prefix has been eliminated and before equalising is:

```python
y = [0.35+0.35j, -0.5+0j, 0+0.25j, -0.35-0.35j, 0.5-0j, -0.17+0.17j, 0-0.5j, 0.35-0.35j, -0.17+0.17j, -0.35-0.35j, 0.5-0j, -0.17+0.17j, -0.35-0.35j, 0.5+0j, -0.25j, 0.35+0.35j, -0.5+0j, 0+0.25j]
```

Calculate the number of carriers in the signal

- 3
## A wireless digital transmission system is based on OFDM. All carriers are modulated with 8-DPSK. The noise power is negligible. Assuming perfect synchronism, the samples of the received signal are:

```Python
r=[0.1+0.5j, -0.7+0.3j, -0.1+0.6j, 0.1+0.5j, -0.7+0.3j, -0.6-1j, -0.3+0.1j, -0.03-0.1j, -0.6-1j, -0.3+0.1j, -0.5-0.8j, 0.3+0.04j, 0.1-0.6j, -0.5-0.8j, 0.3+0.04j, -0.6-1j, -0.3+0.1j, -0.03-0.1j, -0.6-1j, -0.3+0.1j, -0.3-0.6j, -0.8+0.2j, 0.1-0.6j, -0.3-0.6j, -0.8+0.2j, 0.3+0.6j, 0.8-0.2j, -0.1+0.6j, 0.3+0.6j, 0.8-0.2j, -0.5-0.8j, 0.3+0.04j, 0.1-0.6j, -0.5-0.8j, 0.3+0.04j]
```

The output of the receiver, once the cyclic prefix has been eliminated and before equalising is:

```Python
y=[0.35-0.35j, -0.5+0j, 0-0.25j, -0.35-0.35j, 0.5-0j, -0.17+0.17j, 0+0.5j, 0.35-0.35j, -0.17+0.17j, -0.35-0.35j, 0.5-0j, -0.17+0.17j, -0.35-0.35j, +0.5+0j, -0.25j, 0.35+0.35j, -0.5+0j, 0+0.25j, 0-0.5j, 0.35-0.35j, -0.17+0.17j]
```

Calculate the number of carriers in the signal

Solution in Python:

```Python
cp0 = r[0]

for i in range(1, len(r)):
    if r[i] == cp0:
        break
print(f"Number of carriers: {i}")
N=i
print(f"Number of carriers: {N}")

```

- 3
## A wireless digital transmission system is based on OFDM. All carriers are modulated with DQPSK. The noise power is negligible. Assuming perfect synchronism, the samples of the received signal are:

```Python
r = [1.07+0.5j, -0.06+0.24j, -0.71-0.53j, 1.16+1.16j, 0.49-0.35j, -1.16+0.31j, 1.07+0.5j, -0.06+0.24j, -0.71-0.53j, -0.16-0.83j, 0.03-0.38j, 0.29-0.47j, 0.5+0.83j, 0.87-0.18j, -0.53+1.05j, -0.16-0.83j, 0.03-0.38j, 0.29-0.47j, 0.16-0.16j, -0.37+0.38j, 0.7-0.67j, 0.16+0.16j, 0.12+1.34j, 0.2-1.05j, 0.16-0.16j, -0.37+0.38j, 0.7-0.67j]
```

The output of the receiver, once the cyclic prefix has been eliminated and before equalising is:

```Python
y = [0.3+0j, 0.1+0.1j, 0.9-0.3j, -0.4+1.2j, 1.5+1.5j, 0+0.6j, 0.1+0j, 0.6+0.2j, -0.3-0.3j, -0.4+1.2j, 0.5+0.5j, 0+0.6j, 0.1+0j, 0.2+0.2j, 0.9+0.3j, -0.4-0.4j, -1.5-0.5j, 0+0.6j]
```

Calculate the number of transmitted OFDM symbols.

- 3
## A wireless digital transmission system is based on OFDM. All carriers are modulated with DQPSK. The total transmitted bandwidth is 22 MHz. The channel has exponential PDP and a Delay Spread of 4µs.

The number of carriers is designed to assure that each one of them is a narrowband transmission and FFTs are used in the transmission and reception procedures, assuming the bandwidth of each carrier equal to the carrier spacing.
Calculate the effective transmission rate (Mbps) if the system is adequately protected against multipath propagation, 24 carriers (12 in each side of the band) are used as guard band and 1 in every 10 carriers (the rest without the guard band) are used as pilots for channel estimation.

- 35.6 Mbps
## A wireless digital transmission system is based on OFDM. All carriers are modulated with QPSK. The effective data rate is 100 Mbps. The guard interval is 1/5 of the total OFDM symbol duration and protects the system from multipath effects for channels with exponential PDP and a coherence bandwidth of 79.5 kHz or more.

Calculate the number of carriers of the signal.

<!-- Complete solution in Python:

```Python
import numpy as np

Rb = 100e6
BWc = 79.5e3
Tsym = 1 / Rb
Tg = Tsym / 5

T_sp=Tsym-Tg
N=T_sp*Rb-1
print(N)
``` -->

- 500
## A wireless digital transmission system is based on OFDM. All carriers are modulated with Tt/4-DQPSK The total transmitted bandwidth is 4.5 MHz. The duration of the OFDM symbols is 3.2ms and the guard interval is 3/8 of the total OFDM symbol.

Calculate the maximum carrier frequency (MHz) of the transmitted signal in order to fulfil the Doppler rule if the receiver is movin at 54km/h.

Solution in Python:

```Python
import numpy as np

BW = 4.5e6
Tofdm = 3.2e-3
gb = 3 / 8
v = 54 * 1000 / 3600

Delta = gb * Tofdm

N = BW * (Tofdm - Delta) - 1

rsp = BW / (1 + N)
fd = 0.01 * rsp

f = fd * 3e8 / v

print(f / 1e6)
```

- 100 MHz
## A wireless digital transmission system is based on OFDM. All carriers are modulated with π/4-DQPSK. The total transmitted bandwidth is 10 MHz. The channel has exponential PDP and a Delay Spread of 5µs.

Calculate the minimum number of carriers required to assure that each one of them can be considered narrowband and we want to use FFTs in the transmission and reception procedures. Assume the bandwidth of each carrier equal to the carrier spacing.

- 512
## A wireless digital transmission system is based on OFDM. The noise power is negligible. Assuming perfect synchronism, the samples of the received signal are:

```Python
r=[-0.5-0.1j, 0.7-0.1j, 0.3+0.6j, 0.8-0.2j, -0.3+0.1j, -0.03-0.1j, -0.5-0.1j, 0.7-0.1j, -0.6-1j, -0.3-0.1j, -0.5-0.8j,  0.3+0.04j, - 0.3+0.1j, -0.03-0.1j, -0.6-1j, -0.3-0.1j, 0.3+0.6j, 0.8-0.2j, -0.3-0.6j, -0.8+0.2j, 0.8-0.2j, -0.1+0.6j, 0.3+0.6j, 0.8-0.2j]
```

The output of the receiver, once the cyclic prefix has been eliminated and before equalising is:

```Python
y=[-0.084+0.084j, 0.122+0.367j, -0.48-0.16j, 0.197-0.193 0.707+0.703 0.2+0j, 0.254-0.084 -0.367+0.367j, 0.48j, 0.197-0.593j, -0.707+0.707j, 0.2-0j, 0.254+0.254j, 0.367-0.123 0.48+0.48j, -0.593+0.593 0+1j]
```

The total available transmission bandwidth is **_14 MHz._** The first and the last carriers are pilots of unitary amplitude.
The modulation of each carrier is adapted using the bit loading procedure of the water filling algorithm. Calculate the maximum effective transmission rate (Mbps) if the SNR of the first non-pilot frequency carrier is 25dB while the SNR of the rest of all the non-pilot carriers is 41dB.
![[Pasted image 20240613121254.png]]

Complete solution in Python:

```Python
import numpy as np

r = [
    -0.5 - 0.1j,
    0.7 - 0.1j,
    0.3 + 0.6j,
    0.8 - 0.2j,
    -0.3 + 0.1j,
    -0.03 - 0.1j,
    -0.5 - 0.1j,
    0.7 - 0.1j,
    -0.6 - 1j,
    -0.3 - 0.1j,
    -0.5 - 0.8j,
    0.3 + 0.04j,
    -0.3 + 0.1j,
    -0.03 - 0.1j,
    -0.6 - 1j,
    -0.3 - 0.1j,
    0.3 + 0.6j,
    0.8 - 0.2j,
    -0.3 - 0.6j,
    -0.8 + 0.2j,
    0.8 - 0.2j,
    -0.1 + 0.6j,
    0.3 + 0.6j,
    0.8 - 0.2j,
]

y = [
    -0.084 + 0.084j,
    0.122 + 0.367j,
    -0.48 - 0.16j,
    0.197 - 0.193,
    0.707 + 0.703,
    0.2 + 0j,
    0.254 - 0.084 - 0.367 + 0.367j,
    0.48j,
    0.197 - 0.593j,
    -0.707 + 0.707j,
    0.2 - 0j,
    0.254 + 0.254j,
    0.367 - 0.123,
    0.48 + 0.48j,
    -0.593 + 0.593,
    0 + 1j,
]

BW = 14e6
SNR_0 = 25
SNR = 41
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

b2 = np.floor(0.5 * np.log2(1 + 10 ** (SNR_0 / 10)))
b_345 = np.floor(0.5 * np.log2(1 + 10 ** (SNR / 10)))
r_sp = BW / (N + 1)
rb_eff2 = r_sp * b2 * N / M
print(rb_eff2 / 1e6)
rb_eff345 = r_sp * N * (N - 3) * b_345 / M
print(rb_eff345 / 1e6)
rb_eff = rb_eff2 + rb_eff345
print(rb_eff / 1e6)
```

- 33 Mbps
## A wireless digital transmission system is based on OFDM. The noise power is negligible. Assuming perfect synchronism, the samples of the received signal are:

```Python
r=[-0.5-0.1j, 0.7-0.1j, 0.3+0.6j, 0.8-0.2j, -0.3+0.1j, -0.03-0.1j, -0.5-0.1j, 0.7-0.1j, -0.6-1j, -0.3-0.1j, -0.5-0.8j, 0.3+0.04j, -0.3+0.1j, -0.03-0.1j, -0.6-1j, -0.3-0.1j, 0.3+0.6j, 0.8-0.2j, -0.3-0.6j, -0.8+0.2j, 0.8-0.2j, -0.1+0.6j, 0.3+0.6j, 0.8-0.2j]
```

The output of the receiver, once the cyclic prefix has been eliminated and before equalising is:

```Python
y=[0-0.2j, -0.084+0.084j, 0.122+0.367j, -0.48-0.16j, 0.197-0.197j, 0.707+0.707j, 0.2+0j, 0.254-0.084j, -0.367+0.367j, -0.16- 0.48j, 0.197-0.593j, -0.707+0.707j, 0.2-0j, 0.254+0.254j, 0.367-0.122j    0.48+0.48j, -0.593+0.593j, 0+1j]
```

The total available transmission bandwidth is 14 MHz. The first and the last carriers are pilots of unitary amplitude.    The modulation of each carrier is adapted using the bit loading procedure of the water filling algorithm. Calculate the maximum effective transmission rate (Mbps) if the SNR of the first non-pilot frequency carrier is 26dB while the SNR of the rest of all the non-pilot carriers is 42dB.

- 33 Mbps
## A wireless digital transmission system is based on OFDM. The signal is transmitted in the 2.4GHz band. All carriers are modulated with Pi/4-DQPSK. The total transmitted bandwidth is 22 MHz. The channel has exponential PDP and a Delay Spread of 4us.

The number of carriers is designed to assure that each one of them is a narrowband transmission and FFTs are used in the transmission and reception procedures, assuming the bandwidth of each carrier equal to the carrier spacing.
Calculate the maximum speed of a moving receiver (km/h) in order to fulfil the Doppler.

- 96.6 km/h
## A wireless digital transmission system is based on OFDM. The signal is transmitted in the 2.4GHz band. All carriers are modulated with π/4- DQPSK. The total transmitted bandwidth is 22 MHz.

The channel has exponential PDP and a Delay Spread of 4µs. The number of carriers is designed to assure that each one of them is a narrowband transmission and FFTs are used in the transmission and reception procedures, assuming the bandwidth of each carrier equal to the carrier spacing.
Calculate the maximum speed of a moving receiver (km/h) in order to fulfil the Doppler

Solution in Python:

```Python
import numpy as np
import math

bandwidth = 22e6  # 10 MHz
delay_spread = 4e-6  # 5 µs
band = 2.4e9  # 5GHz

n = (bandwidth*2*math.pi*delay_spread)-1
nn = np.ceil(n)
N = 2 ** np.ceil(np.log2(nn))
deltaF = bandwidth/(N+1)
v = (0.01*deltaF*3e8)/(band)
v_km = v*(3600/1000)
print(f"The maximum moving speed of the receiver is: {v} m/s")
print(f"The maximum moving speed of the receiver is: {v_km:.4f} km/h")
```

- 96.6 km/h
## Assess whether the following sentence is TRUE or FALSE:

If the same shaping pulse is used, the PAPR of a signal generated with a 16-QAM modulation is higher than the one generated with an O-QPSK modulation.

- True
## Consider a mobile wireless digital transmission system using CDMA

The base station transmits in the downlink using BPSK modulation. It applies OVSF codes for all transmissions. Assuming perfect synchronism and ideal amplification to compensate channel fading, calculate the bit error probability in the downlink assuming that the Eb/No is 5dB.

Solution in Python:

```Python
from scipy.special import erfc
import numpy as np

EbNo_dB = 5

EbNo = 10 ** (EbNo_dB / 10)

BER = 0.5 * erfc(np.sqrt(EbNo))

print(BER)
```

- 0.0065
## Consider a mobile wireless digital transmission system using CDMA.

The base station transmits in the downlink using BPSK modulation. It applies OVSF codes for all transmissions. Assuming perfect
synchronism and ideal amplification to compensate channel fading, a certain user receives the samples shown in vector r, each one of
them corresponding to one chip. Calculate the bits delivered to the upper layer of a user that has been assigned the code

```Python
r(t)=[2.3 -1.2 3.1 -4.2 1.3 -2.1 2.8 1.9 -2.7 7.1 1.1 -4.2 5.1 -1.2 3.1 -6.4 7.3 -5.2 2.6 -5.7 2.3 4.3-3.2 5.2 -4.2 -4.4 5.3 7.6 -4.9 3.6 -1.1 0.5]
```

- 10
## Consider a mobile wireless digital transmission system using CDMA.

The base station transmits in the downlink using BPSK modulation. It applies OVSF codes for all transmissions. Assuming perfect synchronism and ideal amplification to compensate channel fading, a certain user receives the samples shown in vector r, each one of them corresponding to one chip. Calculate the bits delivered to the upper layer of a user that has been assigned the code Cch16,13

```Python
r = [
    1.1929,
    -0.8028,
    -1.2656,
    -0.1493,
    -1.6364,
    0.0173,
    0.8284,
    0.2177,
    -1.9092,
    -0.5368,
    0.3020,
    1.8136,
    0.9149,
    -0.0571,
    1.3094,
    -1.0447,
    -0.3483,
    1.4126,
    0.7932,
    -0.8984,
    0.15621,
    1.5024,
    0.7304,
    0.4908,
    -0.5861,
    0.7449,
    -0.8282,
    0.5745,
    0.2818,
    1.1393,
    -0.4259,
    0.6361,
    0.7932,
    -0.8984,
    0.1562,
]
```

Solution in Python:

```Python
from scipy.special import erfc
import numpy as np
from scipy.linalg import hadamard
from rich.console import Console
from rich.columns import Columns
from rich.table import Table


def row_to_val(row):
    # computes the value to be able to propery sort the hadamard matrix
    return sum([10**i * (1 if x > 0 else 0) for i, x in enumerate(row[::-1])])


def sort_matrix(m):
    return sorted(m, key=row_to_val)[::-1]


def decode_signal(signal, m):
    # Decodes a BPSK signal
    lm = len(m)
    code = {0: "x", 1: 1, -1: 0}
    return [
        [
            int(sum([signal[i * lm + j] * m[k][j] for j in range(lm)]) / lm > 0)
            for i in range(len(signal) // lm)
        ]
        for k in range(lm)
    ]


def print_ovsf(arr):
    # Pretty printing for the ovsf codes
    table = Table(show_edge=True, show_lines=True)
    table.add_column("Index")
    table.add_column("Code")
    for n, row in enumerate(arr):
        table.add_row(str(n), str(row))
    return table


def print_data(arr):
    # Pretty printing of the decoded signal
    table = Table(show_lines=True)
    table.add_column("Index")
    table.add_column("Data")
    for n, row in enumerate(arr):
        table.add_row(str(n), "".join([str(x) for x in row]))
    return table


console = Console()

r = [
    1.1929,
    -0.8028,
    -1.2656,
    -0.1493,
    -1.6364,
    0.0173,
    0.8284,
    0.2177,
    -1.9092,
    -0.5368,
    0.3020,
    1.8136,
    0.9149,
    -0.0571,
    1.3094,
    -1.0447,
    -0.3483,
    1.4126,
    0.7932,
    -0.8984,
    0.15621,
    1.5024,
    0.7304,
    0.4908,
    -0.5861,
    0.7449,
    -0.8282,
    0.5745,
    0.2818,
    1.1393,
    -0.4259,
    0.6361,
    0.7932,
    -0.8984,
    0.1562,
]

Gp = 16
H = hadamard(Gp)
print(H)

sorted_H = np.array(sort_matrix(H))
print(sorted_H)

columns = Columns()
columns.add_renderable(print_ovsf(sorted_H))

print("numero de bits:", len(r) // len(sorted_H))
columns.add_renderable(print_data(decode_signal(r, sorted_H)))
console.print(columns)
```

- 10
## Consider a mobile wireless digital transmission system using CDMA.

The base station transmits in the downlink using BPSK modulation. It applies OVSF codes for all transmissions. Assuming perfect synchronism and ideal amplification to compensate channel fading, a certain user receives the samples shown in vector r, each one of them corresponding to one chip. Calculate the bits delivered to the upper layer of a user that has been assigned the code Cch8,6

```Python
r(t)=[-0.2438 -0.8976 -0.7923 -0.9530 0.3539 1.5970 0.5275 0.8542 1.3418 -2.4995 -0.1676 0.3530 0.7173 -1.3049 -1.0059 0.7907 -0.1166 0.5531 -0.9606 -1.6338 0.7612 1.1933 1.6321 -1.5322 -1.3369 -1.4738 -0.0417 -0.6155 1.3142 -1.4551 -1.7423 0.2053]
```

- 0101
## Consider a mobile wireless digital transmission system using CDMA.

The base station transmits in the downlink using BPSK modulation. It applies OVSF codes for all transmissions. Assuming perfect synchronism and ideal amplification to compensate channel fading, a certain user receives the samples shown in vector r, each one of them corresponding to one chip. Calculate the bits delivered to the upper layer of a user that has been assigned the code Cch8,6

```Python
r=[-0.2438,-0.8976, -0.7923, -0.9530, 0.3539, 1.5970, 0.5275, 0.8542, 1.3418, -2.4995, -0.1676, 0.3530,
0.7173, -13049, -1.0059, 0.79071, -0.1166, 0.5531, -0.9606, -1.6338, 0.7612, 1.1933, 1.6321, -1.5322,-1.3369,
-1.4738, -0.0417, -0.6155, 1.3142, -1.4551, -1.7423, 0.2053]
```

Solution in Python:

```Python
from scipy.special import erfc
import numpy as np
from scipy.linalg import hadamard
from rich.console import Console
from rich.columns import Columns
from rich.table import Table


def row_to_val(row):
    # computes the value to be able to propery sort the hadamard matrix
    return sum([10**i * (1 if x > 0 else 0) for i, x in enumerate(row[::-1])])


def sort_matrix(m):
    return sorted(m, key=row_to_val)[::-1]


def decode_signal(signal, m):
    # Decodes a BPSK signal
    lm = len(m)
    code = {0: "x", 1: 1, -1: 0}
    return [
        [
            int(sum([signal[i * lm + j] * m[k][j] for j in range(lm)]) / lm > 0)
            for i in range(len(signal) // lm)
        ]
        for k in range(lm)
    ]


def print_ovsf(arr):
    # Pretty printing for the ovsf codes
    table = Table(show_edge=True, show_lines=True)
    table.add_column("Index")
    table.add_column("Code")
    for n, row in enumerate(arr):
        table.add_row(str(n), str(row))
    return table


def print_data(arr):
    # Pretty printing of the decoded signal
    table = Table(show_lines=True)
    table.add_column("Index")
    table.add_column("Data")
    for n, row in enumerate(arr):
        table.add_row(str(n), "".join([str(x) for x in row]))
    return table


console = Console()

r = [
    -0.2438,
    -0.8976,
    -0.7923,
    -0.9530,
    0.3539,
    1.5970,
    0.5275,
    0.8542,
    1.3418,
    -2.4995,
    -0.1676,
    0.3530,
    0.7173,
    -13049,
    -1.0059,
    0.79071,
    -0.1166,
    0.5531,
    -0.9606,
    -1.6338,
    0.7612,
    1.1933,
    1.6321,
    -1.5322,
    -1.3369,
    -1.4738,
    -0.0417,
    -0.6155,
    1.3142,
    -1.4551,
    -1.7423,
    0.2053,
]

Gp = 8
H = hadamard(Gp)
print(H)

sorted_H = np.array(sort_matrix(H))
print(sorted_H)

columns = Columns()
columns.add_renderable(print_ovsf(sorted_H))

print("numero de bits:", len(r) // len(sorted_H))
columns.add_renderable(print_data(decode_signal(r, sorted_H)))
console.print(columns)
```

- 0101
## Consider a mobile wireless digital transmission system using CDMA.

The base station transmits in the downlink using BPSK modulation. It applies OVSF codes for all transmissions. Assuming perfect synchronism and ideal amplification to compensate channel fading, calculate the bit error probability in the downlink assuming that the Eb/No is 4dB.

Solution in Python:

```Python
from scipy.special import erfc
import numpy as np

EbNo_dB = 4

EbNo = 10 ** (EbNo_dB / 10)

BER = 0.5 * erfc(np.sqrt(EbNo))

print(BER)
```

- 0.012
## Consider a mobile wireless digital transmission system using CDMA.

The base station transmits in the downlink using BPSK modulation. It applies OVSF codes for all transmissions. Assuming perfect synchronism and ideal amplification to compensate channel fading, calculate the bit error probability in the downlink assuming that the Eb/No is 6dB.

Solution in Python:

```Python
from scipy.special import erfc
import numpy as np

EbNo_dB = 6

EbNo = 10 ** (EbNo_dB / 10)

BER = 0.5 * erfc(np.sqrt(EbNo))

print(BER)
```

- 0.0025
## Consider a mobile wireless digital transmission system using CDMA. The uplink signal is transmitted by each user modulated with BPSK using a raised cosine shaping pulse with a 10% roll-off while occupying a total bandwidth of 176 MHz. The noise at the input of the receiver has an spectral density of No= 5,10-18W/Hz. Consider a propagation model depending on the distance L(dB) 23 + 3210g(d) where d is the distance in metres. The maximum transmission power of each mobile terminal is 27dBm. The antenna of the base station has a gain of 13 dBi, while the antennae of the mobile terminals are assumed to be isotropic.

The cell is assumed to be circular with a radius Of 1.Ikm and populated with a uniform user density while all users have an activity factor of 60%. Calculate the maximum user density (users/km?) if we want all users to have a 400kbps transmission rate in the uplink (assumed equal for all of them), PN spreading codes are used and all users in the cell must be served with an average bit error probability lower than 12,10-3. The power control assures that the received power for all users is always equal to the one using the maximum transmission power for users in the cell edge.

- 31
## Consider a mobile wireless digital transmission system using CDMA. The uplink signal is transmitted by each user modulated with BPSK using a raised cosine shaping pulse with a 35% roll-off while occupying a total bandwidth of 27 MHz. The noise at the input of the receiver has an spectral density of No: 2,10-17W/Hz. Consider a propagation model depending on the distance L(dB) = 22 + 3110g(d) where d is the distance in metres. The maximum transmission power of each mobile terminal is 33dBm. The antenna of the base station has a gain of 9 dBi, while the antennae of the mobile terminals are assumed to be isotropic.

The cell is assumed to be circular with a radius of 935m and populated with a uniform user density of 27 uslkm2 while all users have an activity factor of 30%. PN spreading codes are used and all users in the cell must be served with an average bit error probability lower than 3.5•10-3. The power control assures that the received power for all users is always equal to the one using the maximum transmission power for users in the cell edge.
A narrowband interference appears within the useful signal band. This interference signal arrives at the base station with a power of -63dBm.
Calculate the maximum transmission rate for all users.
![[Pasted image 20240613204146.png]]
![[Pasted image 20240613204203.png]]
- 155038 bps
## Consider a mobile wireless digital transmission system using CDMA. The uplink signal is transmitted by each user modulated with BPSK using a raised cosine shaping pulse with a 45% roll-off while occupying a total bandwidth of 29 MHz. The noise at the input of the receiver has an spectral density of N = 2·10 W/Hz. Consider a propagation model depending on the distance L(dB) = 23 + 31log(d) where d is the distance in metres. The maximum transmission power of each mobile terminal is 31dBm. The antenna of the base station has a gain of 12 dBi, while the antennae of the mobile terminals are assumed to be isotropic.

The cell is assumed to be circular with a radius of 935m and populated with a uniform user density while all users have an activity factor of 60%. Calculate the maximum user density (users/km ) if we want all users to have a 200kbps transmission rate in the uplink (assumed equal for all of them), PN spreading codes are used and all users in the cell must be served with an average bit error probability lower than 3.5·10 . The power control assures that the received power for all users is always equal to the one using the maximum transmission power for users in the cell edge.

- 13.5
## Consider a mobile wireless digital transmission system using CDMA. The uplink signal is transmitted by each user modulated with BPSK using a raised cosine shaping pulse with a 55% roll-off while occupying a total bandwidth of 31 MHz. The noise at the input of the receiver has an spectral density of N = 2·10 W/Hz. Consider a propagation model depending on the distance L(dB) = 20 + 31log(d) where d is the distance in metres. The maximum transmission power of each mobile terminal is 30dBm. The antenna of the base station has a gain of 10 dBi, while the antennae of the mobile terminals are assumed to be isotropic.

The cell is assumed to be circular with a radius of 935m and populated with a uniform user density of 54 us/km while all users have an activity factor of 15%. PN spreading codes are used and all users in the cell must be served with an average bit error probability lower than 3.5·10 . The power control assures that the received power for all users is always equal to the one using the maximum transmission power for users in the cell edge.
A narrowband interference appears within the useful signal band. This interference signal arrives at the base station with a power of - 63dBm.
Calculate the maximum transmission rate for all users.
Note: You can use bps, kbps or Mbps as units. Write the units after the number.

- 155038 bps
## How is the SNR of each carrier affected by the equalisation process in a wireless communications system based on OFDM?

- Remains constant
## How many antennas are active at any specific instant when applying a Spatial Modulation technique in wireless communications?

- 1
## In a wireless communications system based on OFDM, which is the maximum duration (in the time domain) of a symbol?

- Coherence time
## The 5G communications system new features are represented in a triangle. The three features are the URLLC (Ultra-reliable and Low Latency Communications), the MMTC (Massive Machine Type Communications) and a third one. Which is this third one?

- EMBB
## The figure represents the in-phase and quadrature components of a wireless digital signal generated with a 8-DPSK modulation, The transmission rate is 6 Mbps,

![[Pasted image 20240614121313.png]]
Because of an external interference, the symbol at t/T=5 (and only this) reaches the receiver with an additional phaseshift Of +100.
Calculate the corresponding received bits from until t=7Ts if the table Of the modulation is:

| Bits | $\Delta\Phi$ |
| ---- | ------------ |
| 000  | 45           |
| 001  | 225          |
| 010  | 180          |
| 011  | 0            |
| 100  | 90           |
| 101  | 270          |
| 110  | 315          |
| 111  | 135          |

Solution in Python:

```Python
import numpy as np

inphase = [0.7, 0.7, 0, 1, -0.7, 0.7, -0.7, 0]
quad = [-0.7, 0.7, -1, 0, -0.7, -0.7, 0, -0.7]
channel_shift = 100
idx = 5

mod = {
    (0, 0, 0): 45,
    (0, 0, 1): 225,
    (0, 1, 0): 180,
    (0, 1, 1): 0,
    (1, 0, 0): 90,
    (1, 0, 1): 270,
    (1, 1, 0): 315,
    (1, 1, 1): 135,
}
demod = {v: k for k, v in mod.items()}

angle_rad = np.arctan2(quad, inphase)
angle_deg = np.rad2deg(angle_rad)

angle_deg[idx] += channel_shift

dangle = np.diff(angle_deg)

# mod 360
dangle = dangle % 360
print(dangle)


def get_closest(arr, val):
    return arr[np.argmin(np.abs(arr - val))]


bits = [demod[get_closest(list(mod.values()), angle)] for angle in dangle]

bits = [bit for bits in bits for bit in bits]

print("".join([str(bit) for bit in bits]))
```

- 100001100001010111100
## The figure represents the in-phase and quadrature components of a wireless digital signal generated with a 8-DPSK modulation. The transmission rate is 6 Mbps.

![[Pasted image 20240612201400.png]]
Due to the channel, all the signal reaches the receiver with a phase shift of 270°. In addition, the receiver has a frequency synchronisation error of 100 KHz. Calculate the corresponding received bits from t=0 until t=7·T if the table of the modulation is:

| Bits | ΔΦ   |
| ---- | ---- |
| 000  | 45º  |
| 001  | 315º |
| 010  | 180º |
| 011  | 90º  |
| 100  | 0º   |
| 101  | 270º |
| 110  | 225º |
| 111  | 135º |

- 011110011110011110011
## The figure represents the in-phase and quadrature components of a wireless digital signal generated with a 8-DPSK modulation. The transmission rate is 6 Mbps. Because of an external interference, the symbol at t/Tsym=5 (and only this) reaches the receiver with an additional phase shift of +100. Calculate the corresponding received bits from until if the table of the modulation is:

![[Pasted image 20240612115426.png]]

| Bits | $\Delta \Phi$ |
| ---- | ------------- |
| 000  | 45            |
| 001  | 225           |
| 010  | 180           |
| 011  | 0             |
| 100  | 90            |
| 101  | 270           |
| 110  | 315           |
| 111  | 135           |

Complete solution in Python:

```Python
import numpy as np

inphase =  [ 0.7,0.7, 0,1,-0.7, 0.7,-1, 0]
quad =     [-0.7,0.7,-1,0,-0.7,-0.7, 0,-1]

angle_rad = np.arctan2(quad, inphase)
angle_deg = np.rad2deg(angle_rad)

channel_shift = 100
idx = 5
angle_deg[idx] += channel_shift

mod = {
  (0, 0, 0): 45,
  (0, 0, 1): 225,
  (0, 1, 0): 180,
  (0, 1, 1): 0,
  (1, 0, 0): 90,
  (1, 0, 1): 270,
  (1, 1, 0): 315,
  (1, 1, 1): 135,
}

demod = {v: k for k, v in mod.items()}

dangle = np.diff(angle_deg)

# mod 360
dangle = dangle % 360
print(dangle)
def get_closest(arr, val):
    return arr[np.argmin(np.abs(arr - val))]

bits = [demod[get_closest(list(mod.values()), angle)]
        for angle in dangle]

bits = [bit for bits in bits for bit in bits]

print(''.join([str(bit) for bit in bits]))
```

- 100001100001010111100
## The figure represents the in-phase and quadrature components of a wireless digital signal generated with a 8-DPSK modulation\_ The transmission rate is 6 Mbps.

![[Pasted image 20240614121313.png]]
Due to the channel, all the signal reaches the receiver with a phase shift of 2700. In addition, the receiver has a frequency synchronisation error of 200 KHz.
Calculate the corresponding received bits from t=o until if the table of the modulation is:

| Bits | Value |
| ---- | ----- |
| 000  | 45    |
| 001  | 225   |
| 010  | 180   |
| 011  | 0     |
| 100  | 90    |
| 101  | 270   |
| 110  | 315   |
| 111  | 135   |

Solution in Python:

```Python
import numpy as np

inphase = [0.7, 0.7, 0, 1, -0.7, 0.7, -0.7, 0]
quad = [-0.7, 0.7, -1, 0, -0.7, -0.7, 0, -0.7]
rb = 6e6
channel_shift = 270
sync_err_coeff = 200e3 / rb*360
sync_err = np.array([i * sync_err_coeff for i in range(len(inphase))])
mod = {
    (0, 0, 0): 45,
    (0, 0, 1): 225,
    (0, 1, 0): 180,
    (0, 1, 1): 0,
    (1, 0, 0): 90,
    (1, 0, 1): 270,
    (1, 1, 0): 315,
    (1, 1, 1): 135,
}
demod = {v: k for k, v in mod.items()}

angle_rad = np.arctan2(quad, inphase)
angle_deg = np.rad2deg(angle_rad)

angle_deg += channel_shift
angle_deg += sync_err

dangle = np.diff(angle_deg)

# mod 360
dangle = dangle % 360
print(dangle)


def get_closest(arr, val):
    return arr[np.argmin(np.abs(arr - val))]


bits = [demod[get_closest(list(mod.values()), angle)] for angle in dangle]

bits = [bit for bits in bits for bit in bits]

print("".join([str(bit) for bit in bits]))
```

- 100001100001100001100
## The figure represents the in-phase and quadrature components of a wireless digital signal generated with a 8-DPSK modulation\_ The transmission rate is 6 Mbps.

![[Pasted image 20240614121313.png]]
Due to the channel, all the signal reaches the receiver with a phase shift of 2700. In addition, the receiver has a frequency synchronisation error of 200 KHz.
Calculate the corresponding received bits from t=o until if the table of the modulation is:

| Bits | Value |
| ---- | ----- |
| 000  | 45    |
| 001  | 315   |
| 010  | 180   |
| 011  | 90    |
| 100  | 0     |
| 101  | 270   |
| 110  | 225   |
| 111  | 135   |

Solution in Python:

```Python
import numpy as np

inphase = [0.7, 0.7, 0, 1, -0.7, 0.7, -0.7, 0]
quad = [-0.7, 0.7, -1, 0, -0.7, -0.7, 0, -0.7]
rb = 6e6
channel_shift = 270
sync_err_coeff = 200e3 / rb*360
sync_err = np.array([i * sync_err_coeff for i in range(len(inphase))])
mod = {
    (0, 0, 0): 45,
    (0, 0, 1): 315,
    (0, 1, 0): 180,
    (0, 1, 1): 90,
    (1, 0, 0): 0,
    (1, 0, 1): 270,
    (1, 1, 0): 225,
    (1, 1, 1): 135,
}
demod = {v: k for k, v in mod.items()}

angle_rad = np.arctan2(quad, inphase)
angle_deg = np.rad2deg(angle_rad)

angle_deg += channel_shift
angle_deg += sync_err

dangle = np.diff(angle_deg)

# mod 360
dangle = dangle % 360
print(dangle)


def get_closest(arr, val):
    return arr[np.argmin(np.abs(arr - val))]


bits = [demod[get_closest(list(mod.values()), angle)] for angle in dangle]

bits = [bit for bits in bits for bit in bits]

print("".join([str(bit) for bit in bits]))
```

- 011110011110011110011
## The figure represents the in-phase and quadrature components of a wireless digital signal generated with a raised cosine shaping pulse and a standard modulation with differential coding. The data rate is 6Mbps

![[Pasted image 20240614001842.png]]
Analyse the signal and deduct a possible applied modulation.
Note: there are more than one correct answer, write the qcronym of just one possible modulation

- 8DPSK
## The figure represents the in-phase and quadrature components of a wireless digital signal generated with rectangular shaping pulse and DQPSK modulation.

![[Pasted image 20240614115916.png]]
Because of an external interference, the symbol at t/T=4 (and only this) reaches the receiver with an additional phase shift of +220º.
Calculate the corresponding received bits from until t=10Ts if the table of the modulation is:

| Bits | $\Delta\Phi$ |
| ---- | ------------ |
| "00" | 90           |
| "01" | 270          |
| "10" | 180          |
| "11" | 0            |

Solution in Python:

```Python
import numpy as np

inphase = [0.7, -0.7, -0.7, 0.7, -0.7, 0.7, 0.7, -0.7, -0.7, 0.7, -0.7]
quad = [0.7, 0.7, -0.7, -0.7, 0.7, 0.7, 0.7, 0.7, -0.7, -0.7, 0.7]
channel_shift = 220
idx = 4

mod = {
    (0, 0): 90,
    (0, 1): 270,
    (1, 0): 180,
    (1, 1): 0,
}
demod = {v: k for k, v in mod.items()}

angle_rad = np.arctan2(quad, inphase)
angle_deg = np.rad2deg(angle_rad)

angle_deg[idx] += channel_shift

dangle = np.diff(angle_deg)

# mod 360
dangle = dangle % 360
print(dangle)


def get_closest(arr, val):
    return arr[np.argmin(np.abs(arr - val))]


bits = [demod[get_closest(list(mod.values()), angle)] for angle in dangle]

bits = [bit for bits in bits for bit in bits]

print("".join([str(bit) for bit in bits]))
```

- 00000011001100000010
## The following figure has been obtained in a receiver of a wireless communication system where multipath propagation is present. Asses whether the following sentence is True or False:

![[Pasted image 20240114175534.png]]
The multipath component has Iower power than the main signal.

- True
## The following figure has been obtained in a receiver of a wireless communication system where multipath propagation is present. Asses whether the following sentence is True or False:

![[Pasted image 20240114175534.png]]
The multipath component has the same phase as the main signal

- False
## The following figure has been obtained in a receiver of a wireless communication system where multipath propagation is present. Asses whether the following sentence is True or False:

![[Pasted image 20240114231352.png]]
The multipath component has much lower power than the main signal.

- False
## The following figure has been obtained in a receiver of a wireless communication system where multipath propagation is present. Asses whether the following sentence is True or False:

![[Pasted image 20240114232313.png]]
The PAPR of the signal without the multipath component, is 0 dB

- False
## The following figure has been obtained in a receiver of a wireless communication system where multipath propagation is present. Asses whether the following sentence is True or False:

![[Pasted image 20240114232705.png]]
The delay of the multipath signal must be lower than half the symbol time

- False
## The following figure has been obtained in a receiver of a wireless communication systems. Asses whether the following sentence is True or False:

![[Pasted image 20240114175240.png]]
The shaping pulse signal must be rectangular

- False
## The following figure has been obtained in a receiver of a wireless communication systems. Asses whether the following sentence is True or False:

![[Pasted image 20240612123118.png]]
The modulation of the signal can be 8-PSK

- False
## The following figure has been obtained in a receiver of a wireless communication systems. Asses whether the following sentence is True or False:

![[Pasted image 20240612123118.png]]
The shaping pulse signal must be rectangular

- False
## The following figure has been obtained in a receiver of a wireless communication systems. Asses whether the following sentence is True or False:

![[Pasted image 20240613235701.png]]
The PAPR of the transmitted Signal can be Improved by Increasing the bandwidth of the Signal.

- True
## The following figure has been obtained in a receiver of a wireless communication systems. Asses whether the following sentence is True or False:

![[Pasted image 20240613235701.png]]
The modulation of the signal can be Pi/4-DQPSK

- True
## The following figure has been obtained in a receiver of a wireless communication systems. Asses whether the following sentence is True or False:

![[Pasted image 20240613235701.png]]
The shaping pulse of the signal can be rectangular

- False
## The following figure has been obtained in a receiver of a wireless communication systems. Asses whether the following sentence is True or False:

![[Pasted image 20240613235701.png]]
The shaping pulse of the signal is be rectangular

- False
## The following figure has been obtained in a receiver of a wireless communication systems. Asses whether the following sentence is True or False:

![[Pasted image 20240614000236.png]]
The shaping pulse signal must be rectangular

- False
## The following figure has been obtained in a receiver of a wireless communication systems. Asses whether the following sentence is True or False:

![[Pasted image 20240614000236.png]]
The system cannot affected by a wtlite Gaussian noise

- False
## The following figure has been obtained in a wireless communication system where multipath propagation is present and the noise is negligible. The modulation has some symbols with unitary amplitude. Assess whether the following sentence is TRUE or FALSE

![[Pasted image 20240114233103.png]]
The shaping pulse of the signal may be rectangular.

- False
## The following figure has been obtained in a wireless communication system where multipath propagation is present. Assess whether the following sentence is TRUE or FALSE .

![[Pasted image 20240114175534.png]]
The PAPR of the signal is greater than 1

- True
## The following figure has been obtained in a wireless communication system where multipath propagation is present. Assess whether the following sentence is TRUE or FALSE .

![[Pasted image 20240114175534.png]]
The delay of the multipath signal must be greater than half of the symbol time.

- True
## The following figure has been obtained in a wireless communication system where multipath propagation is present. Assess whether the following sentence is TRUE or FALSE .

![[Pasted image 20240114232313.png]]
The delay of the multipath signal is lower than half of the symbol time

- False
## The following figure has been obtained in a wireless communication system where multipath propagation is present. Assess whether the following sentence is TRUE or FALSE .

![[Pasted image 20240114232313.png]]
The multipath component has significantly less power than the main signal.

- True
## The following figure has been obtained in a wireless communication system where multipath propagation is present. Assess whether the following sentence is TRUE or FALSE .

![[Pasted image 20240114232313.png]]
The multipath component has the same phase as the main signal.

- False
## The following figure has been obtained in a wireless communication system where multipath propagation is present. Assess whether the following sentence is TRUE or FALSE .

![[Pasted image 20240612142848.png]]
The multipath component has a diferent phase with respect to the main signal.

- True
## The following figure has been obtained in a wireless communication system where multipath propagation is present. Assess whether the following sentence is TRUE or FALSE .

![[Pasted image 20240612142848.png]]
The shaping pulse of the signal can not be rectangular

- False
## The following figure has been obtained in a wireless communication system where multipath propagation is present. Assess whether the following sentence is TRUE or FALSE.

![[Pasted image 20240612142848.png]]
The PAPR of the signal without the multipath component, may be greater than 1.

- True
## The following figure has been obtained in the receiver of a wireless communication system, Assess whether the following sentence is TRUE or FALSE

![[Pasted image 20240613234919.png]]
The shaping pulse of the signal cannot be rectangular.

- True
## The following figure has been obtained in the receiver of a wireless communication system. Assess whether the following sentence is TRUE or FALSE

![[Pasted image 20240612115108.png]]
The PAPR of the signal cannot be greater than 1

- False
## The following figure has been obtained in the receiver of a wireless communication system. Assess whether the following sentence is TRUE or FALSE

![[Pasted image 20240612115108.png]]
The modulation used in the system may be a 8-DPSK

- True
## The following figure has been obtained in the receiver of a wireless communication systems. Assess whether the

following sentence is TRUE or FALSE
![[Pasted image 20240114233246.png]]
The PAPR of the transmitted signal must be the optimal value.

- False
## The following figure has been obtained in the receiver of a wireless communication systems. Assess whether the following sentence is TRUE or FALSE

![[Pasted image 20240114233246.png]]
The modulation of the signal can be n/4-DQPSK

- True
## The following figure has been obtained in the receiver of a wireless communication systems. Assess whether the following sentence is TRUE or FALSE

![[Pasted image 20240612123118.png]]
The PAPR of the signal is greater than I

- True
## The following figure has been obtained in the receiver of a wireless communication systems. Assess whether the following sentence is TRUE or FALSE

![[Pasted image 20240613234337.png]]
The PAPR of the signal is greater than 1.

- True
## The following figure have been obtained in the receiver of a wireless communication system. Assess whether the following sentence is TRUE or FALSE

![[Pasted image 20240114175240.png]]
The PAPR of the transmitted signal must be the optimal value.

- False
## The following figure have been obtained in the receiver of a wireless communication system. Assess whether the following sentence is TRUE or FALSE

![[Pasted image 20240114175240.png]]
The modulation of the signal can be 16-QAM

- False
## The following figure have been obtained in the receiver of a wireless communication system. Assess whether the following sentence is TRUE or FALSE

![[Pasted image 20240114175240.png]]
The modulation of the signal can be Pi/4-DQPSK

- True
## The following figures have been obtained in the receiver of three wireless communication systems. Assess whether the following sentence is TRUE or FALSE

![[Pasted image 20240114231628.png]]
The three systems may be affected by a white Gaussian noise

- False
## The following figures have been obtained in the receiver of three wireless communications systems. Assess whether the following sentence is True or False.

![[Pasted image 20240114231628.png]]
The number of symbols and their allocated complex values can be the same for all systems.

- True
## The following figures have been obtained in the receiver of three wireless communications systems. Assess whether the following sentence is True or False.

![[Pasted image 20240114231628.png]]
The three systems may be affected by a white Gaussian noise

- False
## The following figures have been obtained in the receiver of three wireless communications systems. Assess whether the following sentence is True or False.

![[Pasted image 20240114231628.png]]
The transmission bandwidth of the three systems can be identical.

- True
## The following figures have been obtained in the receiver of three wireless communications systems. Assess whether the following sentence is True or False.

![[Pasted image 20240614001508.png]]
The PAPR of the transmitted signal in the three systems can be the optimal value.

- False
## The following figures have been obtained in the receiver of three wireless communications systems. Assess whether the following sentence is True or False.

![[Pasted image 20240614001508.png]]
The number of symbols and their allocated complex values can be the same for all systems.

- True
## The following figures have been obtained in the receiver of three wireless communications systems. Assess whether the following sentence is True or False.

![[Pasted image 20240614001508.png]]
The three signals may be affected by White Gaussian noise.

- True
## The following figures have been obtained in the receiver of two wireless communication systems. Assess whether the following sentence is TRUE or FALSE

![[Pasted image 20240612182522.png]]
The PAPR of the signal (a) is greater than the PAPR of the signal (b)

- False
## The following figures have been obtained in the receiver of two wireless communication systems. Assess whether the following sentence is TRUE or FALSE

![[Pasted image 20240613234208.png]]
The systems can be identical

- True
## The following figures have been obtained in the receiver of two wireless communication systems. Assess whether the following sentence is TRUE or FALSE

![[Pasted image 20240614000403.png]]
The PAPR of the signal in (a) can be lower than the one of the signal in (b).

- True
## The following figures have been obtained in the receiver of two wireless communications systems. Assess whether the following sentence is True or False.

![[Pasted image 20240114232907.png]]
The transmission bandwidth of the systems can be the same

- True
## The following figures have been obtained in two wireless communication systems where multipath propagation is present. Assess whether the following sentence is TRUE or FALSE .

![[Pasted image 20240612120014.png]] ![[Pasted image 20240612120027.png]]
The shaping pulse used in both systems is the same

- False
## The following figures have been obtained in two wireless communication systems where multipath propagation is present. Assess whether the following sentence is TRUE or FALSE .

![[Pasted image 20240612202420.png]]
The shaping pulse used in the first (up) signal must be the same as the one used in the second (down)

- False
## The following figures have been obtained in two wireless communication systems where multipath propagation is present. Assess whether the following sentence is TRUE or FALSE .

| ![[Pasted image 20240614104523.png]] | ![[Pasted image 20240614104604.png]] |
| ------------------------------------ | ------------------------------------ |

The shaping pulse used in both systems is the same

- False
## The new features of 5G wireless communications systems are represented in a triangle. The three main features are the URLLC (Ultra-reliable and Low Latency Communications), the EMB (Enhanced Mobile Broadband) and a third one. Which is this third one?

- MMTC
## There is a wirFeless digital transmission system whose global impulse response h(t) is the one shown in the figure. The transmission is made with BPSK modulation.

![[Pasted image 20240612141234.png]]
Assuming a transmission rate of 200kbps, calculate the SINR improving factor (dB) of a Zero Forcing LTE (4+2) equaliser.
Remember to put the result in dB!!

Solution in Python:

```Python

```

- 17.6 dB
## There is a wireless communications system that uses raised cosine shaping pulse and DQPSK modulation.

Calculate the approximate bit error probability of the system in the presence of an additive white Gaussian noise that generates a measured EB/No at the receiver of 6dB.

Solution in Python:

```Python
from scipy.special import erfc
import numpy as np

EbNo_dB = 6

EbNo = 10 ** (EbNo_dB / 10)

BER = erfc(np.sqrt(EbNo))

print(BER)
```

- 0.005
## There is a wireless communications system that uses raised cosine shaping pulse and DQPSK modulation.

Calculate the approximate bit error probability of the system in the presence of an additive white Gaussian noise that generates a measured Eb/No at the receiver of 4dB.

Solution in Python:

```Python
from scipy.special import erfc
import numpy as np

EbNo_dB = 4

EbNo = 10 ** (EbNo_dB / 10)

BER = erfc(np.sqrt(EbNo))

print(BER)
```

- 0.025
## There is a wireless digital transmission system that uses 16-DPSK modulation and a data rate of 16 Mbps.

Calculate the maximum frequency error (Hz) in the synchronisation mechanism of the receiver to assure that there are no errors in the received bits due to this problem in absence of noise.
Note: You can use Hz, kHz or MHz if you write the units after the number

Solution in Python:

```Python
import numpy as np

nsym = 16
Rb = 16e6
phase_sep = 360 / nsym
rs = Rb / np.log2(nsym)
Deltaf = phase_sep * rs / (2 * 360)
print(Deltaf)
```

- 125000Hz
## There is a wireless digital transmission system that uses 16-DPSK modulation and a data rate of 8 Mbps.

Calculate the maximum frequency error (Hz) in the synchronisation mechanism of the receiver to assure that there are no errors in the received bits due to this problem in absence of noise.
Note: You can use Hz, kHz or MHz if you write the units after the number

- 62500Hz
## There is a wireless digital transmission system that uses 8-DPSK modulation and a data rate of 16 Mbps.

Calculate the maximum frequency error (Hz) in the synchronisation mechanism of the receiver to assure that there are no errors in the received bits due to this problem in absence of noise.
Note: You can use Hz, kHz or MHz if you write the units after the number

- 333333
## There is a wireless digital transmission system that uses 8-DPSK modulation and a data rate of 16 Mbps.

Calculate the maximum frequency error (Hz) in the synchronisation mechanism of the receiver to assure that there are no errors in the received bits due to this problem in absence of noise.
Note: You can use Hz, kHz or MHz if you write the units after the number

Solution in Python:

```Python
import numpy as np

nsym = 8
Rb = 16e6
phase_sep = 360 / nsym
rs = Rb / np.log2(nsym)
Deltaf = phase_sep * rs / (2 * 360)
print(Deltaf)
```

- 333333Hz
## There is a wireless digital transmission system that uses 8-DPSK modulation with the table indicated below. At a reference symbol with value 0 in the in-phase component and 1 in the quadrature component is generated. Suppose absence of noise, matched filter at the receiver and perfect synchronism. The transmitter sends the sequence of bits "110010110010".

The channel generates a single echo (corresponding to a multipath propagation) that comes almost simultaneously and with the same power level as the main signal but with a phase shift of 10 degrees. The channel introduces an additional phase shift of 75 degrees to the overall received signal (both direct and echo signals).
Determine the value of the phase (in degrees within the interval 0-360), of the received signal at t=3Ts.

| Bits | ΔΦ  |
| ---- | --- |
| 000  | 90  |
| 001  | 270 |
| 010  | 180 |
| 011  | 0   |
| 100  | 45  |
| 101  | 315 |
| 110  | 135 |
| 111  | 225 |

Solution in Python:

```Python
import numpy as np

# Initialize variables
msg = "110010110010"
channel = 75
echo = 10
iphase0 = 0
quad0 = 1
angle_0 = np.arctan2(quad0, iphase0) * 180 / np.pi

# Define modulation dictionary
mod = {
    (0, 0, 0): 90,
    (0, 0, 1): 270,
    (0, 1, 0): 180,
    (0, 1, 1): 0,
    (1, 0, 0): 45,
    (1, 0, 1): 315,
    (1, 1, 0): 135,
    (1, 1, 1): 225,
}

# Calculate symbol angles
sym_ang = [angle_0] + [
    mod[tuple(map(int, msg[i : i + 3]))] for i in range(0, len(msg), 3)
]

# Calculate cumulative sum of angles
angle = np.cumsum(sym_ang) + channel + echo / 2

# Normalize angle to be within [0, 360)
angle = angle % 360

# Print the fourth element of the angle array
print(angle[3])
```

- 260
## There is a wireless digital transmission system that uses 8-DPSK modulation with the table indicated below. At a reference symbol with value 1 in the in-phase component and -1 in the quadrature component is generated. Suppose absence of noise, matched filter at the receiver and perfect synchronism. The transmitter sends the sequence Of bits "100101011010101"

The channel generates a single echo (corresponding to a multipath propagation) that comes almost simultaneously and with the same power level as the main signal but with a phase shift of 8 degrees. The channel introduces an additional phase shift of 96 degrees to the overall received signal (both direct and echo signals).
Determine the value of the phase (in degrees within the interval 0-360), of the received signal at t=3Ts.

| Bits | ΔΦ  |
| ---- | --- |
| 000  | 45  |
| 001  | 270 |
| 010  | 225 |
| 011  | 315 |
| 100  | 90  |
| 101  | 180 |
| 110  | 135 |
| 111  | 0   |

Solution in Python:

```Python
import numpy as np

# Initialize variables
msg = "100101011010101"
channel = 96
echo = 8
iphase0 = 1
quad0 = -1
angle_0 = np.arctan2(quad0, iphase0) * 180 / np.pi

# Define modulation dictionary
mod = {
    (0, 0, 0): 45,
    (0, 0, 1): 270,
    (0, 1, 0): 225,
    (0, 1, 1): 315,
    (1, 0, 0): 90,
    (1, 0, 1): 180,
    (1, 1, 0): 135,
    (1, 1, 1): 0,
}

# Calculate symbol angles
sym_ang = [angle_0] + [
    mod[tuple(map(int, msg[i : i + 3]))] for i in range(0, len(msg), 3)
]

# Calculate cumulative sum of angles
angle = np.cumsum(sym_ang) + channel + echo / 2

# Normalize angle to be within [0, 360)
angle = angle % 360

# Print the fourth element of the angle array
print(angle[3])
```

- 280
## There is a wireless digital transmission system that uses 8-DPSK modulation with the table indicated below. At a reference symbol with value 1 in the in-phase component and 1 in the quadrature component is generated. Suppose absence of noise, matched filter at the receiver and perfect synchronism. The transmitter sends the sequence of bits "111011001010001".

The channel generates a single echo (corresponding to a multipath propagation) that comes almost simultaneously and with the same power level as the main signal but with a phase shift of 14 degrees. The channel introduces an additional phase shift of 88 degrees to the overall received signal (both direct and echo signals).
Determine the value of the phase (in degrees within the interval 0-360), of the received signal at t=3Ts.

| Bits | $\Delta \Phi$ |
| ---- | ------------- |
| 000  | 45            |
| 001  | 270           |
| 010  | 0             |
| 011  | 180           |
| 100  | 90            |
| 101  | 315           |
| 110  | 135           |
| 111  | 225           |

![[Pasted image 20240613121739.png]]
![[Pasted image 20240613121748.png]]

Solution in Python:

```Python
import numpy as np
```

Initialize variables

```Python
msg = "111011001010001"
channel = 88
echo = 14
angle_0 = np.arctan2(1, 1) * 180 / np.pi
```

Define modulation dictionary

```Python
mod = {
  (0, 0, 0): 45,
  (0, 0, 1): 270,
  (0, 1, 0): 0,
  (0, 1, 1): 180,
  (1, 0, 0): 90,
  (1, 0, 1): 315,
  (1, 1, 0): 135,
  (1, 1, 1): 225,
}
```

Calculate symbol angles

```Python
sym_ang = [angle_0] + [mod[tuple(map(int, msg[i:i+3]))]
                            for i in range(0, len(msg), 3)]
```

Calculate cumulative sum of angles

```Python
angle = np.cumsum(sym_ang) + channel + echo / 2
```

Normalize angle to be within [0, 360)

```Python
angle = angle % 360
```

Print the fourth element of the angle array

```Python
print(angle[3])
```

Complete solution in Python:

```Python
import numpy as np

# Initialize variables
msg = "111011001010001"
channel = 88
echo = 14
angle_0 = np.arctan2(1, 1) * 180 / np.pi

# Define modulation dictionary
mod = {
  (0, 0, 0): 45,
  (0, 0, 1): 270,
  (0, 1, 0): 0,
  (0, 1, 1): 180,
  (1, 0, 0): 90,
  (1, 0, 1): 315,
  (1, 1, 0): 135,
  (1, 1, 1): 225,
}

# Calculate symbol angles
sym_ang = [angle_0] + [mod[tuple(map(int, msg[i:i+3]))]
                            for i in range(0, len(msg), 3)]

# Calculate cumulative sum of angles
angle = np.cumsum(sym_ang) + channel + echo / 2

# Normalize angle to be within [0, 360)
angle = angle % 360

# Print the fourth element of the angle array
print(angle[3])
```

- 95
## There is a wireless digital transmission system that uses 8-DPSK modulation with the table indicated below. At t=0 a reference symbol with value -1 in the in-phase component and 1 in the quadrature component is generated. Suppose absence of noise, matched filter at the receiver and perfect synchronism. The transmitter sends the sequence of bits "100101011010101".

The channel generates a single echo (corresponding to a multipath propagation) that comes almost simultaneously and with the same power level as the main signal but with a phase shift of 8 degrees. The channel introduces an additional phase shift of 96 degrees to the overall received signal (both direct and echo signals).
Determine the value of the phase (in degrees within the interval 0-360), of the received signal at t=3T.

| Bits  | ΔΦ   |
| ----- | ---- |
| "000" | 45º  |
| "001" | 270º |
| "010" | 225º |
| "011" | 315º |
| "100" | 180º |
| "101" | 90º  |
| "110" | 135º |
| "111" | 0º   |

- 100
## There is a wireless digital transmission system whose global impulse response h(t) is the one shown in the figure. The transmission is made with BPSK modulation.

![[Pasted image 20240612141234.png]]
Assuming a transmission rate of 200kbps, decide adequately the sampling time and calculate the coefficient c1 of a DFE equalizer that eliminates completely the ISI.

- -2
## There is a wireless digital transmission system whose global impulse response h(t) is the one shown in the figure. The transmission is made with BPSK modulation.

![[Pasted image 20240612141234.png]]
Assuming a transmission rate of 200kbps, decide adequately the sampling time and calculate the coefficient c4 of a DFE equalizer that eliminates completely the ISI.
![[Pasted image 20240613121827.png]]
Solution in Python:

```Python
h_t=[-0.1,-0.2,0,1,0.4,0.2,0]
C_0=1/h_t[0]
c=[C_0]
for i in range(1,len(h_t)):
    c.append(-h_t[i]*c[0])

print(c)
```

- 4
## What is AC in the context of the RRM in CDMA wireless communications systems?

- Access Control
## What is CC in the context of the RRM in CDMA wireless communication systems?

- Congestion Control
## What is PN in the context of the spreading codes of a wireless communications system that uses spread spectrum transmission?

- Pseudo Noise
## What is UHF in the context of wireless communications? (use only two words)

- Frequency Band
## What is the ITU?

- International Telecommunications Union
## What is the PN in the context of spreading codes of CDMA wireless communication system?

- Pseudo Noise
## What is the acronym of the official table where the Spanish Government publishes the regulation of radio communications channels within the BOE?

- CNAF
## What is the name of the joint application of ARQ and FEC techniques in wireless communications systems?

- H-ARQ
## What is the name of the joint application of ARQ and FEC techniques in wireless communications systems?

- H-ARQ
## What is the name of the process that converts a digital input signal into a flow of bits?

- Source Coding
## What is the name of the process that transmits a wireless signal by using more bandwidth that the one that is strictly required in order to protect it against interference?

- Spread Spectrum
## What is the name of the technique that uses H-ARQ and changes the coding rate in an adaptive way depending on the quality of the radio channel and the number of attempts for each transmission?

- Incremental Redundancy
## What is the name of the technique used for breaking the burst of errors generated by a wireless channel and spread them in the time domain?

- Interleaving
## Which is the acronym for the unlicensed bands in wireless communications?

- ISM
## Which is the function of the GPS for SFN in the context of wireless communications?

- Synchronization of the transmitter
## Which is the gain (in %) ni terms of number of transmissions that can be achieved by using Network Coding with the most simple configuration in a system as the one shown in the figure?

![[Pasted image 20240612174303.png]]

- 25
## Which is the main feature of the IEEE 802.11n wireless communication standard with respect to the generic 802.11 standard? (write the acronym)

- MIMO
## Which is the mathematical operation performed by the transmitter of a OFDM wireless communication system in order to generate the transmitted symbols?

- Inverse Fast Fourier Transform
## Which is the mathematical operation performed by the transmitter of a OFDM wireless communications system in order to generate the transmitted symbols?

- Fast Fourier Transform
## Which is the maximum frequency (GHz) of the X band in wireless communications?

- 12
## Which is the name of the wireless network used in Catalonia for public and safety corpses?

- RESCAT
## Which is the shape of the vector diagram of a signal with the ideal value of its PAPR?

- Circle
## Which is the size of a cluster in a CDMA-based wireless communications system?

- 1
## Which is the technical acronym for the 3G mobile communications standard?

- UMTS