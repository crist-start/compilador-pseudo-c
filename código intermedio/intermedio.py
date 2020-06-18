import separaPrint as sp
import postfija as pf

def esVariable(a):
    return a in ['x','y','z']

def intermedio(a=[]):
    intermedio=[];
    for i in a:
        if i[0]=='print' or i[0]=='println':
            prints=sp.separaPrint(i)
            intermedio.extend(prints)
        elif esVariable(i[0]):
            if i[3]==';' or i[5]==';' or i[6]==';':
                intermedio.append(i)
            else:
                print('a postfija')
        else:
            intermedio.append(i)
    return intermedio;

a=[['println','(','"dato"',',','"dato2"',',','"dato3"',')',';']
   ,['println','(','"esto es una prueba"',')',';']
   ,['x','=','2','+','3',';']
   ,['y','=','sin','(','x',')',';']
   ,['z','=','x','+','y','+','5',';']
   ,['t','=','2',';']]

s=intermedio(a)

for i in s:
    print (i)
