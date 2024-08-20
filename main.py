# Importación de librerías del sistema
import os
import re

# Importación de librerías especializadas
from dotenv import load_dotenv
import discord
from discord.ext import commands
import wikipedia
import pandas as pd

path_dataset = 'data/row/users_queries.csv'

if os.path.isfile(path_dataset):
    df_queries = pd.read_csv(path_dataset)
else:
    df_queries = pd.DataFrame(columns=['Usuario','Consulta'])

# Cargar variables de entorno
load_dotenv()
# Constante que almacena el token para acceder al bot
BOT_TOKEN = os.getenv('TOKEN_BOT')

# Aqui se configuran los intents con los permisos de acceso
intents = discord.Intents.default() # Por defecto se establecen todos en 'False'
intents.message_content = True  # Se habilita el acceso al contenido de los mensajes
intents.members = True  # Se habilita el acceso a los eventos relacionados con los miembros

# Aqui se crea la instancia del bot con el prefijo y la instancia con los intents necesarios
bot = commands.Bot(command_prefix="!", intents=intents)

def elimina_signos_inecesarios(resultado):
    '''
    Elimina signos inecesarios del resultado arrojado por wWikipedia.

    Args:
        resultado (str): Resultado retornado por la funcion que busca en Wikipedia.

    Returns:
        Str: Retorna el resultado sin los signos inecesarios.
    '''
    expression_regular = "\[[^]]*\]"
    patron_regular = re.compile(expression_regular)
    resultado = patron_regular.sub('', resultado)
    return resultado

# Funcion para la busqueda en wikipedia
def buscar_wikipedia(consulta):
    """
    Busca un resumen de un artículo en Wikipedia en español.

    Args:
        consulta (str): El término de búsqueda proporcionado por el usuario en Discord.

    Returns:
        str: Un resumen del artículo de Wikipedia si se encuentra.
             En caso de ambigüedad, devuelve un mensaje solicitando más especificidad.
             Si no se encuentra ningún artículo, devuelve un mensaje indicándolo.
             Captura otros errores y los reporta al usuario.
    """
    try:
        wikipedia.set_lang("es")  # Establece el idioma de búsqueda en español
        resultado = wikipedia.summary(consulta, sentences=4)
        resultado = elimina_signos_inecesarios(resultado)
        return resultado
    except wikipedia.exceptions.DisambiguationError:
        return f"La búsqueda '{consulta}' es ambigua. Por favor, sé más específico."
    except wikipedia.exceptions.PageError:
        return f"No se encontró ningún artículo relacionado con '{consulta}' en Wikipedia."
    except Exception:
        return "Error al realizar la búsqueda en Wikipedia."

# Evento encargado de detectar cuando el bot esta funcionando
@bot.event
async def on_ready():
    """
    Evento que se ejecuta cuando el bot está listo.
    Establece la presencia del bot y lo marca como activo.
    """
    print(f"Bot {bot.user.name} is ready.")
    await bot.change_presence(activity=discord.Game(name="!pomoc"))

# evento encargado de detectar un nuevo usuario
@bot.event
async def on_member_join(member):
    # Obtengo la info canal
    channel = discord.utils.get(member.guild.text_channels, name="general")
    
    # Si el canal existe, se envia el mensaje de bienvenida personalizado
    if channel:
        await channel.send(f"¡Bienvenido/a {member.mention} al servidor! 🎉")

# Se define comando con el que se llamara a la funcion de buscar en wikipedia
@bot.command()
async def wiki(ctx, *, consulta):
    global df_queries
    usuario_consulta = ctx.author.name
    nueva_fila = pd.DataFrame({'Usuario':[usuario_consulta], 'Consulta':[consulta]})
    df_queries = pd.concat([df_queries, nueva_fila], ignore_index=True)
    df_queries.to_csv(path_dataset, index=False)
    resultado = buscar_wikipedia(consulta)
    await ctx.send(resultado)

# Se realiza la ejecucion del bot
bot.run(BOT_TOKEN)