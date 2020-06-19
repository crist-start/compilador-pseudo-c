def esCadena(a=""):
    return a[0]=='"' and a[-1]=='"'

def separaPrint(a=[]):
    pr=['print','(']
    salida=[]
    for i in a:
        if esCadena(i):
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

def evaluaIds(a,v):
    temp=[]
    cont=0
    for i in range(len(a)):
        if a[i][0]=='var':
            if enTabla(a[i][2],v):
                dat='t'+str(int(a[i][2][-1])+1)
                ant=a[i][2]
                a[i][2]=dat
                a[i+1][0]=dat
                temp.append(Variable(dat,None,None,None))
                for j in range(i+1,len(a)):
                    for k in range(len(a[j])):
                        if a[j][k]==ant:
                            a[j][k]='_'+dat
            else:
                v.append(Variable(a[i][2],None,None,None))
            cont=cont+1
    for i in range (len(a)):
        for j in range(len(a[i])):
            if '_' in a[i][j]:
                a[i][j]=a[i][j].replace('_','')
                

class Variable:
    def __init__(self,idV,tipo,val,dirM):
        self.idV=idV
        self.tipo=tipo
        self.val=val
        self.dirM=dirM

def asignarDir(a,v):
    var=[]
    for i in a:
        if i[0]=='var':
            c=Variable(i[2],i[1],0,v.dirM+1)
            var.append(c)
            v=c
            a.remove(i)
    return var
