import discord
from discord.ext import commands
import random
import requests

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def saludar(ctx):
    await ctx.send('¡Hola!Soy un bot de prueba!')

@bot.command()
async def sumar(ctx, a: int, b: int):
    await ctx.send(f'La suma de {a} y {b} es {a + b}')

@bot.command()
async def lanzar_dado(ctx):
    resultado = random.randint(1, 6)
    if resultado == 1:
        await ctx.send('¡Has sacado un 1! ¡Intenta de nuevo!')
    elif resultado == 6:
        await ctx.send('¡Has sacado un 6! ¡Felicidades!')
    else:
        await ctx.send(f'Has sacado un {resultado}. ¡Sigue jugando!')

@bot.command()
async def generar_contraseña(ctx):
    elements = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""

    for i in range(8):
        password += random.choice(elements)
    await ctx.send(f"Tu contraseña es: {password}")

def get_weather_info(city):
    base_url = f"https://wttr.in/{city}?format=%C+%t&lang=es"
    response = requests.get(base_url)
    if response.status_code == 200:
        return response.text.strip()
    else:
        return "No se pudo obtener la información del clima. Por favor, inténtalo más tarde."
    
@bot.command()
async def weather(ctx, *, city):
    weather_info = get_weather_info(city)
    await ctx.send(f"Clima en {city}: {weather_info}")

bot.run()