""" para convertir json en un hmtl legible rapdidamente """
import json
import os

class ConvertJsonTestToHTML():
    def __init__(self, path_folder, path_file, output_path='html', ):
        self.path_folder = path_folder
        self.path_file = path_file
        self.output_path = output_path
        self.data = None
    
    def cargar_json(self):
        with open(  os.path.join(self.path_folder, self.path_file) , 'r', encoding='utf-8' ) as f:
            self.data = json.load(f) 
    
    def dibujar_html(self):
        html=''
        html_header = """
        <!DOCTYPE html>
            <html lang="es" class="dark">
            <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>Tipo Test</title>
            <script src="https://cdn.tailwindcss.com"></script>
            </head>

            <body class="bg-gray-100 dark:bg-gray-950 text-gray-900 dark:text-gray-100 min-h-screen p-6">
            <main class="max-w-3xl mx-auto space-y-6">
                <h1 class="text-3xl font-bold">Tipo Test</h1>

        """
        
        html += html_header
        
        for p in self.data:
            section_header = f"""
            <section class="bg-white dark:bg-gray-900 rounded-2xl shadow p-6">
            <h2 class="text-xl font-semibold mb-4">
                {p["pregunta"]}
            </h2>
            <div class="space-y-3"> """
        
        
            respuestas_html =""
            for opt, resp  in p["respuestas"].items():
                respuesta_html =f"""
                <div class="p-4 rounded-xl border-2 
                {"border-green-500 bg-green-100 text-green-800" if opt == p["solucion"] else ""} font-semibold">
                {resp} {"✓"  if opt == p["solucion"] else "" }
                </div>
                """
                respuestas_html += respuesta_html
                    
    
        
            section_footer = """
            </div>
            </section>
            """
            
            html+=section_header+respuestas_html+section_footer
            
        
        
        html_footer = """
        </main>
        </body>
        </html>
        """
            
        html+=html_footer
        return html

    def volcar_html(self):
        with open(self.output_path, 'w', encoding='utf-8') as f:
            f.writelines(self.dibujar_html())
            
    def run(self):
        self.cargar_json()
        self.volcar_html()


    
if __name__ == '__main__':
    file = 'simulacro_oviedo_02'
    jsonToHtmlConverter = ConvertJsonTestToHTML(path_folder="notebook", path_file=f"{file}.json", output_path=f"html/{file}.html")
    jsonToHtmlConverter.run()