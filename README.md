# Python PRO Test

### Instrucciones de Uso

**a. Crear una cuenta en Discord:**

1. Si aún no tienes una cuenta, regístrate en Discord.

**b. Crear una aplicación en Discord:**

1. Ve a la [página de desarrolladores de Discord](https://discord.com/developers/).
2. Haz clic en “New Application” y asigna un nombre a tu aplicación.

**c. Autorizar el bot en un servidor:**
1. En la aplicación recién creada, dirígete a la sección “OAuth2” y selecciona “URL Generator”.
2. Marca los permisos necesarios, incluyendo “Manage Channels”.
3.	Copia el enlace generado y pégalo en una nueva pestaña del navegador.
4.	Autoriza el acceso del bot en el servidor donde eres administrador.

**d. Obtener el Token del Bot:**
1. En la sección “Bot”, copia el token del bot.

**e. Configurar el archivo de entorno:**
1. Dentro de la carpeta de este proyecto, crea un archivo llamado .env.
2. Abre el archivo .env y añade la variable TOKEN_BOT de la siguiente forma: TOKEN_BOT="tu_token_aqui"

**f. Ejecucion de consultas desde discord:**
1. Acceder al canal #general del servidor
2. Solicitar la busqueda a Wikipedia desde el comando '!wiki [consulta]'

## Estado del Proyecto
- **Finalizado**

## Estructura de Directorios y Archivos Resultantes

    Discord BOT
    │
    ├── row_data # CSV's
    │
    ├── main.py
    │
    ├── .gitignore
    │
    ├── requirements.txt
    |
    │-- LICENSE.md
    │
    └── README.md

## Tecnologías Utilizadas
- **Programing language:**

  - **Python**
    - *discord.py*
    - *wikipedia*
    - *dotenv*

## Instalación de Paquetes
```bash
pip3 install -r requirements.txt
```