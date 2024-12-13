import matplotlib.pyplot as plt
import numpy as np
import cmath

# フォントサイズ
plt.rcParams.update({'font.size': 28})

# 値の定義
sample_omega = [1, 5, 10]
zeta = 2

# 関数の定義
def y(t, omega_n):
    if zeta == 1:
        return 1 - np.exp(-omega_n * t) - omega_n * t * np.exp(-omega_n * t)
    else:
        return 1 - cmath.exp(-zeta * omega_n * t) / cmath.sqrt(1 - zeta ** 2) * cmath.sin(omega_n * cmath.sqrt(1 - zeta ** 2) * t + cmath.atan(cmath.sqrt(1 - zeta ** 2) / zeta))

# グラフの描画
t = np.linspace(0, 10, 1000)
plt.figure()

for omega in sample_omega:
    omega_n = omega / 2 / zeta
    y_vectorized = np.vectorize(lambda t: y(t, omega_n))
    y_values = y_vectorized(t)
    plt.plot(t, y_values.real, label=f'ω_n={omega}')

plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()