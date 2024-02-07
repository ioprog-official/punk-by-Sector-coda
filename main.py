import discord
from discord.ext import commands
import random
import gifs
import os
from keep_alive import keep_alive


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="*", intents=intents)

@bot.command()
async def dance(ctx):
    emb = discord.Embed(title=ctx.author.name + " Танцует", colour=discord.Colour.random())
    emb.set_image(url=random.choice(gifs.dance))
    await ctx.send(embed=emb)


@bot.command()
async def hi(ctx):
    emb = discord.Embed(title=ctx.author.name + " Приветствует", colour=discord.Colour.random())
    emb.set_image(url=random.choice(gifs.hi))
    await ctx.send(embed=emb)
@bot.command()   
async def ok(ctx):
    emb = discord.Embed(title=ctx.author.name + " одобряет", colour=discord.Colour.random())
    emb.set_image(url=random.choice(gifs.ok))
    await ctx.send(embed=emb)
@bot.command()   
async def explains(ctx):
    emb = discord.Embed(title=ctx.author.name + " Объясняет", colour=discord.Colour.random())
    emb.set_image(url=random.choice(gifs.dance))
    await ctx.send(embed=emb)


@bot.command()
async def a_test(ctx,a):
    ctx.send(ctx.commands.MissingRequiredAttachment(a))



#@bot.command()
#async def concert(ctx):
    #voice_channel = '1158029498072170516'
    #voice_client = await voice_channel.connect()
    #audio_source = discord.FFmpegPCMAudio('song.mp3')
    #voice_client.play(audio_source)

keep_alive()

bot.run('')
