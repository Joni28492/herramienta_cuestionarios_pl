import json
import os 
import random

class Order_system:
    """
    cargamos como un [] base con el orden OK
    barajamos
    cada item tendra el nº del indice asignado
    escribiremos en un input 
    y cada caracter comprobamos indice a indice en una lista de verificados



    """

    def __init__(self, order_folder, order_file_path):
        self.order_folder = order_folder
        self.order_file_path = order_file_path
        self.original_order_sequence = None
        self.random_order = []
        
        self.user_selection = None
        
        self.verificados = []

        


        self.main()


    def cargar_order_sequence(self):
        with open(os.path.join(self.order_folder, self.order_file_path), 'r', encoding='utf-8') as f:
            self.original_order_sequence = json.load(f)

    def barajar_sequencia(self):
        self.random_order = self.original_order_sequence.copy()
        random.shuffle(self.random_order)

    def pretty_print(self, lista, print_num=True):
        for i,item in enumerate(lista):
            if print_num:
                print(i, end='.-   ')
            print( item)


    def input_user_order(self):
        max_digits = len(self.original_order_sequence)
        while True:
            self.user_selection = input(f"Introduce el orden en relacion a la lista que has obtenido (MAX: {max_digits} digitos) :")
            # todo comprobar que sean num
            
            if len(self.user_selection) == max_digits:
                break
            print(f"Debe tener {max_digits} digitos")
        
    def check_correct_numbers_input(self):
        pass

    def comprobar_orden(self):
        splited_order = list(self.user_selection)
        print(splited_order)
        
        for i, item in enumerate(self.original_order_sequence):
            print(f"valor original: {item}")
            print(f"Seleccionado por orden: {self.random_order[int(self.user_selection[i])]} ")
            print()

            
            if item == self.random_order[int(self.user_selection[i])]:
                self.verificados.append("✅")
                # print("✅✅✅ ¡Correcto!")
            else:
                self.verificados.append("❌")
                # print("❌❌❌ Incorrecto")
        print(self.verificados)
# todo estoy por aqui


    def print_pretty_verifications(self):
        print(self.verificados)

    def orden_es_correcto(self):
        return True


    def main(self):
        self.cargar_order_sequence()
        self.barajar_sequencia()
        # self.pretty_print(self.original_order_sequence)
        self.barajar_sequencia() 
        print()
        self.pretty_print(self.random_order, True)
        print()
        ## punto de inicio seleccion
        self.input_user_order()

        # comprobar cada indice
        self.comprobar_orden()
        
        # print resultado verificacion

        # validar si todas estan en orden
        
        
       
        




if __name__ == '__main__':
    

    order = Order_system('order', 'cp_art_30_soportes_difusion.json')
