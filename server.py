# uvicorn main:app --reload
###Documentacion Swagger => http://localhost:8000/docs

from fastapi import FastAPI, HTTPException
import os
from cuestionario import Cuestionario
from pymongo import MongoClient
import json



app = FastAPI()
client = MongoClient('localhost', 27017)
db = client["oposiciones"]
categorias_col = db["categorias_cuestionario"]
cuestionarios_col = db["cuestionarios"]
tests_col = db["tests"]







#ya agregadas
@app.get("/categorias-cuestionario")
def categorias_cuestionario():
    
    categorias = [cat[:-5].replace("_", "-") for cat in os.listdir('backup')]
    
    for cat in categorias:
        categorias_col.insert_one({"categoria":cat})

    return categorias


# ya insertado
@app.get("/cuestionarios_seed")
def cuestionario_seed_backup():
    
    categorias_name = [cat for cat in os.listdir('backup')]
    
    for cat in categorias_name:
        temp_file = None
        abbr_options = None

       
        with open(os.path.join('data', cat), 'r', encoding='utf-8') as f:
            abbr_options = list(dict(json.load(f)).keys())
            # print(abbr_options)

        with open(os.path.join('backup', cat), 'r', encoding='utf-8') as f:
            temp_file = json.load(f)

            for file in temp_file:
                file["categoria"] = cat[:-5].replace("_", "-")
                file["opciones"] = [ otp for otp in abbr_options if otp != 'abrr_opts']
            
            cuestionarios_col.insert_many(temp_file)           
        

    return "seed exitoso!!!"

@app.get("/tests_seed")
def test_seed():

    root_path = 'E:\\ESCRITORIO 2023\\OPOSICIONES\\desarrollo applicaciones\\asturpol-game\\src\\pages\\api\\tests\\db'

    bloques = os.listdir(root_path)
    # print(bloques)

    for b in bloques:
        temas = os.listdir(os.path.join(root_path, b))
        if b == 'otras-preparaciones':
            continue

        for t in temas:
            complete_path =  os.path.join(root_path, b, t) 
            temp_file = None
            #  importar archivos y cargar
            with open(complete_path, 'r', encoding='utf-8') as f:
                temp_file = json.load(f)
                
                for file in temp_file:
                    file["bloque"] = b
                    file["tema"] = t[1:-5]
            tests_col.insert_many(temp_file)



    return "SEED EXITOSO!!"


# ya agregado
@app.get("/seed_convocatorias")
def seed_convocatorias():

    root_path = 'E:\\ESCRITORIO 2023\\OPOSICIONES\\desarrollo applicaciones\\asturpol-game\\src\\pages\\api\\tests\\db\\otras-preparaciones'

    convocatorias = os.listdir(root_path) 

    	
    for convocatoria in convocatorias:
        temp_file = None
        root_path = 'E:\\ESCRITORIO 2023\\OPOSICIONES\\desarrollo applicaciones\\asturpol-game\\src\\pages\\api\\tests\\db\\otras-preparaciones'
 
        # print(os.listdir( os.path.join(root_path, convocatoria) ))
        tests = os.listdir( os.path.join(root_path, convocatoria) )
        for test in tests:
            tipo = ''
            if "aux" in test: tipo = "auxiliar"
            if "interino" in test: tipo = "interino"
            if "especificas" in test: tipo = "especificas"
            if "simulacro" in test: tipo = "simulacro"
            # print(test[1:-5], convocatoria.upper(), tipo)
            complete_path = os.path.join(root_path, convocatoria, test)
            # print(complete_path)
            with open(complete_path, 'r', encoding='utf-8') as f:
                temp_file = json.load(f)
            
            for file in temp_file:
                file["ayto"] = convocatoria
                file["tipo_bolsa"] = tipo
            
            tests_col.insert_many(temp_file)



    

    return "SEED EXITOSO"