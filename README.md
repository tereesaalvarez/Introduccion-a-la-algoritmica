# INTRODUCCIÓN A LA ALGORITMICA




# Ejercicio 8: Porcentajes, IVA e inversiones


1. Escribir un algoritmo que calcula el precio con todos los impuestos incluidos (TII) para un precio sin impuestos y un porcentaje de IVA dado.

2. Escribir un algoritmo que calcula el importe de los intereses generados por un capital invertido a un interés dado durante un tiempo dado, expresado en meses.

* Algoritmo 1:

      Algoritmo impuestos
        Entrada
          precio: Real
            -Valor de un producto
        Precondición
          precio>0
        Constante
          IVA: Real- 0.21
            porcentaje del precio inicial que se suma para calcular el precio final
        Realización
          -
            calcular el precio con el IVA. Cabe destacar que consideramos el IVA como único impuesto porque no se especifica ninguno más en el enunciado.
            precio = precio + precio*IVA
          -
        fin impuestos

# Ejercicio 9: Media aritmética ponderada


1. Escribir un algoritmo que calcula la media aritmética de tres números dados.
  
2. La misma pregunta para una media ponderada cuando se dan los números y los coeficientes de ponderación.

Resuelto con código

      class media_notas:
          def __init__(self, nota1, nota2, nota3):
              self.nota1=nota1
              self.nota2=nota2
              self.nota3=nota3
          def media_aritmetica(self):
                  return (self.nota1+self.nota2+self.nota3)/3
          def media_ponderada(self, media_aritmetica):
              return round(media_aritmetica)

      def introducir_nota(i):

          while true:
              nota=input("Introduce nota:")

              try:
                  nota = float(nota)
                  break
              except:
                  print ("Cambia la coma por un punto")
                  pass
          return nota


      if __name__=="__main__":
          notas=[]
          for i in range(3):
              n= introducir_nota(i)
              notas.append(n)


      total = media_aritmetica(notas[0], notas[1], notas[2])
      print("La media aritmetia es: {}".format(total.media_aritmetica()))
      print("La media ponderada es: {}".format(total.media_ponderada(total.media_aritmetica)))


# Ejercicio 10: Área del triángulo


1. Escribir un algoritmo que calcula el área de un triángulo del que se da la medida de un lado y la de la altura relativa a este lado.

2. ¿Se puede utilizar este algoritmo para un triángulo rectángulo si se dan las medidas de sus dos lados perpendiculares?

Resuelto con código


* Código

      class triangulo: 
          def __init__(self, alto, lado):
              self.alto= alto
              self.lado= lado
          def area(self):
              return(self.alto*self.lado)/2

      def datos(dato):
          while true:
              numero= input("introduce numero {}".format(dato))
              try:
                  numero = float(numero)
                  break
              except:
                  print("Introduzca un valor que sirva")
                  pass
          return numero


      if __name__ == "__main__":
          lado= dame_datos("lado")
          alto= dame_datos("altura")
          resultado= Triangulo(alto,lado)
          print("el area del triangulo es {}".format(resultado.area()))


# Ejercicio 11: Salario y horas extra


El cálculo de una nómina tiene en cuenta el salario bruto asociado a las horas «normales» que debe hacer el empleado y las horas «extra» trabajadas en el mes. Las horas extra se remuneran según las siguientes normas administrativas:

Tarifa por hora aumentada en un 125 % para las horas entre la 36.ª y la 43.ª.
Tarifa por hora aumentada en un 150 % para las horas a partir de la 44.ª.

El aumento se realiza sobre la tarifa por hora normal, calculado a partir del salario mensual bruto para un año de 52 semanas repartidas en 12 meses, sobre la base de 35 horas trabajadas por semana.

Escribir el algoritmo que calcula el importe de las horas extra que hay que pagar, a partir del salario mensual bruto y de la cantidad de horas extra.

Se podrá suponer que el cálculo siempre se usa para una cantidad de horas superior a 8. El problema general supone el estudio previo del capítulo siguiente, que trata de la alternativa.

Resuelto con pseudocódigo

