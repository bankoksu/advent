def impresora(string):
	print(string)
	return "pase al programa"

if __name__ == "__main__":
	string = open("casotest.txt",'r')
	mensaje = string.read()
	string.close()
	print(impresora(mensaje))
