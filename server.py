# uvicorn main:app --reload
###Documentacion Swagger => http://localhost:8000/docs

from fastapi import FastAPI, HTTPException
import os
import random
from cuestionario import Cuestionario


app = FastAPI()


@app.get("/preguntas_cuestionarios/")
def preguntas_cuestionarios():
    pass



@app.get("/preguntas_cuestionario/{tema}")
def get_cuestionario_por_tema(tema:str):
    opt = os.listdir('data') 

    if tema in opt:
        q = Cuestionario('data',tema, 'backup')
        q.importar_backup() # archivo con conteo de fallos

        q.cargar_data()

        data = {
            "data": q.backup_file,
            "opts": list(dict(q.data_brute["abrr_opts"]))
        }
        
        return data
        
        
    raise HTTPException(status_code=404, detail='Contact Not Found')
    



