from settings import settings
import discord
# import * - es una forma rápida de importar todos los archivos en la biblioteca
from algoritbot import gen_pass, gen_emodji, flip_coin

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Habilitando el privilegio de leer los mensajes
intents.message_content = True
# Creando un bot en la variable client y transfiriéndole los privilegios
client = discord.Client(intents=intents)

# Una vez que el bot esté listo, imprimirá su nombre
@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

# Cuando el bot reciba un mensaje, enviará mensajes en el mismo canal
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('hello'):
        await message.channel.send('Hi! I am a bot!')
    elif message.content.startswith('smile'):
        await message.channel.send(gen_emodji())
    elif message.content.startswith('coin'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('pass'):
        await message.channel.send(gen_pass(10))
    else:
        await message.channel.send("Can't process this command, sorry!")

client.run(settings["TOKEN"])
