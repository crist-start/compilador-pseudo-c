
def esNum(a=""):
    for i in a:
        if i not in '0123456789-':
            return False
    return True
def esId(a=""):
    return a[0] in '_abcdefghijklmnopqrstuvwxyz'

def sintaxisExpresion(a=[]):
    estado=0
    cont=0
    for i in a:
        print(estado)
        if estado==0:
            estado=1
        elif estado==1 and i=='=':
            estado=2
        elif estado==2:
            if i in ['sin','cos','tan']:
                estado=6
            elif esNum(i) or esId(i):
                estado=3
            elif i=='(':
                estado=7
                cont=cont+1
            else:
                estado=5#error
        elif estado==3:
            if i in ['+','-','*','/','^']:
                estado=2
            elif i==')':
                estado=3
                cont=cont-1
            elif i==';':
                estado=4
        elif estado==6:
            if i=='(':
                estado=7
                cont=cont+1
            else:
                estado=5#error
        elif estado==7:
            if i in ['sin','cos','tan']:
                estado=6
            elif i=='(':
                estado=7
                cont=cont+1
            elif esNum(i) or esId(i):
                estado=8
            else:
                estado=5#error
        elif estado==8:
            if i==')':
                estado=3
                cont=cont-1
            elif i in ['+','-','*','/','^']:
                estado=7
    print(estado)
    if cont != 0 or estado != 4:
        estado=5
    else:
        estado=9
    return estado

est=sintaxisExpresion(['x','=','a','+','(','b','+','(','c','+','(','d','+','e',')',')',')',';'])
print(est)
