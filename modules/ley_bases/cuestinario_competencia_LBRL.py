import json
import hashlib
import random
from pydantic import BaseModel
from colorama import Style, init, Fore


class Pregunta(BaseModel):
    _id: str
    regimen: str 
    descripcion: str
    compete_a: str
    es_delegable: bool
    aciertos: float
    fallos: float
    racha_fallos: float
    fecha_ultimo_fallo: str
    aciertos_desde_ultimo_fallo: float

class CuestionarioCompetenciasLeyBases():
    
    def __init__(self, data_path="data.json", numero_preguntas=3 ):
        self.data_path = data_path
        self.data_file = None
        self.numero_preguntas = numero_preguntas
        
        self._opciones_respuesta = {
            "Alcalde": ("a", "alcalde"),
            "Pleno": ("p", "pleno"),
            "Junta Gobierno Local": ("jgl", "junta", "junta gobierno local")
        }
        
        
        
        self.preguntas_cuestionario = []
        
    
        
        with open(self.data_path, 'r', encoding='utf-8') as f:
            self.data_file = json.load(f)

        init()
    
    
    def _rellenar_id(self):
        """usar solo si no tiene los ids asignados"""
        for item in self.data_file:
            text_to_encode = f'{item["regimen"]}|{item["descripcion"]}|{item["compete_a"]}|{item["es_delegable"]}'
            encoded_text = hashlib.md5(text_to_encode.encode("utf-8")).hexdigest()
            item["_id"] = encoded_text
        # todo volcar archivo
        with open(self.data_path, 'w', encoding='utf-8') as f:
            json.dump(self.data_file, f, indent=4, ensure_ascii=False)
        
    
    def barajar_y_preguntas(self):
        random.shuffle(self.data_file)
        
        
    def hacer_pregunta(self, pregunta:Pregunta ):
        
        aciertos = 0
        fallos = 0
        
        print(Style.BRIGHT, Fore.CYAN if pregunta["regimen"] == "Regimen Comun" else Fore.YELLOW ,f"{pregunta["regimen"]} => {pregunta["descripcion"]}",Style.RESET_ALL)
        # print(f"Respuesta temporal: {pregunta["compete_a"]}")
        compete_a = input(f"Introduce respuesta: ")
        
        
        color_temps = {
            "Gran Poblacion":"\033[38;5;208m",
            "Junta Gobierno Local":"\033[38;5;13m",
            "Alcalde": "\033[38;5;51m",
            "Pleno": "\033[38;5;93m",
            "Reset": "\033[0m",
        }

        if compete_a in self._opciones_respuesta[pregunta["compete_a"]]:
            print(Fore.GREEN, "✅✅✅ ¡Correcto!",Style.RESET_ALL)
            aciertos += 1
        else: 
            print(Fore.RED,f"❌❌❌ Incorrecto.")
            # print(Fore.GREEN, f"Respuesta: {pregunta["compete_a"]}",Style.RESET_ALL)
            
            
            print( f"{color_temps[pregunta["compete_a"]]}Respuesta: {pregunta["compete_a"]} {color_temps["Reset"]}",Style.RESET_ALL)
            
            
            
        print(Fore.MAGENTA, "Es delegable?", Style.RESET_ALL)
        # print("=> respuesta temporal", pregunta["es_delegable"])
        es_delegable = input("Introduce tu respuesta:").lower()
        
        
        if es_delegable in ("s", "si", "y", "yes"): 
            if pregunta["es_delegable"]:
                print(Fore.GREEN, "✅✅✅ ¡Correcto!",Style.RESET_ALL)
                aciertos +=1
            else:
                print(Fore.RED,f"❌❌❌ Incorrecto.",Style.RESET_ALL)
                fallos+=1
        elif es_delegable in ("n", "no"): 
            if not pregunta["es_delegable"]:
                print("✅✅✅ ¡Correcto!")
                aciertos+=1
            else:
                print(Fore.RED,f"❌❌❌ Incorrecto.",Style.RESET_ALL)
                fallos += 1
        else: 
            pass
        
        if pregunta["hint"]:
            print(Style.BRIGHT,  Fore.RED,  f"OJO CUIDADO: {pregunta["hint"]}", Style.RESET_ALL)
                
        self.preguntas_cuestionario.append({"_id": pregunta["_id"],"aciertos": aciertos, "fallos": fallos})
                     
        
    
    def actualizar_pregunta(self, _id: str, aciertos:int, fallos:int):
        
        # print(_id) 
        indice = None 
        for i, el in enumerate(self.data_file):
            if el["_id"] == _id:
                indice = i
        
        if aciertos > 0:
           self.data_file[indice]["aciertos"] += aciertos
        if fallos > 0:
           self.data_file[indice]["fallos"] += fallos
            
            
        
    
    def realizar_cuestionario(self):
        
        
        for i in range(self.numero_preguntas):
            self.hacer_pregunta(self.data_file[i])
            # print(self.preguntas_cuestionario)
        for pid in self.preguntas_cuestionario:
            self.actualizar_pregunta(pid["_id"], pid["aciertos"], pid["fallos"]) 
    
        self.ordenar_fallos()

        with open(self.data_path, 'w', encoding='utf-8') as f:
            json.dump(self.data_file, f, ensure_ascii=False, indent=4)


    def ordenar_fallos(self):
        self.data_file = sorted(self.data_file, key= lambda x: x["fallos"], reverse=True)

      

    def run(self):
        print("SCRIPT: ley Bases")
        self.numero_preguntas = int(input("Introduce numero de pregntas: "))
        print(f"numero de preguntas: {self.numero_preguntas}")
        self.barajar_y_preguntas()
        
        self.realizar_cuestionario()
        



if __name__ == "__main__":
    game = CuestionarioCompetenciasLeyBases()
    game.run()