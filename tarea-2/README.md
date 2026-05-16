# Tarea 2

### 1. Criptoanálisis lineal. Índice de coincidencia.

**Definición**: Sea $\Sigma$ un conjunto finito, $n \in \mathbb{N}$ y $X = (x_1, ..., x_n)$ una variable aleatoria que toma valores en $\Sigma^n$. El índice de coincidencia $I_c(X)$ es la probabilidad de que, para dos índices aleatorios $j,k$ se tenga que $x_j = x_k$.

Demuestra lo siguiente: Sea $\Sigma = \{ \sigma_1, ..., \sigma_m \}$

1. Si $p_i$ es la probabilidad de que el símbolo $\sigma_i$ aparezca en la variable aleatoria $X$, entonces:

$$
I_c(X) = \sum_{i=1}^{m} p_i^2
$$

en particular, si se trata de sucesos equiprobables, $I_c(X) = \frac{1}{m}$.

2. Si $z \in \Sigma^n$ y $f_i$ es la frecuencia de aparición de $\sigma_i$ en $z$, entonces:

$$
I_c(z) = \frac{\sum_{i=1}^{m} \binom{f_i}{2}}{\binom{n}{2}} = \frac{\sum_{i=1}^{m} f_i(f_i -1)}{n(n-1)}
$$

#### Demostración 1

1. Se debe demostrar que $I_c(X) = \sum_{i=1}^{m} p_i^2$ y que para sucesos equiprobables $I_c(X) = \frac{1}{m}$.

Por definición, el índice de coincidencia $I_c(X)$ es la probabilidad de que al elegir dos índices aleatorios independientes $j$ y $k$, los símbolos en esas posiciones sean idénticos. Es decir, buscamos calcular la probabilidad del evento $P(x_j = x_k)$.

El evento "ambos símbolos son idénticos" ocurre si y solo si ambos son el símbolo $\sigma_1$, **o** ambos son $\sigma_2$, o ambos son $\sigma_3$, y así sucesivamente hasta $\sigma_m$.

Dado que estos eventos son mutuamente excluyentes (no pueden ser $\sigma_1$ y $\sigma_2$ al mismo tiempo), la probabilidad total es la suma de las probabilidades individuales para cada símbolo del alfabeto $\Sigma$:

$$
P(x_j = x_k) = \sum_{i=1}^{m} P(x_j = \sigma_i \cap x_k = \sigma_i)
$$

Como la elección de los índices $j$ y $k$ son eventos independientes, la probabilidad de la intersección es el producto de sus probabilidades:

$$
P(x_j = \sigma_i \cap x_k = \sigma_i) = P(x_j = \sigma_i) \cdot P(x_k = \sigma_i)
$$

Por hipótesis, sabemos que la probabilidad de que aparezca cualquier símbolo $\sigma_i$ es $p_i$. Por lo tanto, $P(x_j = \sigma_i) = p_i$ y $P(x_k = \sigma_i) = p_i$. Sustituyendo esto en nuestra ecuación anterior:

$$
I_c(X) = P(x_j = x_k) = \sum_{i=1}^{m} (p_i \cdot p_i) = \sum_{i=1}^{m} p_i^2 \quad _\blacksquare
$$

Ahora queremos demostrar el caso particular cuando los sucesos son equiprobables.

Si todos los símbolos de $\Sigma$ tienen la misma probabilidad de aparecer, y hay $m$ símbolos en total, entonces para todo $i$, $p_i = \frac{1}{m}$.

Sustituyendo esto en la fórmula que acabamos de demostrar:

$$
I_c(X) = \sum_{i=1}^{m} \left( \frac{1}{m} \right)^2 = \sum_{i=1}^{m} \frac{1}{m^2} = m\left(\frac{1}{m^2}\right) = \frac{m}{m^2} = \frac{1}{m} \quad _\blacksquare
$$

#### Demostración 2

Se quiere demostrar que:

$$
I_c(z) = \frac{\sum_{i=1}^{m} \binom{f_i}{2}}{\binom{n}{2}} = \frac{\sum_{i=1}^{m} f_i(f_i -1)}{n(n-1)}
$$

Utilizamos combinatoria sobre una cadena de texto $z$ de longitud fija $n$ y la definición clásica de probabilidad:

$$
P(A) = \frac{\text{Casos favorables}}{\text{Casos posibles}}
$$

- Casos posibles: El total de casos posibles al elegir un par de letras cualquiera dentro del texto de longitud $n$. El número total de formas de elegir 2 elementos de un conjunto de $n$ elementos sin importar el orden es la combinación $\binom{n}{2}$.
- Casos favorables: Queremos que el par elegido consista en dos letras idénticas.
    
    Si nos enfocamos solo en el símbolo $\sigma_1$, por hipótesis sabemos que aparece $f_1$ veces en el texto. El número de formas de tomar pares iguales de $\sigma_1$ es $\binom{f_1}{2}$, y seguimos sumando los casos para todo $m \in \Sigma$.
    
    Por lo que el número total de casos en las que $z$ tiene dos caracteres iguales es $\sum_{i=1}^{m} \binom{f_i}{2}$.
    

Sustituyendo en la fórmula de probabilidad obtenemos la primera igualdad que buscamos:

$$
I_c(z) = \frac{\sum_{i=1}^{m} \binom{f_i}{2}}{\binom{n}{2}}
$$

Ahora aplicamos la definición del coeficiente binomial, recordando que:

$$
\binom{k}{2} = \frac{k!}{2!(k-2)!} = \frac{k(k-1)}{2}
$$

