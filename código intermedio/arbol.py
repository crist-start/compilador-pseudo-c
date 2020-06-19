class nodoB:
    def __init__(self,izq,dato,der):
        self.izq=izq
        self.der=der
        self.dato=dato
def esId(a=""):
    return a[0] in "_abcdefghijklmnopqrstuvwxyz"
def prioridad(a=''):
    if a in '+-':
        return 1
    elif a in '*/':
        return 2
    elif a in '^':
        return 3

def expresion(a=[]):
    nodo=nodoB(None,None,None)
    temp=nodoB(None,None,None)
    c=0
    if len(a)==1:
        nodo.dato=a[0]
        return nodo
    while c < len(a):
        estado=2
        if nodo.dato==None:
            if a[c] in ['+','-','*','/','^','sin','cos','tan']:
                nodo.dato=a[c]
                if a[c] in ['+','-','*','/','^']:
                    estado=2
                else:
                    estado=6
            elif esId(a[c]):
                nodo.izq=nodoB(None,a[c],None)
                estado=3
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
                nodo.izq=expresion(exp)
                estado=3
        elif nodo.dato in ['+','-','*','/','^']:
            if esId(a[c]):
                nodo.der=nodoB(None,a[c],None)
                estado=3
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
                nodo.der=expresion(exp)
        elif nodo.dato in ['sin','cos','tan']:
            if a[c]=='(':
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
                nodo.der=expresion(exp)
        c=c+1            
    return nodo;
