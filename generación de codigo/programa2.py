def ACompilador(instruccion):
	Comp = open("Codigo.txt","a")
	Comp.write("\n"+instruccion)
	Comp.close()

def Registro(cadena):
	Reg = open("Registro.txt","a")
	Reg.write("\n"+cadena)
	Reg.close()

def Leer(token):
	cadena = ""
	var = token[2]
	tipo = var.tipo
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

def ImprimirCadena(texto):
	cadena = "IN9 {};".format(texto)
	ACompilador(cadena)

def ImprimirVariable(variable):
	cadena = ""
	tipo = variable.tipo
	if tipo == "int":
		cadena = "IN5 {};".format(variable)
	elif tipo == "float":
		cadena = "IN6 {};".format(variable)
	elif tipo == "char":
		cadena = "IN7 {};".format(variable)
	elif tipo == "string":
		cadena = "IN8 {};".format(variable)
	else:
		Error = "No se pudo manejar(imprimir) el tipo de dato de {}.".format(variable)
		Registro(Error)
	ACompilador(cadena)

def AsignarValVar(variable,valor):
	cadena = "LDV {};".format(valor)
	ACompilador(cadena)
	cadena = "STA {};".format(variable.direccion)
	ACompilador(cadena)

def AsignarVarVar(var1,var2):
	cadena = "LDA {};".format(var2.direccion)
	ACompilador(cadena)
	cadena = "STA {};".format(var1.direccion)
	ACompilador(cadena)

def AsignarTrigon(token):
	if token[4][0] in "0123456789":
		dir = token[4]
	else:
		dir = token[4].direccion
	if token[2] == "sin":
		cadena = "SIN {};".format(dir)
	elif token[2] == "cos":
		cadena = "COS {};".format(dir)
	elif token[2] == "tan":
		cadena = "TAN {};".format(dir)
	else:
		Error = "La funcion trigonometrica {} no es procesable.".format(token[2])
		Registro(Error)
		cadena "LDA {};".format(dir)
	ACompilador(cadena)
	cadena = "STA {};".format(token[0].direccion)

def Aritmetica(token):
	OP1 = token[2]
	OP2 = token[4]
	cadena = "LDA {};".format(OP1.direccion)
	ACompilador(cadena)
	if token[3] == "+":
		cadena = "ADD {};".format(OP2.direccion)
	elif token[3] == "-":
		cadena = "SUB {};".format(OP2.direccion)
	elif token[3] == "*":
		cadena = "MUL {};".format(OP2.direccion)
	elif token[3] == "/":
		cadena = "DIV {};".format(OP2.direccion)
	else:
		Error = "El operando {} no se pudo utilizar para operar {} y {}.".format(token[3],OP1,OP2)
		Registro(Error)
		cadena = ""
	ACompilador(cadena)
	Resultado = token[0]
	cadena = "STA {};".format(Resultado.direccion)
	ACompilador(cadena)



def ManejoFor(token):
	pass

def EvaluarInstruccion(token):
	if token[0] == "print":
		if token[2][0] != '"':
			ImprimirVariable(token[2])
		else:
			ImprimirCadena(token[2])
	elif token[0] == "read":
		Leer(token)
	elif token[1] == "=":
		if (("sin" in token[2]) or ("cos" in token[2]) or ("tan" in token[2])):
			AsignarTrigon(token)
		elif token[3] == ";":
			if token[2][0] in "0123456789":
				AsignarValVar(token[0],token[2])
			else:
				AsignarVarVar(token[0],token[2])
		else:
			Aritmetica(token)
	elif #CondicionFor:
		pass
	else:
		pass

def GenerarCodigo(CodigoIntermedio):
	for renglon in range(0,len(CodigoIntermedio)):
		if "condicionfor":
			pass #funcionfor
		else:
			EvaluarInstruccion(CodigoIntermedio[renglon])
			#Funcion pendiente para imprimir token (instr = CodigoIntermedio[renglon])