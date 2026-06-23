numero_preguntas = int(input("Introduce num de preguntas: "))
valor_pregunta = 100/numero_preguntas

aciertos = int(input("Introduce num de aciertos: "))
fallos = int(input("Introduce num de fallos: "))

print(f"aciertos {aciertos} | fallos {fallos}")
print(f"total sin restar: {aciertos*valor_pregunta}")
print(f"total: { (aciertos*valor_pregunta)-((fallos*valor_pregunta)/3) }")