Por lo que:

- Para el numerador: $\sum_{i=1}^{m} \frac{f_i(f_i - 1)}{2}$
- Para el denomidador: $\frac{n(n - 1)}{2}$.

Sustituyendo y desarrollando:

$$
I_c(z) = \frac{ \sum_{i=1}^{m} \frac{f_i(f_i - 1)}{2} }{ \frac{n(n - 1)}{2} } = \frac{\sum_{i=1}^{m} f_i(f_i -1)}{n(n-1)} _\blacksquare
$$

---
### 2. Complejidad algorítmica. Problemas P, NP, NP-Completo.

**Definición**. Se dice que un problema puede resolverse en tiempo polinómico o simplemente que está en P, si una máquina de Turing está diseñada ópticamente para su resolución tras un número de pasos que es una función polinímica de la longitud de los datos de partida.

**Definición**. Se dice que un problema es de resolución no determinista en tiempo polinómico o que está en NP, si una solución a este puede ser comprobada mediante un algoritmo polinómico.

1. Investigue sobre ¿qué son los caminos hamiltonianos?
2. Pruebe que los caminos hamiltonianos son problema NP-Completo.
3. Muestre que el algoritmo DES es un problema tipo P.
4. Dados dos números $m$ y $n$ con $m \geq n$, prueba que usando el algoritmo de Euclides tiene complejidad acotada por: $O(m(\log_2(m))^2)$

#### Investigación

> ¿Qué son los caminos hamiltonianos?
> 

En la teoría de grafos, un grafica o grafo es un conjunto de nodos (vértices) conectados por líneas (aristas).

Un camino hamiltoniano es un recorrido a través de un gráfica que visita absolutamente todos los vértices exactamente una vez.

Ejemplo: Sea $G$ una gráfica con 4 vértices formando un cuadrado en donde A, B, C, D, y las aristas son las líneas del perímetro.

- Un camino `A -> B -> C -> D` es un camino hamiltoniano porque pasamos por los 4 nodos sin repetir ninguno.

#### Demostración 1

> Pruebe que los caminos hamiltonianos son problema NP-Completo.
> 

Para demostrar que el problema de decisión $L$ de encontrar un camino hamiltoniano en cualquier gráfica es NP-Completo, debemos probar obligatoriamente dos condiciones:

1. Que el problema pertenece a la clase NP ($L \in \text{NP}$).
2. Que el problema es NP-Duro (todo problema en NP se puede reducir polinómicamente a $L$).

**Primera parte:** Demostrar que ****($L \in \text{NP}$)

Un problema pertenece a NP si, dada una "solución propuesta", podemos verificar si es correcta en tiempo polinómico.

Sea $G$ una gráfica con vertices $v_1, v_2, ..., v_k$, el algoritmo verificador de la solución:

- Verifica que el número de vértices en la secuencia sea exactamente igual al número total de vértices del grafo $G=(V, E)$. Es decir, que $k = |V|$. Esto toma tiempo $O(|V|)$.
- Verifica que no haya vértices repetidos en la secuencia (se puede hacer ordenando o usando un arreglo hash) en tiempo polinómico $O(|V| \log |V|)$.
- Para cada par consecutivo de vértices $(v_i, v_{i+1})$, verifica que exista una arista en el conjunto $E$. En una matriz de adyacencia, esto toma $O(1)$ por arista, por lo que revisar toda la ruta toma tiempo $O(|V|)$.

Como la verificación total toma tiempo polinómico respecto al tamaño de la gráfica, el problema del camino hamiltoniano $L \in \text{NP}$.

**Primera parte:** Demostrar que es NP-Duro.

Se debe realizar una reducción polinómica desde un problema que ya se sepa que es NP-Completo. El estándar es reducir desde el problema de satisfactibilidad booleana (3-SAT).

Supongamos una fórmula booleana en 3-CNF con variables $x_1, ..., x_n$ y cláusulas $C_1, ..., C_m$.

Construimos un gráfica $G$ estructurada de la siguiente manera:

- Creamos un subgrafo "diamante" por cada variable $x_i$. Recorrer este diamante de izquierda a derecha representará asignar *Verdadero*, y de derecha a izquierda representará *Falso*.
- Creamos un nodo por cada cláusula $C_j$.
- Conectamos los caminos de los diamantes a los nodos de las cláusulas de tal forma que un camino solo pueda visitar el nodo de la cláusula si el valor de verdad asignado en el diamante la satisface.

Esta construcción transforma la fórmula lógica en un grafo en tiempo polinómico $O(n + m)$.

Se demuestra lógicamente que la fórmula 3-SAT original es satisfacible **si y solo si** el grafo resultante contiene un camino hamiltoniano (ya que para visitar todos los nodos de las cláusulas, la asignación de verdad en los diamantes debe ser válida para todas).

Al poder reducir 3-SAT (NP-Completo) al problema del camino hamiltoniano en tiempo polinómico, $L$ es NP-Duro.

**Conclusión:** Al ser NP y NP-Duro simultáneamente, el problema del camino hamiltoniano es $L$ es **NP-Completo**.

#### Demostración 2

> El algoritmo DES es un problema tipo P
> 

Para probar que el Estándar de Encriptación de Datos (DES) está en P, debemos demostrar que una máquina de Turing determinista ejecuta el algoritmo en un número de pasos acotado por un polinomio respecto a la longitud de los datos de entrada.

**Entrada**: El algoritmo DES tiene un tamaño de entrada estrictamente constante y definido: un bloque de texto plano de 64 bits y una clave de 56 bits.

