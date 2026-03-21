import json
from pathlib import Path
import pandas as pd
from datetime import datetime
import hashlib
from pydantic import BaseModel
from typing import List


import unicodedata
import re



    
# 

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
        # text = unicodedata.normalize("NFC", text).encode('ascii', 'ignore').decode('utf-8')
        # text = re.sub(r'[^\w\s]','', text)
        # text = re.sub(r'\s+',' ', text).strip()
        replacements = (("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"))
        for old, new in replacements:
            text=text.replace(old, new)
        
        return text

    def load_fail_register(self):
        
        with open( Path('') /self.data_folder/self.fails_register_file, 'r', encoding='utf-8') as f:
            self.fails_register=json.load(f)
            
        
    def load_current_csv(self):
        
        df = pd.read_csv(Path('') /self.xls_folder/self.current_file, sep=';', encoding='utf-8-sig').fillna('')
        df = df.to_dict(orient="records", ) # con el orient no guarda el archivo
        
        #parsear
        for item in df:

            
           
            
            self.current_csv.append({
                **item,
                '_id':self._hash_calculate(item["question"], item["answer"]),
                "answer": self._normalize_str(item["answer"]),
                "stars":1,
                'created_at': datetime.now().strftime('%d-%m-%Y'),
                'fail_streak': 0,
                'success_since_fail':0,
                'key_words': ''
            })
           
            
        # print(self.current_csv[0])
    
    
    def join_questions(self):
        join_csv = self.fails_register + self.current_csv         
        return join_csv
        
    
    
    def dump_fails_register(self, data):
        # print(self.fails_register_file)
        with open( Path('')/self.data_folder/self.fails_register_file, 'w', encoding='utf-8' ) as f:
            json.dump(data,f, indent=4, ensure_ascii=False)
            
        
        

if __name__ == "__main__":
    
   
    notebook_csv_update = NotebookCSVUpdate(
        # xls_folder="xls", 
        # data_folder="data", 
        # fails_register_file='fails_register.json',
        # current_file='current.csv',
        # fails_register=[], 
        # current_csv=[]
    )
    notebook_csv_update.load_fail_register()
    notebook_csv_update.load_current_csv()
    notebook_csv_update.dump_fails_register( notebook_csv_update.join_questions() )
   
    
   
    