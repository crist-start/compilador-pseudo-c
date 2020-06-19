
from EvaluadorSintactico import *

if (evaluadorSintactico() == True):
    
    class Variable:
        nombre = ""
        tipo = ""
        valor = ""
        direccion = 250

        def __init__(self, n, t, v , d):
            self.nombre = n
            self.tipo = t
            self.valor = v
            self.direccion = d


    # ------- Aqui inicia el manejo de los tokens -------------
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

    def esOperador(caracter):
        return caracter in "+-*/"


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
        return tokens

    def esId(cad):
        if cad[0] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_":
            return True
        else:
            return False
    # ------- Aqui termina el manejo de los tokens    -------------    


    # ------- Aqui inicia el manejo de la tabla de variables --------
    
    
    def agregaVar(varNombre, tipoVar, direccion):
        #print(varNombre, tipoVar)
        
        tablaVar.append(Variable(varNombre, tipoVar, "null" , str(direccion)))
        
        return None
    def setValor(varNombre, valor):    
        for v in tablaVar:
            if (v.nombre == varNombre):
                tipo = getTipo(varNombre)
                if (valor != "null"):
                    if (tipo=="int"):
                        v.valor = int(valor)
                        
                    elif (tipo=="char"):
                        v.valor = '"' + valor[1:-1] + '"'
                       
                    elif (tipo=="string"):
                        v.valor = '"' + valor[1:-1] + '"'
                        
                            
                    elif (tipo=="float"):
                        v.valor = float(valor)
                else:
                    print("error no hay un valor en la variable")
                    #v.valor = valor
                     
        return None

    def esSimboloEsp(caracter):
        return caracter in "+-*;,.:!=%&/()[]<><=>=:="

    def getTipo(varNombre):
        for v in tablaVar:
            if (v.nombre == varNombre):
                return v.tipo
            pass


    def getValor(varNombre):
        for v in tablaVar:
            if (v.nombre == varNombre):
                return v.valor
            pass

    def estaEnTabla(n):
        encontrado = False
        for reg in tablaVar:        
            if reg.nombre == n:
                encontrado = True      
        return (encontrado)

    # ------- Aqui termina el manejo de la tabla de variables --------

    # -------- funciones para evaluar datos ------------------------
    '''
    def evaluandoFor(cad)
                    interrupcion = False
                     
    
    def evaluarFor(cad):
                bandera = False
                if (estaEnTabla(tokens[2])):
                    if (evaluandoFor(tokens)==False):
                        bandera = True
                        
                    
                
                    return interrupcion
                    
                return
    '''
    def evaluarPrinte(cad): 
        bandera = False
        if (len(tokens)== 5): #println ( edad ) ;
            if(estaEnTabla(tokens[2]) and getValor(tokens[-3]) != "null"):
                #print("popo")
                bandera = True
            else:
                bandera =False
                print("nose encontro en la tabla o su valor no existe")
        #elif(tokens[2]) 
        elif (len(tokens)== 9):#print ( edad , " hola " ) ;
            if(esId(tokens[2]) and estaEnTabla(tokens[2]) and getValor(tokens[-3]) != "null" and tokens[3] == ','and tokens[4] == '"'):
                bandera = True
            elif(tokens[2] == '"' and tokens[4] == '"'  and tokens[5] == ','
                 and esId(tokens[-3]) and estaEnTabla(tokens[-3]) and getValor(tokens[-3]) != "null"): #print ( " hola "  , edad ) ;
                bandera = True
        elif (len(tokens) == 7): #print ( " dame tu altura " ) ;
            if(tokens[2]== '"' and tokens[-3] =='"' ):
                bandera = True
            
                
            
            
                   
        return bandera
        
        
    #---------------------------------------------------------------


    # programa principal
    arch = open("codigoSC.txt", "r")
    programa = arch.readlines()
    j = 250
    tablaVar = []
    renglon = ""
    interrupcion = False
    sinErrores = True
    cont = 0
    
    for renglon in programa:
        cont = cont + 1
        #if (interrupcion == False):
        #print(renglon[:])               # ------------- Quita el  # de comentario de esta linea para ver la cadena
        if(renglon!="end;"):        
                
            tokens = tokeniza(renglon)
            print(tokens)
            
            if (tokens[0] =="var"):  # Es una declaracion de variable
                if not(estaEnTabla(tokens[2])): 
                    #print(tokens[2],tokens[1])
                    print("hecho")
                    agregaVar(tokens[2], tokens[1], j)
                    j +=1
                else:
                    interrupcion = True
                    print("Esa variable ya esta declarada")
            
            elif (tokens[0] == "for"): # forma for ( calidad = 10 ; 10 )
                if (esEntero(tokens[-2])or esEntero(getValor(tokens[-2]))):
                    
                    if not(estaEnTabla(tokens[2])):
                        agregaVar(tokens[2], 'int', j)
                        j +=1
                        if(esEntero(tokens[4])):
                            print("hecho")
                            setValor(tokens[2], tokens[4])
                        elif(estaEnTabla(tokens[4])):
                             if( getTipo(tokens[4]) == getTipo(tokens[2])):
                                if (getValor(tokens[4]) != "null"):
                                    print("Hecho")
                                    setValor(tokens[2], getValor(tokens[4]))
                                else:
                                    interrupcion = True
                                    print(tokens[4],"esta bacia .")
                             else:
                                interrupcion = True
                                print ("no concordaron los tipos de las variables")
                        elif not(estaEnTabla(tokens[4])):
                             interrupcion = True
                             print("no existe la variable",tokens[4])
                        else:
                            interrupcion = True
                            print("no es un entero")
                    elif (estaEnTabla(tokens[2]) and getTipo(tokens[2] == int)):
                        if(esEntero(tokens[4])):
                            print("hecho")
                            setValor(tokens[2], tokens[4])
                        elif(estaEnTabla(tokens[4])):
                             if( getTipo(tokens[4]) == getTipo(tokens[2])):
                                if (getValor(tokens[4]) != "null"):
                                    print("hecho")
                                    setValor(tokens[2], getValor(tokens[4]))
                                else:
                                    interrupcion = True
                                    print("Esa variable esta bacia .")
                             else:
                                interrupcion = True
                                print ("no concordaron los tipos de las variables")
                        elif no(estaEnTabla(tokens[4])):
                             interrupcion = True
                             print("no existe la variable")
                        else:
                            interrupcion = True
                            print("no es un entero")
                else:
                    interrupcion = True
                    print(tokens[-2], "no es un entero")
                
                        
            elif (tokens[0] == "print" or tokens[0] == "println"):
                if (evaluarPrinte(tokens) == False):
                    interrupcion = True
                    print(" no se encontro la variable ")
                else:
                    print("hecho")
                
  
                    
                    
                    
                 
                    
            elif(esId(tokens[0]) and estaEnTabla(tokens[0])): # El primer token es un ID
                if (tokens[1]=="="):
                    #print(type(tokens[2]))
                    if (len(tokens)==4 and tokens[0] != tokens[2]): # Es de la forma "ID = valor;"
                        if(esEntero(tokens[2]) or esFlotante(tokens[2])):
                            print("hecho")
                            setValor(tokens[0], tokens[2])
                        elif(estaEnTabla(tokens[2]) and getTipo(tokens[2]) == getTipo(tokens[0])):
                            if ( getValor(tokens[2])!= "null" ):
                                print("hecho")
                                setValor(tokens[0], getValor(tokens[2]))
                            else:
                                interrupcion=True
                                print("La variable esta bacia")
                        else:
                            interrupcion=True
                            print("error Los tipos de datos no coinciden o no esta en la tabla de variables")
                    elif (tokens[2] == '"'and tokens[4] == '"'):
                        #print("entro")
                        if (len(tokens) == 6 ): #and len(tokens[3]) == 3 ): Es de la forma a = "cadena de cualquier extencion" ;                            
                            
                            if (getTipo(tokens[0]) ==  "char"):
                                if (len(tokens[3]) == 3 ):
                                    print("hecho")
                                    setValor(tokens[0], tokens[3])
                                    
                            elif (getTipo(tokens[0]) ==  "string"):
                                if (len(tokens[3]) >= 4):
                                    print("hecho")
                                    setValor(tokens[0], tokens[3])
                            else:
                                interrupcion=True
                                print( tokens[3],"no es la extencion requerida para ser un str ")
                        
                    #elif (tokes ):
                    #    setValor(tokens[0], tokens[3])
                        
                        


                
               
    for e in tablaVar:
        print (e.nombre , e.tipo, e.valor, e.direccion )
                 #funcionRead(tokens)
    
    '''
                else: # Es id = exp  ej. c = a*b+d;                
                        expresion = tokens[2:-1]                
                        posfija = infija2Posfija(expresion)               
                        posfijaV = getValores(posfija)               
                        resultado = evaluarPosfija(posfijaV)                
                        setValor(tokens[0], resultado)
                elif (tokens[0]=="print") or (tokens[0]=="println"):
                    funcionPrint(tokens)
                elif (len(tokens)==2):  # Es solo el identificador
                    print(getValor(tokens[0]))
                    '''
