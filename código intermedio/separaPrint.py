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
