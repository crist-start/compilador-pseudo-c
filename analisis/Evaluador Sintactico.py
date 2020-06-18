class Variable:
    nombre = ""
    tipo = ""
    valor = ""
    def __init__(self, n, t, v):
        self.nombre = n
        self.tipo = t
        self.valor = v
        


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
    #print(tokens)
    return tokens

def esId(cad):
    if cad[0] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_":
        return True
    else:
        return False
# ------- Aqui termina el manejo de los tokens    -------------    


# ------- Aqui inicia el manejo de la tabla de variables --------

def agregaVar(varNombre, tipoVar):
    tablaVar.append(Variable(varNombre, tipoVar, "0"))
    return None

def setValor(varNombre, valor):    
    for v in tablaVar:
        if (v.nombre == varNombre):
            tipo = getTipo(varNombre)
            if (tipo=="int"):
                
                if (estaEnTabla(valor)):
                    v.valor = int(v.valor)
                elif (esEntero(valor)):
                    v.valor = int(valor)
                else:
                    print("Error no existe en la tabla de variables")
                
            elif (tipo == "string"):
                v.valor = valor
            elif (tipo=="char"):
                v.valor = valor
            elif (tipo=="float"):
                v.valor = float(valor)    
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


# -------    Aqui inicia el manejo de expresiones  --------

def getPrioridadOp(o):
    # DEvuelve la prioridad de un operador**.
    return {'(':1, ')':2, '+': 3, '-': 3, '*': 4, '/':4, '^':5}.get(o)

def infija2Posfija(infija):
    '''Convierte una expresión infija a una posfija, devolviendo una lista.'''
    pila = []
    salida = []
    for e in infija:
        if e == '(':
            pila.append(e)
        elif e == ')':
            while pila[len(pila) - 1 ] != '(':
                salida.append(pila.pop())
            pila.pop()
        elif e in ['+', '-', '*', '/', '^']:
            while (len(pila) != 0) and (getPrioridadOp(e)) <= getPrioridadOp(pila[len(pila)-1]):
                salida.append(pila.pop())
            pila.append(e)
        else:
            salida.append(e)
    while len(pila) != 0:
        salida.append(pila.pop())
    return salida

def evaluarPosfija(expresion_posfija):
    '''Si la posfija tiene valores, recibe la lista Posfija y devuelve el resultado.'''
    pila = []
    for i in expresion_posfija:
        if not(i in ['+', '-', '*', '/']):
            pila.append(float(i))
        else:
            op2 = pila.pop()
            op1 = pila.pop()
            if i == '+':
                pila.append(op1 + op2)
            elif i == '-':
                pila.append(op1 - op2)
            elif i == '*':
                pila.append(op1 * op2)
            elif i == '/':
                pila.append(op1 / op2)
            elif i == '^':
                pila.append(op1 ** op2)
    return pila.pop()

def getValores(expresion):
    nuevaExp = []
    for e in expresion:
        print (e)
        if esId(e): # es una variable y requerimos traer el valor
            nuevaExp.append(getValor(e))
        elif (esOperador(e)):
            nuevaExp.append(e)              
        else: # Es un número, o un operador
            if "." in e: # tiene un punto y por lo tanto es un flotante
                nuevaExp.append(float(e))
            else:  # es un entero
                nuevaExp.append(int(e))
    return nuevaExp

# -------    Aqui termina el manejo de expresiones  --------


# -------    Aqui empiezan funciones propias del interprete  --------
def funcionPrint(tokens):
    if (tokens[0]=="print"):  # Funcion print
        f=0
    else:  # funcion println
        f=1
    if(esId(tokens[2])): #Lo que sigue del parentesis es una variable
       valor = getValor(tokens[2]) # recuperamos el valor de la variable
       if (f==0):  # es un print sin salto
           pass
           #print(valor, end="")        
       else:
            print(valor)
    elif (tokens[2]=='"'): # lo que sigue del parentesis son comillas
        #print ("cadena de cualquier longitud")        
        if (f==0):
            pass
            #print (tokens[3], end="")
        else:
            print (tokens[3])
    pass
       
def funcionRead(tokens):    
    if (estaEnTabla(tokens[0])): # la variable si existe
        valor = input("") # lee el valor del teclado
        setValor(tokens[0], valor)
    else:
        print("la variable", tokens[0], " no se encontró")
    pass

