def esCad(a=""):
    return a[0]=='"' and a[-1]=='"'

def esNum(a=""):
    estado=True
    for i in a:
        if i not in '.0123456789-':
            estado=False
    return estado

def separaPrint(a,v):
    pr=['print','(']
    salida=[]
    for i in a:
        if esCad(i) or esNum(i) or enTabla(i,v):
            pr.append(i)
        elif i==',':
            pr.extend([')',';'])
            salida.append(pr)
            pr=['print','(']
        elif i==')':
            pr.append(i)
        elif i==';':
            pr.append(i)
            salida.append(pr)
            if(a[0]=='println'):
                salida.append(['print','(','"\\n"',')',';'])
    return salida;


def expresionPostfija(a):
    if a.der==None and a.izq==None:
        return [a.dato]
    else:
        salida=[]
        salida.extend(expresionPostfija(a.izq))
        salida.extend(expresionPostfija(a.der))
        salida.append(a.dato)
        return salida
    

def intermedio(postfija):
    pila,cod=[],[]
    count=1
    for i in postfija:
        if i in ['+', '-', '*', '/', '^']:
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
        else:
            pila.append(i)
    return cod

def enTabla(a,v):
    for i in v:
        if i.idV==a:
            return True
    return False

def addVar(a,v):
    temp=[]
    for i in range(len(a)):
        if a[i][0]=='var':
            if enTabla(a[i][2],v):
                dat='t'+str(int(a[i][2][-1])+1)
                ant=a[i][2]
                a[i][2]=dat
                a[i+1][0]=dat
                v.append(Variable(dat,None,None,v[-1].dirM+1))
                for j in range(i+1,len(a)):
                    for k in range(len(a[j])):
                        if a[j][k]==ant:
                            a[j][k]='?'+dat
            else:
                v.append(Variable(a[i][2],None,None,v[-1].dirM+1))
    for i in range (len(a)):
        for j in range(len(a[i])):
            if '?' in a[i][j]:
                a[i][j]=a[i][j].replace('?','')
                

class Variable:
    def __init__(self,idV,tipo,val,dirM):
        self.idV=idV
        self.tipo=tipo
        self.val=val
        self.dirM=dirM

def recorrerTab(tab,dato):
    ret=[]
    for i in dato:
        tab.extend(i)
        ret.append(tab)
        tab=['\t']
    return ret

def obtenerVar(a,v):
    for i in v:
        if i.idV==a:
            return i

def analizaCodigo(inter,v):
    for e in inter:
        if 't' in e[0]:
            ins=obtenerVar(e[0],v)
            if e[3]=='/':
                ins.tipo='float'
            elif obtenerVar(e[2],v).tipo == obtenerVar(e[4],v).tipo:
                ins.tipo=obtenerVar(e[2],v).tipo
            else:
                ins.tipo='float'
        else:
            tip=obtenerVar(e[0],v).tipo
            if e[3]=='/' and tip=='float':
                return True
            elif obtenerVar(e[2],v).tipo == obtenerVar(e[4],v).tipo==tip:
                return True
            elif obtenerVar(e[2],v).tipo != obtenerVar(e[4],v).tipo and tip=='float':
                return True
            else:
                return False
            
