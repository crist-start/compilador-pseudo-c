def limpiar():
	pass #Pendiente funcion de limpiar archivos a usar

def ACompilador(instruccion):
	Comp = open("Codigo.txt","a")
	Comp.write("\n"+instruccion)
	Comp.close()

def Registro(cadena):
	Reg = open("Registro.txt","a")
	Reg.write("\n"+cadena)
	Reg.close()

def TokenACadena(token):
	cadena = str(token)
	cadena = cadena.replace("[","")
	cadena = cadena.replace("]","")
	cadena = cadena.replace("'","")
	cadena = cadena.replace(",","")
	cadena = cadena.replace(" ","")
	cadena = cadena.replace("\\n","")
	cadena = cadena.replace("\\t","")
	return cadena

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
	cadena = "STA {};".format(variable.dirM)
	ACompilador(cadena)

def AsignarVarVar(var1,var2):
	cadena = "LDA {};".format(var2.dirM)
	ACompilador(cadena)
	cadena = "STA {};".format(var1.dirM)
	ACompilador(cadena)

def AsignarTrigon(token):
	if token[4][0] in "0123456789":
		dir = token[4]
	else:
		dir = token[4].dirM
	if token[2] == "sin":
		cadena = "SIN {};".format(dir)
	elif token[2] == "cos":
		cadena = "COS {};".format(dir)
	elif token[2] == "tan":
		cadena = "TAN {};".format(dir)
	else:
		Error = "La funcion trigonometrica {} no es procesable.".format(token[2])
		Registro(Error)
		cadena = "LDA {};".format(dir)
	ACompilador(cadena)
	cadena = "STA {};".format(token[0].dirM)

def Aritmetica(token):
	OP1 = token[2]
	OP2 = token[4]
	cadena = "LDA {};".format(OP1.dirM)
	ACompilador(cadena)
	if token[3] == "+":
		cadena = "ADD {};".format(OP2.dirM)
	elif token[3] == "-":
		cadena = "SUB {};".format(OP2.dirM)
	elif token[3] == "*":
		cadena = "MUL {};".format(OP2.dirM)
	elif token[3] == "/":
		cadena = "DIV {};".format(OP2.dirM)
	else:
		Error = "El operando {} no se pudo utilizar para operar {} y {}.".format(token[3],OP1,OP2)
		Registro(Error)
		cadena = ""
	ACompilador(cadena)
	Resultado = token[0]
	cadena = "STA {};".format(Resultado.dirM)
	ACompilador(cadena)

def ManejoFor(token):
	var = token[0][0]
	inicio = int(token[0][1])
	fin = int(token[0][2])
	cadena = "LDV {};".format(inicio)
	ACompilador(cadena)
	cadena = "STA {};".format(var.dirM)
	ACompilador(cadena)
	cadena = "#2 LDV {};".format(fin)
	ACompilador(cadena)
	cadena = "SUB {};".format(var.dirM)
	ACompilador(cadena)
	cadena = "JZ #1;"
	ACompilador(cadena)
	for renglon in range(1,len(token)):
		EvaluarInstruccion(token[renglon])
	cadena = "LDA {};".format(var.dirM)
	ACompilador(cadena)
	cadena = "ADD 1;"
	ACompilador(cadena)
	cadena = "STA {};".format(var.dirM)
	ACompilador(cadena)
	cadena = "JMP #2;"
	ACompilador(cadena)
	cadena = "#1"
	ACompilador(cadena)

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
	else:
		Error = "El la orden {} del token {} no se pudo manejar.".format(token[0],TokenACadena(token))
		Registro(Error)
		pass

def GenerarCodigo(CodigoIntermedio):
	tokensfor=[]
	dentroFor = False
	for renglon in range(0,len(CodigoIntermedio)):
		if dentroFor == True:
			if CodigoIntermedio[renglon][0] == "{":
				pass
			elif CodigoIntermedio[renglon][0] == "}":
				dentroFor = False
				ManejoFor(tokensfor)
				pass
			elif ((CodigoIntermedio[renglon][0] == "\t") or (CodigoIntermedio[renglon][0] == "\\t")):
				temp = CodigoIntermedio[renglon][1:]
				tokensfor.append(temp)
			else:
				Error = "El token {} no se pudo manejar".format(TokenACadena(CodigoIntermedio[renglon]))
				Registro(Error)
		elif dentroFor == False:
			if CodigoIntermedio[renglon][0] == "for":
				t = CodigoIntermedio[renglon]
				temp = [t[renglon][2],t[renglon][4],t[renglon][6]]
				tokensfor.append(temp)
			else:
				EvaluarInstruccion(CodigoIntermedio[renglon])
				print("{} evaluada".format(TokenACadena(CodigoIntermedio[renglon])))
	cadena = "END;"
	ACompilador(cadena)