def cargaPrograma(tokens):
    a = tokens[3]    
    b= ""
    for i in a:
        if (ord(i)!=32):  #quita los espacios del nombre del archivo
            b=b+i    
    arch = open(b, "r")    
    programa = arch.readlines()
    arch.close()
    for renglon in programa:
        tokens = tokeniza(renglon)        
        if (tokens[0] =="var"):  # Es una declaracion de variable
            agregaVar(tokens[2], tokens[1])
        elif (esId(tokens[0])): # El primer token es un ID
            if (tokens[0]=="load"):
                cargaPrograma(tokens)
            elif (tokens[1]=="="):        
                if (len(tokens)==4): # Es de la forma "ID = valor;"            
                    setValor(tokens[0], tokens[2])
                elif (tokens[2]=="read"):
                    funcionRead(tokens)
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
    pass
        
    

# -------    Aqui terminan funciones propias del interprete  --------

#--------    aqui empieza la validacion del codigo       --------------

palabrasReservadas = ['print', 'println', 'for', 'end'  'read', 'var', 'int', 'float', 'string', 'char']
tiposDatos=['int', 'float', 'string' 'char']

alfabetoNA= "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0+×÷=/_€£()@#$%^&*¿¡!-':;,?.`~\|<>{[°•○●□■♤♡♡♧☆▪︎¤《》¥₩]}123456789"

objeto = open("codigoSC.txt", "r")
linea = ""
tokens = []



def evaluardeclaracion(cad):    
    if (tokens[1] in tiposDatos and not tokens[2][0] in alfabetoNA and not tokens[2] in palabrasReservadas and tokens [3]==';' and estaEnTabla(tokens [2])):
        #print ("esta bien")
        bander = True
    else:
        bander = False 
    return(bander)
    
def evaluarfor(cad):
    if (tokens[1]== '(' and tokens[-2] == ')'):
        #print ('esta bien')
        bander = True
    else:
        bander = False 
    return(bander)

def evaluarprint(cad):
    if (tokens[1] == '(' and tokens[-2]== ')' ):
        if (tokens[2]== '"'and not ',' in renglon and tokens[-3]=='"' and len(tokens)==7):
            bander = True
        elif (len(tokens) == 5 and tokens[2] and estaEnTabla(tokens[2]) == True):
            bander = True
        elif (tokens[2]== '"'and estaEnTabla(tokens[-3]) and tokens[-4] == ',' and tokens[-5]== '"'):
            bander = True
        elif (tokens[-3]== '"'and estaEnTabla(tokens[2]) and tokens[3] == ',' and tokens[4]== '"'):
            bander = True
        else:
            bandera = False
    else:
        bander = False 
    return(bander)

def evaluarread(cad):
    if (tokens[1] == '(' and tokens[-2]== ')' and len(tokens)==5 and tokens[-3] == tokens[2]):
         bander = True
        #print('Esta bien')
    else:
        bander = False 
    return(bander)

def evaluarend(cad):
    if (tokens[1] == ';'):
        bander = True 
        #print('Esta bien')
    else:
        bander = False 
    return(bander)

def dentroFore(cad):
    if (evaluarfor(tokens)== True):         
        print("esta bien el for")
        dentroFor = True
    else:
        dentroFor = False
        print("no se declaro bien el for")      
    return(dentroFor)

def evaluarAsignacion(cad):

    if(esEntero(tokens[2]) or esFlotante(tokens[2])): #a = 10.1 ; o a = 10 ;
        if (len(tokens)== 4 ):
            print("dentro")
            bander = True
        else:
            bander = False
                
    elif (estaEnTabla(tokens[2]) == True ):# a = b ;
        print("dentro")
        if not( esEntero(tokens[2]) and esFlotante(tokens[2])):
            bander = True
        else:        
            bander = False
    
    else:        
            bander = False


    return(bander)

    
        
'''
    if (len(tokens)== 4 and estaEnTabala(tokens[2]) == True and tokens[3]== ';' ):# a = b ;
    if (len(tokens)== 4 and tokens[2] == '"' and tokens[-2] == '"' and esEntero(tokens[2]) or esFlotante(tokens[2])): #a = 10.1 ; o a = 10 ;
    if (esEntero(tokens[2]) or esFlotante(tokens[2]) or estaEnTabla(tokens[2])== True):
        if (esOperdor(tokens[3]) == True):
'''            

