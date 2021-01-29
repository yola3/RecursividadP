# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 13:49:23 2020
"""



def numeros_atrasados(numero):# se define una funciony recibe un un parametro ese parametro va indicar cual es limite que desea
    numero-=1 # agrego este numero y le digo que cada vez que se ejecutese va ir restando menos uno
    if numero>0:# aqui voy a preguntar que si el numero es en este caso mayor a 0 tengo que volver a llamar la funcion para que se se vuelva a restar
        print (numero) # aqui mando a imprimir
        numeros_atrasados(numero) #  se llama asi mismo la funcion creando un bucle y terminara cuando se cumpla la condision o el caso base
  
print("ingrese un numero") # aqui solicito el numero desde el teclado
numero=int(input()) # aqui mando a leer mi variable
print(numeros_atrasados(numero)) # aqui imprimir mi codigo 