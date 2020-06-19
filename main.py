'''aqui colocaran la ruta para poder importar sus archivos'''
import sys
sys.path.append('prueba/')
sys.path.append('analisis')
sys.path.append('código intermedio/')
sys.path.append('generación de codigo/')

'''aqui importaran sus archivos para usar sus funciones'''
import an_cod_int as es
import arbol
import programa2 as generador
import tokeniza as ev

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

sc=[]
intermedio=[]

arch=open('analisis/codigoSC.txt','r')

for i in arch:
    i.replace('\n','')
    intermedio.append(ev.tokeniza(i))
    #intermedio.append(ev.tokeniza(i))

'''noError=True

estado=0
for i in sc:
    if noError:
        noError,estado=es.analizaCodigo(i,var,estado,noError,intermedio)
    else:
        print("error")
        break;
generador.var = var
generador.GenerarCodigo(intermedio)'''
