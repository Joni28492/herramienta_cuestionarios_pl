import os
import json

### todo crear index para navegar en docs
class Generar_HTMLs:

    def __init__(self,docs_folder = "docs", ruta_cuestionario=os.path.join("modules", "cuestionarios","backup")):
        self.ruta_cuestionario = ruta_cuestionario
        self.docs_folder = docs_folder
        self.cuestionario_archivos =  os.listdir(self.ruta_cuestionario) 

        self.border_colors = {
            '__all__': 'border-zinc-600',
            'leve': 'border-emerald-500',
            'grave': 'border-amber-400',
            'muy grave': 'border-red-500',

            "eximentes":'border-emerald-500',
            "atenuantes":'border-amber-400',
            "agravantes":'border-red-500',

            "municipio": "border-lime-600",
            "administracion general del estado":"border-orange-400",
            "ministerio del interior": "border-violet-950",

            "policia":  'border-zinc-400',
            "policia nacional": 'border-zinc-800',
            "policia local": 'border-blue-600',
            "guardia civil": 'border-green-900',
            "propias": 'border-rose-600',
            "colaboracion": 'border-yellow-700',
            "simultaneas":  'boder-rose-500',
        

            "nulo pleno derecho":"border-rose-950",
            "anulable":"border-rose-500",
        }



        
    def get_data_index_cuestionarios(self):

      indices_cuestionarios = os.listdir(self.ruta_cuestionario)
      list_index = []
      
      for cuestionario in indices_cuestionarios:
        current_data = {"title": cuestionario, "total": 0,  "aciertos":0, "fallos": 0}
        current_file = None
        with open(os.path.join(self.ruta_cuestionario, cuestionario), 'r', encoding='utf-8'  ) as f:
          current_file = json.load(f)
        current_data["total"] = len(current_file)
        for item in current_file:
            current_data["aciertos"] += item["aciertos"]
            current_data["fallos"] += item["fallos"]
        list_index.append(current_data)


      ## creacion html
      html = ''
      html_section_init = f"""
      <!-- Sección cuestionarios -->
      <section>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
      """
      html+=html_section_init

      for card in list_index:
        html+=f"""
          <a href="cuestionarios/{card["title"].replace("_", " ").replace(".json",".html")}"
              class="group block rounded-2xl border border-zinc-800 bg-zinc-900/60 hover:bg-zinc-900 transition shadow-md">
              <div class="p-6">
                <div class="flex items-start justify-between gap-3">
                  <div>
                    <h2 class="text-lg font-semibold text-zinc-100 h-22 group-hover:text-emerald-400 transition">
                      {card["title"].replace("_", " ").replace(".json","")}
                    </h2>
                    <p class="text-xs text-zinc-400 font-mono mt-1">
                      {card["title"]}
                    </p>
                  </div>

                  <span class="text-xs rounded-full border border-zinc-700 px-2 py-1 text-zinc-300">
                    {card["total"]}
                  </span>
                </div>

                <div class="mt-4 flex items-center gap-3 text-sm">
                  <span class="text-red-400">Fallos: <span class="font-semibold"> {card["fallos"]} </span></span>
                  <span class="text-zinc-700">|</span>
                  <span class="text-emerald-400">Aciertos: <span class="font-semibold"> {card["aciertos"]} </span></span>
                </div>

                <div class="mt-4 text-xs text-zinc-500">
                  Abrir informe →
                </div>
              </div>
            </a>
        """


      html_section_end ="""   
        </div>
      </section>
      """
      html += html_section_end

      # print(html)
      return html
     
    

    

    def generar_index(self, sections=[]):
      """esta funcion genera la pagina index.html para acceder a los modulos correspondientes"""
      # todo add t anchor to ley bases competencias
      html =""
      ### todo pintar HTML
      html_start_header = f"""
      <!doctype html>
      <html lang="es">
      <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>Índice de Cuestionarios</title>
        <script src="https://cdn.tailwindcss.com"></script>
      </head>

      <body class="bg-zinc-950 text-zinc-100 min-h-screen">
        <main class="max-w-6xl mx-auto px-4 py-10">

          <!-- Header -->
          <header class="mb-10">
            <h1 class="text-3xl font-semibold tracking-tight">
              Índice de Cuestionarios
            </h1>
            <p class="text-zinc-400 mt-2">
              Acceso directo a los informes HTML generados.
            </p>
          </header>
        
    
        
    """
      html_end_footer = """
        <!-- Footer -->
        <footer class="mt-12 pt-6 border-t border-zinc-900 text-xs text-zinc-500">
          Plantilla HTML + Tailwind CDN.
        </footer>

      </main>
    </body>
    </html>
    """
      html+=html_start_header
      ### secciones
      for section in sections: 
         html+=section
      
      # prvisional enlace a ley bases
      html+= "<a href='lbr/competencias_lbrl.html' class='text-2xl mt-4 py-2 font-bold hover:text-orange-400'>Competencias Ley Bases Regiemn local</a>"
      ##footer
      html += html_end_footer

      # crear index html
      with open(os.path.join(self.docs_folder, 'index.html'), 'w', encoding='utf-8') as f:
         f.write(html)
      print(f"Index creado en {self.docs_folder} ")
      return None



    def generar_html_cuestionario_archivo(self, archivo_json='alcohol_y_drogas.json'):
        """Generar cada archivo html de la seccion cuestionarios"""
        
        title = archivo_json[:-5].replace("_"," ")
        json_file = None

        with open(os.path.join(self.ruta_cuestionario, archivo_json), 'r', encoding='utf-8' ) as f:
            json_file = json.load(f)

        total_aciertos = 0 
        total_fallos = 0 

        for p in json_file:
            total_aciertos += p["aciertos"]
            total_fallos += p["fallos"]
        

        html = ''
        html_header = f'''
            <!doctype html>
            <html lang="es">
            <head>
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1" />
            <title> {title.upper()} </title>
            <script src="https://cdn.tailwindcss.com"></script>
            </head>
              <!doctype html>
            <html lang="es">
            <head>
              <meta charset="utf-8" />
              <meta name="viewport" content="width=device-width, initial-scale=1" />
              <title>Informe {title.upper()} </title>
              <script src="https://cdn.tailwindcss.com"></script>
            </head>
            <body class="bg-zinc-950 text-zinc-100 min-h-screen">
          <main class="max-w-5xl mx-auto px-4 py-10">
            <!-- Header -->
            <header class="mb-8">
              <div class="flex items-start justify-between gap-4">
                <div>
                  <h1 class="text-2xl font-semibold tracking-tight">Sistema de columnas</h1>
                  <p class="text-zinc-400 mt-1">
                    Archivo: <span class="font-mono text-zinc-300"> {archivo_json} </span>
                  </p>
                </div>

             
                <div class="text-right">
                  <p class="text-sm text-zinc-400">Resumen</p>
                  <p class="text-sm">
                    Fallos: <span class="text-red-400 font-semibold">{total_fallos}</span>
                    <span class="text-zinc-600 px-2">|</span>
                    Aciertos: <span class="text-emerald-400 font-semibold">{total_aciertos}</span>
                  </p>
                </div>
              </div>
            </header>
              <!-- Lista de items -->
            <section class="space-y-4">
        '''
        html_footer = f'''
           </section>

                <!-- Pie / nota -->
                <footer class="mt-10 text-xs text-zinc-500">
                <p>
                    Plantilla HTML + Tailwind (CDN). Los bordes (<span class="text-zinc-300">border-emerald-500 / border-amber-400 / border-red-500</span>)
                  
                </p>
                </footer>
            </main>
            </body>
            </html>

        '''
        
        html += html_header
        # bucle items preguntas
        for item in json_file:

            # borde = self.border_colors[item["respuesta"]]
            borde = self.border_colors.get(item.get("respuesta",""), self.border_colors["__all__"])
            html += f"""
                  <article class="rounded-xl border-l-4 {borde} bg-zinc-900/60 shadow-sm">
                    <div class="p-5">
                      <div class="flex items-start justify-between gap-4">
                        <div class="min-w-0">
                          <p class="text-xs uppercase tracking-wide text-zinc-400">
                            Ítem <span class="font-mono text-zinc-300">#</span>
                          </p>
                          <h2 class="mt-1 text-base font-medium leading-snug break-words">
                            {item["pregunta"]}
                          </h2>
                          <p class="mt-2 text-sm text-zinc-300">
                            Solución: <span class="font-semibold text-zinc-100">{item["respuesta"]}</span>
                          </p>
                        </div>
    
                        <div class="shrink-0 text-right">
                          <p class="text-sm">
                            Fallos: <span class="text-red-400 font-semibold">{item["fallos"]}</span>
                          </p>
                          <p class="text-sm">
                            Aciertos: <span class="text-emerald-400 font-semibold">{item["aciertos"]}</span>
                          </p>
                        </div>
                      </div>
                    </div>
                  </article>
            """


        html += html_footer

        

        # crear archivo
        with open(os.path.join('docs','cuestionarios', title+'.html'), 'w', encoding='utf-8') as f:
            f.write(html)

    def generar_archivo_ley_bases(self, archivo_json='data.json'):
        json_file = None
        with open(os.path.join('modules','ley_bases', archivo_json), 'r', encoding='utf-8') as f:
          json_file = json.load(f)

        temp_styles =  {
          "__all__": {
              "border": "border-zinc-600",
              "badge_bg": "bg-zinc-500/15",
              "badge_text": "text-zinc-300",
              "box_bg": "bg-zinc-500/10",
          },
          "Alcalde": {
              "border": "border-sky-500",
              "badge_bg": "bg-sky-500/15",
              "badge_text": "text-sky-300",
              "box_bg": "bg-sky-500/10",
          },
          "Pleno": {
              "border": "border-violet-500",
              "badge_bg": "bg-violet-500/15",
              "badge_text": "text-violet-300",
              "box_bg": "bg-violet-500/10",
          },
          "Junta Gobierno Local": {
              "border": "border-orange-500",
              "badge_bg": "bg-orange-500/15",
              "badge_text": "text-orange-300",
              "box_bg": "bg-orange-500/10",
          },
}


        html = ''
        html_header ="""
        <!doctype html>
      <html lang="es">
      <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>Competencias · Informe</title>
        <script src="https://cdn.tailwindcss.com"></script>
      </head>

      <body class="bg-zinc-950 text-zinc-100 min-h-screen">
        <main class="max-w-5xl mx-auto px-4 py-10">

          <header class="mb-8">
            <div class="flex items-start justify-between gap-4">
              <div>
                <h1 class="text-2xl font-semibold tracking-tight">Sistema de columnas · Competencias</h1>
                <p class="text-zinc-400 mt-1">
                  Archivo: <span class="font-mono text-zinc-300">competencias_municipales.json</span>
                </p>
              </div>

              <div class="text-right">
                <p class="text-sm text-zinc-400">Resumen</p>
                <p class="text-sm">
                  Fallos: <span class="text-red-400 font-semibold">12</span>
                  <span class="text-zinc-600 px-2">|</span>
                  Aciertos: <span class="text-emerald-400 font-semibold">37</span>
                </p>
              </div>
            </div>
          </header>

          <section class="space-y-4">



        """
        html+=html_header
        
        # todo separar por regimen
        for pregunta in json_file:
         

          html_tmp = f"""
             <article class="rounded-xl border-l-4 {temp_styles[pregunta["compete_a"]]["border"]} bg-zinc-900/60 shadow-sm">
              <div class="p-5">
                <div class="flex items-start justify-between gap-4">
                  <div class="min-w-0">
                    <div class="flex flex-wrap items-center gap-2">
                      <span class="text-xs uppercase tracking-wide text-zinc-400">Gran Población</span>
                      <span class="rounded-full {temp_styles[pregunta["compete_a"]]["badge_bg"]} px-2 py-0.5 text-xs font-medium {temp_styles[pregunta["compete_a"]]["badge_text"]}">
                        {pregunta["compete_a"]}
                      </span>
                    </div>

                    <h2 class="mt-3 text-base font-medium leading-snug break-words">
                      {pregunta["descripcion"]}
                    </h2>

                    <p class="mt-3 text-sm text-zinc-300">
                      Compete a:
                      <span class="rounded-md {temp_styles[pregunta["compete_a"]]["box_bg"]} px-2 py-1 font-semibold {temp_styles[pregunta["compete_a"]]["badge_bg"]}">
                         {pregunta["compete_a"]}
                      </span>
                    </p>

                    <p class="mt-2 text-xs text-zinc-500 font-mono">
                      ID: {pregunta["_id"]}
                    </p>
                  </div>

                  <div class="shrink-0 text-right">
                    <p class="text-sm">
                      Fallos: <span class="text-red-400 font-semibold">{pregunta["fallos"]} </span>
                    </p>
                    <p class="text-sm">
                      Aciertos: <span class="text-emerald-400 font-semibold">{pregunta["aciertos"]}</span>
                    </p>
                    <p class="mt-2 text-xs text-zinc-500">
        Delegable: <span class="text-xl font-bold {"text-red-500" if pregunta["es_delegable"] else "text-emerald-400" }">{ "Si" if pregunta["es_delegable"] else "No" }</span>
                    </p>
                  </div>
                </div>
              </div>
            </article>
          """
          html+=html_tmp

        
        
        html_footer ="""
            </section>
          <footer class="mt-10 text-xs text-zinc-500">
                <p>
                  Competencias ley bases regiemn local
                </p>
              </footer>

            </main>
          </body>
          </html>
        """
        html +=html_footer
        
        # crear archivo
        with open(os.path.join('docs', 'lbr', 'competencias_lbrl.html'), 'w', encoding='utf-8') as f:
          f.writelines(html)
          
        
      


    def generar_htmls(self):
        self.generar_archivo_ley_bases()
        for archivo_json in self.cuestionario_archivos:
            self.generar_html_cuestionario_archivo(archivo_json)
        
           
        


## todo generar archivo html para ley bases
    



if __name__ == '__main__':
    generador = Generar_HTMLs()
    generador.generar_index( str(generador.get_data_index_cuestionarios())  )
    
    generador.generar_html_cuestionario_archivo()
    generador.generar_htmls()