**Ejecución**: DES funciona bajo una Red de Feistel que realiza exactamente los siguientes pasos:

- Una permutación inicial (operación de reordenamiento matricial) sobre 64 bits.
- 16 rondas idénticas que incluyen: expansión de 32 a 48 bits, aplicación de XOR con la subclave correspondiente, sustitución a través de 8 cajas S (S-Boxes, que son operaciones de búsqueda directa en memoria $O(1)$), y una permutación final P.
- Una permutación inversa final.

**Análisis de tiempo:** Dado que el tamaño de bloque es fijo (64), el número de operaciones en cada ronda es una constante $c$.

- Dado que el número de rondas es fijo (16), el número total de operaciones requeridas para cifrar un bloque es $16c + d$ (donde $d$ son las permutaciones iniciales y finales).
- El tiempo de ejecución es estricta y determinantemente $O(1)$.

La complejidad $O(1)$ es un polinomio de grado cero ($n^0$). Incluso si se asume un enfoque asintótico donde DES procesa un mensaje de tamaño $N$ dividiéndolo en bloques, el tiempo sería lineal $O(N)$, el cual es un polinomio de grado 1. En cualquier interpretación, el algoritmo opera en tiempo polinómico determinista, por lo tanto, DES $\in \text{P} _\blacksquare$

#### Demostración 3

> Complejidad $O(m(\log_2(m))^2)$ del Algoritmo de Euclides.
> 

Dados dos números $m$ y $n$ con $m \geq n$, probar que el tiempo de ejecución del algoritmo de Euclides para hallar el Máximo Común Divisor (MCD) está acotado superiormente por $O(m(\log_2(m))^2)$.

La complejidad estricta a nivel de bits del algoritmo de Euclides es $O((\log_2(m))^2)$. Demostraremos esta cota estricta y, por implicación algebraica, demostraremos que satisface la cota que se pide.

El algoritmo de Euclides realiza divisiones sucesivas. Definimos la sucesión de restos: $r_0 = m$, $r_1 = n$, y el paso general es $r_{i-1} = q_i r_i + r_{i+1}$, donde $r_{i+1} = r_{i-1} \pmod{r_i}$.

El cálculo del número de pasos:

- Sabemos por el teorema del residuo que $r_{i+1} < r_i$.
- Más estrictamente, se puede demostrar que $r_{i+1} < \frac{r_{i-1}}{2}$.
- Como el valor se reduce a menos de la mitad cada dos pasos, el número máximo de divisiones necesarias para que el residuo llegue a cero (caso base) es $2 \log_2(r_0)$.
- Como $r_0 = m$, el número de iteraciones es a lo más $2 \log_2(m)$, lo que nos da un número de iteraciones o pasos de $O(\log_2(m))$.

Ahora para el costo de cada paso (en complejidad de bits), analizamos lo siguiente:

- La división entera de $r_{i-1}$ entre $r_i$ requiere operaciones a nivel de bit. El costo computacional de dividir un número de tamaño $r_{i-1}$ entre $r_i$ es proporcional a la multiplicación de su número de bits: 
$O(\log_2(r_{i-1}) \cdot \log_2(q_i))$.
- Para obtener la complejidad total de bits, se suman los costos de todas las divisiones en las iteraciones. El límite superior de la suma de estos costos a lo largo de toda la sucesión está matemáticamente acotado por $O((\log_2(m))^2)$.

De esta forma hemos demostrado que la división de bits que el costo real es $O((\log_2(m))^2)$. 

Dado que para todo número entero positivo $m \geq 1$, se cumple la desigualdad $(\log_2(m))^2 \leq m(\log_2(m))^2$.

Por definición de cota superior, si una función está acotada por $O((\log_2(m))^2)$, automáticamente satisface estar acotada por funciones de mayor crecimiento.

Por lo tanto, queda probado que la complejidad está estrictamente acotada por **$O(m(\log_2(m))^2)$.**

---
### 3. RSA. Complejidad tipo P.

Use lo siguiente como cierto e investigue:

- Teorema Chino
- Teorema de Cauchy

Un usuario del RSA con claves públicas $(n, e)$ y privada $d$, pruebe que puede factorizar $n$ de modo eficiente (se convierte en un problema $P$).

#### Investigación 1

> Teorema Chino del Resto
> 

Este teorema nos dice que si conocemos los residuos de un número al dividirlo por varios divisores coprimos (que no comparten factores), podemos reconstruir el número original de forma única hasta cierto límite.

Definición: Sean $m_1, m_2, \dots, m_k$ enteros positivos coprimos dos a dos (es decir, $\gcd(m_i, m_j) = 1$ para $i \neq j$). Dado cualquier conjunto de enteros $a_1, a_2, \dots, a_k$, el sistema de congruencias:

$$
x \equiv a_1 \pmod{m_1} \\
x \equiv a_2 \pmod{m_2} \\
\vdots \\
x \equiv a_k \pmod{m_k}
$$

tiene una solución simultánea $x$. Además, esta solución es única módulo $M$, donde $M = m_1 \cdot m_2 \cdots m_k$.

En RSA, trabajamos con $n = p \cdot q$. Como $p$ y $q$ son primos distintos, $\gcd(p, q) = 1$. El TCR nos garantiza que cualquier ecuación módulo $n$ puede dividirse en dos ecuaciones independientes: una módulo $p$ y otra módulo $q$.

#### Investigación 2

> Teorema de Cauchy
> 

