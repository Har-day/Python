'''
Created on 3/11/2022

@author: Harday
'''
huespedes={101:'Juan Valdes', 105:'Paquita la del Barrio', 202: 'Mariana Pajon'}


print (huespedes)#IMPORIME EL DICCIONARIO NORMAL
print (huespedes.items())#IMPRIME EL DICCIONARIO PERO AGRUPANDO CADA ITEM POR CLAVE Y VALOR 

print (huespedes.keys())#IMPREME SOLO LAS CLAVES DEL DICCIONARIO
for key in huespedes:
    print (key)     #IMPRIME CADA UNA DE LAS CLAVES EN EL DICCIONARIO

print (huespedes.values()) #IMPRIME SOLO LOS VALORES DEL DICCIONARIO

for key in huespedes:
    print (huespedes[key]) #IMPRIME CADA UNO DE LOS VALORES PARA CADA CLAVE
print()

for habitacion in huespedes:
    print (habitacion,':',huespedes[habitacion])  #IMPRIME CADA CLAVE SEGUIDO DE ':' Y EL VALOR DEL LA CLAVE
print()

for habitacion,huesped in huespedes.items():    #CAMBIA TODOS LOS VALORES DE LAS CLAVES CON EL VALOR DE LA CLAVE FINAL
    print (habitacion,':',huespedes[key])

for indice, key in enumerate(huespedes):
    print (indice+1,key,huespedes[key])   #IMPRIME UN CONTADOR DE CADA ITEM DEL DICCIONARIO 
print()

print (huespedes[105]) #IMPRIME EL VALOR DE LA CLAVE 105
print (huespedes.get(105))#IMPRIME EL VALOR DE LA CLAVE 105

print ('====================================')

huespedes[102]='Fanny Lu'
huespedes[107]='Don Omar'
huespedes.setdefault(109,'Luis Miguel')   #AGREGA NUEVAS CLAVES Y VALORES AL DICCIONARIO
for habitacion,huesped in huespedes.items():
    print (habitacion,':',huesped)
print()                                     #IMPRIME EL DICCIONARIO CON SUS NUEVOS ITEMS

registroshoy={201:'Vicente Fernandez',301:'Pepe Guardiola'} #CREA UN NUEVO DICCIONARIO
huespedes.update(registroshoy)  #SUMA EL DICCIONARIO registroshoy EN EL DICCIONARIO INICIAL huespedes
for habitacion, huesped in huespedes.items():
    print (habitacion,':',huesped)
print()
                                                #IMPRIME EL DICCIONARIO CON SUS ACTUALIZACIONES
print ('====================================')

huespedes[107]='Ricky Martin'   #REMPLAZA EL VALOR EN EL DICCIONARIO DE LA CLAVE 107
print (huespedes)            #IMPRIME EL DICCIONARIO CON SUS MODIFICACIONES

print ('====================================')


del huespedes[102]
huespedes.pop(202)  #ELIMINA LOS ITEMS CORRESPONIENTES A LAS CLAVES 102 Y 202 , Y VUELVE A IMPRIMIR EL DICCIONARIO SIN ESTAS
print(huespedes)

print ('====================================')

copia1=huespedes.copy() #REALIZA UN DUPLICADO DEL DICCIONARIO HUESPEDES Y A ESTA COPIA LE ASIGNA EL NOMBRE DE COPIA1
print ('copia1: ',copia1)
copia2={}           #CREA UN DICCIONARIO LLAMADO COPIA2 VACIO Y LUEGO AGREGA LOS VALORES DEL DICCIONARIO HUESPEDES
copia2.update(huespedes)
print ("copia2: ",copia2) #IMPRIME EL DICCIONARIO COPIA2

print ('====================================')

lista=[2,5,7,1]
diccio=dict.fromkeys(lista,"xxx")
print(diccio)  #CREA UNA LISTA Y LUEGO UN DICCIONARIO Y AL DICCIONARIO LE ASIGNA PARA LAS CLAVES LOS CARACTERES DE LA LISTA Y PARA LOS VALORES DE LAS CLAVES xxx PARA TODAS

print ('====================================')
inventario={"plata": (500,2500), 'cartera' : ["Cedula","Moneda","Boletas"],'mecato':'Detodito','dias':1}
print (inventario)                                          #CREA UN DICCIONARIO Y LO IMPRIME 
inventario["cartera"].sort()  #ORDENA EN ORDEN ALFABETICO LOS VALORES DE LA CLAVE CARTERA
print(inventario) #IMMPRIUME EL DICCIONARIO CON LA MODIFICACION DE ORDEN  
#inventario["cartera"].remove("Moneda")
del inventario['cartera']
print(inventario)
print(inventario.get("plata")[0])
