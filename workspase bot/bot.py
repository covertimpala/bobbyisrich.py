import discord
from discord.ext import commands
import time
PREFIX = '$'
INTENTS = discord.Intents.default()
bot = commands.Bot(command_prefix=PREFIX, intents=INTENTS)


@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def imitate(ctx,*, mssg=None):
  if mssg == None:
    await ctx.send('Put the message you need in.')
  else:
    await ctx.send(f'{mssg}')


@bot.command()
async def countdown(ctx,*, x=None):
    if x == None:
        embed=discord.Embed(title='How to use Countdown Command', description='`$countdown <sec>`')
        await ctx.send(embed=embed)
    else:
        await ctx.send(f'timer set to {x} seconds')
        print(f'countdown has been set to {x} seconds')
        x = float(x)
        time.sleep(x)
        await ctx.send('time up!')


@bot.command()
async def bh(ctx):
    embed=discord.Embed(title=f"{bot.user.name} Help", description="this page lists my prefixes and commands", color=0xff0000)
    embed.add_field(name="otbh", value="list other bot prefixes", inline=False)
    embed.add_field(name="ping", value="try it!", inline=True)
    await ctx.send(embed=embed)


@bot.command()
async def otbh(ctx):
    embed=discord.Embed(title="Other Bots Help", description="other bot prefixes", color=0xff0000)
    embed.add_field(name="Dank Memer", value="`pls`", inline=True)
    embed.add_field(name="MEE6", value="`!`", inline=True)
    embed.add_field(name="IdleRPG", value="`'`", inline=True)
    embed.add_field(name="Idle miner", value="`_`", inline=True)
    embed.add_field(name="Soldier", value="`s!`", inline=True)
    embed.add_field(name="gambling bot", value="`+`", inline=True)
    embed.add_field(name="Disboard", value="`!d`", inline=True)
    embed.add_field(name="DuckBot", value="`,`", inline=True)
    embed.add_field(name="Dyno", value="`?`", inline=True)
    embed.add_field(name="PokéMeow", value="`;`", inline=True)
    embed.add_field(name="Atlas", value="`a!`", inline=True)
    embed.add_field(name="Avrae", value="`av`", inline=True)
    embed.add_field(name="IdleRPG", value="`'`", inline=True)
    await ctx.send(embed=embed)

bot.run(TOKEN)
