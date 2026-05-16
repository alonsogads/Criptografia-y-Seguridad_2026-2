# ==============================================================================
# Problema 1: Cifrado César
# ==============================================================================

# Definimos nuestro alfabeto de 27 caracteres como una constante global
ALFABETO = "abcdefghijklmnñopqrstuvwxyz"
MODULO = len(ALFABETO) #27

def descifrar_cesar(texto_cifrado, clave):
    """
    Función que recorre un texto y realiza una rotación de letras
    según la clave proporcionada, respetando los espacios.
    """
    texto_desplazado = ""
    for caracter in texto_cifrado.lower():
        if caracter in ALFABETO:
            # Obtenemos la posición de la letra cifrada
            indice_cifrado = ALFABETO.index(caracter)
            # Aplicamos la fórmula de descifrado
            indice_rotado = (indice_cifrado - clave) % MODULO
            # Añadimos la letra descifrada al resultado
            texto_desplazado += ALFABETO[indice_rotado]
        else:
            # Si es un espacio u otro símbolo, lo dejamos igual
            texto_desplazado += caracter
    return texto_desplazado

# ------------------------------------------------------------------------------
# Caso 1. Ataque por Fuerza Bruta
# ------------------------------------------------------------------------------
print("--- 1. ATAQUE POR FUERZA BRUTA ---")
texto1 = "Nc xkfc gu dgnnc"

# Probamos las 27 claves posibles (de 0 a 26)
for clave_prueba in range(MODULO):
    intento = descifrar_cesar(texto1, clave_prueba)
    # Al imprimir, buscaremos visualmente el mensaje en español
    print(f"Clave {clave_prueba}: {intento}")

# ------------------------------------------------------------------------------
# 2. Ataque por Conocimiento Adicional
# ------------------------------------------------------------------------------
print("\n--- 2. ATAQUE POR CONOCIMIENTO ADICIONAL ---")
texto2 = "Zo qgweidugotío sh jb hsqgsid"

# Sabemos que la 'd' (cifrada) corresponde a la 'o' (descifrada)
indice_cifrado = ALFABETO.index('d')  # Posición 3
indice_descifrado = ALFABETO.index('o')    # Posición 15

# Calculamos la clave con la fórmula de descifrado
clave_conocida = (indice_cifrado - indice_descifrado) % MODULO

print(f"Clave calculada: {clave_conocida}")
print(f"Mensaje descifrado: {descifrar_cesar(texto2, clave_conocida)}")

# ------------------------------------------------------------------------------
# 3. Ataque por Análisis de Frecuencias
# ------------------------------------------------------------------------------
print("\n--- 3. ATAQUE POR ANÁLISIS DE FRECUENCIAS ---")
texto3 = "Jx qzd kfhnp mjwnw f ptx ijqfx xnr ifwxj hzjryf xtgwj ytit hzfrit jwjx ñtajr"

# Contamos las apariciones de cada letra manualmente usando un diccionario
conteo_letras = {}
for caracter in texto3.lower():
    if caracter in ALFABETO:
        if caracter in conteo_letras:
            conteo_letras[caracter] += 1
        else:
            conteo_letras[caracter] = 1

# Buscamos la letra con el mayor número de apariciones
letra_mas_frecuente = ''
max_apariciones = 0

for letra, cantidad in conteo_letras.items():
    if cantidad > max_apariciones:
        max_apariciones = cantidad
        letra_mas_frecuente = letra

print(f"Letra más frecuente en el texto cifrado: '{letra_mas_frecuente}' ({max_apariciones} apariciones)")

# Asumimos que esta letra corresponde a la 'e' del español
indice_frecuente = ALFABETO.index(letra_mas_frecuente)
indice_e = ALFABETO.index('e')

# Calculamos la clave bajo esta suposición
clave_frecuencia = (indice_frecuente - indice_e) % MODULO

print(f"Clave inferida estadísticamente: {clave_frecuencia}")
print(f"Mensaje descifrado: {descifrar_cesar(texto3, clave_frecuencia)}")