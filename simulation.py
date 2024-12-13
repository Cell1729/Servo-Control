import matplotlib.pyplot as plt
import numpy as np
import cmath

# フォントサイズ
plt.rcParams.update({'font.size': 28})

# 値の定義
omega_c = 5
zeta = 1
omega_n = omega_c / 2 / zeta

# 関数の定義
def y(t):
    if zeta == 1:
        return 1 - np.exp(-omega_n * t) - omega_n *t * np.exp(-omega_n * t)
    else:
        return 1 - cmath.exp(-zeta * omega_n * t) / cmath.sqrt(1 - zeta ** 2) * cmath.sin(omega_n * cmath.sqrt(1 - zeta ** 2) * t + cmath.atan(cmath.sqrt(1 - zeta ** 2) / zeta))

# グラフの描画
t = np.linspace(0, 10, 1000)
y_vectorized = np.vectorize(y)
y_values = y_vectorized(t)

plt.plot(t, y_values.real, label='Real part')
# plt.plot(t, y_values.imag, label='Imaginary part')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()