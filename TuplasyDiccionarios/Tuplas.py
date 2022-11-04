'''
Created on 3/11/2022

@author: Harday
'''
t = (23,'a',(2.5,3.7,'x'),["perrito","gatito"],'Pepe')      #Crear un tupla llamada t
print (t)           #Imprimir la tupla
print (len(t))  #Imprimir la cantidad de compartimientos 


print ('=====================================')
print (t[0]) #Imprimir lo que esta en el compartimiento 0
print (t[3])#Imprimir lo que esta en el compartimiento 3
print (t[1:3])#Imprimir lo que esta en el compartimiento 1 y 2
print (t[3][1])#Imprimir lo que esta en el compartimiento 3 en el subespacio 1


print ('====================================')
print (t[3]) #Imprimir lo que esta en el compartimiento 3
t[3].append('lorito')#Agregar un subespacion con 'lorito' al compartimiento 3
print (t)   #Imprimir la tupla con la modificacion

print ('====================================')
for elemento in t:
    print (elemento)   #Imprime todos los compatimientos por separado

print ('====================================')
for index in range(0,len(t)):
    print (t[index])                #Otra forma de imprimir todos los compatimientos por separado

print ('====================================')
if 'a' in t:
    print ("El elemento 'a' esta en la tupla") #Busca los terminos de todo el compartimiento en la tupla e imprimi si existe en ella 

print ('====================================')
lista=list(t)  #Crea una lista y le asigna los valores de la conversion de la tupla a lista
lista[1]='A'   #Modifica el compartimiento 1 de la lista
print (lista)  #Imprime la lista con su comidicacion 

tupla=tuple(lista) #Crea un tupla y le asigna los valores de la conversion de la lista a tupla
print (tupla)  #imprime la tupla convertida

print ('====================================')
l = [(1,1), (2,4), (3,9), (4,16), (5,25)]
for x, y in l:
    print (x, ':', y)           #Imprime l añadiendole estilo
