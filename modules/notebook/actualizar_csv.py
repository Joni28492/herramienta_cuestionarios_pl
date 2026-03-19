import json
from pathlib import Path
import pandas as pd
from datetime import datetime
import hashlib
from pydantic import BaseModel
from typing import List


import unicodedata
import re


class NotebookQuestion(BaseModel):
    
    id: str
    question: str
    answer: str
    stars:int
    created_at: str
    fail_streak: int
    success_since_fail:int
    key_words: str

class NotebookCSVUpdate():
    
    def __init__(self, xls_folder:str="xls", data_folder:str="data", fails_register_file:str= 'fails_register.json', current_file='current.csv', fails_register:List=[], current_csv:List=[]):
        self.xls_folder = xls_folder
        self.data_folder = data_folder
        self.fails_register_file = fails_register_file
        self.current_file = current_file
        self.fails_register = fails_register
        self.current_csv = current_csv

    def _hash_calculate(self, question:str, answer:str):
        text = f'{question}|{answer}'
        return hashlib.md5(text.encode("utf-8")).hexdigest()
    
    def _normalize_str(self, text:str):
        text = text.lower()
        text = unicodedata.normalize("NFKC", text).encode('ascii', 'ignore').decode('utf-8')
        text = re.sub(r'[^\w\s]','', text)
        text = re.sub(r'\s+',' ', text).strip()
        return text

    def load_fail_register(self):
        
        with open( Path('') /self.data_folder/self.fails_register_file, 'r', encoding='utf-8') as f:
            self.fails_register=json.load(f)
            
        
    def load_current_csv(self):
        
        df = pd.read_csv(Path('') /self.xls_folder/self.current_file, sep=';', encoding='utf-8-sig').fillna('')
        df = df.to_dict(orient="records") # con el orient no guarda el archivo
        
        #parsear
        for item in df:

            
           
            
            self.current_csv.append({
                **item,
                'id':self._hash_calculate(item["question"], item["answer"]),
                "answer": self._normalize_str(item["answer"]),
                "stars":1,
                'created_at': datetime.now().strftime('%d%m%Y'),
                'fail_streak': 0,
                'success_since_fail':0,
                'key_words': ''
            })
           
            
        print(self.current_csv[0])
    
    
    def update_question_on_register(self, question:NotebookQuestion, missed:bool=False):
        ### comprobar si existe cada uno de los items en el archivo global
        _id = question.id
        
        
        
        for i, item in enumerate(self.fails_register):
            if item["id"] == _id:
                # actualizar pregunta
                self.fails_register[i] = {
                    **item,
                    'updated_at': datetime.now().strftime('%d%m%Y'),
                    'fail_streak': item["fail_streak"] + 1 if missed else 0,
                    'success_since_fail': item["success_since_fail"] + 1 if not missed else 0,
                }
       
        
         
        # añadir pregutna pregunta 
        self.fails_register.append({
                'id':self._hash_calculate(item["question"], item["answer"]),
                "answer": item["answer"].lower(),
                "stars":1,
                'created_at': datetime.now().strftime('%d%m%Y'),
                'fail_streak': 0,
                'success_since_fail':0,
                'key_words': ''
            })
        
    def fill_fails_register(self):
        for item in self.current_csv:
            self.update_question_on_register(item)
            
        print(self.fails_register[0])
    
    def dump_fails_register(self):
        pass
            
        
        

if __name__ == "__main__":
    
    notebook_csv_update = NotebookCSVUpdate()
    notebook_csv_update.load_fail_register()
    notebook_csv_update.load_current_csv()
    notebook_csv_update.fill_fails_register()
    
   
    