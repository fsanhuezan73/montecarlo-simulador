# Imagen base oficial de Python
FROM python:3.11-slim

# Establecer directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar archivos del proyecto
COPY . .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto donde correrá Flask
EXPOSE 5001

# Ejecutar la aplicación
CMD ["python", "app.py"]