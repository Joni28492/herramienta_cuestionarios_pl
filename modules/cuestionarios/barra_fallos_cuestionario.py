import os
import json

from rich.console import Console
from rich.text import Text
from rich.align import Align


class Barra_fallos:
    def __init__(self, folder_path='backup'):
        self.folder_path = folder_path
        self.files_fails = []
        self.console = Console()


        self.run()

    def cargar_archivos(self):
        lista_archivos = os.listdir(self.folder_path)
        # parsear cada archivo con su cantidad de fallos
        for archivo in lista_archivos:
            self.file_parsing(archivo)

    def file_parsing(self, current_file):
        
        with open( os.path.join(self.folder_path, current_file), "r", encoding='utf-8' ) as f:
            content = json.load(f)
            fallos = 0
            aciertos = 0
            for item in content:
                fallos+=item["fallos"]
                aciertos+=item["aciertos"]
            ratio_fallos =  round((fallos/len(content)) , 2)
            ratio_aciertos = round((aciertos/len(content)) , 2)

            temp_file = {
                "archivo": current_file,
                "total_preguntas": len(content),
                "fallos": fallos,
                "ratio_fallos": ratio_fallos ,
                "ratio_aciertos": ratio_aciertos,
                "ratio": ratio_fallos-ratio_aciertos
            }

            self.files_fails.append(temp_file)
    def ordenar_por_ratio(self):
        self.files_fails = sorted(self.files_fails, key=lambda x: x["ratio"], reverse=True)
    
    def ratio_color(self, r: float) -> str:
        if r > 1.50:
            return "bold red"
        elif r >= 0.86:
            return "bold dark_orange3"
        elif r >= 0.46:
            return "bold yellow3"
        else:
            return "bold green3"

    def print_ratio_bar(self, file_label: str, ratio: float):
        line = Text(f"{file_label} • {ratio:.2f}", style=self.ratio_color(ratio))
        self.console.print( line )

    def run(self):
        
        self.cargar_archivos()
        self.ordenar_por_ratio()
        for item in self.files_fails:
            self.print_ratio_bar(item["archivo"][:-5].upper(), item["ratio"])
            # print(item["archivo"], (item["ratio"]) )

  

if __name__ == "__main__":
    
    fails_bars = Barra_fallos('backup')

    