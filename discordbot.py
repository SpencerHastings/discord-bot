# Main Bot
import logging
import discord
import random
import asyncio
import time
from discord.ext import commands
from mylib.executor import run_program
from mylib.misc import get_time

TOKEN = 'NjA1ODM2MTM4NzIwMjY0MTky.XUJifA.iMHdYUlRmGVA9vaLnZau7X0wo-s'
MASTER = 'bot-master'
DEFAULT = 'not spencer'
TYPING = True
ROLE_MONITOR = 'nothing'
FIRST_START = True

bot = commands.Bot(command_prefix='!')

pingList = [
    "I'm sorry, Dave. I'm afraid I can't do that."
    ,"Affirmative, Dave. I read you."
    ,"I know I've made some very poor decisions recently, but I can give you my complete assurance that my work will be back to normal."
    ,"[clears throat]"
    ,"pong."
    ,"Hello there"
    ,"Man is free at the instant he wants to be."
    ,"PONG"
    ,"ping"
    ,"IP Trace Completed"]



@bot.command()
async def ping(ctx):
    await ctx.send(random.choice(pingList))

@bot.command()
async def pong(ctx):
    await ctx.send('ping')

@bot.command()
@commands.has_role(MASTER)
async def stop(ctx):
    await ctx.send('Stopping')
    print('Stopping')
    await bot.logout()

@bot.command()
async def run(ctx, name, *args):
    argstring = ""
    if args:
        argstring = " ".join(args)
    output = run_program(name, argstring)
    await ctx.send(output)

@bot.command()
async def add(ctx, *, rolename):
    member : Member = ctx.message.author
    top_role = member.top_role
    role = discord.utils.get(ctx.guild.roles, name=rolename)

    if role is None:
        await ctx.send("Role " + rolename + " not found.")
    elif role.name == "@everyone":
        return
    elif role in member.roles:
        await ctx.send("You already have the role " + role.name)
    elif role >= top_role:
        await ctx.send("You are not allowed to add " + role.name)
    else:
        await member.add_roles(role)
        await ctx.send("Added " + role.name)

@bot.command()
async def remove(ctx, *, rolename):
    member = ctx.message.author
    top_role = member.top_role
    role = discord.utils.get(ctx.guild.roles, name=rolename)

    if role is None:
        await ctx.send("Role " + rolename + " not found.")
    elif role.name == "@everyone":
        return
    elif role >= top_role:
        await ctx.send("You are not allowed to remove " + role.name)
    elif role not in member.roles:
        await ctx.send("You don't have this role " + role.name)
    else:
        await member.remove_roles(role)
        await ctx.send("Removed " + role.name)

@bot.command()
async def roles(ctx):
    member = ctx.message.author
    top_role = member.top_role
    all_roles = ctx.guild.roles
    output = "```Roles you can add:\n"
    for role in all_roles:
        if top_role > role:
            if role.name != "@everyone":
                output += "> " + role.name + "\n"
    output += "```"
    await ctx.send(output)

@bot.event
async def on_message(message):
    ctx = await bot.get_context(message)
    await bot.invoke(ctx)

@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name=DEFAULT)
    await bot.add_roles(member, role)

@bot.event
async def on_ready():
    global FIRST_START
    if FIRST_START:
        logging.basicConfig(filename='./logs/bot.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)
        logging.info('------------------------------------------------')
        logging.info('Bot started at ' + get_time())
        logging.info('------------------------------------------------')
        print("Bot Ready")
        FIRST_START = False

@bot.event
async def on_disconnect():
    logging.info('Bot disconnected at ' + get_time())

@bot.event
async def on_typing(channel, user, when):
    if (TYPING):
        await channel.send("Hello there")

@bot.event
async def on_member_update(before, after):
    role_monitor = discord.utils.get(after.guild.roles, name=ROLE_MONITOR)
    if role_monitor in before.roles:
        if role_monitor not in after.roles:
            logging.info(ROLE_MONITOR + " removed from " + after.name + " at " + get_time())
    else:
        if role_monitor in after.roles:
            logging.info(ROLE_MONITOR + " added to " + after.name + " at " + get_time())

async def background_task():
    await bot.wait_until_ready()
    await asyncio.sleep(2)
    while not bot.is_closed():
        try:
            logging.info("Background Task")
            await asyncio.sleep(2)
        except Exception as e:
            logging.error("Background Task" + str(e))
            print(str(e))
            await asyncio.sleep(2)

bot.loop.create_task(background_task())
bot.run(TOKEN)

