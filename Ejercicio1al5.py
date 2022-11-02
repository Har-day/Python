'''
Created on 1/11/2022

@author: Harday
'''
#Ejercicio 1: las cadenas internamente son arreglos 

cadena='Pepito' 

for letra in cadena: 

    print(letra) 

#Imprime cada caracter del arreglo, recorriendo todas la posiciones mediante un FOR

#Ejercicio 2: buscar segmentos de la lista sin iterar 

animales="gatoperrorana" 

print (animales[:4]) 

     

print (animales[4:9]) 

     

print (animales[9:]) 

#Imprime un rango de caracteres proporcionandole un intervalo de posiciones

#Ejercicio 3: Operaciones directas sobre listas 

miLista = [1,9,3,8,5,7,2,0,4,6] #arreglo de numeros 

print (miLista)  

print (len(miLista))  #Imprime cuantos caracteres existe en el arreglo

print (sum(miLista))  #Imprime la sumatoria de todos los numeros en el arreglo 

print (min(miLista))  #Imprime el numero menor del arreglo 

print (max(miLista))  #Imprime el numero mayor del artreglo 

 

 

copia=miLista.copy() #Crea un duplicado del arreglo y a este lo llama 'copia'

copia.reverse()  #Cambia a un orden inverso el arreglo copia

print (copia)  #imprime el arreglo en el orden, anteriormente invertido el orden de los valores

 

ordenada=sorted(miLista)  #Crea un arreglo basado en el arreglo inicial pero ahora lo ordena de menor a mayor

print (ordenada)  #Imprime el arreglo ordenado 

 

ordenada=sorted(miLista,reverse=True)  
                                            #Crea e imprime el arreglo pero de un orden Mayor a menor
print (ordenada)  
print("")
print("")

#Ejercicio 4: segmentos y saltos sin iterar 

print (miLista[4::])  #Imprimir los caracteres desde la posicion 4 y avanzando de a una posicion hasta el final

print (miLista[:2:])   #Imprimir los caracteres desde la posicion inicial y avanzando de a una posicion y hasta la posicicion 2

print (miLista[::2])  #Imprimir los caracteres desde la posicion inicial y avanzando de a dos posiciones y hasta la posicicion final

print (miLista[1:7:3])  #Imprimir los caracteres desde la posicion 1 y avanzando de a tres posiciones y hasta la posicicion 7 sin contarla

sorpresa=miLista[::-1]  

print (sorpresa) #Imprime la lista al reves 

 

sorpresa=miLista[::-2]  

print (sorpresa)  #Imprime la lista al reves saltando de a 2 posiciones 

print("")
print("")
print("")
print("")
#Ejercicio 5: usando iteracion 
print(miLista)
for numero in miLista: #Multiplica cada numero del arreglo por 2 y lo imprime pero no lo almacena 

    print (2*numero, end=' ')  

 
print("")
for i in range(0, len(miLista)): #Imprime el arreglo quitandole el estilo original de corchetes y comas

    print (miLista[i],end=' ')  

print() 

print() 

 

lista1 = [1, 2]; lista2 = ['a', 'b']  

for i1, i2 in zip(lista1, lista2): 

    print (i1, i2)  

print() 

 

otraLista = [2,4,8,10,30,40,50,60,70,80,90,22,14] 

for a, b in zip(miLista, otraLista): 

    print (a,b)  
