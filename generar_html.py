import os
import json

class Generar_HTMLs:

    def __init__(self, ruta_cuestionario='backup'):
        self.ruta_cuestionario = ruta_cuestionario
        self.cuestionario_archivos =  os.listdir(self.ruta_cuestionario) 

        # todo arreglar color para todos
        self.border_colors = {
            '__all__': 'border-zinc-600',
            'leve': 'border-emerald-500',
            'grave': 'border-amber-400',
            'muy grave': 'border-red-500',
        }

    def generar_html_cuestionario_archivo(self, archivo_json='alcohol_y_drogas.json'):
        
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
        with open(os.path.join('html', title+'.html'), 'w', encoding='utf-8') as f:
            f.write(html)

    def generar_htmls(self):
        for archivo_json in self.cuestionario_archivos:
            self.generar_html_cuestionario_archivo(archivo_json)
           
        



    



if __name__ == '__main__':
    generador = Generar_HTMLs()
    # generador.generar_html_cuestionario_archivo()
    generador.generar_htmls()