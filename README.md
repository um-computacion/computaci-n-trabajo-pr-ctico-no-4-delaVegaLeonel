# Trabajo Práctico 4: Recursividad

## Información del Alumno
- Nombre: Leonel 
- Apellido: de la Vega
- Legajo: 62187

## Objetivos
- Comprender y aplicar el concepto de recursividad
- Implementar soluciones iterativas y recursivas para problemas clásicos
- Practicar el desarrollo guiado por pruebas (TDD)
- Trabajar con estructuras de datos anidadas
- Utilizar el framework de testing unittest de Python

## Requisitos Previos
- Python 3.x
- Conocimientos básicos de programación
- Git y GitHub
- unittest (incluido en la biblioteca estándar de Python)

## Estructura del Trabajo
El trabajo está dividido en etapas, cada una debe ser implementada en commits separados dentro del mismo repositorio:

### Etapa 1: Factorial
Implementar dos versiones de la función factorial:
1. Versión iterativa
2. Versión recursiva

**Requisitos:**
- Crear un archivo `factorial.py` con las implementaciones
- Crear un archivo `test_factorial.py` con los casos de prueba
- Implementar manejo de casos especiales (números negativos, cero)
- Documentar las funciones con docstrings

### Etapa 2: Fibonacci
Implementar dos versiones de la función fibonacci:
1. Versión iterativa
2. Versión recursiva

**Requisitos:**
- Crear un archivo `fibonacci.py` con las implementaciones
- Crear un archivo `test_fibonacci.py` con los casos de prueba
- Implementar manejo de casos especiales (números negativos, cero)
- Documentar las funciones con docstrings

### Etapa 3: Aplanar Listas
Implementar una función recursiva que aplane listas anidadas.

**Requisitos:**
- Crear un archivo `flatten.py` con la implementación
- Crear un archivo `test_flatten.py` con los casos de prueba
- Manejar diferentes tipos de estructuras de datos anidadas

## Casos de Prueba

### Caso 1: Lista Simple
```python
lista = [1, 2, 3, 4]
resultado_esperado = [1, 2, 3, 4]
```

### Caso 2: Lista con Listas Anidadas
```python
lista = [1, [2, 3], [4, [5, 6]]]
resultado_esperado = [1, 2, 3, 4, 5, 6]
```

### Caso 3: Lista con Diferentes Estructuras
```python
lista = [1, (2, 3), {'a': 4, 'b': 5}, [6, [7, 8]]]
resultado_esperado = [1, 2, 3, 'a', 4, 'b', 5, 6, 7, 8]
```

## Criterios de Evaluación
1. Correctitud de las implementaciones
2. Cobertura de casos de prueba
3. Calidad del código (legibilidad, documentación)
4. Uso correcto de TDD
5. Manejo de casos especiales
6. Organización del repositorio

## Entrega
Para cada etapa:
1. Realizar un commit con los cambios correspondientes
2. Incluir los archivos de implementación y pruebas
3. Incluir un README.md con:
   - Descripción del problema
   - Instrucciones de ejecución
   - Ejemplos de uso
   - Capturas de pantalla de los tests ejecutados

## Notas Importantes
- Cada etapa debe ser implementada en commits separados
- Los tests deben ejecutarse correctamente
- El código debe estar documentado
- Se debe seguir el enfoque TDD




# Etapa 1 entrega 
# Factorial

## Descripción

Este módulo implementa la función factorial de dos maneras:
- Iterativa
- Recursiva

También incluye pruebas automatizadas usando `unittest`.

## Instrucciones de Ejecución

1. Ejecutar los tests con:

```bash
python -m unittest test_factorial.py
``` 
## Ejemplo de uso
```python
from factorial import factorial_iterative, factorial_recursive

print(factorial_iterative(5))  # 120
print(factorial_recursive(3))  # 6
```
### Imagen

# Etapa 2 entrega
# Fibonacci

## Descripción

Este módulo implementa la secuencia de Fibonacci de dos maneras:
- Iterativa
- Recursiva

Incluye pruebas automatizadas usando `unittest`.

## Instrucciones de Ejecución

Ejecutar los tests con:

```bash
python -m unittest test_fibonacci.py
```


## Ejemplo de uso
```python
from fibonacci import fibonacci_iterative, fibonacci_recursive

print (fibonacci_iterative(10))   # 55
print(fibonacci_recursive(5))    # 5
```
### Imagen 

# Etapa 3 entrega
# Flatten (Aplanar Listas)

## Descripción

Este módulo contiene una función recursiva para aplanar estructuras de datos anidadas, como listas, tuplas y diccionarios, en una lista simple.

## Instrucciones de Ejecución

```bash
python -m unittest test_flatten.py
```
## Ejemplo de uso
```python
from flatten import flatten

print(flatten([1, [2, 3], [4, [5, 6]]]))
# [1, 2, 3, 4, 5, 6]

print(flatten([1, (2, 3), {'a': 4, 'b': 5}, [6, [7, 8]]]))
# [1, 2, 3, 'a', 4, 'b', 5, 6, 7, 8]
```
### Imagen