* Algoritmo 1: Remuneración de horas extra – Solución de principio

      Algoritmo horas_extra
          # Establece la remuneración de `horas_ext' adicionales para
          # un salario mensual bruto de `salario_mensual_bruto'.
      Entrada
          salario_mensual_bruto : REAL
              # Importe del salario mensual bruto
          horas_ext : ENTERO
              # Cantidad de horas extra del mes a pagar

      precondición
          salario_mensual_bruto > 0
          horas_ext ≥ 0

      constante
          CANTIDAD_SEMANAS : ENTERO ← 52
              # Cantidad de semanas de trabajo 
          CANTIDAD_HORAS_SEMANA : ENTERO ← 35
              # Cantidad legal de horas de trabajo semanales 
          CANTIDAD_HORAS_MAX_1 : ENTERO ← 8
              # Umbral de cambio de precio de remuneración
          PRECIO_1 : REAL ← 1,25
              # Tarifa de remuneración de CANTIDAD_HORAS_MAX_1 primeras
              # horas extra
          PRECIO_2 : REAL ← 1,50
              # Tarifa de remuneración de las otras horas extra

      variable
          horas_ext_1 : ENTERO
              # Cantidad de horas extra con PRECIO_1 %
          horas_ext_2 : ENTERO
              # Cantidad de horas extra con PRECIO_2 %
          precio_hora : REAL
              # Precio hora de la remuneración bruta básica

      realización
          calcular el precio_hora de la remuneración bruta básica

          Resultado ← precio_hora x 
                   (
                     inf(horas_ext, CANTIDAD_HORAS_MAX_1) x PRECIO_1 
                   +
                     sup(horas_ext – CANTIDAD_HORAS_MAX_1, 0) x PRECIO_2
                   )

      postcondición
      ...
      fin horas_extra


* Cálculo del precio bruto por hora

      # Cálculo del precio_hora de la remuneración bruta básica
      precio_hora ← salario_mensual_bruto x 12
                    /
                     (REAL(CANTIDAD_HORAS_SEMANA) x REAL(CANTIDAD_SEMANAS))

* Algoritmo 2 : Remuneración de las horas extra

      Algoritmo horas_extra
          # Establece la remuneración de `horas_ext' adicionales para 
          # un salario mensual bruto `salario_mensual_bruto'.

      Entrada
          salario_mensual_bruto : REAL
              # Importe del salario mensual bruto
          horas_ext : ENTERO
              # Cantidad de horas extra del mes a remunerar

      precondición
          salario_mensual_bruto > 0
          horas_ext ≥ 0

      constante
          CANTIDAD_HORAS_MAX_1 : ENTERO ← 8
              # Umbral de cambio de precio de remuneración
          PRECIO_1 : REAL ← 1,25
              # Precio de remuneración de CANTIDAD_HORAS_MAX_1 primeras
              # horas extra
          PRECIO_2 : REAL ← 1,50
              # Precio de remuneración de las otras horas extra

      variable
          horas_ext_1 : ENTERO
              # Cantidad de horas extra con PRECIO_1 %
          horas_ext_2 : ENTERO
              # Cantidad de horas extra con PRECIO_2 %
          precio_hora : REAL
              # Precio hora de la remuneración bruta de base

      realización
          # Cálculo del precio_hora de la remuneración bruta de base 
          precio_hora ← precio_hora_bruto(salario_mensual_bruto)

          # Cálculo de la cantidad de horas de cada categoría
          horas_ext_1 ← inf(horas_ext, CANTIDAD_HORAS_MAX_1)
          horas_ext_2 ← sup(horas_ext – CANTIDAD_HORAS_MAX_1, 0)

          # Cálculo de la remuneración de las horas extra
          Resultado ← precio_hora x (horas_ext_1 x PRECIO_1 +
                                     horas_ext_2 x PRECIO_2)

      postcondición
      ...
      fin horas_extra


* Algoritmo 3 : Definición de la función precio_hora_bruto

      precio_hora_bruto(salario_mensual_bruto : REAL) : REAL
          # El precio hora bruto correspondiente al `salario_mensual_bruto'.

      Precondición
           salario_mensual_bruto > 0

      constante
          CANTIDAD_SEMANAS : ENTERO ← 52
              # Cantidad de semanas de trabajo
          CANTIDAD_HORAS_SEMANA : ENTERO ← 35
              # Cantidad legal de horas de trabajo semanales

      realización
          # Cálculo del  precio_hora de la remuneración bruta de base
          Resultado ← salario_mensual_bruto x 12 /
                     (REAL(CANTIDAD_HORAS_SEMANA) x REAL(CANTIDAD_SEMANAS))

      postcondición
          Resultado = salario_mensual_bruto x 12,0 / REAL(35 x 52)

      fin precio_hora_bruto


# Ejercicio 12: Cuenta de depósito

Se considera las cuentas de depósitos alojadas en un banco por los clientes. Solo se permite hacer una retirada si el saldo que queda en la cuenta no es negativo.

1. Definir el tipo de datos CUENTA..

2. Definir las operaciones aplicables.

En determinadas circunstancias y para determinados clientes, la banca autoriza un descubierto limitado y temporal.

3. Volver a hacer las definiciones previas para permitir estos descubiertos.

Resuelto con pseudocódigo

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


