
import os
import random
import json


class Cuestionario ():
    def __init__(self, folder, file, backup_fails_folder, numero_preguntas=10):
        self.numero_preguntas = numero_preguntas
        self.folder = 'data'
        self.file = 'seguridad_ciudadana.json'
        self.backup_fails_folder = backup_fails_folder
        self.path = os.path.join(folder, file) 

        # obtener data
        self.opciones_respuesta =[] # pasar a tupla posteriormente
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
                print(f"Error, Las opciones de respuesta son {self.opciones_respuesta}")
            else:
                print(f"Respondida { temp_resp.upper()}" )

            
                if temp_resp in self.data_brute["abrr_opts"][pregunta["respuesta"]]:
                    print("✅ ¡Correcto!")
                else:
                    print(f"❌ Incorrecto. Respuesta correcta: {pregunta["respuesta"]}")    
                    self.contabilizar_fallo(pregunta)
                break



    def contabilizar_fallo(self, pregunta_fallada):
        for _, item in enumerate(self.backup_file):
            if item["pregunta"] == pregunta_fallada["pregunta"]:
                print("Incrementamos error")
                item["fallos"] = item["fallos"] + 1

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
        else:
            self.importar_backup()
        self.generar_cuestionario()
        self.barajar_cuestionario()
        self.iniciar_cuestionario(5)
        self.reordenar_fallos()
        self.guardar_fallos()
        
    def generar_resumen_fallos_aciertos(self):
        pass
        
    

if __name__ == "__main__":
    cuestionario = Cuestionario('data', 'seguridad_ciudadana.json', "backup" ) 