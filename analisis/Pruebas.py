#tokens =['for', '(', 'a', ')', '{']
#tokens =['print','(','hola','mundo',')',';']
#tokens =['read','(','a',')', ';']
#tokens = ['end', ';']
#tokens = ['var','int','edad',';']

palabrasReservadas = ['print', 'println', 'for', 'end'  'read', 'var', 'int', 'float', 'string', 'char']
tiposDatos=['int', 'float', 'string' 'char']

alfabetoNA= "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0+×÷=/_€£()@#$%^&*¿¡!-':;,?.`~\|<>{[°•○●□■♤♡♡♧☆▪︎¤《》¥₩]}123456789"

objeto = open("codigoSC.txt", "r")
linea = ""
tokens = []



def evaluardeclaracion(cad):    
    if (tokens[1] in tiposDatos and not tokens[2][0] in alfabetoNA and not tokens[2] in palabrasReservadas and tokens [3]==';'):
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
    if (tokens[1] == '('):
        if(tokens[-2]== ')'):
            bander = True
            #print('Esta bien')
    else:
        bander = False 
    return(bander)

def evaluarread(cad):
    if (tokens[1] == '(' and tokens[-2]== ')'):
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
   
#------------------------------------

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

cont =1
for linea in objeto:
    
    #print(linea)
    #cad2.append(cad)
    tokens =  linea.split()
    #print(tokens)
    if not (tokens[0] == "for"):
        #evaluarCodigo(tokens)
        if (evaluarCodigo(tokens) == False):            
            print("error en la linea" , cont)
    cont = cont + 1



