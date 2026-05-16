import re
import math
import hashlib
import unicodedata
import string
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# === Funciones básicas ===

def es_primo(numero):
    """
    Revisa si un numero es primo.
    """
    if numero < 2: 
        return False
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0: 
            return False
    return True

def generar_primos(n):
    """
    Crea una lista con los primeros n numeros primos.
    """
    lista_primos = []
    candidato = 2
    while len(lista_primos) < n:
        if es_primo(candidato): 
            lista_primos.append(candidato)
        candidato += 1
    return lista_primos

def limpiar_texto(ruta_del_archivo):
    """
    Abre el archivo de texto y le realiza:
    - Normalizacion: Quita las tildes y lo pasa a minusculas
    - Limpieza: Elimina simbolos que no sean letras (a-zA-Z).
    """
    with open(ruta_del_archivo, 'r', encoding='utf-8') as archivo:
        texto_sucio = archivo.read()
        
    # Le quitamos las tildes a las vocales (ejemplo: c a i a) para no perder letras
    texto_sin_acentos = unicodedata.normalize('NFKD', texto_sucio).encode('ASCII', 'ignore').decode('utf-8')
    
    # Borramos todo lo que no sea una letra de la a a la z y lo pasamos a minusculas
    texto_final = re.sub(r'[^a-zA-Z]', '', texto_sin_acentos).lower()
    return texto_final

# === Generacion de claves ===

def generar_claves(texto_limpio, palabra_base="kevinmitnick"):
    """
    Genera varias opciones de clave probando distintas formas
    de sacar letras del texto y de mezclarlas con la palabra secreta.
    """
    primos = generar_primos(50)
    longitud_texto = len(texto_limpio)
    longitud_palabra = len(palabra_base)
    abecedario = string.ascii_lowercase  # Las letras de la 'a' a la 'z'
    
    opciones_de_extraccion = []
    
    # Forma 1: Sacar la letra directo de la posicion (primo - 2)
    letras_forma1 = ""
    for p in primos:
        posicion = (p - 2) % longitud_texto
        letras_forma1 += texto_limpio[posicion]
    opciones_de_extraccion.append(letras_forma1)
    
    # Forma 2: Sacar la letra de la posicion (p) y recorrerla en el abecedario
    letras_forma2 = ""
    for p in primos:
        letra = texto_limpio[p % longitud_texto]
        lugar_en_abecedario = abecedario.index(letra)
        nuevo_lugar = (lugar_en_abecedario + (p - 2)) % 26
        letras_forma2 += abecedario[nuevo_lugar]
    opciones_de_extraccion.append(letras_forma2)
    
    # Forma 3: Sacar de (p-2) y tambien recorrerla en el abecedario
    letras_forma3 = ""
    for p in primos:
        letra = texto_limpio[(p - 2) % longitud_texto]
        lugar_en_abecedario = abecedario.index(letra)
        nuevo_lugar = (lugar_en_abecedario + (p - 2)) % 26
        letras_forma3 += abecedario[nuevo_lugar]
    opciones_de_extraccion.append(letras_forma3)
    
    # Ahora mezclamos las letras extraidas con la palabra base
    claves_candidatas = []
    for grupo_letras in opciones_de_extraccion:
        
        # Mezcla A: Sumar sus posiciones en el abecedario (Vigenere)
        mezcla_suma = ""
        for i in range(50):
            lugar_letra1 = abecedario.index(grupo_letras[i])
            lugar_letra2 = abecedario.index(palabra_base[i % longitud_palabra])
            mezcla_suma += abecedario[(lugar_letra1 + lugar_letra2) % 26]
        claves_candidatas.append(mezcla_suma)
        
        # Mezcla B: Restar sus posiciones en el abecedario
        mezcla_resta = ""
        for i in range(50):
            lugar_letra1 = abecedario.index(grupo_letras[i])
            lugar_letra2 = abecedario.index(palabra_base[i % longitud_palabra])
            mezcla_resta += abecedario[(lugar_letra1 - lugar_letra2) % 26]
        claves_candidatas.append(mezcla_resta)
        
        # Mezcla C: Una letra y una letra (Intercalado simple)
        # Solo damos 25 vueltas para juntar exactamente 50 caracteres (25 pares)
        mezcla_intercalada = ""
        for i in range(25):
            letra_del_texto = grupo_letras[i]
            letra_de_palabra = palabra_base[i % longitud_palabra]
            mezcla_intercalada += letra_del_texto + letra_de_palabra
        claves_candidatas.append(mezcla_intercalada)
        
    return claves_candidatas

