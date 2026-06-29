
from colorama import Style, init as initColorama, Fore
import json



class SeguridadVial: 
    
    def __init__(self, file='delitos_seguridad_vial.json', num_preguntas=2):
        initColorama()
        self.file= file
        self.data_brute = None
        self.data_filtered = None        

    def cargar_data(self): 
        with open(self.file, 'r', encoding='utf-8') as f:
            self.data_brute = json.load(f)
        
        
    def filtrar_data(self): pass
    def barajar_data(self): pass
    def realizar_cuestionario(self): pass
    def hacer_pregunta(self, pregunta): 
        pass
        # pregunta sobre prision
        # pregunta sobre multa
        # pregunta sobre tbc
        # pregunta sobre pdc
        # pregunta sobre y o
        
        
    def volcar_data(self): pass

    def run(self):
        print("TEST DELITOS SEGURIDAD VIAL PENAS")
        self.cargar_data()





if __name__ == '__main__':
    seguridad_vial = SeguridadVial()
    seguridad_vial.run()