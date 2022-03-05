# 1. Combinatoria

**Problema tipus**
Urna amb n boles i en treiem k

- Ordre
  - Amb => [Permutacions](#11-permutacions)
  - Sense => [Combinacions](#12-combinacions)
- Repetició
  - Amb ([Permutacions](#112-amb-repetici), [Combinacions](#122-amb-repetici))
  - Sense ([Permutacions](#111-sense-repetici), [Combinacions](#121-sense-repetici))

## 1.1 Permutacions

**Def**: el nombre de mostres ordenades

### 1.1.1 Sense repetició

Sense repetició

$$
P_{n,k}=V_{n,k}=\frac{n!}{(n-k)!}
$$

$$
P_{n,n}=P_n=n!
$$

### 1.1.2 Amb repetició

$$
PR_{n,k}=n^k
$$

## 1.2 Combinacions

**Def**: el nombre de mostres no ordenades

### 1.2.1 Sense repetició

$$
C_{n,k}=\binom{n}{k}=\frac{n!}{k!(n-k)!}
$$

#### Binomi de Newton

$$
(x+y)^n=\sum_{i=0}^n\binom{n}{i}x^iy^{n-i}
$$

#### 1.2.1.1 Propietats

1. **Symetria**:$$\binom{n}{k}=\binom{n}{n-k}$$
2. **Extrems**:$$\binom{n}{0}=\binom{n}{n}=1$$
3. **Recurrencia**:
   $$
   \binom{n}{k}=\binom{n-1}{k-1}+\binom{n-1}{k}
   $$

### 1.2.2 Amb repetició

$$
CR_{n,k}=\binom{n+k-1}{k}=\binom{n+k-1}{n-1}
$$