# === Comprobacion y descifrado ===

def comprobar_clave(clave_candidata, ruta_del_archivo_hashes):
    """
    Convierte la clave a hash y busca si esta en la lista de validacion.
    """
    hash_generado = hashlib.sha256(clave_candidata.encode()).hexdigest()
    
    with open(ruta_del_archivo_hashes, 'r', encoding='utf-8') as archivo:
        # Usamos un 'set' para que la busqueda sea instantanea
        hashes_set = set(linea.strip() for linea in archivo.readlines())
        
    if hash_generado in hashes_set:
        print(f"\n[*] ¡Exito! Se ha encontrado el hash: {hash_generado}")
        print(f"[*] La clave correcta es: {clave_candidata}")
        return True
    return False

def revelar_secreto(ruta_mensaje_cifrado, clave_correcta):
    """
    Intenta descifrar el mensaje cifrado de diferentes formas.
    """
    # Guardamos el hash en formato de texto normal (64 caracteres)
    hash_texto = hashlib.sha256(clave_correcta.encode()).hexdigest()
    
    # Leemos el archivo cifrado y le quitamos los saltos de linea
    with open(ruta_mensaje_cifrado, 'r', encoding='utf-8') as archivo:
        texto_hexadecimal = archivo.read().replace('\n', '').strip()
        
    try:
        # Convertimos el texto hexadecimal a bytes puros
        datos_completos = bytes.fromhex(texto_hexadecimal)
    except ValueError:
        print("[-] El archivo cipher.txt no tiene un formato hexadecimal valido.")
        return
        
    # En el estandar AES-GCM, los primeros 12 bytes siempre son el Nonce
    nonce = datos_completos[:12]
    mensaje_cifrado = datos_completos[12:]
    
    # Diccionario con 3 posibles interpretaciones de la llave (todas dan 32 bytes)
    llaves_a_probar = {
        "hash a bytes": bytes.fromhex(hash_texto),
        "doble Hash": hashlib.sha256(hash_texto.encode()).digest(),
        "original": hashlib.sha256(clave_correcta.encode()).digest()
    }
    
    exito = False
    
    # Probamos cada llave. Si una falla, el 'except' la atrapa y pasamos a la siguiente.
    for nombre_metodo, llave_en_bytes in llaves_a_probar.items():
        herramienta_aes = AESGCM(llave_en_bytes)
        try:
            # Si esta linea no marca error, significa que la llave era la correcta
            mensaje_abierto = herramienta_aes.decrypt(nonce, mensaje_cifrado, None).decode('utf-8')
            
            print("\n ***  Mensaje desenciptado ***   ")
            print(f"[*] El candado abrio usando: {nombre_metodo}")
            print(mensaje_abierto)
            print("\n")
            
            exito = True
            break
        except Exception:
            # Ignoramos el error y el ciclo prueba la siguiente opcion
            continue
            
    if not exito:
        print("[-] Ningun metodo pudo descifrar")

# === Programa principal ===

def iniciar_programa():
    print("- Iniciando y limpiando el texto...")
    texto = limpiar_texto('archivos/file.txt')
    print(f"- El texto se limpio y quedaron {len(texto)} letras para usar.")
    
    lista_de_claves = generar_claves(texto)
    print(f"- Se crearon {len(lista_de_claves)} posibles claves. Se prueban todas.")
    
    for indice, posible_clave in enumerate(lista_de_claves, 1):    
        if comprobar_clave(posible_clave, 'archivos/hashes.txt'):
            revelar_secreto('archivos/cipher.txt', posible_clave)
            break
    else:
        print("\n- Error, ninguna clave dio resultado.")

if __name__ == "__main__":
    iniciar_programa()
