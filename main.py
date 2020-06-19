'''aqui colocaran la ruta para poder importar sus archivos'''
import sys
sys.path.append('prueba/')
sys.path.append('código intermedio/')
sys.path.append('generación de codigo/')

'''aqui importaran sus archivos para usar sus funciones'''
import an_cod_int as es
import arbol
import programa2 as generador

class Variable:
    def __init__(self,idV,tipo,val,dirM):
        self.idV=idV
        self.tipo=tipo
        self.val=val
        self.dirM=dirM

'''aqui usaran las funciones que importaron'''

var=[Variable('a','int','0',200)
     ,Variable('b','int','0',201)
     ,Variable('c','int','0',202)
     ,Variable('d','int','0',203)
     ,Variable('e','int','0',204)
     ,Variable('y1','int','0',205)
     ,Variable('y2','int','0',206)
     ,Variable('x2','int','0',207)
     ,Variable('x','int','0',208)
     ,Variable('y','float','0',209)
     ]


a=[['var', 'int', 'x', ';']
   ,['var', 'int', 'y', ';']
   ,['var', 'int', 'y1', ';']
   ,['read', '(', 'a', ')', ';']
   ,['print', '(', '"en estos no se hizo intermedio"', ')', ';']
   ,['x', '=', 'd', '+', 'e', ';']
   ,['y', '=', 'sin', '(', 'x', ')', ';']
   ,['println', '(', '"en estos "', ',', '0.15', ')', ';']
   ,['x', '=', '(', 'y2', '-', 'y1', ')', '*', 'x2', ';']
   ,['y', '=', 'a', '+', '(', 'b', '+', '(', 'c', '+', '(', 'd', '/', 'e', ')', ')', ')', ';']
   ,['for','(','c','=','1',';','5',')']
   ,['{']
   ,['read','(','a',')',';']
   ,['a', '=', 'a', '*', '2', ';']
   ,['print', '(', 'y2', ',', '112', ')', ';']
   ,['}']
   ]

noError=True
intermedio=[]

estado=0
for i in a:
    if noError:
        noError,estado=es.analizaCodigo(i,var,estado,noError,intermedio)
    else:
        print("error")
        break;
generador.GenerarCodigo(intermedio)
