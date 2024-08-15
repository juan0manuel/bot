import discord
from discord.ext import commands
import algoritbot as ab

intents = discord.Intents.default()
intents.message_content = True
token = ""

bot = commands.Bot(command_prefix = "%" , intents = intents)

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

bot.run(token)
