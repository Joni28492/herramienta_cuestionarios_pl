FROM ubuntu:22.04

# 1. Instalar Python y pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# 2. Carpeta de trabajo
WORKDIR /app

# 3. (Opcional) Instalar dependencias de Python
# COPY requirements.txt .
# RUN pip3 install -r requirements.txt
RUN pip3 install colorama

# 4. Copiar el código
COPY . .

# 5. Por defecto, entrar en bash para que tú elijas qué .py ejecutar
CMD ["bash"]
