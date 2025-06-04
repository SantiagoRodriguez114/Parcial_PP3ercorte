# Parcial_PP3ercorte

### Objetivo
- Este ejrcicio tiene como finalidad comparar el tiempo de ejecucion de la serie de Fourier en el lenguaje de python utlizando dos enfoques, recursivo e iterativo.

### Resultados

| N (armónicos) | Iterativo (s) | Recursivo (s) |
| ------------- | ------------- | ------------- |
| 5             | 0.000432      | 0.000948      |
| 10            | 0.000619      | 0.003478      |
| 20            | 0.001221      | 0.013019      |
| 50            | 0.002877      | 0.078512      |

# Analisis y conclusiones

![comparacion_barras](https://github.com/user-attachments/assets/9c3fd40a-7f84-4388-9fd9-6f579feae08a)

![image](https://github.com/user-attachments/assets/db4959f9-430a-4ef1-8317-18cfb27f69f1)
![image](https://github.com/user-attachments/assets/5ae02204-4d53-4e7e-84fd-b556e5ccec46)



## ¿Cuál método resulta más eficiente?

Basado en los datos analizados, **el método iterativo resulta significativamente más eficiente** que el método recursivo para calcular armónicos. Las mediciones de tiempo muestran que:

- Para N=5, el método iterativo es 2.19 veces más rápido
- Para N=10, el método iterativo es 5.62 veces más rápido
- Para N=20, el método iterativo es 10.66 veces más rápido
- Para N=50, el método iterativo es 27.29 veces más rápido

Esta diferencia se amplía drásticamente conforme aumenta el valor de N, lo que indica una escalabilidad mucho mejor del método iterativo.

## ¿Por qué existe esta diferencia?

### Complejidad Temporal

- **Método Iterativo**: Tiene una complejidad temporal de O(n), donde n es el número de armónicos. Esto significa que el tiempo de ejecución crece de manera lineal con respecto al tamaño de entrada.

- **Método Recursivo**: Aunque la función recursiva para calcular armónicos también tiene una complejidad teórica de O(n), en la práctica muestra un comportamiento mucho peor debido a la sobrecarga adicional que implica cada llamada recursiva.

### Profundidad de Recursión

- El método recursivo para calcular armónicos genera una pila de llamadas de profundidad N. Esto significa que:
  - Para N=50, se realizan 50 llamadas recursivas anidadas
  - Cada llamada recursiva requiere:
    - Asignación de memoria para la nueva instancia de la función
    - Almacenamiento del estado actual y punto de retorno
    - Sobrecarga del sistema para gestionar la pila de llamadas

- Esta sobrecarga se acumula significativamente a medida que N aumenta, lo que explica por qué la diferencia de rendimiento se amplifica para valores mayores de N.

### Uso de Memoria

- **Método Iterativo**: Utiliza una cantidad constante de memoria independientemente del valor de N, ya que solo necesita almacenar unas pocas variables.

- **Método Recursivo**: Consume memoria proporcional a N debido a la pila de llamadas, lo que puede llevar a desbordamientos de pila (stack overflow) para valores muy grandes de N.

### Optimización del Compilador/Intérprete

- Los métodos iterativos suelen beneficiarse más de las optimizaciones del compilador o intérprete, como:
  - Desenrollado de bucles
  - Optimizaciones de registro
  - Predicción de saltos

- Las funciones recursivas son más difíciles de optimizar debido a su naturaleza dinámica y dependencia de la pila de llamadas.

### Legibilidad del Código

- **Método Recursivo**: 
  - Ventajas: Puede resultar más elegante y cercano a la definición matemática para algunos problemas.
  - Desventajas: Para cálculos simples como los armónicos, la recursión añade complejidad innecesaria.

- **Método Iterativo**:
  - Ventajas: Es más directo, fácil de seguir y mantener para este tipo de problema.
  - Desventajas: En problemas inherentemente recursivos (como recorrido de árboles), puede resultar menos intuitivo.

## Conclusión

El método iterativo es claramente superior para el cálculo de armónicos tanto en eficiencia como en uso de recursos. La diferencia de rendimiento se vuelve crítica para valores grandes de N, donde el método recursivo muestra un deterioro exponencial en comparación con el crecimiento lineal del método iterativo.

Para este tipo de problemas matemáticos secuenciales, la recursión no aporta beneficios significativos en términos de legibilidad o mantenibilidad que justifiquen su considerable costo en rendimiento.
