from abc import ABC
import os



class Cuestionario(ABC):
    def __init__(self, data_folder, file, bacup_folder, question_number=10):
        self.data_folder = data_folder
        self.file = file
        self.bacup_folder = bacup_folder
        self.question_number = question_number


        self.answer_otp = []
        self.raw_data = None
        self.cuestionario = []
        self.current_fails = None


    
    


if __name__ == "__main__":
    pass
