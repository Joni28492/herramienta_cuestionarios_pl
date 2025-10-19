import subprocess
import os 
import time


path_asturpol_game = r"E:\ESCRITORIO 2023\OPOSICIONES\desarrollo applicaciones\asturpol-game"
astro_url = 'http://localhost:4321'

init_path  = os.path.abspath('.')


os.chdir(init_path)
try:
    subprocess.run(["git", "add", "."], shell=True)
    subprocess.run(["git", "commit", "-m", '"prueba script python"'], shell=True)
    subprocess.run(["git", "push"], shell=True)

except subprocess.CalledProcessError as e:
    print(e)


# os.chdir(path_asturpol_game)

# try:
#     subprocess.run(["npm", "run", "dev"], shell=True )
    
#     time.sleep(10)
    
    
# except subprocess.CalledProcessError as e:
#     print(f"Error al ejecutar npm run dev: {e}")





