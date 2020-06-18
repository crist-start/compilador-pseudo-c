
def convertirInfijaAPostfija(infija):
    '''Convierte una expresión infija a una posfija, devolviendo una lista.'''
    pila = []
    salida = []
    for e in infija:
        if e == '(':
            pila.append(e)
        elif e == ')':
            while pila[len(pila) - 1 ] != '(':
                salida.append(pila.pop())
            pila.pop()
        elif e in ['+', '-', '*', '/', '^']:
            while (len(pila) != 0) and obtenerPrioridadOperador(e) >= obtenerPrioridadOperador(pila[len(pila) - 1]):
                salida.append(pila.pop())
            pila.append(e)
        else:
            salida.append(e)
    while len(pila) != 0:
        salida.append(pila.pop())
    return salida

def intermedio(postfija,var):
    pila,cod=[],[]
    count=1
    for i in postfija:
        if i in var:
            pila.append(i)
        elif i in ['+', '-', '*', '/', '^']:
            op2=pila.pop()
            temp=["t"+str(count),"=",pila.pop(),i,op2,";"]
            cod.append(["var","t_dato","t"+str(count),";"])
            cod.append(temp)
            pila.append("t"+str(count))
            count=count+1
        elif i in ["sin","cos","tan"]:
            temp=['t'+str(count),'=',i,'(',pila.pop(),')',';']
            cod.append(temp)
            pila.append("t"+str(count))
            count=count+1
    return cod

class nodoB:
    def __init__(self,izq,dato,der):
        self.izq=izq
        self.der=der
        self.dato=dato
def esId(a=""):
    return a[0] in "_abcdefghi"
def prioridad(a=''):
    if a in '+-':
        return 1
    elif a in '*/':
        return 2
    elif a in '^':
        return 3
def arbolExpresion(a=[]):
    nodo=nodoB(None,None,None)
    temp=nodo
    c=0
    while c < len(a):
        if nodo.dato==None:
            if a[c] in ['+','-','*','/','^','sin','cos','tan']:
                nodo.dato=a[c]
            elif esId(a[c]):
                nodo.izq=nodoB(None,a[c],None)
            elif a[c]=='(':
                cont=1
                exp=[]
                while cont!=0 and c != len(a):
                    c=c+1
                    exp.append(a[c])
                    if a[c]=='(':
                        cont=cont+1
                    if a[c]==')':
                        cont=cont-1
                exp.pop()
                print(exp)
                nodo.izq=arbolExpresion(exp)
        elif nodo.dato in ['+','-','*','/','^','sin','cos','tan']:
            if esId(a[c]):
                nodo.der=nodoB(None,a[c],None)
            elif a[c]=='(':
                cont=1
                exp=[]
                while cont!=0 and c != len(a):
                    c=c+1
                    exp.append(a[c])
                    if a[c]=='(':
                        cont=cont+1
                    if a[c]==')':
                        cont=cont-1
                exp.pop()
                print(exp)
                nodo.der=arbolExpresion(exp)
        c=c+1            
    return nodo;

def expresionPostfija(a=nodoB(None,None,None)):
    if a.der==None:
        return a.dato
    else:
        salida=[]
        salida.extend(expresionPostfija(a.izq))
        salida.extend(expresionPostfija(a.der))
        salida.append(a.dato)
        return salida

a=arbolExpresion(['(','a','-','b',')','/','(','c','-','d',')'])
post=expresionPostfija(a)
inter=intermedio(post,['a','b','c','d'])
