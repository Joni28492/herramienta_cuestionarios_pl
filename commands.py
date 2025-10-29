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

def ejecutar_cuestionario():
    os.chdir(init_path)

    try:
        subprocess.run(["python.exe", "cuestionario.py"], shell=True )
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar Cuestionario: {e}")

def ejecutar_test_selector():
    os.chdir(init_path)

    try:
        subprocess.run(["python.exe", "test_selector.py"], shell=True )
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar Cuestionario: {e}")

def activar_enviroment():
    os.chdir(init_path)

    try:
        subprocess.run([".\\enviroment\\Scripts\\activate"], shell=True )
    except subprocess.CalledProcessError as e:
        print(f"Error al activar env: {e}")

def generar_informe_completo():
    os.chdir(init_path)

    try:

        subprocess.run(["python.exe", "generar_informe_completo.py"], shell=True )
    except subprocess.CalledProcessError as e:

        print(f"Error al generar informe completo: {e}")


if __name__ == '__main__':

    commands = [ 
        ejecutar_astro_asturpol_game,
        crear_commit,
        ejecutar_cuestionario,
        ejecutar_test_selector,
        generar_informe_completo
        # activar_enviroment
    ]

    for opt, c in enumerate(commands):
        print(opt+1, c.__name__)
    selected_otp = int(input("Que ejecutar: ")) - 1

    print(f"Ejecutando commando: {commands[selected_otp].__name__}")
    commands[selected_otp]()
    

    



