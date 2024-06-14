import os
import discord
import requests
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

# Load environment variables
WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')
BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command(name='say_hello')
async def say_hello(ctx):
    response = requests.post(WEBHOOK_URL, json={"content": "Hello!"})
    if response.status_code == 204:
        await ctx.send('Message sent to webhook!')
    else:
        await ctx.send('Failed to send message to webhook.')

bot.run(BOT_TOKEN)
