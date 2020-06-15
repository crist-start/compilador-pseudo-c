
def comentario(codigo=""):
    estado=0;
    cod,temp="",""
    for i in codigo:
        if(i=='/' and estado==0):
            estado=1
            temp=i
        elif(estado==1):
            if(i=='*'):
                estado=2
                temp=""
            elif(i=='/'):
                estado=4
                temp=""
            else:
                estado=0
                cod=cod+temp+i
                temp=""
        elif(estado==2):
            if(i=='*'):
                estado=3
        elif(estado==3):
            if(i=='/'):
                estado=0
            elif(i=='*'):
                estado=3
            else:
                estado=2;
        elif(estado==4):
            if(i=='\n'):
                estado=0
                cod=cod+i
        else:
            cod=cod+i
    return cod;

arch=open('Certificado.java','r')
coment=comentario(arch.read())
arch2=open('sin comentarios.java','w')
arch2.write(coment)
arch2.close()
