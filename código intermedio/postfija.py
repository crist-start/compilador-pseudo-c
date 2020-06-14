def obtenerPrioridadOperador(op):
    if op in "+-":
        return 0
    elif op in "*/":
        return 1
    elif op=="^":
        return 2
    else:
        return 3;

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

e1 = ["(","y2","-","y1",")","/","(","x2","-","x1",")"]
e2=['(','a','+','b',')','-','(','c','/','d',')','+','e']
pf=convertirInfijaAPostfija(e2);
print(pf)

def esVariable(var=""):
    return var in ["a","b","c","d","e"]
def esOperador(op=""):
    return op in "+-*/^"
def esTrigonometrica(tr=""):
    return tr in ["sin","cos","tan"]

def intermedio(postfija=[]):
    pila,cod=[],[]
    count=1
    for i in postfija:
        if esVariable(i):
            pila.append(i)
        elif esOperador(i):
            op2=pila.pop()
            temp=["t"+str(count),"=",pila.pop(),i,op2,";"]
            cod.append(temp)
            pila.append("t"+str(count))
            count=count+1
        elif esTrigonometrica(i):
            temp=['t'+str(count),'=',i,'(',pila.pop(),')',';']
            cod.append(temp)
            pila.append("t"+str(count))
            count=count+1
    return cod

cod=intermedio(['a', 'b', '+', 'c', 'd', '/', '-', 'e','sin','+'])
for i in cod:
    print (i)
