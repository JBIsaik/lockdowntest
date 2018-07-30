import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random

Client = discord.Client()
bot = commands.Bot(command_prefix="$")
lines = open(r'spotify.txt').read().splitlines()

@bot.event
async def on_ready():
    print("The bot is online!")
    await bot.change_presence(game=discord.Game(name='Type $uplay'))

@commands.cooldown(1, 30, commands.BucketType.user)
@bot.command(pass_context=True)
async def uplay(ctx):
    userName = ctx.message.author.name
    userID = ctx.message.author.id

    if ctx.message.server:
    myline = random.choice(lines)
    split = myline.partition(":")
    
    embed=discord.Embed(title="Minecraft Account", color=0xf45eff)
    embed.set_thumbnail(url="https://pre00.deviantart.net/3d13/th/pre/i/2016/343/0/7/free_minecraft_logo_template_by_curtzeninja-dar2dou.png")
    embed.add_field(name="Email:", value=split[0], inline=False)
    embed.add_field(name="Password:", value=split[2], inline=False)
    await bot.send_message(ctx.message.author, embed=embed)

    print("{} Typed !gen".format(userName))

bot.run("NDcyMzU0NjA0ODMxNzM1ODE4.Dj3LlQ.Uq7P7i9IaSZ7fNBocU0-_za1tbM")
