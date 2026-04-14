# ==============================================================================
# Problema 3: Cifrado Vigenère (Test de Kasiski)
# ==============================================================================

def limpiar_texto(texto):
    """Elimina signos que no esten en el alfabeto y deja solo letras mayúsculas A-Z."""
    texto_limpio = ""
    for caracter in texto.upper():
        if 'A' <= caracter <= 'Z':
            texto_limpio += caracter
    return texto_limpio

def buscar_patrones_y_distancias(texto, longitud_patron=3):
    """Encuentra n-gramas repetidos y calcula la distancia entre ellos."""
    posiciones = {}
    
    # Recorremos el texto para extraer todos los bloques de 'longitud_patron' letras
    for i in range(len(texto) - longitud_patron + 1):
        patron = texto[i:i + longitud_patron]
        if patron in posiciones:
            # Si el patrón ya estaba en el diccionario, agrega su nuevo índice de ubicación
            posiciones[patron].append(i)
        else:
            # Si el patrón es nuevo, lo agrega al diccionario junto con su índice de ubicación
            posiciones[patron] = [i]

    patrones_repetidos = {}
    distancias = []
    
    # Filtramos los patrones que aparecen más de una vez
    for patron, lista_posiciones in posiciones.items():
        if len(lista_posiciones) > 1:
            # Agregamos el patron repetido al diccionario con su lista de posiciones
            patrones_repetidos[patron] = lista_posiciones
            
            # Calculamos la distancia entre apariciones consecutivas
            for j in range(1, len(lista_posiciones)):
                distancia = lista_posiciones[j] - lista_posiciones[j-1]
                # Agregamos una nueva distancia si es que no estaba een la lista
                distancias.append(distancia)
                
    return patrones_repetidos, distancias

def obtener_divisores(numero):
    """Encuentra todos los divisores enteros de un número (mayor a 2)."""
    divisores = []
    # Empezamos en 3 porque el factor 1 y 2 no nos sirve para una clave de Vigenère
    for i in range(3, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    return divisores

# ------------------------------------------------------------------------------
# Ejecución del programa
# ------------------------------------------------------------------------------

texto_interceptado = """
ECISCRVSWVLGDDWUEFHFNGESXUVTICOKQOTA.JPHWAKFBNA
EUONOJFHONCPHRZNSCOKEWLSUFPFEEUWOMHPQFAEEDOLDB
QROKFZLNQBSXVMFZZNMQQSACESDDVMONHBROUEBGMOCVI
SLZAOXDGTJDAQVZLDRTOVAKDDWOKJTFEJBBFNHBGLCRJRLS
KVEVUDBXOPVDVZADBGSLCPOKUWSSJCRQWCOLFOKUC
"""

print("--- INICIANDO TEST DE KASISKI ---")

# Limpiamos el texto
texto_procesado = limpiar_texto(texto_interceptado)

# Buscamos los trigramas (3 letras)
patrones, lista_distancias = buscar_patrones_y_distancias(texto_procesado, 3)

print("\nPatrones repetidos encontrados y sus posiciones (índices):")
for patron, posiciones in patrones.items():
    print(f"    - '{patron}': Posiciones {posiciones}")

print(f"\nDistancias calculadas entre repeticiones: {lista_distancias}")

# Obtenemos los divisores de las distancias
conteo_divisores = {}
for dist in lista_distancias:
    divisores = obtener_divisores(dist)
    for f in divisores:
        if f in conteo_divisores:
            conteo_divisores[f] += 1
        else:
            conteo_divisores[f] = 1

# Ordenamos el diccionario de mayor a menor frecuencia de divisores
divisores_ordenados = sorted(conteo_divisores.items(), key=lambda item: item[1], reverse=True)

print("\nLas 5 posibles longitudes de clave:")
# Mostramos los primeros 5 resultados para dar contexto
for i in range(min(5, len(divisores_ordenados))):
    divisor, frecuencia = divisores_ordenados[i]
    print(f"    - Longitud {divisor}: Aparece {frecuencia} veces como divisor común")