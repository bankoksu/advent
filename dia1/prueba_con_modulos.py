def contador(string):
	comparador = [0]
	sumatorio = 0
	contador = 0
	string = string.replace('"','')
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

def lecturatxt(archivo):
		archivotxt = open(archivo,'r')
		mensaje = archivotxt.read()
		archivotxt.close()
		return contador(mensaje)

if __name__ == '__main__':
	print(lecturatxt("casotest.txt"))
	


"""
string = open("casotest.txt",'r')
mensaje = string.read()
print(mensaje)
string.close()
"""
