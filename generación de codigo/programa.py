def Instruccion(ins):
	CODIGO = open("Codigo.txt","a")
	CODIGO.write("\n"+cadena)
	CODIGO.close

def RevisarTipo(var):
	if variables[0] == var:
		return variables[1]
	else:
		Error = "La variable {} no se encuentra en la tabla de variables".format(var)
		Registro(Error)
		return None

def DirVar(var): #Obtener la dirección de la variable
	if variables[0]==var:
		return variables[3]
	else:
		Error = "La variable {} no esta en la tabla.".format(var)
		Registro(Error)
		return None

def Registro(cadena):
	REG = open("Registro.txt","a")
	REG.write("\n"+cadena)
	REG.close

def Leer(var):
	cadena = ""
	tipo=RevisarTipo(var)
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
	tipo=RevisarTipo(var)
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
	direccion = DirVar(var)
	cadena = "STA {};".format(direccion)
	Instruccion(cadena)

def AsignarVarVar(var1,var2): #Asignación de la forma b=a
	dirvar2 = DirVar(var2)
	cadena = "LDA {};".format(dirvar2)
	Instruccion(cadena)
	dirvar1 = DirVar(var1)
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
	OP1 = DirVar(Operando1)
	cadena = "LDA {};".format(OP1)
	Instruccion(cadena)
	OP2 = DirVar(Operando2)
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
	

