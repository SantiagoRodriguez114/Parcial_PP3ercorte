import numpy as np
import time

def regla_trapecio(f, x, dx):
    return dx * (np.sum(f[1:-1]) + (f[0] + f[-1])/2)

def calcular_serie_fourier_iterativa(f, t, T, N):
    
    dt = t[1] - t[0]
    
    a0 = 2 * regla_trapecio(f, t, dt) / T
    
    an = np.zeros(N)
    bn = np.zeros(N)
    
    for n in range(1, N+1):
        
        cos_term = np.cos(2 * np.pi * n * t / T)
        an[n-1] = 2 * regla_trapecio(f * cos_term, t, dt) / T
        
        sin_term = np.sin(2 * np.pi * n * t / T)
        bn[n-1] = 2 * regla_trapecio(f * sin_term, t, dt) / T
    
    return a0, an, bn

def calcular_coeficiente_recursivo(f, t, T, n, coef_type, dt):
    if n <= 0:
        return 0
    
    if coef_type == 'cos':
        term = np.cos(2 * np.pi * n * t / T)
    elif coef_type == 'sin':
        term = np.sin(2 * np.pi * n * t / T)
    else:
        return 0
    
    coef_actual = (2/T) * regla_trapecio(f * term, t, dt)
    
    if n > 1:
        _ = calcular_coeficiente_recursivo(f, t, T, n-1, coef_type, dt)
    
    return coef_actual

def calcular_serie_fourier_recursiva(f, t, T, N):
    
    dt = t[1] - t[0]
    
    a0 = 2 * regla_trapecio(f, t, dt) / T
    
    an = np.zeros(N)
    bn = np.zeros(N)
    
    for n in range(1, N+1):
        an[n-1] = calcular_coeficiente_recursivo(f, t, T, n, 'cos', dt) 
        bn[n-1] = calcular_coeficiente_recursivo(f, t, T, n, 'sin', dt) 
    
    return a0, an, bn

def comparar_rendimiento():
    
    T = 2 * np.pi
    t = np.linspace(0, T, 1000, endpoint=False)
    f = np.sign(np.sin(t))
    
    N_valores = [5, 10, 20, 50]
    tiempos_iter = []
    tiempos_recur = []
    
    for N in N_valores:
        
        inicio = time.time()
        calcular_serie_fourier_iterativa(f, t, T, N)
        fin = time.time()
        tiempos_iter.append(fin - inicio)
        
        inicio = time.time()
        calcular_serie_fourier_recursiva(f, t, T, N)
        fin = time.time()
        tiempos_recur.append(fin - inicio)
    
    print("\nTabla de tiempos de ejecución:")
    print("N\tIterativo (s)\tRecursivo (s)")
    print("-" * 40)
    for i, N in enumerate(N_valores):
        print(f"{N}\t{tiempos_iter[i]:.6f}\t{tiempos_recur[i]:.6f}")

if __name__ == "__main__":
    comparar_rendimiento()
