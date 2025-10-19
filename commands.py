import subprocess
import os 
import time


path_asturpol_game = r"E:\ESCRITORIO 2023\OPOSICIONES\desarrollo applicaciones\asturpol-game"
astro_url = 'http://localhost:4321'

init_path  = os.path.abspath('.')



def crear_commit():

    msg = input("introduce msg commit: ")

    os.chdir(init_path)
    try:
        subprocess.run(["git", "add", "."], shell=True)
        subprocess.run(["git", "commit", "-m", f'"{msg}"'], shell=True)
        subprocess.run(["git", "push"], shell=True)

    except subprocess.CalledProcessError as e:
        print("Error al ejecutar commit:", e)

def ejecutar_astro_asturpol_game():
    os.chdir(path_asturpol_game)

    try:
        subprocess.run(["npm", "run", "dev"], shell=True )
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar npm run dev: {e}")



if __name__ == '__main__':

    commands = [ 
        ejecutar_astro_asturpol_game,
        crear_commit 
    ]

    for opt, c in enumerate(commands):
        print(opt+1, c.__name__)
    selected_otp = int(input("Que ejecutar: ")) - 1

    print(f"Ejecutando commando: {commands[selected_otp].__name__}")
    commands[selected_otp]()
    

    



