#----------- manejo de archivos --------- 
programa = []
objeto = open("codigo.txt", "r")
cad = ""
#----------------------------------------
cad2 = []
dic=[]
comentario = []
cadsin= ""
tokens = []

elemento = 0


# ------ codigo para almacenar el texto en una cadena ------------------
print("------ codigo recibido ------------")
for cad in objeto:
    print(cad)
    cad2.append(cad)
#print(cad2)

cad = ""
for ele in cad2:  
    cad += ele
#print(cad)

#------------------------------------------------------------------
#-------- codigo para quitar los comentarios----------------------
while (elemento < len(cad)): # 
#for elemento in range (len(cad)):
    
    if(cad[elemento] == '/' and cad[elemento+1] == '*'):
            #print(elemento)
            while not ( cad[elemento] == '*' and cad[elemento + 1] == '/' ): # ciclo 
                
                comentario.append(cad[elemento])
                #print("dentro")
                #print(cad[elemento])
                elemento  = elemento + 1
                #print(elemento)
            while ( (cad[elemento] == '*' and cad[elemento + 1] == '/') or (cad[elemento] == '/' and cad[elemento-1] == '*' )):
                #print (cad[elemento])
                comentario.append(cad[elemento])
                elemento =elemento+1
    else:
        dic.append(cad[elemento] )
        elemento =elemento+1
#print (dic)        
#print (comentario)

for ele in dic:
    cadsin += ele
    
print("-----codigo sin comentarios ------\n" + cadsin)

#---------- gurdado del codigo sin comentarios en un txt ------------

algo = open("codigoSC.txt", "w")
algo.write(cadsin)
algo.close()

algo = open("comentarios.txt", "w")
algo.write("comentario")
algo.close()
#------------------------------------------
