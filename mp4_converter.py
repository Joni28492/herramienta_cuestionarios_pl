from pydub import AudioSegment
import os
# necesita instalra FFMPG
folder = "audios_notebookllm"
m4a_file = 'Homicidio,_Lesiones_y_Libertad__Desgranando_los_Delitos_Clave_d.m4a'
mp3_salida = 'Homicidio,_Lesiones_y_Libertad__Desgranando_los_Delitos_Clave_d.mp3'


audio = AudioSegment.from_file( os.path.join(folder, m4a_file), format='m4a' )

audio.export( os.path.join(folder,mp3_salida), format='mp3', bitrate='192k')