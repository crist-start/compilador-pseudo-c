def esSeparador(caracter):
        return caracter in " \n\t"

def esSimboloEsp(caracter):
        return caracter in "+-*;,.:!=%&/()[]<><=>=:="

def esEntero(cad):
        valido = True
        for c in cad:
                if c not in "0123456789":
                        valido = False
        return valido

def esFlotante(cad):
        valido = True
        for c in cad:
            if c not in "0123456789.":
                valido = False
        return valido

def esOperador(cad):
        valido = False
        if cad in "+-*/()":
                valido = True
        return valido

def tokeniza(linea):
        tokens = []
        tokens2 = []    
        dentro = False   
        for l in linea:
            if esSimboloEsp(l) and not(dentro):
                tokens.append(l)
            if (esSimboloEsp(l) or esSeparador(l)) and dentro:
                tokens.append(cad)
                dentro = False
                if esSimboloEsp(l):
                    tokens.append(l)
            if not (esSimboloEsp(l)) and not (esSeparador(l)) and not(dentro):
                dentro = True
                cad=""
            if not (esSimboloEsp(l)) and not (esSeparador(l)) and dentro:
                    cad = cad + l   
        compuesto = False
        for c in range(len(tokens)-1):
            if compuesto:
                compuesto = False
                continue
            if tokens[c] in "=<>!" and tokens[c+1]=="=":
                tokens2.append(tokens[c]+"=")
                compuesto = True
            else:
                tokens2.append(tokens[c])
        tokens2.append(tokens[-1])    
        for c in range(1,len(tokens2)-1):
            if tokens2[c]=="." and esEntero(tokens2[c-1]) and esEntero(tokens2[c+1]):
                tokens2[c]=tokens2[c-1]+tokens2[c]+tokens2[c+1]
                tokens2[c-1]="borrar"
                tokens2[c+1]="borrar"    
        porBorrar = tokens2.count("borrar")
        for c in range(porBorrar):
            tokens2.remove("borrar")
        tokens=[]
        dentroCad = False
        cadena = ""
        for t in tokens2:        
            if dentroCad:
                if t[-1]=='"':
                    cadena=cadena+" "+t
                    tokens.append('"')
                    tokens.append(cadena[1:-1])
                    tokens.append('"')
                    dentroCad = False
                else:
                    cadena = cadena+" "+t
            elif ((t[0]=='"')):
                  cadena= t;
                  dentroCad = True
            else:              
                  tokens.append(t)
        #print(tokens)
        return tokens
