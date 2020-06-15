'''aqui colocaran la ruta para poder importar sus archivos'''
import sys
sys.path.append('prueba/')
sys.path.append('código intermedio/')
sys.path.append('generación de codigo/')

'''aqui importaran sus archivos para usar sus funciones'''
#ejemplo
import separaPrint as p
import prueba2 as t

'''aqui usaran las funciones que importaron'''
#ejemplo

token=['print','(','"valor"',')',';']

res=p.separaPrint(token)

cod=generaCodigo(res)

opt=optimizacion(cod)