Augustin-Louis Cauchy formuló un teorema fundamental para entender la estructura interna de los grupos finitos (las estructuras algebraicas sobre las que opera la aritmética modular).

Sea $G$ un grupo finito con un número de elementos (orden) igual a $|G|$. Si $p$ es un número primo que divide al orden del grupo ($p \mid |G|$), entonces existe al menos un elemento $g \in G$ tal que el orden de $g$ es $p$. Es decir:

$$
g^p = e
$$

donde $e$ es el elemento neutro del grupo.

RSA opera sobre el grupo multiplicativo de enteros módulo $n$, denotado como $(\mathbb{Z}/n\mathbb{Z})^*$. El orden de este grupo es la función de Euler $\phi(n) = (p-1)(q-1)$. El Teorema de Cauchy nos asegura matemáticamente que, dado que el orden es par (pues $p-1$ y $q-1$ son pares), existirá garantizadamente un elemento de orden 2. Es decir, garantiza la existencia de "raíces cuadradas no triviales de 1" dentro del sistema, las cuales son la llave maestra para quebrar $n$.

#### Demostración

> Factorización eficiente de $n$ dado $(n, e, d)$
> 

**Hipótesis:** 

- Se tiene un módulo RSA $n = pq$, donde $p$ y $q$ son primos desconocidos.
- Se conocen los exponentes público $e$ y privado $d$, los cuales cumplen que $ed \equiv 1 \pmod{\phi(n)}$.

Se quiere demostrar que existe un algoritmo con complejidad polinómica (Clase P) capaz de encontrar $p$ y $q$.

Sabemos por definición de RSA que $ed - 1$ es un múltiplo entero de $\phi(n)$. Dado que $\phi(n) = (p-1)(q-1)$ es un número par (porque $p$ y $q$ son primos impares mayores a 2), entonces $ed - 1$ también debe ser un número par.
Por el teorema fundamental de la aritmética, podemos factorizar las potencias de 2 de este número. Sea $s \geq 1$ y $t$ un número impar tal que:

$$
ed - 1 = 2^s \cdot t
$$

Elegimos un entero aleatorio $a$ en el intervalo $1 < a < n-1$.
Calculamos el máximo común divisor $\gcd(a, n)$ usando el Algoritmo de Euclides (que es de clase P):

- Si $\gcd(a, n) > 1$, hemos tenido una suerte astronómica y hemos encontrado un factor de $n$. El algoritmo termina exitosamente.
- Si $\gcd(a, n) = 1$, entonces $a$ es coprimo con $n$ y pertenece al grupo multiplicativo $(\mathbb{Z}/n\mathbb{Z})^*$. Pasamos al siguiente paso.

Además, calculamos el valor base:

$$
x_0 \equiv a^t \pmod n
$$

Si $x_0 \equiv 1 \pmod n$ o $x_0 \equiv -1 \pmod n$, el algoritmo falla para esta base $a$ (elegimos otra).
Si no, construimos una sucesión elevando al cuadrado repetidamente (un máximo de $s$ veces):

$$
x_i \equiv x_{i-1}^2 \pmod n \quad \text{para } i = 1, 2, \dots, s
$$

Sabemos por el Teorema de Euler que $a^{\phi(n)} \equiv 1 \pmod n$. Como $ed - 1$ es múltiplo de $\phi(n)$, obligatoriamente el último término de nuestra sucesión será 1:

$$
x_s \equiv a^{ed-1} \equiv 1 \pmod n
$$

Al retroceder en nuestra sucesión $(x_0, x_1, \dots, x_s)$, sabemos que terminará en 1. Buscamos el índice exacto $j$ donde aparece el 1 por primera vez. Es decir, encontramos un $x_{j}$ tal que:

$$
x_{j}^2 \equiv 1 \pmod n
$$

mientras que su valor anterior cumplía:

$$
x_j \not\equiv 1 \pmod n \quad \text{y} \quad x_j \not\equiv -1 \pmod n
$$

Al valor $x_j$ se le llama raíz cuadrada no trivial de la unidad.

Usando el Teorema Chino del Rest**o**: La ecuación $x^2 \equiv 1 \pmod n$ equivale al sistema $x^2 \equiv 1 \pmod p$ y $x^2 \equiv 1 \pmod q$. Esto genera 4 soluciones: $1$, $-1$, y dos raíces no triviales. (El Teorema de Cauchy nos garantiza que estas raíces de orden 2 existen en la estructura del grupo).

Hemos encontrado un número $x_j$ tal que $x_j^2 \equiv 1 \pmod n$.
Restando 1 a ambos lados y factorizando como diferencia de cuadrados:

$$
x_j^2 - 1 \equiv 0 \pmod n \implies (x_j - 1)(x_j + 1) = k \cdot n
$$

Esto significa que $n$ divide al producto $(x_j - 1)(x_j + 1)$. Sin embargo, como $x_j$ es una raíz no trivial (no es ni $1$ ni $-1 \pmod n$), $n$ no divide a ninguno de los dos paréntesis por separado.

Por lo tanto, $\gcd(x_j - 1, n)$ debe contener obligatoriamente uno de los factores primos ($p$ o $q$). El otro factor se obtiene calculando $\gcd(x_j + 1, n)$.

Evaluamos el costo computacional de las operaciones de este algoritmo:

1. Extraer potencias de 2 ($s$ y $t$) toma tiempo $O(\log n)$.
2. La exponenciación modular inicial ($a^t \pmod n$) se realiza mediante el algoritmo de "cuadrar y multiplicar" en tiempo $O((\log n)^3)$.
3. Las $s$ elevaciones al cuadrado toman a lo sumo $O((\log n)^3)$.
4. El cálculo final de $\gcd(x_j - 1, n)$ por Euclides toma tiempo $O((\log n)^2)$.

