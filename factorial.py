class factorial_iterative:
    def __init__(self, n):
        self.n = n
        self.result = 1

    def __call__(self):
        if self.n == 0:
            return self.result
        else:
            self.result *= self.n
            self.n -= 1
            return self()   
    

def factorial_iterative(n):
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")

    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


def factorial_recursive(n):
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")

    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)