def evaluarCodigo(codigosc):
    sinErrores = True
    dentroFor = False
            
    if (tokens[-1] == ';'):

        if (tokens[0] == 'print' or tokens[0]== 'println'):
            if (evaluarprint(tokens) == True):
                sinErrores = True
                print ("esta bien el print")
            else:
                sinErrores = False
                print ("esta mal el print")
              
        if (tokens[0] == 'read'):
            if (evaluarread(tokens) == True ):
                sinErrores = True
                print("esta bien el read")
            else:
                sinErrores = False
                print ("hubo error en el read")
    
        if (tokens[0] == 'end'):
            if (evaluarend(tokens) == True ):
                sinErrores = True
                print("esta bien el end")
            else:
                sinErrores = False
                print ("hubo error en el end")
    
        if (tokens[0] == 'var'):
            if (evaluardeclaracion(tokens) == True ):
                sinErrores = True
                print("esta bien la declaracion")
            else:
                sinErrores = False
                print ("hubo error la declaracion")
                
        if(tokens[1] == "=" and estaEnTabla(tokens[0])):
             if (evaluarAsignacion(tokens) == True):
                sinErrores = True
                print("esta bien la asignacion")
             else:
                
                sinErrores = False
                print ("hubo error la asignacion ")
                
            
    elif (tokens[-1] == '{' or tokens[0] == '}' or tokens[0] == 'end'):
        if (tokens[0] == 'for'):
            hayFor = True
            #dentroFor(tokens)
            dentroFor = str(dentroFore(tokens))
            
        else:
            hayFor = False
        #print("el for esta " + str(dentroFor))
            
        if(tokens[0]== '}' and dentroFor == "True"):
            dentroFor = "False"
            print("esta bien el for cola")
        #print("el for" + str(dentroFor))
        if (tokens[0]== '}' and hayFor == False and dentroFor == "False"):
            print("Error no se encontro bloque de repeticion")
        #print("el for" + str(dentroFor))
        if(tokens[0]== 'end' and dentroFor == "True"):
            print("Error no se encontro } de cierre")

    else:
        #print("Error")
        sinErrores = False
    
        
          
    return sinErrores
#--------    aqui termina la validacion del codigo       --------------

# programa principal
tablaVar = []
renglon = ""
arch = open("codigoSC.txt", "r")
programa = arch.readlines()
#print(programa)
cont =1
for renglon in programa:
    
        print(renglon[0:-1])
    #while (renglon!="end;"):        
        tokens = tokeniza(renglon)
        print(tokens)
        

        
        if (tokens[0] =="var"):  # Es una declaracion de variable
            agregaVar(tokens[2], tokens[1])
        elif (esId(tokens[0])): # El primer token es un ID
            if (tokens[1]=="="):        
                if (len(tokens)==4): # Es de la forma "ID = valor;"
                    #if not (esId(tokens[2])):

                        setValor(tokens[0], tokens[2])

                '''elif (tokens[2]=="read"):
                    funcionRead(tokens)
                else: # Es id = exp  ej. c = a*b+d;                
                    expresion = tokens[2:-1]                
                    posfija = infija2Posfija(expresion)               
                    posfijaV = getValores(posfija)               
                    resultado = evaluarPosfija(posfijaV)                
                    setValor(tokens[0], resultado)
            elif (tokens[0]=="print") or (tokens[0]=="println"):
                funcionPrint(tokens)
            elif (len(tokens)==2):  # Es solo el identificador
                #print(getValor(tokens[0]))
                print ("")'''
                
        if (evaluarCodigo(tokens) == False):            
                print("error en la linea" , cont)
        cont = cont + 1
        print("\n")
pass
'''
        #print(linea)
        #cad2.append(cad)
        tokens =  linea.split()
        #print(tokens)
        #if not (tokens[0] == "for"):
            #evaluarCodigo(tokens)
        if (evaluarCodigo(tokens) == False):            
                print("error en la linea" , cont)
        cont = cont + 1
pass

cargaPrograma(tokens)
tablaVar = []
renglon = ""

while (renglon!="end;"):
    renglon=input("##")    
    tokens = tokeniza(renglon)
    print(tokens)
    if (tokens[0] =="var"):  # Es una declaracion de variable
        agregaVar(tokens[2], tokens[1])
    elif (esId(tokens[0])): # El primer token es un ID
        if (tokens[0]=="load"):
            cargaPrograma(tokens)
        elif (tokens[1]=="="):        
            if (len(tokens)==4): # Es de la forma "ID = valor;"            
                setValor(tokens[0], tokens[2])
            elif (tokens[2]=="read"):
                funcionRead(tokens)
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

