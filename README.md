# INTRODUCCIÓN A LA ALGORITMICA




# Ejercicio 8: Porcentajes, IVA e inversiones


1. Escribir un algoritmo que calcula el precio con todos los impuestos incluidos (TII) para un precio sin impuestos y un porcentaje de IVA dado.

2. Escribir un algoritmo que calcula el importe de los intereses generados por un capital invertido a un interés dado durante un tiempo dado, expresado en meses.


# Ejercicio 9: Media aritmética ponderada


1. Escribir un algoritmo que calcula la media aritmética de tres números dados.

2. La misma pregunta para una media ponderada cuando se dan los números y los coeficientes de ponderación.


# Ejercicio 10: Área del triángulo





1. Escribir un algoritmo que calcula el área de un triángulo del que se da la medida de un lado y la de la altura relativa a este lado.

2. ¿Se puede utilizar este algoritmo para un triángulo rectángulo si se dan las medidas de sus dos lados perpendiculares?


# Ejercicio 11: Salario y horas extra







El cálculo de una nómina tiene en cuenta el salario bruto asociado a las horas «normales» que debe hacer el empleado y las horas «extra» trabajadas en el mes. Las horas extra se remuneran según las siguientes normas administrativas:

Tarifa por hora aumentada en un 125 % para las horas entre la 36.ª y la 43.ª.
Tarifa por hora aumentada en un 150 % para las horas a partir de la 44.ª.

El aumento se realiza sobre la tarifa por hora normal, calculado a partir del salario mensual bruto para un año de 52 semanas repartidas en 12 meses, sobre la base de 35 horas trabajadas por semana.

Escribir el algoritmo que calcula el importe de las horas extra que hay que pagar, a partir del salario mensual bruto y de la cantidad de horas extra.

Se podrá suponer que el cálculo siempre se usa para una cantidad de horas superior a 8. El problema general supone el estudio previo del capítulo siguiente, que trata de la alternativa.




# Ejercicio 12: Cuenta de depósito

Se considera las cuentas de depósitos alojadas en un banco por los clientes. Solo se permite hacer una retirada si el saldo que queda en la cuenta no es negativo.

1. Definir el tipo de datos CUENTA..

2. Definir las operaciones aplicables.

En determinadas circunstancias y para determinados clientes, la banca autoriza un descubierto limitado y temporal.

3. Volver a hacer las definiciones previas para permitir estos descubiertos.

* Algoritmo 1: Definición de abrir una cuenta

      abrir(c : CUENTA ; saldo_inicial : REAL)
          # Inicializar `c' mediante un `saldo_inicial'.

      Precondición
          saldo_inicial > 0

      realización
          c.descubierto ← 0
          c.saldo ← saldo_inicial

      postcondición
          c.descubierto = 0
              # El descubierto no está autorizado
          antiguo(saldo_inicial) = saldo_inicial
          c.saldo = saldo_inicial

      fin abrir
      
* Algoritmo 2: abonar una cuenta

      abonar(c : CUENTA ; crédito : REAL)
          # Crédito `c' de la suma `crédito'.

      Precondición
          c.saldo ≠ NULO
          crédito ≠ NULO

      realización
          c.saldo ← c.saldo + crédito

      postcondición
          # El descubierto autorizado y el importe del `crédito' no se
          # modifican
          antiguo(c).descubierto = descubierto
          antiguo(c).crédito = crédito

          # El saldo aumenta con el `crédito'
          c.saldo = antiguo(c).saldo + crédito

      fin abonar


* Algoritmo 3: cargar una cuenta

      cargar(c : CUENTA ; débito : REAL)
          # Carga `c' con la suma `débito'.

      Precondición
          c.saldo ≠ NULO
          débito ≠ NULO
          c.saldo + c.descubierto ≥ débito ≥ 0

      realización
          abonar(c, –débito)

      postcondición
          # El descubierto autorizado y el importe del `débito' no se
          # modifican
          antiguo(c).descubierto = descubierto
          antiguo(débito) = débito

          # Al saldo se le resta el `débito'
          c.saldo = antiguo(c).saldo – débito

      fin cargar


* Algoritmo 4: función consultar una cuenta

      consultar(c : CUENTA) : REAL
          # El `saldo' de la cuenta `c'.

      precondición
          c.saldo ≠ NULO

      realización
          Resultado ← c.saldo

      postcondición
          Resultado = c.saldo

      fin consultar


* Algoritmo 5: Definición de es_acreedora

      es_acreedora(c : CUENTA) : BOOLEANO
          # ¿`c' es acreedora?

      precondición
          c.saldo ≠ NULO

      Realización
          Resultado ← (c.saldo > 0)

      postcondición
          Resultado = (c.saldo > 0)

      fin es_acreedora
      

* Algoritmo 5: Definición de es_deudora

      es_deudora (c : CUENTA) : BOOLEANO
          # ¿`c' es deudora?

      precondición
          c.saldo ≠ NULO

      Realización
          Resultado ← (– c.descubierto ≤ c.saldo ≤ 0)

      postcondición
          Resultado = (– c.descubierto ≤ c.saldo ≤ 0)

      fin es_deudora


* Tipo cuenta

      tipo CUENTA estructura
          saldo : REAL
          descubierto : REAL

          invariante
              # El descubierto está autorizado
              descubierto ≥ 0

              # el saldo debe ser superior al descubierto autorizado
              saldo ≥ – descubierto
      fin CUENTA


* Algoritmo 6: Definición de abrir una cuenta con descubierto autorizado

      abrir(c : CUENTA ; saldo_inicial : REAL ; descubierto_MAX : REAL)
          # Inicializar `c' mediante un `saldo_inicial' y un 
          # `descubierto_MAX'.

      Precondición
          saldo_inicial > 0
          descubierto_MAX ≥ 0

      realización
          c.descubierto ← descubierto_MAX
          c.saldo ← saldo_inicial

      postcondición
          c.descubierto = descubierto_MAX
          c.saldo = saldo_inicial

      fin abrir


* Tipo cuenta

      tipo CUENTA estructura
          # Cuenta con descubierto autorizado con una duración limitada.

          saldo : REAL
          descubierto : REAL      # importe del descubierto autorizado 
          fecha_descubierto : FECHA # decha de inicio del último descubierto
          duración_max : FECHA      # Duración máxima del descubierto

          invariante
              # El descubierto está autorizado durante un tiempo limitado
              descubierto ≥ 0
              fecha_descubierto ≠ 0 => 
                             fecha_descubierto + duración_max ≤ 
          fecha_actual

              # el saldo debe ser superior al descubierto autorizado 
              saldo ≥ descubierto
      fin CUENTA


* Algoritmo 7: Definición de abrir una cuenta con descubierto autorizado durante un tiempo limitado

      Algoritmo abrir
          # Inicializar `c' mediante un `saldo_inicial' y un 
          # `descubierto_MAX' durante una `duración_max'.

      Entrada
          c : CUENTA
          saldo_inicial : REAL
          descubierto_MAX : REAL
          duración_max : FECHA

      Precondición
          saldo_inicial > 0
          descubierto_MAX ≥ 0
          duración_max ≥ 0

      realización
          c.descubierto ← descubierto_MAX
          c.saldo ← saldo_inicial
          c.fecha_descubierto ← 0
          c.duración_max ← duración_max

      postcondición
          c.descubierto = descubierto_MAX
          c.saldo = saldo_inicial
          c.duración_max = duración_max
          c.fecha_descubierto = 0

      fin abrir


