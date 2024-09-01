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
token = "Token"

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

@bot.command(name = "PRE")
async def proyect(ctx):
    await ctx.send("¡Hola! 🌍//  Nos emociona que estés considerando unirte al Proyecto Reciclable Educativo (P.R.E.). Este proyecto es una oportunidad increíble para aprender más sobre cómo cuidar nuestro planeta a través de prácticas ecológicas y la reducción de residuos. ¡Con tu participación, podemos hacer un cambio positivo en el mundo y en tu vida!, Usa los comandos %Basuras (Color de la basura deseada),%Cambios (Material que deseas cambiar por uno mas sostenible) para lograr cambiar el mundo")
    @bot.command(name = "Basuras")
    async def paper(ctx, color: str):
        color = color.lower()  # Asegura que el color sea manejado en minúsculas
        response = ""

        if color in ["verde", "green", "vert"]:
            response = "🟢 **Basura Orgánica:** Aquí se botan los restos de comida, cáscaras de frutas, y otros desechos biodegradables."
        elif color in ["azul", "blue", "bleu"]:
            response = "🔵 **Papel y Cartón:** Aquí se botan papeles, revistas, cajas de cartón, y otros materiales similares."
        elif color in ["amarillo", "yellow", "jaune"]:
            response = "🟡 **Plásticos y Metales:** Aquí se botan botellas de plástico, latas, y otros envases plásticos o metálicos."
        elif color in ["gris", "gray", "grey"]:
            response = "⚫ **Residuos No Reciclables:** Aquí se botan restos de cerámica, papel sucio, pañales, y otros residuos que no pueden reciclarse."
        elif color in ["rojo", "red", "rouge"]:
            response = "🔴 **Desechos Peligrosos:** Aquí se deben depositar productos químicos, pilas, y otros materiales peligrosos."
        elif color in ["marrón", "brown", "brun"]:
            response = "🟤 **Desechos Orgánicos de Jardín:** Aquí se botan hojas, ramas, y otros desechos vegetales."
        else:
            response = "❌ Lo siento, no reconozco ese color. Por favor, elige entre verde/green/vert, azul/blue/bleu, amarillo/yellow/jaune, gris/gray/grey, rojo/red/rouge, o marrón/brown/brun."

        await ctx.send(response)

    @bot.command(name = "Cambios")
    async def change(ctx, cambio:str):
        if cambio == "Bolsas":
            with open(f"PRE/bolsas.PNG","rb") as f:
                picture = discord.File(f)
            await ctx.send(file = picture)
            await ctx.send(f"Una alternativa al uso de bolsas de plástico es optar por bolsas de papel o de tela. Las bolsas de papel son biodegradables y se descomponen más fácilmente en el medio ambiente, lo que reduce el impacto ecológico. Las bolsas de tela, por otro lado, son reutilizables y duraderas, lo que les otorga una segunda vida útil y disminuye la necesidad de producir nuevas bolsas constantemente. Al elegir estas opciones, contribuimos a un menor uso de plásticos y ayudamos a proteger nuestro planeta.")
        elif cambio == "Pitillos":
            with open(f"PRE/pitillos.png","rb") as f:
                picture = discord.File(f)
            await ctx.send(file=picture)
            await ctx.send(f"Una alternativa a los pitillos de plástico sería utilizar pitillos de papel o de materiales reutilizables como el acero o el bambú. Estos materiales son más fáciles de degradar y ofrecen una opción más sostenible para el medio ambiente, ayudando a reducir la cantidad de residuos plásticos que contaminan los océanos y la tierra.")
        elif cambio == "Vasos":
            with open(f"PRE/vasos.png","rb") as f:
                picture = discord.File(f)
            await ctx.send(file=picture)
            await ctx.send(f"Una alternativa a los vasos de plástico sería utilizar vasos de papel, vidrio, acero inoxidable o materiales biodegradables como el PLA (ácido poliláctico). Estos materiales no solo son más fáciles de degradar, sino que también pueden ser reutilizados, lo que reduce significativamente la cantidad de residuos plásticos en el medio ambiente. Además, optar por vasos reutilizables en lugar de desechables ayuda a disminuir la contaminación y promueve un estilo de vida más sostenible.")

    @bot.command(name = "Plantando")
    async def practicando(ctx):
        await ctx.send(f"Gracias a ti plantaremos un arbolito en este chat :deciduous_tree:")

bot.run(token)
