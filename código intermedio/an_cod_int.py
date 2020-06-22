import intermedio as cod_int
import arbol

def analizaCodigo(i,var,estado,noError,intermedio):
    tab=['\t']
    if i[0]=='print' or i[0]=='println':
        prints=cod_int.separaPrint(i,var)
        if estado==1:
            intermedio.extend(cod_int.recorrerTab(tab,prints))
        else:
            intermedio.extend(prints)
    elif i[0] == 'for':
        intermedio.append(i)
        estado=1
    elif i[0] == '{':
        intermedio.append(i)
    elif i[0] == '}':
        intermedio.append(i)
        estado=0
    elif i[1]=='=':
        if i[3]==';' or i[5]==';' or i[6]==';':
            if estado==1:
                tab.extend(i)
                intermedio.append(tab)
            else:
                intermedio.append(i)
        else:
            #ab=arbol.expresion(i[2:-1])
            postfija=cod_int.infija2Postfija(i[2:-1])
            inter=cod_int.intermedio(postfija)
            inter.pop(-2)
            inter[-1][0]=i[0]
            cod_int.addVar(inter,var)
            for i in inter:
                if i[0]=='var':
                    inter.remove(i)
            noError=cod_int.analizaCodigo(inter,var)
            if estado==1:
                intermedio.extend(cod_int.recorrerTab(tab,inter))
            else:
                intermedio.extend(inter)
    elif i[0] != 'var':
        if estado==1:
            tab.extend(i)
            intermedio.append(tab)
        else:
            intermedio.append(i)
    else:
        print('linea no utilizaada:',i)
    return noError,estado
            
