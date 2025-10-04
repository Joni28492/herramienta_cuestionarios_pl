
import os
import random
import json


def generar_backup_fails(folder_to_check, file_to_check, cuestionario_original):
    temp_dump = cuestionario_original.copy()
    for item in temp_dump:
        item["fallos"] = 0
    with open(os.path.join(folder_to_check, file_to_check), 'w', encoding="utf-8") as f:
        json.dump(temp_dump, f, indent=4, ensure_ascii=False)



   
    print("FAILLSS!!!")


def main():
    folder = 'data'
    file = 'seguridad_ciudadana.json'
    backup_fails_folder = "backup"
    path = os.path.join(folder, file) 

    # obtener data
    opciones_respuesta =[] # pasar a tupla posteriormente
    data_brute = None
    cuestionario = []
    # respuestas = []
    backup_file = None # archivo que importa lista con conteo de fallos

    with open(path, 'r', encoding='utf-8') as f:
        data_brute = json.load(f)



    # asignar opciones de respuesta, gestionar en funcion de clase
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

    
    #comprobar si existe backup de fallos
    if file not in os.listdir(backup_fails_folder):
        generar_backup_fails(backup_fails_folder,file,cuestionario)


    #cargamos el file en la variable
    with open(os.path.join(backup_fails_folder, file), 'r', encoding='utf-8') as f:
        backup_file = json.load(f)
        

    # barajar preguntas
    random.shuffle(cuestionario)


    # iteraciones del cuestionario
    

    # todo hacer bucle
    #ejemplo con la pregunta[3]
    print(cuestionario[3])
    # realizar pregunta
    print("3.- ",cuestionario[3]["pregunta"])
    while True:
        temp_resp = input("Respuesta: ")
        if(temp_resp not in(opciones_respuesta)):
            print(f"Error, Las opciones de respuesta son {opciones_respuesta}")
        else:
            print(f"Respondida { temp_resp.upper()}" )

           
            if temp_resp in data_brute["abrr_opts"][cuestionario[3]["respuesta"]]:
                print("✅ ¡Correcto!")
            else:
                print(f"❌ Incorrecto. Respuesta correcta: {cuestionario[3]["respuesta"]}")
                for _, item in enumerate(backup_file):
                    if item["pregunta"] == cuestionario[3]["pregunta"]:
                        print("Incrementamos error")
                        item["fallos"] = item["fallos"] + 1


            break

   
    print("FAILLSS!!!")
 
    
    # reordenar
    backup_file = sorted(backup_file, key=lambda x: x["fallos"], reverse=True)
    #
    with open(os.path.join(backup_fails_folder, file), 'w', encoding="utf-8") as f:
            json.dump(backup_file, f, indent=4, ensure_ascii=False)

    

if __name__ == "__main__":
    main()