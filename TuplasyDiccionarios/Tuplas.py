'''
Created on 3/11/2022

@author: Harday
'''
t = (23,'a',(2.5,3.7,'x'),["perrito","gatito"],'Pepe')
print (t)
print (len(t))


print ('=====================================')
print (t[0])
print (t[3])
print (t[1:3])
print (t[3][1])


print ('====================================')
print (t[3])
t[3].append('lorito')
print (t)

print ('====================================')
for elemento in t:
    print (elemento)

print ('====================================')
for index in range(0,len(t)):
    print (t[index])

print ('====================================')
if 'a' in t:
    print ("El elemento 'a' esta en la tupla")

print ('====================================')
lista=list(t)
lista[1]='A'
print (lista)

tupla=tuple(lista)
print (tupla)

print ('====================================')
l = [(1,1), (2,4), (3,9), (4,16), (5,25)]
for x, y in l:
    print (x, ':', y)