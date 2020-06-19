import separaPrint as sp
import postfija as pf
import arbol

class Variable:
    def __init__(self,idV,tipo,val,dirM):
        self.idV=idV
        self.tipo=tipo
        self.val=val
        self.dirM=dirM


var=[Variable('a','int','0',200)
     ,Variable('b','int','0',201)
     ,Variable('c','int','0',202)
     ,Variable('d','int','0',203)
     ,Variable('e','int','0',204)
     ,Variable('y1','int','0',205)
     ,Variable('y2','int','0',206)
     ,Variable('x2','int','0',207)
     ,Variable('x','int','0',208)]

variables=[]
for e in var:
    variables.append(e.idV)
def obtenerVar(a=""):
    for i in var:
        if i.idV==a:
            return i

def intermedio(a=[]):
    intermedio=[];
    for i in a:
        if i[0]=='print' or i[0]=='println':
            prints=sp.separaPrint(i)
            intermedio.extend(prints)
        elif i[0] in variables and i[1]=='=':
            if i[3]==';' or i[5]==';' or i[6]==';':
                intermedio.append(i)
            else:
                ab=arbol.expresion(i[2:-1])
                postfija=pf.expresionPostfija(ab)
                #print(postfija)
                inter=pf.intermedio(postfija,variables)
                inter.pop(-2)
                inter[-1][0]=i[0]
                pf.evaluaIds(inter,variables)
                var.extend(pf.asignarDir(inter,var[-1]))
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
    return intermedio;

cod=[]
text=open('prueba.cpp','r')
for i in text:
    j=i.split(' ')
    j[-1]=';'
    cod.append(j)

t1=intermedio(cod)

interm=open('intermedio.cpp','w');

for i in t1:
    for j in i:
        interm.write(j)
        if j != ';':
            interm.write(' ')
    interm.write('\n')
        
interm.close()
