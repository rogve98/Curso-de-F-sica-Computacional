"""
Función que determina el potencial de un dipolo dada una red de 100 x 100
"""
import numpy as np
from scipy.special import roots_legendre

ϵ0 = 8.845e-12
k = 1/(4*np.pi*ϵ0)
q0 = 100
placa = 10
px_inicio,px_fin = 45 , 55
py_inicio,py_fin = 45 , 55
#ϵ = 0.1

def potencialDipolo(ϵ):
    Φ = np.zeros([100,100])
    for i in range(100):
        for j in range(100):
            # if not(i==49 and j==54) and not(i==49 and j==44):
                r1 = np.sqrt((i - 49)**2 + (j - 54)**2) + ϵ
                r2 = np.sqrt((i - 49)**2 + (j - 44)**2) + ϵ
                Φ[i, j] = 1 / r1 - 1 / r2
    return k*Φ

def Gradiente(f,x,y,h):
    df_x = (f(x+h/2,y)-f(x-h/2,y))/h
    df_y = (f(x,y+h/2)-f(x,y-h/2))/h
    return np.array([df_x,df_y])

def ΦDip(x,y):
    ϵ = 1   
    y1,x1 = 0.5,0.65
    y2,x2 = 0.5,0.35
    r1 = np.sqrt((x - x1)**2 + (y - y1)**2) + ϵ
    r2 = np.sqrt((x - x2)**2 + (y - y2)**2) + ϵ
    return k*(1/r1 - 1/r2)

def potencialycampoDip(N):
    x = np.linspace(0,1,N)
    y = np.linspace(0,1,N)
    X,Y= np.meshgrid(x,y)
    Ex = np.zeros([N,N])
    Ey = np.zeros([N,N])
    Φ = np.zeros([N,N])
    for i in range(N):
        for j in range(N):
            x, y = X[i,j], Y[i,j]
            Φ[i,j] = ΦDip(x,y)
            Ex[i,j],Ey[i,j] = Gradiente(ΦDip,x,y,0.001)
    return Φ,Ex,Ey


def sigma(i,j):
    xs = np.linspace(px_inicio,px_fin,placa)
    ys = np.linspace(py_inicio,py_fin,placa)
    I , J = np.meshgrid(xs,ys,indexing='ij')
    σ = q0 * np.sin(2 * np.pi * I / placa) * \
               np.sin(2 * np.pi * J / placa)
    return σ[i,j]

def Φsigma(u,v):
    ϵ = 1e3
    xs = np.linspace(px_inicio,px_fin,placa)
    ys = np.linspace(py_inicio,py_fin,placa)
    Φ = 0
    for i in range(10):
        for j in range(10):
            r = np.sqrt((u  - xs[i])**2 + (v - ys[j])**2) + ϵ
            Φ += sigma(i,j)/r
    return Φ

def potencialycampoσ(L):
    ϵ = 1e3
    Φ = np.zeros([L,L])
    Ex,Ey = np.zeros_like(Φ),np.zeros_like(Φ)
    xs = np.linspace(0,100,L)
    ys = np.linspace(0,100,L)
    us = np.linspace(px_inicio,px_fin,placa)
    vs = np.linspace(px_inicio,px_fin,placa)
    I,J = np.meshgrid(us,vs)
    σ = q0 * np.sin(2 * np.pi * I / placa) * \
               np.sin(2 * np.pi * J / placa)
    for x in range(L):
        for y in range(L):
            potencial = 0
            for i in range(placa):
                for j in range(placa):
                    u = px_inicio + i
                    v = py_inicio + j
                    r = np.sqrt((xs[x] - u)**2 + (ys[y] - v)**2) + ϵ
                    potencial += σ[i,j]/r
            Φ[x,y] = k*potencial
    h = 1e-5  # Incremento pequeño para la derivada
    for x in range(L):
        for y in range(L):
            Ex[x,y], Ey[x,y] = Gradiente(lambda xi, yi: Φ[int(xi), int(yi)], x, y, h)
    
    return Φ,Ex,Ey

def cuadratura_gauss_2d(f, limites_u, limites_v, n):
    # Obtener puntos y pesos de Gauss-Legendre
    gauss_p, pesos = roots_legendre(n)
    
    # Cambiar los puntos y pesos a los límites deseados
    u_mid, u_range = (limites_u[1] + limites_u[0]) / 2, (limites_u[1] - limites_u[0]) / 2
    v_mid, v_range = (limites_v[1] + limites_v[0]) / 2, (limites_v[1] - limites_v[0]) / 2
    puntos_u = u_mid + u_range * gauss_p
    puntos_v = v_mid + v_range * gauss_p
    pesos_u = u_range * pesos
    pesos_v = v_range * pesos

    # Inicializar la integral
    integral = 0.0

    # Realizar la doble suma para la cuadratura de Gauss
    for i in range(n):
        for j in range(n):
            integral += pesos_u[i] * pesos_v[j] * f(pesos_u[i], pesos_v[j])
    
    return integral

"""
from tqdm import tqdm

# Parámetros de la malla
malla_size = 100
potencial_malla = np.zeros((malla_size, malla_size))

# Crear puntos en el plano para la malla (de 0 a 100)
u_points = np.linspace(0, 100, malla_size)
v_points = np.linspace(0, 100, malla_size)

# Calcular el potencial en cada punto de la malla
for i, u in tqdm(enumerate(u_points)):
    for j, v in enumerate(v_points):
        potencial_malla[i, j] = main.cuadratura_gauss_2d(lambda x, y: main.Φsigma(u, v), u_limits, v_limits, 2)
"""