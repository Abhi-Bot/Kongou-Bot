import discord
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
import asyncio
import random
import time
import requests
from discord.ext.commands import Bot
from discord.ext import commands
import pickle
import os

Client = discord.Client()
bot_prefix = "-"
client = commands.Bot(command_prefix=bot_prefix)
help_color = 0xFF8B00
eightball_yes = 0x55FF23
eightball_no = 0xFF0000
eightball_maybe = 0xFFFF00
bot_owner = 263847460923768832

response_yes = []
response_no = []
response_maybe = []

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('Bot made by Abhi')
    print('------')


@client.command(pass_context = True)
async def test(ctx):
    await ctx.send("THIS IS A TEST" + ctx.author.mention)



@client.command(pass_context = True)
async def h(ctx):
    embed = discord.Embed(description = "**Command list**: \n **Selfhost guide**: \n **__Add me to your server!__** \n https://discordapp.com/oauth2/authorize?client_id=354748838306775042&scope=bot", color = help_color)
    await ctx.author.send(embed = embed)

@client.command(pass_context = True)
async def Test(ctx):
    await ctx.send("Use a Lowercase T " + ctx.author.mention + ", you fag")

@client.event
async def on_member_join(member):
    await client.say(message.channel, "Hello! welcome to my server!")


client.run('Get ur own token -_-')
