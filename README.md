# Proyecto de Configuración de Dispositivos de Red

Este proyecto automatiza la configuración de interfaces y el enrutamiento en dispositivos de red, basándose en un archivo CSV para definir los detalles de cada interfaz y su configuración de enrutamiento. Utiliza **Jinja2** para renderizar una plantilla de configuración y **Nornir** para implementar la configuración en dispositivos de red.

## Requisitos

- Python 3.7+
- **Nornir**: Biblioteca de automatización para orquestar tareas en dispositivos de red.
- **Netmiko**: Plugin de Nornir para interactuar con dispositivos de red a través de SSH.
- **Jinja2**: Biblioteca de plantillas para crear configuraciones dinámicas.
  
Puedes instalar los requisitos utilizando:
```bash
pip install nornir jinja2 nornir_netmiko nornir_utils
```

## Uso

### 1. Crear el archivo CSV de interfaces.

Primero, ejecuta **router_interfaces.py** para crear el archivo router_interfaces.csv con datos de ejemplo para cada interfaz del dispositivo.

```bash
python3 router_interfaces.py
```

### 2. Generar y aplicar la configuración

Ejecuta el script **config.py** para procesar el archivo CSV, generar configuraciones en base a la plantilla, y enviar las configuraciones a los dispositivos de red.

```bash
python3 config.py
```