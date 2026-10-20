EXAMEN PARCIAL DE MANEJO Y ESTRUCTURA DE DATOS
Estudiante: Anderson Ezequiel Reyes Rivera
Universidad de Oriente (UNIVO)

PARTE I. Preguntas de análisis y razonamiento (60%)

1. Selección de estructuras de datos (10 puntos)
A. Procesar solicitudes de despacho en el mismo orden en que fueron recibidas.
- Estructura seleccionada: Cola (Queue / FIFO - First In, First Out).
- Justificación: Garantiza que el primer elemento en ingresar sea el primero en ser atendido, manteniendo la equidad temporal.

B. Permitir que un supervisor revierta la última modificación registrada.
- Estructura seleccionada: Pila (Stack / LIFO - Last In, First Out).
- Justificación: El comportamiento LIFO permite acceder y eliminar de manera directa el elemento que se agregó más recientemente.

C. Mantener códigos numéricos de productos en un árbol binario de búsqueda para facilitar su consulta.
- Estructura seleccionada: Árbol Binario de Búsqueda (BST).
- Justificación: Permite búsquedas, inserciones y eliminaciones eficientes organizando los elementos de menor a mayor valor.

Problema operativo si se usara una pila en el apartado A: 
Se produciría una inversión de prioridades, donde las solicitudes más antiguas quedarían al fondo de la pila y tendrían que esperar a que se atiendan todas las solicitudes nuevas ingresadas posteriormente, rompiendo el orden de llegada.

2. Auditoría de Pila (Stack)
- Tabla de trazado:
Operación      | Contenido de la pila (base a cima)
Inicial        | []
append M101    | ['M101']
append M102    | ['M101', 'M102']
append M103    | ['M101', 'M102', 'M103']
pop()          | ['M101', 'M102']
append M104    | ['M101', 'M102', 'M104']
pop()          | ['M101', 'M102']

- Elemento en la cima al finalizar: "M102"
- Contenido final desde la cima hasta la base: "M102", "M101"
- Justificación sobre pop(0): pop(0) remueve el primer elemento (índice 0, la base), lo que simula un comportamiento FIFO (cola) y requiere desplazar todos los elementos restantes, violando la regla LIFO pura de una pila convencional.

3. Centro de Soporte (Cola / Queue)
- Tabla de trazado:
Operación      | Contenido de la cola (primero a último)
Inicial        | []
append T01     | ['T01']
append T02     | ['T01', 'T02']
append T03     | ['T01', 'T02', 'T03']
pop(0)         | ['T02', 'T03']
append T04     | ['T02', 'T03', 'T04']
pop(0)         | ['T03', 'T04']
append T05     | ['T03', 'T04', 'T05']

- Ticket que se atendería a continuación: "T03"
- Siguiente ticket después de ese: "T04"
- Consecuencia de atender siempre el último ingresado: Se transforma en una pila (LIFO), provocando que los tickets antiguos nunca sean atendidos si siguen ingresando nuevos.
- Condición previa antes de retirar un elemento: Verificar que la cola no esté vacía (len(cola) > 0) para evitar errores de índice.

4. Árbol Binario de Búsqueda (BST)
- Inserción (50, 30, 70, 20, 40, 60, 80):
      50
     /  \
   30    70
  /  \  /  \
 20  40 60  80

- Resultado en Inorden: 20, 30, 40, 50, 60, 70, 80
- Explicación: El recorrido inorden (Izquierda, Raíz, Derecha) visita primero todos los valores menores al nodo actual, luego la raíz y finalmente los mayores, dando como resultado una secuencia estrictamente ordenada de menor a mayor.

5. Eliminación en un árbol (10 puntos)
- Hijos del nodo 30: Tiene dos hijos (20 y 40).
- Procedimiento de eliminación: Para eliminar un nodo con dos hijos, se busca su sucesor inorden (el nodo más a la izquierda del subárbol derecho, que es el 40), se reemplaza su valor y se elimina el nodo duplicado original.
- Árbol resultante:
      50
     /  \
   40    70
  /     /  \
 20    60  80
- Propiedad que se incumpliría: Si se reemplaza arbitrariamente sin verificar las relaciones, se rompería la regla del ABB donde todo valor a la izquierda debe ser menor y todo valor a la derecha debe ser mayor que la raíz del subárbol.

6. Diagnóstico de una solución
- Solicitud que se atiende: "A03"
- Estructura y operación representada: Una pila (Stack) utilizando .pop() sin argumentos, que extrae el último elemento.
- Instrucción corregida para cumplir orden de llegada: atendida = solicitudes.pop(0)
- Explicación: Se ejecuta sin errores porque .pop() por defecto elimina el último elemento de la lista. Sin embargo, incumple la regla de negocio porque despacha al último en llegar en lugar del primero.