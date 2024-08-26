# Python PRO Test

Este proyecto es parte del test del curso ‘Python PRO’ de Kodland LATAM. Consiste en un bot para Discord que da la bienvenida a cada nuevo usuario en el canal general del servidor autorizado y realiza búsquedas en Wikipedia mediante el comando !wiki seguido del término de búsqueda. Si encuentra información, el bot devolverá un resumen.

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