La suma de operaciones polinómicas da como resultado un polinomio. Se demuestra en teoría de números que al menos el 50% de las bases $a$ elegidas al azar revelarán una raíz no trivial. Por lo tanto, en un par de intentos (tiempo constante esperado), el algoritmo factorizará $n$.

Al estar acotado estrictamente por un tiempo de ejecución del orden $O((\log n)^3)$, el problema se resuelve de forma determinista en tiempo polinómico. Por lo tanto, la factorización con clave privada conocida $\in \text{P}$.

---
### 4. Seguridad en el algoritmo ElGamal

En esta parte se vuelve intersante los temas de seguridad ya que es una aplicación directa de un ataque conocido. Investigue:

- ¿Cómo se calcula el logaritmo discreto?
- ¿Cómo se efectúa Man-In-The-Middle?

La seguridad de ElGamal radica en la dificultad del problema del logaritmo discreto (PLD). Se debe tomar $p$ primo muy grande tal que $\frac{p-1}{2}$ se aprimo. Examine los dos casos en particular. ¿Qué pasa con la clva privada y pública? Note que la clve está en usar logaritmos discretos, verifique si se usa un Man-in-the-Middle este podrá obtener las claves a partir de cómo se calcule el logaritmo discreto (un problema computacional grande).

#### Investigación 1

> Logaritmo discreto
> 

En los números reales, sea $x\in \mathbb{R}$, $g \in (0,\infty)-\{1\}$, $y\in (0, \infty)$, sabemos que: 

$$
y=g^x \quad \Longleftrightarrow \quad x=\log_g(y)
$$

Sin embargo, en la aritmética modular sobre un grupo finito, el logaritmo discreto cambia:

$$
y \equiv g^x \pmod p
$$

Dado $g$ (la base), $x$ (el exponente) y $p$ (un número primo), calcular $y$ es fácil usando exponenciación modular. Pero si hacemos lo inverso: se dan $y$, $g$ y $p$, y se pido encontrar  $x$, el problema se vuelve dificilmente computacional. No hay un logaritmo directo que se pueda aplicar.

Para números pequeños, se usa fuerza bruta. Para números medianos, algoritmos como el *Baby-step Giant-step* de Shanks o el *Algoritmo $\rho$ de Pollard*. Para números grandes, se usa el *Cálculo de Índices* (Index Calculus). Pero si $p$ es lo suficientemente grande (ej. 2048 bits) y está bien elegido, todos estos algoritmos tardarían millones de años.

#### Investigación 2

> El ataque Man-in-the-Middle
> 

El MitM (Hombre en el Medio) es un ataque donde el adversario intercepta y retransmite los mensajes entre dos partes que creen estar hablando directamente entre sí.

En criptografía de clave pública (como ElGamal), ocurre en el momento de intercambiar las llaves públicas. Suponer que A quiere comunicarse con B:

1. A envía su llave pública a B.
2. C (el atacante) intercepta el mensaje. C guarda la llave de A y le manda su propia llave pública a B, fingiendo ser A.
3. B recibe la llave y manda la suya.
4. C intercepta la llave de B, la guarda y le manda su propia llave pública a A.

Ahora, C tiene un canal cifrado con A y otro con B. Cuando A envía un mensaje cifrado, C lo abre (porque está cifrado con la llave de C), lo lee, lo vuelve a cifrar con la llave de B y lo envía. Nadie nota nada raro, pero la seguridad está comprometida al 100%.

#### Justificación

**Análisis del problema: Seguridad en el algoritmo ElGamal**

Primero definiremos el sistema de claves: Sea un número primo grande $p$ y un generador $g$ del grupo multiplicativo $(\mathbb{Z}/p\mathbb{Z})^*$:

- La clave privada es un entero aleatorio $x$ tal que $1 \leq x \leq p-2$.
- La clave pública es el valor $y$ calculado como $y \equiv g^x \pmod p$. La clave pública completa es la tupla $(p, g, y)$.

**Caso 1: Seguridad matemática computacional (ataque al logaritmo discreto)**

En este escenario, el atacante C intercepta la clave pública $(p, g, y)$ e intenta descubrir la clave privada $x$. Para ello, debe resolver la congruencia $y \equiv g^x \pmod p$, lo que se conoce como el Problema del Logaritmo Discreto (PLD).

¿Qué pasa con las claves y por qué es vital la condición del primo seguro?

El enunciado indica que $p$ debe ser un primo tal que $q = \frac{p-1}{2}$ también sea primo. A $p$ se le conoce como un **Primo Seguro**. Esto significa que el orden del grupo multiplicativo, que es $p-1$, tiene exactamente dos factores primos: $2$ y $q$.

$$
p - 1 = 2 \cdot q
$$

- **Si no se usa un primo seguro:** Si $p-1$ estuviera compuesto por muchos factores primos pequeños (ej. $p-1 = 2^a \cdot 3^b \cdot 5^c \dots$), el atacante podría utilizar el **Algoritmo de Pohlig-Hellman**. Este algoritmo reduce el PLD en el grupo grande a resolver varios PLD en subgrupos mucho más pequeños (usando el Teorema Chino del Resto), haciendo que el cálculo del logaritmo discreto pase de tiempo exponencial a tiempo polinómico. La clave privada $x$ sería comprometida rápidamente.
- **Al usar un primo seguro:** El algoritmo de Pohlig-Hellman se vuelve inútil, ya que el factor más grande del grupo es $q$, que es inmenso. El atacante se ve forzado a usar algoritmos genéricos (como el Cálculo de Índices), cuya complejidad es subexponencial pero computacionalmente intratable para un $p$ grande (por ejemplo de de 2048 bits o superior).
- **Conclusión:** Las claves permanecen matemáticamente seguras. La clave pública es de dominio abierto, pero la clave privada $x$ es imposible de derivar con la tecnología computacional actual.

