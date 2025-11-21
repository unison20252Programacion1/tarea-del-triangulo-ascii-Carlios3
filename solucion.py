# En este archivo debes implementar la función

def triangulo_simetrico(m: int, s: str) -> str:
    # TODO: validar altura mayor que 0 e imprimir "Error: La altura debe ser un entero positivo" y salir
    if m <= 0:
        print("Error: La altura debe ser un entero positivo")
        return
        
    # Triangulo creciente:
    for i in range(1, m + 1):
        print(s * i)

    # Triangulo decreciente
    for i range(m - 1, 0, -1):
        print(s * i)
