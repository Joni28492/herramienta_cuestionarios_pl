# todo CSV parser
import os
import json

class CSV_Parser:
    def __init__(self, folder_path = 'csv', folder_parsed = ' chained', file_to_insert = 'mix_questions.json' ):
        self.folder_path = folder_path
        self.csv_list = os.listdir(self.folder_path)
        self.questions = []

    def fill_questions(self, file=''):
        print(file)

    def run(self):
        print("run")
        self.fill_questions( self.csv_list[0] )

if __name__ == '__main__':
    Csv_parser = CSV_Parser()
    Csv_parser.run()