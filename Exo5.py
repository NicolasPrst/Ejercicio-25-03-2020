def fibo(n,a=0,b=1):
   while n!=0:
      return fibo(n-1,b,a+b)
   return a

for i in range(0,10):
   print(fibo(i))

# Este ejercicio es un ejemplo de la secuencia de Fibonnaci. Esta secuencia es una secuencia de enteros en la que cada
# numero es la suma de los dos numeros anteriores.

# En este ejercicio, tenemos tres variables que son a, b y n
# n es la variable que dice cuantos ciclos el "While" va a hacer
# a y b son las dos primeras variables de la secuencia de Fibonnaci

# El ejercicio hace linea por linea :
# La bucle while permite una ejecution de las autras intructiones en el caso de n es differente de 0
# La recursion de function fibo permite de calcular el nuevo termo de la secuencia (suma de los dos anteriores termos)
# La function returna la valor de a
# El bucle for va a imprimar 10 veces la variable "a" (son los termos de la secuencia de Fibonnaci)
