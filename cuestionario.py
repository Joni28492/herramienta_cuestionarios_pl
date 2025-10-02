
import os
import random
import json





def main():
    folder = 'data'
    file = 'seguridad_ciudadana.json'
    path = os.path.join(folder, file) 

    # obtener data
    opciones_respuesta =[] # pasar a tupla posteriormente
    data_brute = None
    cuestionario = []

    with open(path, 'r', encoding='utf-8') as f:
        data_brute = json.load(f)

    # asignar opciones de respuesta
    for key in data_brute.keys():
    
        if key != "abrr_opts":
            # generar cuestionario
            for value in data_brute[key]:
                cuestionario.append({
                    "pregunta": value,
                    "respuesta": key
                })    
            
            # agregar opciones de respuesta
            opciones_respuesta.append(key)
            for opt in data_brute["abrr_opts"][key]:
                opciones_respuesta.append(opt)

    
       
    # barajar preguntas
    random.shuffle(cuestionario)


    # iteraciones del cuestionario
    
    #ejemplo con la pregunta[3]
    print(cuestionario[3])
    # realizar pregunta
    print("3.- ",cuestionario[3]["pregunta"])
    while True:
        temp_resp = input("Respuesta: ")
        if(temp_resp not in(opciones_respuesta)):
            print(f"Error, Las opciones de respuesta son {opciones_respuesta}")
        else:
            print(f"Respondida {data_brute["abrr_opts"][cuestionario[3]["respuesta"]]}")

            # if temp_resp in cuestionario[3]["respuesta"]:
            if temp_resp in data_brute["abrr_opts"][cuestionario[3]["respuesta"]]:
                print("✅ ¡Correcto!")
            else:
                print(f"❌ Incorrecto. Respuesta correcta: {cuestionario[3]["respuesta"]}")
            break



if __name__ == "__main__":
    main()