
fich = open ("/etc/passwd","r");
Lineas = fich.readlines();
dic = {}


for Linea in Lineas:
	usuario = Linea.split(':')
	dic[usuario[0]] = {usuario[6]}
	
try:
	print (dic["root"])
	print (dic["imaginario"])

except:			#Si no lo encuentra:
	print ("Usuario no válido")

fich.close()
