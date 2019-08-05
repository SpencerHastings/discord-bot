import discord
from discord.ext import commands
import time
import logging
import asyncio
import subprocess
import os

TOKEN = 'NjA3NzQzNDkzMjQyMzU1NzEy.XUeDSA.sCU34yUWjOnnDrpxyNcYdWsE0TI'
MASTER = 'spencer'
BOT_FILE = 'discordbot.py'

bot = commands.Bot(command_prefix='%')

childbot = None

@bot.command()
@commands.has_role(MASTER)
async def stop(ctx):
    await ctx.send('Stopping')
    await bot.logout()

@bot.command()
@commands.has_role(MASTER)
async def restart(ctx):
    await ctx.send('!stop')
    #await asyncio.sleep(10)
    #cp = subprocess.run(['git pull'], shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #output = "```" + cp.stdout + "```"
    #await ctx.send(output)
    #childbot = subprocess.Popen(['python3', BOT_FILE])

@bot.command()
@commands.has_role(MASTER)
async def start(ctx):
    childbot = subprocess.Popen(['python3', BOT_FILE])


bot.run(TOKEN)