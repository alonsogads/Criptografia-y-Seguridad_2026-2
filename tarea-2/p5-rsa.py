import math
import matplotlib.pyplot as plt

# 1. Funcion preliminar: Simulador de cifrado RSA
def rsa_encrypt(message, e, n):
    """
    Retorna el criptograma usando exponenciacion modular.
    Representa la intercepcion de un mensaje en texto plano.
    """
    return pow(message, e, n)

# 2. Funcion de probabilidad del ataque de cumpleanos
def collision_probability(d, m):
    """
    Calcula la probabilidad de interceptar dos criptogramas iguales.
    d: numero de mensajes interceptados
    m: tamano del espacio de mensajes posibles (claves o textos)
    """
    # Se usa la formula: 1 - exp(-d(d-1) / 2m)
    exponent = -(d * (d - 1)) / (2 * m)
    return 1 - math.exp(exponent)

def main():
    # Parametros iniciales de la simulacion
    m = 100000  # Espacio de mensajes posibles (ej. 100,000 PINs o datos estructurados)
    
    # Generacion de datos para el eje X (mensajes interceptados)
    # Vamos desde 1 hasta 2500 con saltos de 10 en 10
    d_values = list(range(1, 2500, 10)) 
    
    # Calculo del eje Y (probabilidades)
    probabilities = [collision_probability(d, m) for d in d_values]
    
    # 3. Calculo del punto de inflexion (probabilidad muy cercana a 1)
    # Buscamos en que momento la probabilidad llega al 99% (0.99)
    # Despeje: d = sqrt(-2 * m * ln(1 - P))
    target_p = 0.99
    inflection_point = math.ceil(math.sqrt(-2 * m * math.log(1 - target_p)))
    
    print("--- Resultados de la Simulacion del Ataque ---")
    print(f"Tamano del espacio de mensajes (m): {m}")
    print(f"Punto de colision casi segura (~99%): {inflection_point} mensajes interceptados")
    print("Generando grafica para el reporte...")

    # 4. Generacion de la grafica
    plt.figure(figsize=(10, 6))
    plt.plot(d_values, probabilities, label="Probabilidad de colision", color="blue", linewidth=2.5)
    
    # Lineas de referencia
    plt.axvline(x=inflection_point, color="red", linestyle="--", 
                label=f"Exito del 99% (d = {inflection_point})")
    
    # Opcional: Mostrar tambien la frontera del 50%
    punto_medio = math.ceil(1.17741 * math.sqrt(m))
    plt.axvline(x=punto_medio, color="green", linestyle=":", 
                label=f"Exito del >50% (d = {punto_medio})")

    # Etiquetas de la grafica (sin acentos)
    plt.title("Ataque basado en la Paradoja del Cumpleanos (RSA)")
    plt.xlabel("Numero de mensajes interceptados (d)")
    plt.ylabel("Probabilidad de colision")
    plt.legend(loc="lower right")
    plt.grid(True, alpha=0.6)
    
    # Mostrar ventana
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()