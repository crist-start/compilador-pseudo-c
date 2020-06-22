import math 
from EvaluadorSintactico import *

if (evaluadorSintactico() == True):
    
    class Variable:
        nombre = ""
        tipo = ""
        valor = ""
        direccion = 250

        def __init__(self, idV, tipo, val , dirM):
            self.nombre = idV
            self.tipo = tipo
            self.valor = val
            self.direccion = dirM


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
                error=("nose encontro en la tabla o su valor no existe")
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
    funTri = ["sin", "cos" , "tan"]
    tem = ""
    fin = False
    cont =1
    error = ""
    seHizo = ""
    
    for renglon in programa:
        cont = cont + 1
        if (interrupcion == False):
        #print(renglon[:])               # ------------- Quita el  # de comentario de esta linea para ver la cadena
        #while(fin == False):
            if(renglon!="end;"):
                fin = True
                
            tokens = tokeniza(renglon)
            #print(tokens)
            #----------------- si la primer varible es un var ----------------
            if (tokens[0] =="var"):  # Es una declaracion de variable
                if not(estaEnTabla(tokens[2])): 
                    #print(tokens[2],tokens[1])
                    seHizo = ("hecho")
                    agregaVar(tokens[2], tokens[1], j)
                    j +=1
                else:
                    interrupcion = True
                    error = ("Esa variable ya esta declarada")
            #----------------- si la primer varible es un for ----------------
            elif (tokens[0] == "for"): # forma for ( calidad = 10 ; 10 )
                if (esEntero(tokens[-2])or esEntero(getValor(tokens[-2]))):
                    
                    if not(estaEnTabla(tokens[2])):
                        agregaVar(tokens[2], 'int', j)
                        j +=1
                        if(esEntero(tokens[4])):
                            seHizo =("hecho")
                            setValor(tokens[2], tokens[4])
                        elif(estaEnTabla(tokens[4])):
                             if( getTipo(tokens[4]) == getTipo(tokens[2])):
                                if (getValor(tokens[4]) != "null"):
                                    seHizo =("Hecho")
                                    setValor(tokens[2], getValor(tokens[4]))
                                else:
                                    interrupcion = True
                                    error =(tokens[4],"esta bacia .")
                             else:
                                interrupcion = True
                                error =("no concordaron los tipos de las variables")
                        elif not(estaEnTabla(tokens[4])):
                             interrupcion = True
                             error =("no existe la variable",tokens[4])
                        else:
                            interrupcion = True
                            error =("no es un entero")
                    elif (estaEnTabla(tokens[2]) and getTipo(tokens[2] == int)):
                        if(esEntero(tokens[4])):
                            seHizo =("hecho")
                            setValor(tokens[2], tokens[4])
                        elif(estaEnTabla(tokens[4])):
                             if( getTipo(tokens[4]) == getTipo(tokens[2])):
                                if (getValor(tokens[4]) != "null"):
                                    seHizo =("hecho")
                                    setValor(tokens[2], getValor(tokens[4]))
                                else:
                                    interrupcion = True
                                    error =("Esa variable esta bacia .")
                             else:
                                interrupcion = True
                                error = ("no concordaron los tipos de las variables")
                        elif no(estaEnTabla(tokens[4])):
                             interrupcion = True
                             error =("no existe la variable")
                        else:
                            interrupcion = True
                            error =("no es un entero")
                else:
                    interrupcion = True
                    error =(tokens[-2], "no es un entero")
                    
            #----------------- si la primer varible es un print ----------------                        
            elif (tokens[0] == "print" or tokens[0] == "println"):
                if (evaluarPrinte(tokens) == False):
                    interrupcion = True
                    error =(" no se encontro la variable ")
                else:
                    seHizo =("hecho")
            #----------------- si la primer varible es un read ----------------

            elif(tokens[0] == "read"):   #read ( altura ) ;
                if not(estaEnTabla(tokens[2])):
                    interrupcion = True
                    error =(" no se encontro la variable ")
                else:
                    seHizo =("hecho")
                    
            #----------------- si la primer varible es una Funcion Trigonometrica ----------------                    
            elif(tokens[0] in  funTri  and len(tokens) == 3): #sin a ;
                if(estaEnTabla(tokens[1])):                 
                    if(getValor(tokens[1]) != "null" and esEntero(str(getValor(tokens[1]))) or esEntero(str(getValor(tokens[1])))):
                        seHizo =("hecho")                        
                        
                    else:
                        interrupcion = True
                        error =("la variable esta vacia")
                
  
                elif(esFlotante(tokens[1]) or esEntero(tokens[1])): #sin 3 ;
                    seHizo =("hecho")
                    interrupcion = False
                
                else:
                    error =("la variable no existe");
                    interrupcion = True
                     
            #----------------- si la primer varible es un = ----------------
            if (len(tokens) >1 and tokens[1]=="="):
                if(esId(tokens[0]) and estaEnTabla(tokens[0]) ):#and getValor(tokens[0])!= "null"  ): # El primer token es un ID
                    #print(type(tokens[2]))
                                        
                    if (len(tokens)==4 ): # Es de la forma "ID = valor;"
                        if(esId(tokens[2])and ( not esEntero(tokens[2]) or not esFlotante(tokens[2]))):
                            if (estaEnTabla(tokens[2])):
                                if (getTipo(tokens[2]) == getTipo(tokens[0])):
                                    if ( getValor(tokens[2])!= "null" ):
                                        seHizo =("hecho")
                                        setValor(tokens[0], getValor(tokens[2]))
                                    else:
                                        interrupcion=True
                                        error =("La variable ",tokens[2]," esta vacia")
                                else:
                                    interrupcion=True
                                    error =(tokens[0] ," y ", tokens[2], "tienen tipos de datos diferentes")
                            else:
                                interrupcion=True
                                error =("error var" ,(tokens[2]),"no existe")
                                
                        elif(esEntero(tokens[2]) or esFlotante(tokens[2])):                            
                            if ( esFlotante(tokens[2]) == True  and getTipo(tokens[0]) ==  "float" or esEntero(tokens[2]) == True  and getTipo(tokens[0]) ==  "int" ):
                                seHizo =("echo")
                                setValor(tokens[0], tokens[2])                                
                            else:
                                interrupcion=True
                                error =(tokens[0] ," y ", tokens[2], "tienen tipos de datos diferentes")
                        else:
                            error =(tokens[2],"no es una variable valida")
                            
                    elif (len(tokens) == 6 and tokens[2] == '"'  and tokens[-2] == '"' ) : # Es de la forma a = "cadena de cualquier extencion" ;
                        if (getTipo(tokens[0]) == "string" or getTipo(tokens[0]) == "char" ):
                            if (getTipo(tokens[0]) ==  "char"):
                                
                                if (len(tokens[3]) == 3 ):
                                    seHizo =("hecho")
                                    setValor(tokens[0], tokens[3])
                                    
                                else:
                                    interrupcion = True
                                    error =(tokens[3],"no tiene la extencion requerida para ser un char " )
                                    
                            elif (getTipo(tokens[0]) ==  "string"):
                                
                                    seHizo =("hecho")
                                    setValor(tokens[0], tokens[3])
                            else:
                                interrupcion=True
                                error =( tokens[3],"no es un carecter o una cadena ")
                        else:
                            interrupcion=True
                            error =( tokens[0],"no es de tipo cadena o de tipo caracter ")
                    
                
                    elif(len(tokens) == 7 and tokens[2] in funTri):
                        #print(getTipo(tokens[4]))
                        
                        if(estaEnTabla(tokens[4])):
                            #print("entro 2")
                            if (getValor(tokens[4])!= "null"):
                                #print(getTipo(tokens[4]))
                                if(getTipo(tokens[4]) == "int" or getTipo(tokens[4]) == "float" ):
                                    
                                    if(tokens[2] == "sin"):
                                        seHizo =("hecho")                                   
                                        setValor(tokens[0], math.sin(getValor(tokens[4])))
                                    elif(tokens[2] == "cos"):
                                        seHizo =("hecho")
                                        setValor(tokens[0], math.cos(getValor(tokens[4])))
                                    elif(tokens[2] == "tan"):
                                        seHizo =("hecho")
                                        setValor(tokens[0], math.tan(getValor(tokens[4])))
                                    else:
                                        error =("fuera de rango")
                                else:
                                    error =("La variable ", tokens [4], " no es valida se esperaba un numero")
                            else:
                                error =( "la variable ",tokens[4]," Esta vacia")
                                #print(getValor(tokens[4]))
                        elif(esEntero(tokens[4])or esFlotante(tokens[4])):
                                    if(tokens[2] == "sin"):
                                        seHizo =("hecho")
                                        setValor(tokens[0], math.sin(float(tokens[4])))
                                    elif(tokens[2] == "cos"):
                                        seHizo =("hecho")
                                        setValor(tokens[0], math.cos(float(tokes[4])))
                                    elif(tokens[2] == "tan"):
                                        seHizo =("hecho")
                                        setValor(tokens[0], math.tan(float(tokens[4])))
                                    else:
                                        error =("fuera de rango")
                                
                        else:
                            error =("la variable ",tokens[4]," no esta declarada ")
                            
                        
        if (interrupcion == True):
                sinErrores = False
                
                print("---Error en el analsis sintactico----")
                print(" hay un error en la linea : \n", cont, renglon[0:-1])
                print("Descripcion ", error ,"\n")
                
                
        interrupcion = False
        cont = cont + 1
        '''
        print(tokens)
        if (error != "" ):
            print("Descripcion ", error ,"\n")
        print(seHizo)
        '''

        error = ""
        seHizo = ""
        #else:
        #    print("falta programar")
    algo = open("algo.txt", "w")
    algo.write(" -----Tabla de Variables ----- \n")
    
    for e in tablaVar:
        algo.write(str(e.nombre + " "  + e.tipo + " "+ str(e.valor) + " " + str(e.direccion + "\n") ))
        print (e.nombre , e.tipo, e.valor, e.direccion )
                 #funcionRead(tokens)
    algo.close()
    '''
                    
                            
                                
                            
                        
                                
                                    
                                
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
                        
                        if (len(tokens) == 6 and getTipo(tokens[0]) ==  "char" or getTipo(tokens[0]) ==  "string"): #and len(tokens[3]) == 3 ): Es de la forma a = "cadena de cualquier extencion" ;                            
                            
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
                        
                            elif (tokes ):
                            setValor(tokens[0], tokens[3])'''
                        
                        


                
               
    
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
