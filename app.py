import re
import json

exam = None
nombre_archivo = "oviedo_interino"

regex_pregunta = r"\d{1,2}.-"
regex_respuestas = r"[a-dA-D]\) "

with open(f'{nombre_archivo}.txt', 'r', encoding='utf-8') as f:
    exam = f.read().replace("\n", " ")

items = re.split(regex_pregunta, exam)

exam_json = []
soluciones = [
    "c","c","c","d","c",  "d","a","c","d","a",
    "d","b","d","b","b",  "c","c","c","b","a",
    "a","c","b","c","d",  "c","b","c","a","c",
    "c","c","d","c","a",  "c","a","b","a","d",
    "d","c","a","b","b",  "a","c","b","d","c",
    # reserva
    "b","b","d","b","d",  "c","c","a","c","c",
    ]

for num, pregunta in enumerate(items):

    respuestas = re.split(regex_respuestas, items[num])

    if len(respuestas) == 5:
        item = {
            "pregunta": f"{num+1}.- {respuestas[0]}",
            "respuestas": {
                "a": "a) "+ respuestas[1],
                "b": "b) "+ respuestas[2],
                "c": "c) "+ respuestas[3],
                "d": "d) "+ respuestas[4]
            },
            "solucion": soluciones[num],
            "explicacion": ""
        }
        
        exam_json.append(item)


with open(f'{nombre_archivo}.json', "w", encoding="utf-8") as f:
    json.dump(exam_json, f, ensure_ascii=False, indent=4)

