# Herramienta para preparar oposicion

Requiere tener la instalacionde python en el equipo

```
python -m venv venv
```

para activar el entorno
```
# windows
./venv/Scripts/activate

# linux/MAC OS
source venv/bin/activate
```

instalacion librerias

```
pip install requeriments.txt
```


## Diferentes Modulos

### cuestionarios
Este modulo se basa en sistema de listados o columnas, cuando tenemos diferentes listados, o como puede ser infracciones con diferente gravedad, creamos un JSON 
con sus respectivas abreviaturas en `/modules/cuestionarios/nombre_archivo.json`

formato

```
{
 
    "abrr_opts": {
        "leve": ["l", "leve", "LEVE", "L"],
        "grave": ["g", "grave", "GRAVE", "G"],
        "muy grave": ["mg", "muy grave", "MUY GRAVE", "MG"]
    },
    "leve": [
        "inf1",   
        "inf2",   
    ],
    "grave": [
        ...
    ],
    "muy grave": [
        ...
    ]

}
```

y una vez finalizado lo contabilizara en la carpeta `backup` del modulo

es posible que la primera vez de un fallo al crear el archivo en backup, con reiniciarlo sin borrar el archivo es suficiente


### test selector

### order system

### informes 


#### otros sin implementar o de menor relevancia