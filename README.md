## Django Test Unit Tests

- [Pruebas Pytest](https://www.youtube.com/watch?v=pdatgYDXmSE)
- [Pytest Documentation](https://pytest-django.readthedocs.io/en/latest/)
- [Pytest Unit Testing](https://dev.to/xarala221/django-testing-using-pytest-1pak)

Son casos particulares para validar que el funcionamiento de cada elementos siga siendo el mismo.
Instalacion basica:
```bash
pip  install pytest pytest-django 
```

Definicion del module de settings con django
```bash
touch pytest.ini # windows ni -Type File pytest.ini

# Ejecucion de los tests creados
python manage.py test
pytest -v
```

- [Entrega final](https://docs.google.com/presentation/d/1gmo2LfnRNWUjzVJAVbhGnpG7hq2jS3__S1F8IXsseK4/edit?slide=id.g21bfe238241_0_648#slide=id.g21bfe238241_0_648zu)


## Python Avanzado

### Índice
1. Generadores
2. Funciones Lambda
3. Métodos para Iteradores (filter/map)
4. Expresiones Regulares (REGEXP)
5. Bases de Datos (Django ORM / MySQL)

---

## 1.  GENERADORES

### Teoría
Los generadores son funciones especiales que retornan un iterador y generan valores "bajo demanda" usando `yield` en lugar de `return`. Son **eficientes en memoria** porque no almacenan todos los valores a la vez.

### Ventajas
- Ahorro de memoria (lazy evaluation)
- Ideales para grandes conjuntos de datos
- Pueden generar secuencias infinitas

### Sintaxis Básica

```python
# Generador con función
def contador(max):
    n = 0
    while n < max:
        yield n
        n += 1

# Uso
for num in contador(5):
    print(num)  # 0, 1, 2, 3, 4
```

### Generator Expressions (Expresiones Generadoras)

```python
# Similar a list comprehension pero con ()
cuadrados = (x**2 for x in range(1000000))  # No consume memoria

# Lista tradicional (consume toda la memoria)
lista = [x**2 for x in range(1000000)]
```

### Ejemplo Práctico: Lectura de Archivos Grandes

```python
def leer_archivo_grande(ruta):
    """Lee líneas de un archivo sin cargar todo en memoria"""
    with open(ruta, 'r') as archivo:
        for linea in archivo:
            yield linea.strip()

# Uso
for linea in leer_archivo_grande('datos.txt'):
    if 'error' in linea:
        print(linea)
```

### Ejemplo: Fibonacci Infinito

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Obtener los primeros 10 números
fib = fibonacci()
primeros_10 = [next(fib) for _ in range(10)]
print(primeros_10)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### Métodos de Generadores
- `next(gen)` - Obtiene el siguiente valor
- `gen.send(valor)` - Envía un valor al generador
- `gen.close()` - Cierra el generador

---

## 2. λ FUNCIONES LAMBDA

### Teoría
Las funciones lambda son **funciones anónimas de una sola línea**. Se usan para operaciones simples y rápidas sin necesidad de definir una función completa con `def`.

### Sintaxis

```python
# Función tradicional
def sumar(x, y):
    return x + y

# Función lambda equivalente
sumar = lambda x, y: x + y

print(sumar(3, 5))  # 8
```

### Características
- Solo **una expresión** (no statements)
- Retorno implícito
- Útiles como argumentos de otras funciones
- No pueden tener múltiples líneas
- No tienen docstring

### Ejemplos Prácticos

```python
# Ordenar lista de tuplas por el segundo elemento
estudiantes = [('Ana', 85), ('Luis', 92), ('María', 78)]
ordenados = sorted(estudiantes, key=lambda x: x[1])
print(ordenados)  # [('María', 78), ('Ana', 85), ('Luis', 92)]

# Operaciones matemáticas
cuadrado = lambda x: x**2
print(cuadrado(5))  # 25

# Condiciones en lambda
es_par = lambda x: x % 2 == 0
print(es_par(4))  # True

# Lambda con múltiples parámetros
calcular = lambda x, y, z: (x + y) * z
print(calcular(2, 3, 4))  # 20
```

### Cuándo NO usar Lambda
```python
# ❌ MAL: Demasiado complejo
resultado = lambda x: x**2 if x > 0 else -x**2 if x < 0 else 0

# BIEN: Usar función normal
def procesar(x):
    if x > 0:
        return x**2
    elif x < 0:
        return -x**2
    else:
        return 0
```

---

## 3. MÉTODOS PARA ITERADORES

### `filter()` - Filtrar Elementos

#### Teoría
`filter(función, iterable)` retorna un iterador con los elementos que cumplen una condición.

```python
# Sintaxis
filter(función_booleana, iterable)

# Filtrar números pares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4, 6, 8, 10]

# Filtrar strings no vacíos
palabras = ['', 'hola', '', 'mundo', '']
sin_vacios = list(filter(None, palabras))  # None = identidad
print(sin_vacios)  # ['hola', 'mundo']

# Filtrar estudiantes aprobados
estudiantes = [
    {'nombre': 'Ana', 'nota': 85},
    {'nombre': 'Luis', 'nota': 55},
    {'nombre': 'María', 'nota': 92}
]
aprobados = list(filter(lambda e: e['nota'] >= 60, estudiantes))
```

#### Comparación con List Comprehension

```python
# Con filter
pares = list(filter(lambda x: x % 2 == 0, numeros))

# Con list comprehension (más pythónico)
pares = [x for x in numeros if x % 2 == 0]
```

---

### `map()` - Transformar Elementos

#### Teoría
`map(función, iterable)` aplica una función a cada elemento del iterable.

```python
# Sintaxis
map(función_transformadora, iterable)

# Elevar al cuadrado
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)  # [1, 4, 9, 16, 25]

# Convertir a mayúsculas
palabras = ['hola', 'mundo', 'python']
mayusculas = list(map(str.upper, palabras))
print(mayusculas)  # ['HOLA', 'MUNDO', 'PYTHON']

# Múltiples iterables
nums1 = [1, 2, 3]
nums2 = [10, 20, 30]
sumas = list(map(lambda x, y: x + y, nums1, nums2))
print(sumas)  # [11, 22, 33]
```

#### Comparación con List Comprehension

```python
# Con map
cuadrados = list(map(lambda x: x**2, numeros))

# Con list comprehension (más pythónico)
cuadrados = [x**2 for x in numeros]
```

---

### Combinando `filter()` y `map()`

```python
# Obtener el cuadrado de los números pares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Método 1: Encadenando
resultado = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numeros)))

# Método 2: List comprehension (más legible)
resultado = [x**2 for x in numeros if x % 2 == 0]

print(resultado)  # [4, 16, 36, 64, 100]
```

---

## 4. EXPRESIONES REGULARES (REGEXP)

### Teoría
Las expresiones regulares son patrones de búsqueda para trabajar con texto. Python usa el módulo `re`.

### Importar el Módulo

```python
import re
```

### Métodos Principales

#### `re.search()` - Busca en cualquier parte
```python
texto = "Mi email es juan@example.com"
patron = r'\w+@\w+\.\w+'
resultado = re.search(patron, texto)

if resultado:
    print(resultado.group())  # juan@example.com
    print(resultado.start())  # Posición de inicio
```

#### `re.match()` - Busca al inicio
```python
texto = "Python es genial"
if re.match(r'Python', texto):
    print("Coincide al inicio")
```

#### `re.findall()` - Encuentra todas las coincidencias
```python
texto = "Contactos: juan@email.com, maria@gmail.com"
emails = re.findall(r'\w+@\w+\.\w+', texto)
print(emails)  # ['juan@email.com', 'maria@gmail.com']
```

#### `re.sub()` - Reemplazar
```python
texto = "Teléfono: 123-456-7890"
nuevo = re.sub(r'\d', 'X', texto)
print(nuevo)  # Teléfono: XXX-XXX-XXXX
```

#### `re.split()` - Dividir
```python
texto = "uno,dos;tres:cuatro"
partes = re.split(r'[,;:]', texto)
print(partes)  # ['uno', 'dos', 'tres', 'cuatro']
```

### Metacaracteres Básicos

| Patrón | Significado | Ejemplo |
|--------|-------------|---------|
| `.` | Cualquier carácter | `a.c` → abc, aZc |
| `^` | Inicio de línea | `^Hola` |
| `$` | Fin de línea | `mundo$` |
| `*` | 0 o más repeticiones | `ab*` → a, ab, abb |
| `+` | 1 o más repeticiones | `ab+` → ab, abb |
| `?` | 0 o 1 repetición | `ab?` → a, ab |
| `{n}` | Exactamente n | `\d{3}` → 123 |
| `{n,m}` | Entre n y m | `\d{2,4}` |
| `[]` | Conjunto de caracteres | `[aeiou]` |
| `[^]` | Negación | `[^0-9]` |
| `\|` | OR lógico | `gato\|perro` |
| `()` | Grupo de captura | `(ab)+` |

### Clases de Caracteres

| Patrón | Equivalente | Descripción |
|--------|-------------|-------------|
| `\d` | `[0-9]` | Dígito |
| `\D` | `[^0-9]` | No dígito |
| `\w` | `[a-zA-Z0-9_]` | Alfanumérico |
| `\W` | `[^a-zA-Z0-9_]` | No alfanumérico |
| `\s` | `[ \t\n\r]` | Espacio en blanco |
| `\S` | `[^ \t\n\r]` | No espacio |

### Ejemplos Prácticos

#### Validar Email
```python
def validar_email(email):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(patron, email))

print(validar_email("test@example.com"))  # True
print(validar_email("test@com"))  # False
```

#### Validar Teléfono Argentino
```python
def validar_telefono_ar(tel):
    # Formatos: +54 11 1234-5678 o 11-1234-5678
    patron = r'^(\+54\s?)?(\d{2,4})[\s-]?\d{4}[\s-]?\d{4}$'
    return bool(re.match(patron, tel))

print(validar_telefono_ar("+54 11 1234-5678"))  # True
```

#### Extraer Hashtags
```python
texto = "Me encanta #Python y #Django para #WebDev"
hashtags = re.findall(r'#\w+', texto)
print(hashtags)  # ['#Python', '#Django', '#WebDev']
```

#### Limpiar HTML
```python
html = "<p>Hola <strong>mundo</strong></p>"
texto_limpio = re.sub(r'<[^>]+>', '', html)
print(texto_limpio)  # Hola mundo
```

### Grupos de Captura

```python
# Capturar partes de una fecha
texto = "Fecha: 25/12/2024"
patron = r'(\d{2})/(\d{2})/(\d{4})'
match = re.search(patron, texto)

if match:
    dia = match.group(1)    # 25
    mes = match.group(2)    # 12
    anio = match.group(3)   # 2024
    print(f"Día: {dia}, Mes: {mes}, Año: {anio}")
```

### Flags (Modificadores)

```python
# re.IGNORECASE - Ignorar mayúsculas/minúsculas
resultado = re.search(r'python', 'Me gusta PYTHON', re.IGNORECASE)

# re.MULTILINE - ^ y $ aplican a cada línea
texto = """línea1
línea2
línea3"""
lineas = re.findall(r'^línea\d', texto, re.MULTILINE)
```

## RECURSOS RECOMENDADOS

### Documentación Oficial
- Python Docs: https://docs.python.org/es/3/
- Django Docs: https://docs.djangoproject.com/
- MySQL Python: https://dev.mysql.com/doc/connector-python/

### Práctica
- HackerRank: https://www.hackerrank.com/domains/python
- LeetCode: https://leetcode.com/
- Real Python: https://realpython.com/
