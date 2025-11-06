
import os
import random
import json
# from colorama import init, Fore, Back, Style


class Cuestionario ():
    # todo crear init como dict para mejorar legibilidad
    def __init__(self, folder, file, backup_fails_folder, numero_preguntas=10):
        self.numero_preguntas = numero_preguntas
        self.folder = folder
        self.file = file
        self.backup_fails_folder = backup_fails_folder
        self.path = os.path.join(folder, file) 

        # obtener data
        self.opciones_respuesta =[] # opciones con las que permite responder 
        self.data_brute = None
        self.cuestionario = []
        self.backup_file = None # archivo que importa lista con conteo de fallos

        # ejecutar programa
        self.main()
        
    def cargar_data(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            self.data_brute = json.load(f)
        

 
    def generar_cuestionario_agregar_opciones_respuesta(self):
        for key in self.data_brute.keys():
    
            if key != "abrr_opts":
                # generar cuestionario
                for value in self.data_brute[key]:
                    self.cuestionario.append({
                        "pregunta": value,
                        "respuesta": key
                    })    
                
                # agregar opciones de respuesta
                self.opciones_respuesta.append(key)
                for opt in self.data_brute["abrr_opts"][key]:
                    self.opciones_respuesta.append(opt)

    def chekear_si_existe_backup_file(self):
        if self.file not in os.listdir(self.backup_fails_folder):
            return False
        return True

    def generar_backup_fails(self):
        temp_dump = self.cuestionario.copy()
        for item in temp_dump:
            item["fallos"] = 0
            item["aciertos"] = 0

        print("Generar backup", self.file)
        with open(os.path.join(self.backup_fails_folder, self.file), 'w', encoding="utf-8") as f:
            json.dump(temp_dump, f, indent=4, ensure_ascii=False)
    
    def importar_backup(self):
        with open(os.path.join(self.backup_fails_folder, self.file), 'r', encoding='utf-8') as f:
            self.backup_file = json.load(f)


    def generar_cuestionario(self):
        for key in self.data_brute.keys():
    
            if key != "abrr_opts":
                # generar cuestionario
                for value in self.data_brute[key]:
                    self.cuestionario.append({
                        "pregunta": value,
                        "respuesta": key
                    })    

    def barajar_cuestionario(self):
        random.shuffle(self.cuestionario)

    def realizar_pregunta(self, pregunta):

        print(pregunta["pregunta"])
        while True:
            temp_resp = input("Respuesta: ")
            if(temp_resp not in(self.opciones_respuesta)):
                print( f"Error, Las opciones de respuesta son {self.opciones_respuesta}")
            else:
                print(f"Respondida { temp_resp.upper()}" )

            
                if temp_resp in self.data_brute["abrr_opts"][pregunta["respuesta"]]:
                    print("✅✅✅ ¡Correcto!")
                    self.contabilizar_fallo_acierto(pregunta, True)
                   
                else:
                    print(f"❌❌❌ Incorrecto. Respuesta correcta: ===> {pregunta["respuesta"].upper()} <===") 
                    self.contabilizar_fallo_acierto(pregunta, False)
                break



    def contabilizar_fallo_acierto(self, pregunta, fallo_acierto: bool):
        for _, item in enumerate(self.backup_file):
            if item["pregunta"] == pregunta["pregunta"]:
                if not fallo_acierto:
                    print("Incrementamos error")
                    item["fallos"] = item["fallos"] + 1
                else:
                    print("Incrementamos aciertos")
                    item["aciertos"] = item["aciertos"] + 1

    def guardar_fallos(self):
        with open(os.path.join(self.backup_fails_folder, self.file), 'w', encoding="utf-8") as f:
            json.dump(self.backup_file, f, indent=4, ensure_ascii=False)

    def reordenar_fallos(self):
        self.backup_file = sorted(self.backup_file, key=lambda x: x["fallos"], reverse=True)
            
    def iniciar_cuestionario(self):
        for i, pregunta in enumerate(self.cuestionario[:self.numero_preguntas]):
            print(f"Pregunta numero: {i+1} ")
            self.realizar_pregunta(pregunta)

    def main(self):
        self.cargar_data()
        self.generar_cuestionario_agregar_opciones_respuesta()
        if not self.chekear_si_existe_backup_file(): # ojo a la iversion de logica
            self.generar_backup_fails()
            self.importar_backup()
        else:
            self.importar_backup()
        self.barajar_cuestionario()
        self.iniciar_cuestionario()
        self.reordenar_fallos()
        self.guardar_fallos()
        

    # otras funciones para mejorarlo
    def generar_resumen_fallos_aciertos(self):
        pass

    def reset_fallos(self):
        # por ahora con eliminar el archivo apañamos
        pass
        
    

if __name__ == "__main__":

    

    carpeta_data = 'data'
    archivo_seleccionado = None
    
    # que test tengo disponibles
    opciones_cuestionarios = os.listdir(carpeta_data)
    print("#"*40)
    for i, opt in enumerate(opciones_cuestionarios):
        # print(Fore.RED, f"# {i+1}.-  {opt.replace("_", " ")[:-5].upper()}")
        print(f"# {i+1}.-  {opt.replace("_", " ")[:-5].upper()}")
        
    print("#"*40)
    # seleccionar cuestionario
    while True:
        eleccion = int(input("Elige cuestionario: "))
        if eleccion > 0 and eleccion <= len(opciones_cuestionarios):
            print("SELECIONADO", opciones_cuestionarios[eleccion-1])
            archivo_seleccionado = opciones_cuestionarios[eleccion-1]
            break
        else:
            print(f"opcion no valida, introduce opcion del 1 al {len(opciones_cuestionarios)}")
    print(archivo_seleccionado)
            
    cantidad_preguntas = int(input( "\n¿Cuantas preguntas quieres hacer?: " ))

    cuestionario = Cuestionario('data', archivo_seleccionado, "backup", cantidad_preguntas ) 


   
    # todo agregar opcion de articulo para la gravedad de la infraccion
