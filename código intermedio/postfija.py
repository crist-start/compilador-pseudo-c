def expresionPostfija(a):
    if a.der==None and a.izq==None:
        return [a.dato]
    else:
        salida=[]
        salida.extend(expresionPostfija(a.izq))
        salida.extend(expresionPostfija(a.der))
        salida.append(a.dato)
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

def evaluaIds(a=[],v=[]):
    inter=[]
    for i in range(len(a)):
        if a[i][0]=='var':
            if a[i][2] in v:
                dat='t'+str(int(a[i][2][-1])+1)
                ant=a[i][2]
                a[i][2]=dat
                a[i+1][0]=dat
                v.append(dat)
                for j in range(i+1,len(a)):
                    for k in range(len(a[j])):
                        if a[j][k]==ant:
                            a[j][k]='_'+dat
            else:
                v.append(a[i][2])
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
