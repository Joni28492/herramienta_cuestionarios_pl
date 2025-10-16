import sys
import subprocess

print(sys.platform)
nombre_enviroment = 'enviroment'
path_win = f'.\\{nombre_enviroment}\\Scripts\\activate'
path_linux = f'.\\{nombre_enviroment}\\bin\\activate'

if sys.platform == "win32":
    print("activar en windows")
    subprocess.run([path_win])
else:
    print("activar en linux")
# todo pendiente de hacer