Python PRO Test

Este proyecto es parte del test del curso ‘Python PRO’ de Kodland LATAM. Consiste en un bot para Discord que da la bienvenida a cada nuevo usuario en el canal general del servidor autorizado y realiza búsquedas en Wikipedia mediante el comando !wiki seguido del término de búsqueda. Si encuentra información, el bot devolverá un resumen.

Instrucciones de Uso

	1.	Crear una cuenta en Discord:
	  •	Si aún no tienes una cuenta, regístrate en Discord.
	2.	Crear una aplicación en Discord:
	  •	Ve a la página de desarrolladores de Discord.
	  •	Haz clic en “New Application” y asigna un nombre a tu aplicación.
	3.	Autorizar el bot en un servidor:
	  •	En la aplicación recién creada, dirígete a la sección “OAuth2” y selecciona “URL Generator”.
	  •	Marca los permisos necesarios, incluyendo “Manage Channels”.
	  •	Copia el enlace generado y pégalo en una nueva pestaña del navegador.
	  •	Autoriza el acceso del bot en el servidor donde eres administrador.
	4.	Obtener el Token del Bot:
	  •	En la sección “Bot”, copia el token del bot.
	5.	Configurar el archivo de entorno:
	  •	Dentro de la carpeta de este proyecto, crea un archivo llamado .env.
	  •	Abre el archivo .env y añade la variable TOKEN_BOT de la siguiente forma: TOKEN_BOT="tu_token_aqui"

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

## Personas Desarrolladoras del Proyecto:
- [IanCristianAriel](https://github.com/ianCristianAriel)