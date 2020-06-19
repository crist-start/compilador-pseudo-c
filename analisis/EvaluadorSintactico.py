def evaluadorSintactico():

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

    def esId(cad):
        if cad[0] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_":
            return True
        else:
            return False
    # ------- Aqui termina el manejo de los tokens    -------------    


    #--------    aqui empieza la validacion del codigo       --------------

    palabrasReservadas = ['print', 'println', 'for', 'end'  'read', 'var', 'int', 'float', 'string', 'char' , 'sin', 'cos','tan']

    tiposDatos=['int', 'float', 'string','char']

    alfabetoNA= "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0+×÷=/_€£()@#$%^&*¿¡!-':;,?.`~\|<>{[°•○●□■♤♡♡♧☆▪︎¤《》¥₩]}123456789"

    objeto = open("codigoSC.txt", "r")
    linea = ""
    funcionesAridmeticas = ['sin', 'cos', 'tan']
    tokens = []



    def evaluardeclaracion(cad):
        bander = False
        if (tokens[1] in tiposDatos):
            if (not tokens[2][0] in alfabetoNA and not tokens[2] in palabrasReservadas and tokens [3]==';' ):
                #print ("esta bien")
                bander = True
        else:
            bander = False 
        return(bander)
        
    def evaluarfor(cad):
        bander = False
        if (len(tokens)== 8 and tokens[1]== '(' and tokens[3]== '=' and tokens[5] == ';' and tokens[-1] == ')'
            and (esId(tokens[2]) or esEntero(tokens[2]))and (esId(tokens[4]) or esEntero(tokens[4]))and (esId(tokens[6]) or esEntero(tokens[6]))):
            #print ('esta bien el for')
            bander = True
        else:
            bander = False
        #print(bander)
        return(bander)

    def evaluarprint(cad):
        bander = False
        if (tokens[1] == '(' and tokens[-2]== ')' ):
            if (tokens[2]== '"'and not ',' in renglon and tokens[-3]=='"' and len(tokens)==7):
                bander = True
            elif (len(tokens) == 5 and tokens[2] and esId(tokens[2]) == True):
                bander = True
            elif (tokens[2]== '"'and esId(tokens[-3]) and tokens[-4] == ',' and tokens[-5]== '"'):
                bander = True
            elif (tokens[-3]== '"'and esId(tokens[2]) and tokens[3] == ',' and tokens[4]== '"'):
                bander = True
            else:
                bandera = False
        else:
            bander = False 
        return(bander)

    def evaluarread(cad):
        bander = False
        if (tokens[1] == '(' and tokens[-2]== ')' and len(tokens)==5 and tokens[-3] == tokens[2]):
             bander = True
            #print('Esta bien')
        else:
            bander = False 
        return(bander)

    def evaluarend(cad):
        bander = False
        if (tokens[1] == ';'):
            bander = True 
            #print('Esta bien')
        else:
            bander = False 
        return(bander)

    def esFor(cad):
        hayFor = False
        if (tokens[0] == 'for'):
            #if(evauarfor(tokens) == True
                hayFor = True
                #dentroFor(tokens)
                #dentroFor = str(dentroFore(tokens))
                
        else:
            hayFor = False
            #print("el for esta " + str(dentroFor))
        return hayFor

    def evaluarAsignacion(cad):
        bander = False

        if (len(tokens)== 4 ):
            if(esEntero(tokens[2]) or esFlotante(tokens[2]) or esId(tokens[2])): #a = 10.1 ; o a = 10 ; o a = edad ;
                #print("dentro")
                bander = True          
            else:        
                bander = False
                
        elif (esOperador(tokens[3]) and not len(tokens) == 5 and not (tokens[2] in funcionesAridmeticas)): # a = a * b / 10 * var
             #print("entro")
             i=2
             while(i<len(tokens) and not tokens[i-1] == ';' ):
                #print("entro")
                 if(esEntero(tokens[i]) or esFlotante(tokens[i]) or esId(tokens[i])):
                     if (tokens[i+1] == ';'):
                         #print("entro")
                         bander= True
                     i=i+2
                     
                 else:
                     bander = False
        elif(len(tokens)== 7 and tokens[2] in funcionesAridmeticas ): # a = cos ( 10 ) o a = cos ( c )
            if (tokens[3]== '(' and tokens[5] == ')' and (esEntero(tokens[4]) or esFlotante(tokens[4]) or esId(tokens[4]))):
                #print("Entro")
                bander= True
            else:
                bander = False
                
        elif(tokens[2]== '"' and tokens[-2]== '"' ):
            j=3
            if( len(tokens) == 6  and tokens[3]!= '"'):
                bander = True
            
            elif not(len(tokens)== 6):
                print ("entro")
                for j in range (len(tokens)-3):
                    
                    if not(tokens[j] == '"' ):
                        bander = True
        
        else:       
                bander = False
                
        return(bander)


    def evaluarCodigo(codigosc):
        sinErrores = False
        dentroFor = False
                
        if (tokens[-1] == ';'):

            if (tokens[0] == 'print' or tokens[0]== 'println'):
                if (evaluarprint(tokens) == True):
                    sinErrores = True
                    #print ("esta bien el print")
                else:
                    sinErrores = False
                    #print ("esta mal el print")
                  
            if (tokens[0] == 'read'):
                if (evaluarread(tokens) == True ):
                    sinErrores = True
                    #print("esta bien el read")
                else:
                    sinErrores = False
                    #print ("hubo error en el read")
        
            if (tokens[0] == 'end'):
                if (evaluarend(tokens) == True ):
                    sinErrores = True
                    #print("esta bien el end")
                else:
                    sinErrores = False
                    #print ("hubo error en el end")
        
            if (tokens[0] == 'var'):
                if (evaluardeclaracion(tokens) == True ):
                    sinErrores = True
                    #print("esta bien la declaracion")
                else:
                    sinErrores = False
                    #print ("hubo error la declaracion")
            if (len(tokens)== 3 and (tokens[0] == 'sin' or tokens[0] == 'cos' or tokens[0] == 'tan')):
                if(esId(tokens[0]) == True or esEntero(tokens[0]) == True or esFlotante(tokens[0]) == True):
                    sinErrores = True
                    #print("esta bien la declaracion")
                else:
                    sinErrores = False
            
                    
            if(tokens[1] == "=" and esId(tokens[0])):
                 if (evaluarAsignacion(tokens) == True):
                    sinErrores = True
                    #print("esta bien la asignacion")
                 else:
                    #print("holaguapo")
                    sinErrores = False
                    #print ("hubo error la asignacion ")
                    
        elif (len(tokens)== 1):
            #print("holaguapo")
            if (tokens[0] == '{' or tokens[0] == '}'):
                if (dentroDelFor == True):
                    sinErrores = True
                    #print("esta bien la asignacion")
                else:
                    sinErrores = False
            else:                
                sinErrores = False
                #print ("hubo error la asignacion ")
                

        else:
            #print("Error")
            sinErrores = False
        
            
              
        return sinErrores
    #--------    aqui termina la validacion del codigo       --------------


    # programa principal
    tablaVar = []
    renglon = ""
    interrupcion = False
    arch = open("codigoSC.txt", "r")
    programa = arch.readlines()
    dentroDelFor = False
    contlineafor = 0
    contadorfors = 0
    sinErrores = True
    #print(programa)
    cont =1
    
    for renglon in programa:
        #if (interrupcion == False):
        #print(renglon[:])               # ------------- Quita el  # de comentario de esta linea para ver la cadena
        if(renglon!="end;"):        
            tokens = tokeniza(renglon)
            #print(tokens)                     #  ------------- Quita el  # de comentario de esta linea para ver la cadena en tokes
            dentroDelFor == False
            

            
            if interrupcion == False:
                if(not tokens[0] == 'for' and dentroDelFor == False):
                    #print("hola guapo")
                    if (evaluarCodigo(tokens) == False):
                        interrupcion = True
                        print("error en la linea" , cont)
                    cont = cont + 1
                    #print("\n")
                    
                elif (esFor(tokens) == True):
                    if(evaluarfor(tokens) == True):
                        
                        dentroDelFor = True
                        contlineafor = 100
                        contadorfors = contadorfors + 1
                        #print("dentro for = ")
                        #print(dentroDelFor)

                    else:
                        interrupcion = True
                        print(" error en la linea" , cont)
                    cont = cont + 1
                    #print("\n")
                
                elif( not tokens[0] == 'for' and dentroDelFor == True ):
                    #print("entro")
                    if (evaluarCodigo(tokens) == False):
                        interrupcion = True
                        print(" error en la linea" , cont)
                    cont = cont + 1
                    
                    #print("\n")
                    
                    if ( '''len(tokens)== 1''' and tokens[0] == '}' and dentroDelFor == True):
                        dentroDelFor = False
                        #print("se cerro el for")
                        
                    if(tokens[0] == 'end' and dentroDelFor == True and evaluarCodigo(tokens) == True):
                        interrupcion = True
                        print(" error en la linea no se encontro la llave '}' de cierre del for " , cont)
                        print("\n")
                        
                    if (tokens[0] == '{' and evaluarCodigo(tokens) == True and not contlineafor == 101 ):                        
                        interrupcion = True
                        print(" error en la linea ",cont," no se encontro la llave '{' de spues del for ")
                        print("\n")
                
                else:
                    interrupcion = True
                    print(" error no es una linea valida")
            contlineafor = contlineafor + 1
            if (interrupcion == True):
                sinErrores = False
                print(renglon[0:-1])
            interrupcion = False
            
    pass
    return(sinErrores)

#evaluadorSintactico()            #   ------------- Quita el  # de comentario de esta linea para ejecutar el codigo


