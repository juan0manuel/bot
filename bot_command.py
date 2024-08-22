import discord
from discord.ext import commands
import algoritbot as ab
import os,random
import requests

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

intents = discord.Intents.default()
intents.message_content = True
token = "your token plis "

bot = commands.Bot(command_prefix = "%" , intents = intents, help_command = None)

@bot.event
async def on_ready():
    print(f"Hola soy: {bot.user}")

@bot.command(name = "Hi")
async def hello(ctx,nombre):
    await ctx.send(f"Hola soy: {bot.user} un gusto conocerte {nombre}")

@bot.command(name = "psw")
async def password(ctx,a:str,b:int):
    nombre = str(a)
    cr = ab.gen_pass(b)
    await ctx.send(f"Su contraseña es: {cr}{nombre}")

@bot.command(name = "HELP")
async def helpme(ctx):
    help_text = "**Comandos disponibles:**\n"
    for command in bot.commands:
        help_text += f"- `%{command.name}`\n"
    
    await ctx.send(help_text)

@bot.command(name = "momasos")
async def mem(ctx,a):
    if a == "memes":
        j = random.choice(os.listdir("memes"))
        with open(f"memes/{j}","rb") as f:
            picture = discord.File(f)
        await ctx.send(file = picture)
    elif a == "chamba":
        i = random.choice(os.listdir("chamba"))
        with open(f"chamba/{i}","rb") as f:
            picture = discord.File(f)
        await ctx.send(file = picture)

@bot.command(name = "momasos_porcentaje")
async def mem(ctx):
    archivos_memes = os.listdir("memes")
    probabilitis=[0.1,0.3,0.6]
    a = random.choices(archivos_memes, weights=probabilitis)[0]
    with open(f"memes/{a}","rb") as f:
        picture = discord.File(f)
    await ctx.send(file = picture)

@bot.command(name = "pato")
async def duck(ctx):
    image = get_duck_image_url()
    await ctx.send(image)
bot.run(token)
