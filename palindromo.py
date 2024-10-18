def es_palindromo(x):
    # Verificar si el número está en el rango válido
    if x < 1 or x > 10000:
        return -1
    
    # Guardar el número original
    num_original = x
    num_revertido = 0
    
    # Invertir el número
    while x > 0:
        digito = x % 10  # Obtener el último dígito
        num_revertido = num_revertido * 10 + digito  # Construir el número invertido
        x = x // 10  # Eliminar el último dígito
    
    # Verificar si el número original es igual al invertido
    if num_original == num_revertido:
        return 1  # Es un palíndromo
    else:
        return 0  # No es un palíndromo

# Ejemplo de uso
x = 55
resultado = es_palindromo(x)
if resultado == 1:
    print(f"{x} es un palíndromo.")
elif resultado == 0:
    print(f"{x} no es un palíndromo.")
else:
    print("Número fuera de rango.")