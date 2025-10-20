import os
import json
from colorama import Fore, Style, init
import random

class Custom_chained_questions():

    def __init__(self, path_base='chained',file_base='chained_base.json', backup_folder='chained_backup', backup_file='custom.json' ):
        self.path_base = path_base
        self.file_base = file_base

        self.backup_folder = backup_folder 
        self.backup_file = backup_file

        self.backup_importado = None

        self.quesion_list = None
    
        self.backup_preguntas = []

    def fill_quesion_list(self):
        with open(os.path.join(self.path_base, self.file_base), 'r', encoding='utf-8') as f:
            self.quesion_list = json.load(f)

    
    def importar_backup(self):
        with open(os.path.join(self.backup_folder, self.backup_file), 'r', encoding='utf-8') as f:
            self.backup_importado = json.load(f)


    def resolver_pregunta_simple(self, pregunta):

        question_log = {
            "tipo": pregunta["tipo"],
            "pregunta": pregunta["pregunta"],
            "respuesta": pregunta["respuesta"],
            "fallos": 0,
            "aciertos": 0
        }

        print(Style.BRIGHT, pregunta["pregunta"], Style.RESET_ALL)
        log = input("La sabias: ")

        if log == 's':
            print(Fore.GREEN, Style.BRIGHT ,"guardar correcto", Style.RESET_ALL)
            question_log["aciertos"] = 1

        else:
            print(Fore.RED, Style.BRIGHT ,"guardar fallo", Style.RESET_ALL)
            question_log["fallos"] = 1
        self.backup_preguntas.append(question_log)
        

    
    def resolver_pregunta_listado(self, pregunta):
        log_pregunta_listado = {
            "tipo": pregunta["tipo"],
            "pregunta": pregunta["pregunta"],
            "listado": [],
        }
        print(pregunta["pregunta"], "(listado)")
        input("Pulsa Enter cuando creas que las tienes.")

        for i, p in enumerate(pregunta["listado"]):
            print(i, p)
            p_log = input("la sabias?:")
            if p_log == 's':
                log_pregunta_listado["listado"].append({
                    "item": pregunta["listado"][i],
                    "aciertos": 1,
                    "fallos": 0
                })
                print("Si la sabia")
            else:
                log_pregunta_listado["listado"].append({
                    "item": pregunta["listado"][i],
                    "aciertos": 0,
                    "fallos": 1
                }),
                print("No la sabia")
        self.backup_preguntas.append(log_pregunta_listado)

    def resolver_pregunta_encadenada(self, pregunta):
        log_cahined = {
            "tipo":"encadenada",
            "pregunta_inicial": pregunta["pregunta_inicial"],
            "respuesta_inicial": pregunta["respuesta_inicial"],
            "fallos_inicial": 0,
            "aciertos_inicial": 0,
            "subpreguntas": []
        }


        print(pregunta["pregunta_inicial"], "(encadenada)")
        input("Esperando...")
        print(Fore.GREEN, Style.BRIGHT ,pregunta["respuesta_inicial"], Style.RESET_ALL)
        init_log = input("Acertaste la primera?")

        if init_log == 's':
            log_cahined["aciertos_inicial"] = 1
            print("✅✅✅")
        else:
            log_cahined["fallos_inicial"] = 1
            print("❌❌❌")




        # encadenamiento de preguntas
        for p in pregunta["subpreguntas"]:
            print(p["pregunta"])

            sub_log = {
                "tipo": p["tipo"],
                "pregunta": p["pregunta"],
                "respuesta":p["respuesta"],
                "aciertos": 0,
                "fallos": 0
            }
            input("Esperando...")
            print(Fore.GREEN, Style.BRIGHT ,p["respuesta"], Style.RESET_ALL)
            opt = input("Correcta?: ")
            if opt == 's':
                print("✅✅✅")
                log_cahined["subpreguntas"].append({
                    **sub_log,
                    "aciertos": 1
                })
            else:
                print("❌❌❌")
                log_cahined["subpreguntas"].append({
                    **sub_log,
                    "fallos": 1
                })
        self.backup_preguntas.append(log_cahined)
        

    def realizar_cuestionario(self):
        # print(len(self.quesion_list))
        for pregunta in self.quesion_list:
            if pregunta["tipo"] == "simple":
                self.resolver_pregunta_simple(pregunta)
            elif pregunta["tipo"] == 'list':
                self.resolver_pregunta_listado(pregunta)
            else:
                self.resolver_pregunta_encadenada(pregunta)

    def randomizar_cuestionario(self):
        random.shuffle(self.quesion_list)

    def run(self):
        self.importar_backup()
        # print(self.backup_importado)
        self.fill_quesion_list()
        # self.randomizar_cuestionario()
        # self.realizar_cuestionario()

        # self.resolver_pregunta_encadenada(self.quesion_list[2])
        # self.resolver_pregunta_listado(self.quesion_list[1])
        # self.resolver_pregunta_simple(self.quesion_list[0])
        # print(self.backup_preguntas)


        # todo guardar registro de fallos




if __name__ == '__main__':
    init() # inicio colorama
    chained_system = Custom_chained_questions() 
    chained_system.run()