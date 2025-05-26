def fibonacci_iterative(n):
    if n < 0:
        raise ValueError("La secuencia de Fibonacci no está definida para números negativos")

    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fibonacci_recursive(n):
    if n < 0:
        raise ValueError("La secuencia de Fibonacci no está definida para números negativos")

    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
