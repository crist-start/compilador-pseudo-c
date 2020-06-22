'''aqui colocaran la ruta para poder importar sus archivos'''
import sys
sys.path.append('prueba/')
sys.path.append('analisis/')
sys.path.append('código intermedio/')
sys.path.append('generación de codigo/')

'''aqui importaran sus archivos para usar sus funciones'''
import an_cod_int as es
import arbol
import programa2 as generador
from AnalisadorSemantico import *

class Variable:
    def __init__(self,idV,tipo,val,dirM):
        self.idV=idV
        self.tipo=tipo
        self.val=val
        self.dirM=dirM

'''aqui usaran las funciones que importaron'''

var=[]
for i in tablaVar:
    var.append(Variable(i.nombre,i.tipo,i.valor,i.direccion))

sc=[]
intermedio=[]

arch=open('codigoSC.txt','r')
print('-----------------')
for i in arch:
    i=i.replace('\n','')
    temp2=i.split(' ')
    temp=[]
    estado=0
    cad=""
    for j in temp2:
        if(estado==0):
            if j=='"':
                estado=1
                cad=cad+j
            else:
                temp.append(j)
        else:
            if j=='"':
                estado=0
                cad=cad+j
                temp.append(cad)
                cad=""
            else:
                cad=cad+j+' '
    sc.append(temp)

noError=True

estado=0
contador=0
for i in sc:
    if noError:
        noError,estado=es.analizaCodigo(i,var,estado,noError,intermedio)
        contador=contador+1
    else:
        print("error en linea",contador,'(',sc[contador-1],'.')
        break;
if noError:
    for i in intermedio:
        print(i)

#if noError:
#    generador.var = var
#    generador.GenerarCodigo(intermedio)
