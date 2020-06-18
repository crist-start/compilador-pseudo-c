import separaPrint as sp
import postfija as pf

variables=["x","y","a","b","c","d","e",'x1','x2','y1','y2','z','5']

def intermedio(a=[]):
    intermedio=[];
    for i in a:
        if i[0]=='print' or i[0]=='println':
            prints=sp.separaPrint(i)
            intermedio.extend(prints)
        elif i[0] in variables and i[1]=='=':
            if i[3]==';' or i[5]==';' or i[6]==';':
                intermedio.append(i)
            else:
                print(i[2:-1])
                postfija=pf.convertirInfijaAPostfija(i[2:-1])
                inter=pf.intermedio(postfija,variables)
                inter.pop(-2)
                inter[-1][0]=i[0]
                for j in inter:
                    if j[0]=='var':
                        print()
                intermedio.extend(inter)
        else:
            intermedio.append(i)
    return intermedio;

a=[['print','(','"esto es una prueba"',')',';']
   ,['println','(','"dato"',',','"dato2"',',','"dato3"',')',';']
   ,['println','(','"esto es una prueba"',')',';']
   ,['x','=','2','+','3',';']
   ,['y','=','sin','(','x',')',';']
   ,['z','=','x','+','y','+','5',';']
   ,['t','=','2',';']]

s=intermedio(a)


interm=open('intermedio.cpp','w');
for i in s:
    print(i)
    for j in i:
        interm.write(j)
    interm.write('\n')

interm.close()
