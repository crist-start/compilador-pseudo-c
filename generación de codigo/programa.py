def Instruccion(ins): #Limpiar en caso de error
	COMPILADOR = open("Codigo.txt","a")
	COMPILADOR.write("\n"+ins)
	COMPILADOR.close

def Registro(cadena): 
	REG = open("Registro.txt","a")
	REG.write("\n"+cadena)
	REG.close

def Leer(var):
	cadena = ""
	#tipo=RevisarTipo(var)
	tipo=var.tipo
	if tipo == "int":
		cadena = "IN1 {};".format(var)
		Instruccion(cadena)
	elif tipo == "float":
		cadena = "IN2 {};".format(var)
		Instruccion(cadena)
	elif tipo == "char":
		cadena = "IN3 {};".format(var)
		Instruccion(cadena)
	elif tipo == "string":
		cadena = "IN4 {};".format(var)
		Instruccion(cadena)
	else:
		Error = "No se pudo manejar(leer) el tipo de dato de {}.".format(var)
		Registro(Error)

def ImprimirCadena(cadena):
	cadena = "IN9 {};".format(cadena)
	Instruccion(cadena)

def ImprimirVariable(var):
	cadena = ""
	#tipo=RevisarTipo(var)
	tipo = var.tipo
	if tipo == "int":
		cadena = "IN5 {};".format(var)
		Instruccion(cadena)
	elif tipo == "float":
		cadena = "IN6 {};".format(var)
		Instruccion(cadena)
	elif tipo == "char":
		cadena = "IN7 {};".format(var)
		Instruccion(cadena)
	elif tipo == "string":
		cadena = "IN8 {};".format(var)
		Instruccion(cadena)
	else:
		Error = "No se pudo manejar(imprimir) el tipo de dato de {}.".format(var)
		Registro(Error)

def AsignarValVar(var,value): #Asignación de la forma a=10
	cadena = "LDV {};".format(value)
	Instruccion(cadena)
	#direccion = DirVar(var)
	direccion = var.direccion
	cadena = "STA {};".format(direccion)
	Instruccion(cadena)

def AsignarVarVar(var1,var2): #Asignación de la forma b=a
	#dirvar2 = DirVar(var2)
	dirvar2 = var2.direccion
	cadena = "LDA {};".format(dirvar2)
	Instruccion(cadena)
	#dirvar1 = DirVar(var1)
	dirvar1 = var1.direccion
	cadena = "STA {};".format(dirvar1)
	Instruccion(cadena)

def Operacion(cadena):
	temp = list(cadena)
	pos = 0
	cad = ""
	for i in temp:
		if temp[i] == "=":
			Resultado = cad
			cad = ""
		elif temp[i] in "+-*/":
			Operador = temp[i]
			Operando1 = cad
			cad = ""
		elif temp[i] == ";":
			Operando2 = cad
			cad = ""
		else:
			cad = cad + temp[i]
	#OP1 = DirVar(Operando1)
	OP1 = Operando1.direccion
	cadena = "LDA {};".format(OP1)
	Instruccion(cadena)
	#OP2 = DirVar(Operando2)
	OP2 = Operando2.direccion
	if Operador == "+":
		cadena = "ADD {};".format(OP2)
	elif Operador == "-":
		cadena = "SUB {};".format(OP2)
	elif Operador == "*":
		cadena = "MUL {};".format(OP2)
	elif Operador == "/":
		cadena = "DIV {};".format(OP2)
	else:
		Error = "El operando {} no se pudo utilizar para operar {} y {}.".format(Operador,Operando1,Operando2)
		Registro(Error)
		cadena = ""
	Instruccion(cadena)
	#TipoOp1 = RevisarTipo(Operando1)
	TipoOp1 = Operando1.tipo
	#TipoOp2 = RevisarTipo(Operando2)
	TipoOp2 = Operando2.tipo
	if ((TipoOp1 == "int") and (TipoOp2 == "int") and (Operador in "+-*")):
		TipoRes = "int"
	else:
		TipoRes = "float"
	DirLibre = (variables[-1][-1])+1
	#variables(Resultado,TipoRes,0,DirLibre)
	Resultado.tipo = TipoRes
	#Result = DirVar(Resultado)
	Result = Resultado.direccion
	cadena = "STA {};".format(Result)

def ManejoFor(cadena): #Tienes que recibir cadena desde for hasta la llave de cierre
	texto = cadena.splitlines()
	texto.remove("")
	condicion = texto[0][4:-1]
	#inicio
	#fin
	bloque = texto[2:-1]
	for i in range(0,len(bloque)):
		bloque[i] = bloque[i].replace("\t","")
	cantidad = bloque.count("")
	for i in range(0,cantidad):
		bloque.remove("")
	for i in range(0,len(bloque)):
		EvaluarInstruccion(bloque[i])

def EvaluarInstruccion(inst):
	pass

def LeerCodigo(archivo):
	codigo = open(archivo,"r")
	temp = codigo.read()
	codigo.close()
	codigo = temp.splitlines()
	for renglon in range(0,len(codigo)):

def GenerarCodigo(CodigoIntermedio2x2): #Esta funcion se va a ir a main
	pass

#Este codigo queda obsoleto con los ajustes a el manejo de variables

