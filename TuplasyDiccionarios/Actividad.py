# -- coding: utf-8 --
"""
Created on Tue Nov  8 21:52:37 2022

@author: Laura Rairan - Harold Vargas
"""

n = 9

Estudiantes= {1: {"codigo": 11, "nombre": "Juan", "apellido":  "Lopez", "n1": 2.0, "n2": 3.6, "n3": 3.2},
        2: {"codigo": 12, "nombre": "Camilo", "apellido":  "Jimenez", "n1": 1.0, "n2": 2.3, "n3": 1.1},
        3: {"codigo": 13, "nombre": "Eduard", "apellido":  " Meza", "n1": 4.5, "n2": 4.2, "n3": 4.7},
        4: {"codigo": 14, "nombre": "Pablo", "apellido":  "Flores", "n1": 5.0, "n2": 3.1, "n3": 2.3},
        5: {"codigo": 15, "nombre": "David", "apellido":  "Vargas", "n1": 2.5, "n2": 5.0, "n3": 1.5},
        6: {"codigo": 16, "nombre": "Gabriela", "apellido":  "Montero", "n1": 1.7, "n2": 3.4, "n3": 4.6},
        7: {"codigo": 17, "nombre": "Daniel", "apellido":  "Mejia", "n1": 3.9, "n2": 1.6, "n3": 3.2},
        8: {"codigo": 18, "nombre": "Daniela", "apellido":  "Mendoza", "n1": 4.3, "n2": 2.7, "n3": 3.3},
        9: {"codigo": 19, "nombre": "María", "apellido":  "Garcia", "n1": 1.2, "n2": 3.9, "n3": 3.6},
        10: {"codigo": 20, "nombre": "Juca", "apellido":  "Romero", "n1": 3.3, "n2": 2.2, "n3": 1.1}}

def agregar(n):
    
    i = int(input("Cuantos estudiantes desea agregar?: "))
    for a in range(i):
        Estudiantes[n+1]={"codigo": input("Ingrese el codigo del estudiantes"), "nombre": input("Ingrese el nombre: "), "apellido":input("Ingrese el apellido: "), "nota1": input("ingrese nota 1 "), "nota2": input("Ingrese nota 2"), "nota3":input("Ingrese nota 3 ")}
        n+=1
        
def modificar():
    
    a = int(input("Ingrese el codigo del estudiante"))
    
    for i in range(1, len(Estudiantes)):
        if a== Estudiantes[i]["codigo"]:
            
            x = int(input("Que dato Requiere modificar:  \n1. Codigo \n2. Nombre \n3. Apellido \n4. Nota 1 \n5. Nota 2 \n6. Nota 3"))
            if x ==1:
                c = int(input("Ingrese el nuevo codigo: "))
                Estudiantes[i].update(codigo=c)
            elif x ==2:
                n = input("Ingrese el nuevo nombre: ")
                Estudiantes[i].update(nombre=n)
            elif x ==3:
                a = input("Ingrese el nuevo apellido: ")
                Estudiantes[i].update(apellido=a)
            elif x ==4:
                na = int(input("Ingrese la nota 1: "))
                Estudiantes[i].update(n1=na)
            elif x == 5:
                nb = int(input("Ingrese la nota 2: "))
                Estudiantes[i].update(n2=nb)
            else:
                nc = int(input("Ingrese la nota 3: "))
                Estudiantes[i].update(n3=nc)
                
                
def eliminar():
    
    numero= int(input("Ingrese el código del estudiante que quiere eliminar\n->"))
    for i in range(1, len(Estudiantes)):
        if Estudiantes[i]["codigo"]== numero:
            del Estudiantes[i]
    print(Estudiantes)
    
    
def calcularNotas(): 
    
    calcular_notas = int(input("¿Qué opción desea? \n1. Promedio de cada estudiante: \n2. Promedio general del salón: ")) 
    if calcular_notas == 1:    
        for i in range(1, len(Estudiantes)):
            a = Estudiantes[i]["n1"],  b = Estudiantes[i]["n2"] , c = Estudiantes[i]["n3"]
            print(f"{Estudiantes[i]['nombre']},{Estudiantes[i]['apellido']},Nota promedio: {((a+b+c)/3)}") 
            
    prom= 0
    
    if  calcular_notas == 2:
        for i in range(1, len(Estudiantes)):
            a = Estudiantes[i]["n1"], b = Estudiantes[i]["n2"], c = Estudiantes[i]["n3"]
            prom+= (a+b+c)/3
    
        prom/= len(Estudiantes)
        print(f"Promedio general:{prom}")    
        


"""Menu Principal"""

Menu = int(input("Ingrese una opción: " ,
                 "\n1. Agregar estudiante",
                 "\n2. Modificar datos",
                 "\n3. Eliminar datos",
                 "\n4. Calcular notas",
                 "\n5. Mostar lista de estudiantes  \n"))

if Menu == 1:    
    agregar(n)    
    
elif Menu == 2:    
    modificar() 
    
elif Menu == 3:    
     eliminar() 
     
elif Menu == 4:    
    calcularNotas()
    
elif Menu == 5:
    for i in Estudiantes:
            print(Estudiantes[i])
