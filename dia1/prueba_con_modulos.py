"""def contador(string):
	print((string),"pase por el print")
	comparador = [0]
	sumatorio = 0
	contador = 0
	for number in string:
		if number == comparador[-1]:
			sumatorio += int(number)
			comparador.append(number)
			contador += 1
		else:
			comparador.append(number)
			contador += 1
	if string[0] == string[-1]:
		sumatorio += int(number)		
	return sumatorio
	"""

#if __name__ == '__main__':
def lecturatxt(archivo):
	print(archivo)
	archivotxt = open(archivo,'r')
	mensaje = archivotxt.read()
	string = []
	for line in mensaje:
		print(line)
	archivotxt.close()

"""
string = open("casotest.txt",'r')
mensaje = string.read()
print(mensaje)
string.close()
"""