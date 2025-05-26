def flatten(data):
    resultado = []
    if isinstance(data, dict):
        for clave, valor in data.items():
            resultado.extend(flatten(clave))
            resultado.extend(flatten(valor))
    elif isinstance(data, (list, tuple, set)):
        for item in data:
            resultado.extend(flatten(item))
    else:
        resultado.append(data)

    return resultado
