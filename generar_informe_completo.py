import json
import os


class Informe_generator():

    def __init__(self):
        self.backup_path_list = []
        self.backup_list = []

        self.test_paths = []
        self.test_list = []
        
        self.report_path = 'informe_completo'

        
    
    def seed_backup_list(self):
        self.backup_path_list = os.listdir("backup")
        for file_name in self.backup_path_list:
            temp_list = []
            with open(os.path.join('backup', file_name), 'r', encoding='utf-8') as f:
                temp_list = json.load(f)
            for s, item in enumerate(temp_list):
                temp_list[s]= {
                    **item,
                    "file_name_secction":file_name.split(".")[0].replace("_", " "),
                    "mode": "columns system" 
                }
            self.backup_list += temp_list


    def seed_test_fails_date(self):
        self.test_paths = os.listdir("test")
        for file_name in self.test_paths:
            temp_list = []
            with open(os.path.join("test", file_name), 'r', encoding='utf-8') as f:
                temp_list = json.load(f)
            for s, item in enumerate(temp_list):
                temp_list[s] = {
                    **item,
                    "date": file_name.split(".")[0],
                    "mode": "test system"
                }
            self.test_list += temp_list


    def generate_report(self):
        reporte = []
        reporte += self.test_list + self.backup_list
        
        with open(os.path.join(self.report_path, "informe_completo.json"), 'w', encoding='utf-8') as f:
            json.dump(reporte, f, indent=4, ensure_ascii=False)

        


    def run(self):
        print("Run")
        self.seed_backup_list()
        self.seed_test_fails_date()
        self.generate_report()


if __name__ == '__main__':
    generador = Informe_generator()

    generador.run()