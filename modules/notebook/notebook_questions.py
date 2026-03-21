import json
from pathlib import Path
from typing import List
import pandas as pd
from pydantic import BaseModel
from datetime import datetime, timedelta, date



class FlashCard(BaseModel):
    question: str
    answer: str
    stars: int
    created_at: str
    updated_at: str
    last_time_from_last_fail:str
    fail_streak:int
    success_since_fail: int
    section: int
    topics: int
    key_words: str
    next_review_at: str
    _id: str

class Notebok_flashcards():
    
    def __init__(self, data_folder:str='data', fails_file:str='fails_register.json', current_exercise:List=[]):
        self.data_folder = data_folder
        self.fails_file = fails_file
        self.current_exercise = current_exercise
        
        self.aciertos_fallos_pregunta = []
        
        self.load_data()
    
    
    def load_data(self):
        df = pd.read_json( Path('')/self.data_folder/self.fails_file, orient='records' ).fillna('')
        self.current_exercise = df.to_dict(orient='records')
        # print(self.current_exercise)
        
        
            
        
    
    def filter_data(self):
        pass
    
    def _print_placeholder(self, text):
        placeholder = ''
        for word in text.split(" "):
            placeholder+= "_"*len(word)+" "
        print(placeholder)
        

    def make_question(self, card:FlashCard):
        ### todo
        print(card["question"])
        print(card["answer"])
        # placeholder
        self._print_placeholder(card["answer"])
        print()
        
        resp = input(card["question"]+"\n")
        
        if resp == card["answer"]:
            print("Correcto!!!")
            self.aciertos_fallos_pregunta.append({ "_id": card["_id"], "es_correcta": True })
        else:
            is_valid = input("¿Aceptar pregunta como valida?[N/y]:\n")
            
            if is_valid in ('s', 'S', 'si', 'SI', 'y', 'Y', 'yes', 'YES'):
                print("Correcto pregunta validada")
                self.aciertos_fallos_pregunta.append({ "_id": card["_id"], "es_correcta": True })
            else:        
                print(f"Incorrecto!!! \n pregunta correcta es {card["answer"]}")
                self.aciertos_fallos_pregunta.append({ "_id": card["_id"], "es_correcta": False })
 
                
    def print_failed(self):
        # todo generar un prin bonito
        # filtrar falladas 
        filtradas = [ p["_id"] for p in  self.aciertos_fallos_pregunta if p["es_correcta"] == False]
        fails_on_last_exercise = [ (p["question"]+"\n"+p["answer"]+"\n") for p in self.current_exercise if p["_id"] in filtradas  ] 
        for f in fails_on_last_exercise:
            print(f)
    
    def update_questions(self):
        full_data = None
        path = Path('')/self.data_folder/self.fails_file
        
        with open(path,'r', encoding='utf-8' ) as f:
            full_data = json.load(f)
            
        for question in self.aciertos_fallos_pregunta:
            print(question["_id"])
            for i, card in enumerate(full_data):
                if question["_id"] == card["_id"]:
                    if question["es_correcta"]:
                        full_data[i] = {
                            **card,
                            "success_since_fail": card["success_since_fail"]+1,
                            "updated_at": datetime.now().strftime('%d-%m-%Y'),
                            "fail_streak":0,
                            "next_review_at": (date.today() + timedelta(days=7)).strftime("%d-%m-%Y"), 
                        }## todo formatear fecha
                    else:
                        full_data[i] = {
                            **card,
                            "success_since_fail": 0,
                            "updated_at": datetime.now().strftime('%d-%m-%Y'),
                            "last_time_from_last_fail": datetime.now().strftime('%d-%m-%Y'),
                            "fail_streak": card["fail_streak"] + 1,
                            "next_review_at":  (date.today() + timedelta(days=3)).strftime("%d-%m-%Y"), 
                        }
        print(full_data[0])  
        
        ## todo dumpear al json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(full_data, f, indent=4, ensure_ascii=False)          
        
            
        
        

    
    
    
    
    
if __name__ == '__main__':
    flash_cards = Notebok_flashcards()
    flash_cards.make_question(flash_cards.current_exercise[0])
    flash_cards.make_question(flash_cards.current_exercise[1])
    flash_cards.make_question(flash_cards.current_exercise[2])
    # flash_cards.print_failed()
    flash_cards.update_questions()
    
    