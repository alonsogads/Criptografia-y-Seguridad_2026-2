# ==============================================================================
# Problema 2: Cuadrado de Polibio
# ==============================================================================

# Definimos nuestra matriz 5x5 como una lista de listas.
# Excluimos la 'z' y la 'ñ' (alfabeto de 25 letras).
CUADRADO_POLIBIO = [
    ['a', 'b', 'c', 'd', 'e'],
    ['f', 'g', 'h', 'i', 'j'],
    ['k', 'l', 'm', 'n', 'o'],
    ['p', 'q', 'r', 's', 't'],
    ['u', 'v', 'w', 'x', 'y']
]

def limpiar_texto(texto):
    """
    Estandariza el texto a nuestro alfabeto: cambia a minúsculas, quita acentos, 
    reemplaza 'z' por 's' y elimina espacios/signos de puntuación.
    """
    texto = texto.lower()
    
    # Estandariza acentos y sustituye la letra 'z' por 's'
    reemplazos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'z': 's'}
    for original, nuevo in reemplazos.items():
        texto = texto.replace(original, nuevo)
        
    texto_limpio = ""
    # Conserva solo las letras que existen en nuestra matriz (de la 'a' a la 'y' después de la estandarización)
    # Elimina espacios y signos de puntuación.
    for caracter in texto:
        if 'a' <= caracter <= 'y':
            texto_limpio += caracter
            
    return texto_limpio

def encriptar_polibio(texto):
    """
    Busca cada letra en la matriz 5x5 y devuelve sus coordenadas (Fila-Columna).
    """
    texto_limpio = limpiar_texto(texto)
    resultado = ""
    
    for letra in texto_limpio:
        # Recorremos la matriz buscando la letra
        for fila in range(5):
            for columna in range(5):
                if CUADRADO_POLIBIO[fila][columna] == letra:
                    # Sumamos 1 porque los índices en Python empiezan en 0 pero en Polibio empiezan en 1
                    coordenada = str(fila + 1) + str(columna + 1)
                    resultado += coordenada + " " # Agregamos el espacio entre cada coordenada
                    
    # Retornamos el resultado quitando el espacio final extra
    return resultado.strip()

def desencriptar_polibio(texto_cifrado):
    """
    Toma pares de números y extrae la letra correspondiente de la matriz.
    """
    # Separamos la cadena de números por los espacios
    pares = texto_cifrado.split(" ")
    texto_descifrado = ""
    
    for par in pares:
        # El primer número es la fila, el segundo es la columna.
        # Restamos 1 para convirtir los índices (1-5) a los de Python (0-4).
        indice_fila = int(par[0]) - 1
        indice_columna = int(par[1]) - 1
        
        # Extraemos la letra directamente de la matriz
        letra_encontrada = CUADRADO_POLIBIO[indice_fila][indice_columna]
        texto_descifrado += letra_encontrada
        
    return texto_descifrado

# ------------------------------------------------------------------------------
# Pruebas de cifrado y descifrado
# ------------------------------------------------------------------------------
print("--- DESENCRIPTACIÓN DE CUADRADO DE POLIBIO ---")
mensaje_cifrado = "15 32 45 24 15 33 41 35 34 35 15 44 41 15 43 11 11 34 11 14 24 15"
mensaje_descifrado = desencriptar_polibio(mensaje_cifrado)
print(f"Cifrado: {mensaje_cifrado}")
print(f"Descifrado: {mensaje_descifrado}")

print("\n--- ENCRIPTACIÓN DE CUADRADO DE POLIBIO ---")
mensaje_claro = "Si la felicidad tuviera una forma, tendría forma de cristal, porque puede estar a tu alrededor sin que la notes. Pero si cambias de perspectiva, puede reflejar una luz capaz de iluminarlo todo."
mensaje_encriptado = encriptar_polibio(mensaje_claro)
print(f"Texto original:\n{mensaje_claro}")
print(f"\nTexto procesado:\n{limpiar_texto(mensaje_claro)}")
print(f"\nTexto encriptado:\n{mensaje_encriptado}")