# Main Bot
import discord
from discord.ext import commands
from lib.executor import run_program

TOKEN = 'NjA1ODM2MTM4NzIwMjY0MTky.XUJifA.iMHdYUlRmGVA9vaLnZau7X0wo-s'
MASTER = 'spencer'

bot = commands.Bot(command_prefix='!')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
@commands.has_role(MASTER)
async def stop(ctx):
    await ctx.send('Stopping')
    await bot.logout()

@bot.command()
async def run(ctx, name):
    output = run_program(name)
    await ctx.send(output)

@bot.command()
async def add(ctx, *, rolename):
    member = ctx.message.author
    top_role = member.top_role
    role = discord.utils.get(ctx.guild.roles, name=rolename)

    if role is None:
        await ctx.send("Role " + rolename + " not found.")
    elif role in member.roles:
        await ctx.send("You already have the role " + role.name)
    elif role >= top_role:
        await ctx.send("You are not allowed to add " + top_role)
    else:
        await member.add_roles(role)
        await ctx.send("Added " + role.name)

@bot.command(pass_context=True)
async def remove(ctx, *, rolename):
    member = ctx.message.author
    top_role = member.top_role
    role = discord.utils.get(ctx.guild.roles, name=rolename)

    if role is None:
        await ctx.send("Role " + rolename + " not found.")
    elif role >= top_role:
        await ctx.send("You are not allowed to remove " + top_role.name)
    elif role not in member.roles:
        await ctx.send("You don't have this role " + role.name)
    else:
        await member.remove_roles(role)
        await ctx.send("Removed " + role.name)


bot.run(TOKEN)
