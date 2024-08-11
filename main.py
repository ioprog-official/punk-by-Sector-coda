import discord
from discord.ext import commands
import random
import gifs
import os
from keep_alive import keep_alive
import praw
import anyio

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="*", intents=intents)




bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')



@bot.command()
async def dance(ctx):
    emb = discord.Embed(description=f'{ctx.author.mention} танцует',colour=discord.Colour.random())
    emb.set_image(url=random.choice(gifs.dance))
    await ctx.send(embed=emb)


@bot.command()
async def hi(ctx):
    emb = discord.Embed(description=f'{ctx.author.mention} машет рукой',colour=discord.Colour.random())
    emb.set_image(url=random.choice(gifs.hi))
    await ctx.send(embed=emb)

@bot.command()
async def like(ctx):
    emb = discord.Embed(description=f'{ctx.author.mention} показывает класс',colour=discord.Colour.random())
    emb.set_image(url=random.choice(gifs.like))
    await ctx.send(embed=emb)


@bot.command()
async def cray(ctx):
    emb = discord.Embed(description=f'{ctx.author.mention} плачет',colour=discord.Colour.random())
    emb.set_image(url=random.choice(gifs.cray))
    await ctx.send(embed=emb)


@bot.command()
async def gun(ctx):
    emb = discord.Embed(description=f'{ctx.author.mention} стреляет в воздух',colour=discord.Colour.random())
    emb.set_image(url=random.choice(gifs.gun))
    await ctx.send(embed=emb)



@bot.command()
async def fartuna(ctx,text):
    items=text.split(",")
    emb = discord.Embed(description=f'поздравляю, {ctx.author.mention}\nвам выпло: {random.choice(items)}',colour=discord.Colour.random())
    emb.set_image(url=random.choice(gifs.fartuna))
    await ctx.send(embed=emb)


keep_alive()

bot.run(os.getenv("BOT_TOKEN"))
