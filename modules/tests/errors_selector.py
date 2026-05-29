import os,  datetime
import json
import pandas as pd

# todo hacer para poder seleccionar el dia 

# solo vuelca los errores
class ErrosSelector():
    def __init__(self, mode="today", path_folder='backup', erros_folder_path ='errors'):
        self.today = datetime.date.today()
        self.mode = mode  
        self.data_brute = None
        self.data_errors = [] 
        self.path_folder = path_folder
        self.erros_folder_path = erros_folder_path
        
        
    def run(self):
        
        
        with open(os.path.join(self.path_folder, str(self.today)+'.json'), 'r', encoding='utf-8') as f:
            self.data_brute = json.load(f)
        self.filtrar_errores()
        self.volcar_errores_json()
        print(f"Errores volcados, total fallos: {len(self.data_errors)}")
        self.volcar_errores_csv()
        print("CSV Creado")
        


        
    def filtrar_errores(self):
        for pregunta in self.data_brute:
            if pregunta["opcion_correcta"] != pregunta["opcion_selecionada"]:
                self.data_errors.append(pregunta)
    
    def volcar_errores_json(self):
        with open(os.path.join(self.erros_folder_path, 'json',str(self.today)+'.json'), 'w', encoding='utf-8') as f:
            json.dump(self.data_errors,f,indent=4, ensure_ascii=False)
    
    def volcar_errores_csv(self):
        # todo mejorar para que respuesta no esten todas en una celda
        data_errors_falten = []
        
        for item in self.data_errors:
            
            opciones = item.pop("opciones_respuesta")
            
            
            
            data_errors_falten.append({
                **item,
                "a": opciones["a"],
                "b": opciones["b"],
                "c": opciones["c"],
                "d": opciones["d"],
                
            })
        
        
        # df = pd.DataFrame(self.data_errors)
        df = pd.DataFrame(data_errors_falten)
        df.to_csv( os.path.join(self.erros_folder_path,'csv', str(self.today)+'.csv'), encoding='utf-8', index=False )
        
        
        
if __name__ == '__main__':
    error_capture = ErrosSelector(mode="today")
    error_capture.run()