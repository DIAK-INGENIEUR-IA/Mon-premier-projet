a = float(input("Premier nombre : "))
b = float(input("Deuxième nombre : "))
operation = input("Opération ( +, -, *, /) : ")
if operation == "+":
	print("Le resultat est : ", a + b)
elif operation == "-":
	print("Le resultat est : ", a - b)
elif operation == "*":
	print("Le resultat est : ", a*b)
elif operation == "/":
	if b == O:
		print("Erreur : division par zéro")
	else:
		print("Le resultat est : ", a/b)
else:
	print("Opération inconnue")
