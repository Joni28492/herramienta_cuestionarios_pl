import os
import json
import random

class Definiciones():

    def __init__(self, file_selected, folder_data, backup_folder):
        
        self.file_selected = file_selected
        self.folder_data = folder_data
        self.data = None
        
        self.opciones_respuesta = []
        self.cuestionario = []


        self.backup_folder = backup_folder
        self.back_file = []



        self.main()


    def importar_data(self):
        with open(os.path.join(self.folder_data, self.file_selected), 'r', encoding='utf-8') as f:
            self.data = json.load(f)

    def asignar_opciones_respuesta(self):
        for key in self.data.keys():            
            self.opciones_respuesta.append(key.lower())

    def mostar_opciones_respuesta(self):
        print(self.opciones_respuesta)
        

    def generar_cuestionario(self):
        for key, value in self.data.items():
            self.cuestionario.append({
                "definicion": value,
                "respuesta": key
            })
    def barajar_cuestionario(self):
        random.shuffle(self.cuestionario)

    def preguntar_definicion(self, pregunta):
        self.mostar_opciones_respuesta()
        print()
        print(pregunta["definicion"])
        print(f"la respuesta es {pregunta["respuesta"]}")

        while True:
            
            respuesta = input("Definicion: ")

            if respuesta not in self.opciones_respuesta:
                print("No es una respuesta valida, las opciones de respuesta son las siguientes:")
                self.mostar_opciones_respuesta()
                continue

            if pregunta["respuesta"].lower() == respuesta.lower():
                 print("✅✅✅ ¡Correcto!")
            else:
                print(f"❌❌❌ Incorrecto. Respuesta correcta: ===> {pregunta["respuesta"].upper()} <===") 
                self.contabilizar_fallo(pregunta)
            break


     

    # todo mejorar importacion
    def comprobar_si_existe_backup(self):
        # crea carpeta en caso de no existir
        if  self.backup_folder not in  os.listdir('.'):
            os.makedirs(self.backup_folder)
        if  self.back_file not in os.listdir(self.backup_folder):
            self.crear_backup_file()
        else:
            self.importar_backup_file()
        
        print(self.back_file, "====")

        
        
        
 
    def crear_backup_file(self):
        for value in self.cuestionario:
            self.back_file.append({
                "definicion": value["definicion"],
                "respuesta": value["respuesta"],
                "fallos": 0
            })
            
        # generar archivo
        with open( os.path.join(self.backup_folder, self.file_selected), 'w', encoding='utf-8' ) as f:
            json.dump( self.back_file,f, indent=4, ensure_ascii=False )
        
    def contabilizar_fallo(self, pregunta):
        print("Contabilizar fallo")

    
    def importar_backup_file(self):
        with open(os.path.join(self.folder_data, self.file_selected), 'r', encoding='utf-8') as f:
            self.back_file = json.load(f)


    def reordenar_fallos(self):
        pass
        


    def main(self):
        self.importar_data()
        self.asignar_opciones_respuesta()
        self.generar_cuestionario()
        self.barajar_cuestionario()

        # todo crear bucle cuestionario 
        # todo crear menu de opciones 
        # print(self.cuestionario[3])
        # self.preguntar_definicion(self.cuestionario[3])

        self.comprobar_si_existe_backup()



        
        





if __name__ == "__main__":
    definiciones = Definiciones("animales.json", 'definiciones_data', 'definiciones_backup')
