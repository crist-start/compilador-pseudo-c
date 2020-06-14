'''aqui colocaran la ruta para poder importar sus archivos'''
import sys
sys.path.append('prueba/')
sys.path.append('prueba2/')

'''aqui importaran sus archivos para usar sus funciones'''
#ejemplo
import prueba as p
import prueba2 as t

'''aqui usaran las funciones que importaron'''
#ejemplo
a=open('texto.txt','r')
p.recorreLista(a)#uso de prueba/prueba.py
t.triangulo(10)#uso de prueba2/prueba2
