'''aqui colocaran la ruta para poder importar sus archivos'''
import sys
sys.path.append('prueba/')
sys.path.append('código intermedio/')
sys.path.append('generación de codigo/')

'''aqui importaran sus archivos para usar sus funciones'''
import intermedio as cod_int
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
     ,Variable('x','int','0',208)]


def obtenerVar(a=""):
    for i in var:
        if i.idV==a:
            return i
estado=True
intermedio=[]
a=[['var', 'int', 'x', ';']
   ,['var', 'int', 'y', ';']
   ,['var', 'int', 'y1', ';']
   ,['print', '(', '"en estos no se hizo intermedio"', ')', ';']
   ,['x', '=', 'd', '+', 'e', ';']
   ,['y', '=', 'sin', '(', 'x', ')', ';']
   ,['println', '(', '"en estos "', ',', '"si se hizo intermedio"', ')', ';']
   ,['x', '=', '(', 'y2', '-', 'y1', ')', '*', 'x2', ';']
   ,['x', '=', 'a', '+', '(', 'b', '+', '(', 'c', '+', '(', 'd', '/', 'e', ')', ')', ')', ';']
   ]

if estado:
    for i in a:
        if i[0]=='print' or i[0]=='println':
            prints=cod_int.separaPrint(i)
            intermedio.extend(prints)
        elif i[1]=='=':
            if i[3]==';' or i[5]==';' or i[6]==';':
                intermedio.append(i)
            else:
                ab=arbol.expresion(i[2:-1])
                postfija=cod_int.expresionPostfija(ab)
                inter=cod_int.intermedio(postfija)
                inter.pop(-2)
                inter[-1][0]=i[0]
                cod_int.evaluaIds(inter,var)
                var.extend(cod_int.asignarDir(inter,var[-1]))
                intermedio.extend(inter)
                for e in inter:
                    if 't' in e[0]:
                        ins=obtenerVar(e[0])
                        if e[3]=='/':
                            ins.tipo='float'
                        elif obtenerVar(e[2]).tipo == obtenerVar(e[4]).tipo:
                            ins.tipo=obtenerVar(e[2]).tipo
                        else:
                            ins.tipo='float'
        elif i[0] != 'var':
            intermedio.append(i)

for i in intermedio:
    print (i)

generador.GenerarCodigo(intermedio)