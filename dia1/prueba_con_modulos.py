def contador(string):
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

if __name__ == "__main__":

	string = "./casotest.txt"
	print(contador(string))