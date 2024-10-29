import numpy as np
import matplotlib.pyplot as plt

# Definir la función a integrar
def f(x):
    return x**2  # Por ejemplo, f(x) = x^2

"""
# Definir los límites y el número de intervalos
a = 0  # Límite inferior
b = 1  # Límite superior
n = 1000  # Número de subintervalos

# Calcular el ancho de cada subintervalo
delta_x = (b - a) / n

# Generar los puntos de la suma de Riemann izquierda
x_left = np.linspace(a, b - delta_x, n)  # n puntos desde a hasta b - delta_x

# Calcular la suma de Riemann
suma_riemann = np.sum(f(x_left) * delta_x)

print("La aproximación de la integral usando la suma de Riemann izquierda es:", suma_riemann)"""

# Definimos la función que queremos integrar
def f(x):
    return x**2

"""
# Parámetros de integración
a = 0    # Inicio del intervalo
b = 1    # Fin del intervalo
n = 1000 # Número de subintervalos

# Calculamos el ancho de cada subintervalo
dx = (b - a) / n
"""
# Suma de Riemann Izquierda
def riemann_left(f, a, b, n):
    dx = (b - a) / n
    sum_left = sum(f(a + i * dx) for i in range(n)) * dx
    return sum_left

# Suma de Riemann Derecha
def riemann_right(f, a, b, n):
    dx = (b - a) / n
    sum_right = sum(f(a + (i + 1) * dx) for i in range(n)) * dx
    return sum_right

# Suma de Riemann en el Punto Medio
def riemann_midpoint(f, a, b, n):
    dx = (b - a) / n
    sum_mid = sum(f(a + (i + 0.5) * dx) for i in range(n)) * dx
    return sum_mid
"""
# Llamamos a las funciones e imprimimos los resultados
left = riemann_left(f, a, b, n)
right = riemann_right(f, a, b, n)
midpoint = riemann_midpoint(f, a, b, n)

print(f"Suma de Riemann Izquierda: {left}")
print(f"Suma de Riemann Derecha: {right}")
print(f"Suma de Riemann en el Punto Medio: {midpoint}")
"""

#Sumas de riemann para potencial eléctrico de una placa
"""
# Constantes
ϵ0 = 8.845e-12
q0 = 100#1e-6  # Densidad de carga máxima
L = 10.0    # Lado de la placa
"""
# Definición de la densidad de carga
def sigma(x, y):
    return q0 * np.sin(2 * np.pi * x / L) * np.cos(2 * np.pi * y / L)

# Definición del potencial en un punto (x, y, z) debido a la placa
def potencial(x, y, z, x_vals, y_vals, dx, dy):
    V = 0
    for x_prime in x_vals:
        for y_prime in y_vals:
            r = np.sqrt((x - x_prime)**2 + (y - y_prime)**2 + z**2)
            if r != 0:  # Evitar la singularidad
                V += sigma(x_prime, y_prime) / r
    V *= dx * dy / (4 * np.pi * ϵ0)
    return V

"""
# Parámetros de la cuadrícula para la placa
N = 30
x_vals = np.linspace(0, L, N)
y_vals = np.linspace(0, L, N)
dx = x_vals[1] - x_vals[0]
dy = y_vals[1] - y_vals[0]

# Cálculo del potencial en la cuadrícula (z = 0)
X, Y = np.meshgrid(x_vals, y_vals)
V_grid = np.zeros_like(X)
for i in range(N):
    for j in range(N):
        V_grid[i, j] = potencial(X[i, j], Y[i, j], z=0, x_vals=x_vals, y_vals=y_vals, dx=dx, dy=dy)

# Cálculo del campo eléctrico (gradiente del potencial)
Ey, Ex = np.gradient(-V_grid, dx, dy)

# Graficar el potencial y el campo eléctrico
plt.figure(figsize=(10, 8))
plt.contourf(X, Y, V_grid, levels=50, cmap='viridis')
plt.colorbar(label='Potencial (V)')
plt.quiver(X, Y, Ex, Ey, color='red')
plt.title('Campo eléctrico y potencial de una placa cargada')
plt.xlabel('x')
plt.ylabel('y')
plt.show()"""
