import os
import json
import random
from colorama import Style, init, Fore
import datetime
import time



# todo calcular nota

class Test_Selector():
    def __init__(self, cantidad_preguntas=3):
        self.root_path = 'E:\\ESCRITORIO 2023\\OPOSICIONES\\desarrollo applicaciones\\asturpol-game\\src\\pages\\api\\tests\\db'
        self.mixed_path = ''
        self.test_backup = 'test'
        self.cuestionario = None
        self.cantidad_preguntas = cantidad_preguntas

        self.resp_options = ("a","b","c","d", "")

        self.listado_aciertos_errores = []

        self.listado_preguntas_respondidas = []
        self.fails_path = 'test'

        init()
        self.main()
    

    def volcar_logs_preguntas(self):
        # print(self.listado_preguntas_respondidas)
        hoy = datetime.date.today()
        file_name = f"{hoy}.json"
        file_path = os.path.join(self.fails_path , file_name)
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(self.listado_preguntas_respondidas, f, indent=4, ensure_ascii=False)
        
        



    def construir_log_pregunta(self, pregunta, path, opcion_elegida):
        question_log = {
            # todo optimizar timestamp
            "timestamp": time.time(),
            # todo optimizar ruta
            "path": path.replace('E:\\ESCRITORIO 2023\\OPOSICIONES\\desarrollo applicaciones\\asturpol-game\\src\\pages\\api\\tests\\db', '').replace("\\", "/"),
            "id": "id2340234",
            "pregunta": pregunta["pregunta"],
            "opciones_respuesta": {
                "a": pregunta["respuestas"]["a"],
                "b": pregunta["respuestas"]["b"],
                "c": pregunta["respuestas"]["c"],
                "d": pregunta["respuestas"]["d"],
            },
            "opcion_correcta": pregunta["solucion"],
            "opcion_selecionada": opcion_elegida,

        }
        print("log, guardando pregunta")
        # print(question_log)
        self.listado_preguntas_respondidas.append(question_log)


    def importar_cuestionario(self):
        print(f"importar {self.mixed_path}")
        
        with open(self.mixed_path, 'r', encoding='utf-8') as f:
            self.cuestionario = json.load(f)
        
    def barajar_cuestionario(self):
        random.shuffle(self.cuestionario)

    def pretty_print_preguntas(self,pregunta, seleccion=''):
        
        temp_list = self.resp_options[:len(self.resp_options) - 1]
        print("="*50)
        if seleccion == '':
            print()
            print(Style.RESET_ALL, Style.BRIGHT,pregunta["pregunta"])
            print()
            for p in temp_list:
                print(Style.RESET_ALL, f"\t{p})", pregunta["respuestas"][p])
            print()
            print(Style.BRIGHT, "Solucion", pregunta["solucion"])
            print()
        else:
            if pregunta["solucion"] != seleccion:
                # impresion correcion
                self.listado_aciertos_errores.append("❌")
                print(f"❌❌❌ Incorrecto.")
                
                print()
                print(Style.RESET_ALL, Style.BRIGHT,pregunta["pregunta"])
                print()
                for p in temp_list:
                    if p == pregunta["solucion"]:
                        print(Style.BRIGHT, Fore.GREEN, f"\t{p})", pregunta["respuestas"][p])
                    else:
                        if p == seleccion:
                            print(Style.BRIGHT, Fore.RED, f"\t{p})", pregunta["respuestas"][p])
                        else:
                            print(Style.RESET_ALL, f"\t{p})", pregunta["respuestas"][p])

                print()
                    
            else:
               # impresion corecta
                self.listado_aciertos_errores.append("✅")
                print("✅✅✅ ¡Correcto!")
                print()
                print(Style.RESET_ALL, Style.BRIGHT,pregunta["pregunta"])
                print()
                for p in temp_list:
                    if p == pregunta["solucion"]:
                        print(Style.BRIGHT, Fore.GREEN, f"\t{p})", pregunta["respuestas"][p])
                    else:
                        print(Style.RESET_ALL, f"\t{p})", pregunta["respuestas"][p])
                print()
        print(self.listado_aciertos_errores)
        print(Style.RESET_ALL,"="*50)

        
                
    def comprobar_si_existe_registro_fallos_diario(self):
        hoy = datetime.date.today()
        file = f"{hoy}.json"
        full_path = os.path.join(self.fails_path, file) 

        print(os.listdir(self.fails_path))

        if file not in os.listdir(self.fails_path):
            print(f"Creando Archivo registro de hoy {hoy}")
            with open(full_path, 'w', encoding='utf-8') as f:
                json.dump([], f, indent=4)
            print("Archivo creado con exito")
        else:
            print(f"importando archivo {hoy}.json")
            with open(full_path, 'r', encoding='utf-8') as f:
                self.listado_preguntas_respondidas = json.load(f)
            # importar archivo de hoy
        # print(self.listado_preguntas_respondidas)
        
        
        
               
    def realizar_cuestionario(self):

        for pregunta in self.cuestionario:
            self.realizar_pregunta(pregunta)


    def  realizar_pregunta(self, pregunta):
        # imprimir pregunta
        self.pretty_print_preguntas(pregunta)
        temp_user_selection = None
        
        while True:
            temp_user_selection = input("Escoge opcion: ")

            if temp_user_selection not in self.resp_options:            
                print(Fore.RED, f"opcion incorrecta, utiliza las siguientes o deja en blanco, {self.resp_options}")
            else:
                # comprobar resultado
                if temp_user_selection == '':
                    print("Continuar siguiente pregunta")
                    # contabilizar en blanco
                    self.listado_aciertos_errores.append("")
                else: 
                    self.pretty_print_preguntas(pregunta, temp_user_selection)
                   
                    
                self.construir_log_pregunta(pregunta, self.mixed_path, temp_user_selection)

                break
            


    def menu_seleccion(self):
        while True:

            temp_list = os.listdir(os.path.join(self.root_path, self.mixed_path))
            
            # imprimir menu
            for opt, folder in enumerate(temp_list):
                print(opt, folder)
            # selecionar
            selection = input("Introduce opt: ")
            # comprobar dir or file tipo .json
            if temp_list[int(selection)].endswith('.json'):
                
                self.mixed_path = os.path.join( self.root_path, temp_list[int(selection)]  )
                print("Test Selecionado", self.mixed_path)
                
                self.importar_cuestionario()
                self.barajar_cuestionario()

                #Recortar cantidad preguntas
                self.cantidad_preguntas = int(input("Cuantas preguntas quieres realizar: "))
                self.cuestionario = self.cuestionario[:self.cantidad_preguntas] 
                self.realizar_cuestionario()
                # self.realizar_pregunta(self.cuestionario[0])

                # guardar todo el log de preguntas
                self.volcar_logs_preguntas()
                                
                
                break


            else:
                self.root_path = os.path.join( self.root_path, temp_list[int(selection)]  )
                

    def main(self):
        self.comprobar_si_existe_registro_fallos_diario()
        self.menu_seleccion()
       

if __name__ == '__main__':
    test_selection = Test_Selector() 