**Caso 2: El ataque Man-in-the-middle**

En este escenario, el atacante C tiene control activo sobre el canal de comunicación entre A y B. ¿El MitM podrá obtener las claves a partir de cómo se calcula el logaritmo discreto?

La respuesta es no. El ataque Man-in-the-Middle es devastador porque evade por completo el problema matemático. El atacante no intenta resolver el Logaritmo Discreto computacionalmente grande.

¿Qué pasa exactamente con las claves públicas y privadas?

El ataque vulnera el protocolo de intercambio, no la matemática subyacente. El proceso paso a paso demuestra el estado de las claves:

1. A genera su par de claves: Privada $x_A$ y pública $y_A$. Envía $y_A$ a B.
2. C intercepta $y_A$. Z no puede descifrar $x_A$ (el PLD sigue siendo seguro).
3. En su lugar, C genera su propios pares de claves ElGamal: privada $x_C$ y pública $y_C$. C envía $y_C$ a B fingiendo ser A.
4. B recibe $y_C$ creyendo que es de A. B genera su par de claves: privada $x_B$, pública $y_B$. Envía $y_B$ a A.
5. C intercepta $y_B$ y le manda a A otra clave pública forjada $y_{C'}$.

Podemos concluir que:

- El atacante nunca obtiene las claves privadas originales ($x_A$ y $x_B$). Siguen siendo matemáticamente un misterio para él porque requerirían calcular el logaritmo discreto.
- Sin embargo, el atacante no necesita las claves privadas originales. Al sustituir las claves públicas en el tránsito, C obliga a A a cifrar sus mensajes con $y_{C'}$. C descifra el mensaje con su propia clave privada $x_{C'}$, lo lee, y lo vuelve a cifrar con la clave pública de B $y_B$.
- El algoritmo ElGamal falla en este escenario porque carece de un mecanismo de autenticación. Para mitigar este caso, la clave pública $(p, g, y)$ no debe enviarse en texto plano, sino encapsulada dentro de un Certificado Digital dirmado por una Autoridad Certificadora o utilizar firmas digitales (como DSA/RSA) para garantizar que la clave pública legítimamente pertenece a quien dice ser.

---
### 5. Birthday attack aplicado a RSA

Observe que:

$$
\lambda(n) = mcm(p-1, q-1) = \frac{(p-1)(q-1)}{(p-1, q-1)} = \frac{\phi(n)}{(p-1, q-1)}
$$

Por lo que si $p-1$ y $q-1$ tienen muchos factores comunes, entonces $mcm(p-1, q-1)$ será “pequeño” y, por tanto, un ataque busque factorizar $\phi(n)$ puede triunfar fácilmente.

**Teorema**. Si de un conjunto de $n$ elementos se toman $d$ elementos (con repetición, cada vez que toma uno, se repone antes de tomar el siguiente), entonces la probabilidad de tomar dos veces el mismo es aproximadamente $1 - \exp ( - \frac{d(d-1)}{2m} )$. En particular, para tener una probabilidad mayor que 1/2, basta tomar al menos

$$
\frac{1}{2} (1+\sqrt{1+8n \ln (2)} \approx 1.17741 \sqrt{n}
$$

elementos (el lado derecho es una aproximación para $n >> 0$).

Simule un programa que realice el ataque basado en la paradoja del cumpleaños. Como parte preliminar a esta práctica se ha de construir una función que simule los sucesivos mensaje s cifrados que se van interceptando. En este caso será un cifrado RSA, muestre en una gráfica:

- Número de mensajes interceptados
- La probabilidad de colisión
- Calcule el punto de inflexión donde el ataque es efectivo, es decir, ¿a los cuantos mensajes interceptados la probabilidad de colisión es $\approx 1$ o muy cercana a 1?

#### Introducción

**La paradoja del cumpleaños**

La paradoja clásica nos dice que en una habitación con solo 23 personas, hay más de un **50%** de probabilidad de que dos cumplan años el mismo día. La intuición falla porque no comparamos a una persona con las demás, sino que comparamos *todos los pares posibles* entre sí. El número de pares crece de forma cuadrática.

**¿Cómo se aplica a RSA?**

El algoritmo RSA (sin esquemas de relleno aleatorio como OAEP) es determinista: si se cifra el mismo mensaje exacto dos veces con la misma clave pública, se obtendrá exactamente el mismo criptograma.

La función de Carmichael $(\lambda(n))$ nos indica el máximo ciclo posible de las exponenciaciones modulares. Sin embargo, para el ataque de intercepción de mensajes, el enfoque principal recae en el tamaño del "espacio de mensajes posibles" $m$.

Si un atacante intercepta $d$ mensajes cifrados, la probabilidad de que dos criptogramas sean idénticos (lo que revela que se envió el mismo texto plano original) está dada por la aproximación dada:

$$
P(d) \approx 1 - \exp\left( - \frac{d(d-1)}{2m} \right)
$$

#### Implementación

El script de Python se divide en las siguientes partes:

- **Simulación RSA (`rsa_encrypt`):** Una función básica que aplica la fórmula $C \equiv M^e \pmod n$. Aunque la gráfica se basa en la probabilidad matemática de la paradoja, dejamos esta función implementada para cumplir con el requisito de "construir una función que simule los sucesivos mensajes cifrados".
- **Cálculo de Probabilidad (`collision_probability`):** Implementa la fórmula $P(d) = 1 - \exp\left( - \frac{d(d-1)}{2m} \right)$.
- **Despeje del Punto de Inflexión:** Para responder a la pregunta *¿A los cuántos mensajes la probabilidad es cercana a 1?*, el programa hace un despeje algebraico. Fijamos la probabilidad objetivo en $0.99$ (99%). Asumiendo que para un $d$ grande $d(d-1) \approx d^2$, el despeje de la fórmula original queda así:

$$
0.99 = 1 - \exp\left( - \frac{d^2}{2m} \right)
$$

$$
0.01 = \exp\left( - \frac{d^2}{2m} \right)
$$

$$
\ln(0.01) = - \frac{d^2}{2m}
$$

$$
d \approx \sqrt{-2m \ln(0.01)}
$$

El programa calculará este valor exacto e imprimirá el resultado en la terminal, además de trazarlo como una línea roja en la gráfica.

- **Graficación:** Utilizaremos `matplotlib` para generar la curva de probabilidad visualizando el crecimiento característico de la paradoja del cumpleaños.

### 6. Cifrado DES

Investigue lo siguiente:

- ¿Qué es EAX y ECB? ¿Cuál es la principal diferencia.

Implemente usando un código donde se cifre y pueda descifrar información usando DES, pero que no tenga implementado EAX, solamente ECB. La salida de sugerencia debe estar en Base64, por ejemplo, use el mensaje m = noche697 y la clave k = data7Qa=, entonces la salida en Base64 es c =obuzqeTZFwc= el texto cifrado.
Revise el GitHub para el acomodo de las matrices ya definidas y el pseudocódigo como guia.

#### Investigación

La invención de DES fue diseñada para cifrar bloques de tamaño fijo (64 bits). Cuando el mensaje es más largo que el tamaño del bloque se usan Modos de Operación, que dictan cómo se encadenan los bloques.

- ECB (Electronic Codebook - Libro de códigos electrónico)
Es el modo más básico. Toma el mensaje, lo parte en bloques de 64 bits y cifra cada bloque por separado usando exactamente la misma clave.
El problema es que es determinista. Si dos bloques de texto plano son idénticos, producirán exactamente el mismo bloque de texto cifrado. No oculta los patrones de los datos.
- EAX (Encrypt-then-Authenticate-then-Translate)
Es un modo AEAD (Cifrado Autenticado con Datos Asociados) moderno y robusto. No solo cifra los datos para que sean confidenciales, sino que además genera una "etiqueta" (tag) criptográfica para asegurar que nadie modificó el mensaje en el camino (integridad). Utiliza un *Nonce* (un número que se usa una sola vez) para garantizar que si se cifraa el mismo mensaje dos veces, los criptogramas sean completamente distintos.

ECB solo cifra, de forma determinista y bloque por bloque, dejando expuestos los patrones de la información. EAX cifra y autentica, usando valores aleatorios (nonces) para ocultar patrones y garantizar que el mensaje no ha sido alterado. El código `Crypto.Cipher`, utiliza EAX para mostrar un cifrado seguro, pero para entender las matemáticas de DES, únicamente se implementara ECB.

Ejemplo: Supongamos que se quiere cifrar el mensaje bancario: `PAGO$100PAGO$100` (dos bloques idénticos de 8 caracteres).

- **En ECB:** El bloque 1 (`PAGO$100`) se cifra como `A8F4...`. El bloque 2 (`PAGO$100`) se cifra también como `A8F4...`. El criptograma final es `A8F4...A8F4...`. Un atacante sabe que se repitió un comando, aunque no sepa cuál es.
- **En EAX:** El bloque 1 se cifra mezclándolo con un *nonce* aleatorio, dando `X7B9...`. El bloque 2 se cifra con el estado actualizado del cifrador, dando `M2Q1...`. El atacante solo ve caracteres aleatorios `X7B9...M2Q1...` y no puede deducir que los bloques eran iguales.

#### Implementación

Se nos ha dado las matrices predefinidas (`IP`, `FP`, `E`, `P`, `PC1`, `PC2`, `S_BOXES`) en el repositorio, por lo que haremos lo siguiente:

1. **Preparación de claves:** Tomaremos la clave (`data7Qa=`), la pasaremos por la permutación PC1, la dividiremos en dos, aplicaremos rotaciones de bits según `KEY_SHIFT`, y la comprimiremos con PC2 para generar 16 subclaves de 48 bits.
2. **Procesamiento del texto:** El mensaje `noche697` tiene exactamente 8 caracteres (64 bits). En ECB, lo convertiremos directamente a su representación numérica.
3. **Red de Feistel (16 Rondas):** Aplicaremos la Permutación Inicial (IP), dividiremos el bloque en Izquierda/Derecha, y ejecutaremos el bucle: expandir la derecha con `E`, hacer XOR con la subclave, pasar por las Cajas-S (S-Boxes) para la sustitución no lineal, permutar con `P`, y hacer XOR con la izquierda.
4. **Codificación:** Al terminar las 16 rondas y aplicar la Permutación Final (FP), obtendremos un arreglo de bytes que convertiremos a Base64 usando la librería nativa de Python. El objetivo es que nuestra salida coincida carácter por carácter con `obuzqeTZFwc=`.
5. **Descifrado:** Reutilizaremos la misma lógica, pero invirtiendo el orden del arreglo de las 16 subclaves generadas.

El programa en Python toma las matrices del repositorio y completa el flujo de la siguiente manera:

- **Base64:** Importaremos el módulo estándar `base64`. El cifrado DES produce bytes crudos (ilegibles). Base64 los convierte a caracteres de texto imprimibles (ASCII) que podemos leer y transmitir, obteniendo el `obuzqeTZFwc=` esperado.
- **Modo ECB (El código crudo):** La función `des_encrypt` divide el mensaje en bloques de 8 bytes y procesa cada uno con `des_block`. Como no añade ningún vector de inicialización (IV) ni *nonce*, ni altera los bloques basándose en los anteriores, estamos implementando implícitamente el ECB.
- **Descifrado:** Tomaremos el texto en Base64, lo decodificaremos de vuelta a bytes usando `base64.b64decode`, y aplicaremos `des_decrypt` (que invierte el orden de las subclaves) para recuperar `noche697`.

---
### 7. Claves finitas y Playfair

- En el GitHub habrá una lista de palabras en las cuales son representaciones de claves, el trabajo aquí es usar la clave correcta para descifrar el texto en base64 (se basa en el ejercicio anterior), $c = h+F7XMoHpF0=$ y ver cuál es la clave correcta.
- Una vez obteniendo la información, c se convertirá en k, ya que se tiene el siguiente texto que fue cifrado por PlayFair:

> SHPETXSQZNSPLBMBWFFKCEBRBQMVQSEGOLRBLGXPPSUXHWLGXPDLSZSNAZINELFTEQRGTSRIFWKBRGZVNPWKBQPGPBMZOMGEQMXPHGUFDIKBSCMGQMSHVZXTQMFXFOGPSHBWIOSNOQNPWKKCOQMFAVSHSMFOSNDKHGMVSZSHQPIYSQAVPNEGCERZQBQOKSSCOFOHPYQSBKQOZSHPFKEGKCRLSNQOIKOQOWPSTDPSBRAVGMVZQZKGFRZVVPZVSHPGVAOHRBGEZVEQHGWMKSNSZSRZPHZVPSZSIRDLSNAZINDLOBFWSKGPZSMZQZOWMCAVSHGRMPXGNSPGFPKFHBMGSQSGPEKGQSFSSNOWBLPYSQKBSQBRQSEFSGKSKSUXHWLGXPZSZSNSZKRGFZQPOQDYSXTFRZQMPQRGXECNZPCEGLBQNQPCMESNOWBLPYSCGSOHQPFSRIFWKBQBDTQOQNDOZVMIZPUFDIKBSCNGRYCYBLQGBQOQZAMRZPBRPESNGRQEPESNVPVZBKZVVPPSKSSPQBKGBKQOBKWHKDZVYMMGMQZLKEIOEQGLBRWHUXFOSPZSGPGFQOGKAV
> 

Además, una pista de la matriz es la siguiente:

$$
\left( \begin{matrix}
? & ? & ? & ? & ? \\
? & ? & B & C & D \\
F & H & I & K & L \\
M & N & O & Q & R
\end{matrix} \right)
$$

#### Introducción

**Ataque de Fuerza Bruta en DES**

El algoritmo DES (Data Encryption Standard) utiliza una clave de 64 bits (donde 8 son de paridad, dejando 56 bits efectivos). Aunque el espacio de búsqueda de 56 bits es gigante ($2^{56}$), si sabemos que la clave pertenece a un conjunto reducido (como una lista de palabras comunes o un archivo `words.txt`), podemos realizar un ataque de diccionario.

En este caso, iteramos sobre cada palabra del archivo, la convertimos al formato entero requerido por la implementación de DES y desciframos el criptograma. El éxito se define al obtener un texto en lenguaje natural o una cadena que sirva como clave para el siguiente paso.

**Cifrado Playfair**

Recordemos que es un cifrado de sustitución polialfabética que en este caso, utiliza una matriz de 5x5. Se basa en pares de letras (digramas) en lugar de letras individuales.

- Construcción de la matriz: Se elige una clave, se eliminan las letras repetidas y se rellena el resto de la matriz con el alfabeto (usualmente combinando I y J).
- Descifrado:
    - Si las letras están en la misma fila, se toma la letra a la izquierda de cada una.
    - Si están en la misma columna, se toma la letra de arriba.
    - Si forman un rectángulo, se toman las letras en las esquinas opuestas de la misma fila.

#### Implementación

El código en Python realizará exactamente los siguientes pasos:

1. **Fuerza Bruta DES:** Abrirá el archivo `words.txt` y probará cada palabra (que mide exactamente 8 caracteres, es decir, 64 bits) como llave para descifrar el criptograma `h+F7XMoHpF0=`.
2. **Validación de Texto Plano:** Sabemos que el resultado correcto de DES debe ser una palabra legible (la clave de Playfair). El programa filtrará los descifrados que tengan caracteres ASCII válidos.
3. **Generación de la Matriz Playfair:** Una vez obtenida la clave, construirá la matriz de 5x5.
4. **Descifrado Playfair:** Tomará el criptograma “SHPET…”, lo dividirá en pares (digramas) y aplicará las reglas inversas de Playfair (desplazar izquierda en filas, desplazar arriba en columnas, o cruzar rectángulos) para revelar el mensaje final.