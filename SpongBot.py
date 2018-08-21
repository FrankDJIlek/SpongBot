import os
import time
import discord
import random
from discord.ext import commands
from time import sleep
from os import system

BOT = 'SpongBot'
VERSION = '0.3'
AUTHOR = 'Spongbap#9945'
LOADING = 'Loading...'
INFO = ('{} {}'.format(BOT, VERSION))

#Just a simple loading screen, with some useful information.
system("title "+LOADING)
print('Loading ''{}'' on version ''{}''...'.format(BOT, VERSION)) ; sleep(1)
print('Errors:')

TOKEN = ''

client = commands.Bot(command_prefix = 'fuck!')
client.remove_command('help')

waaArray = ["https://cdn.discordapp.com/attachments/449769149061660672/473326931845054474/d8112039c89320bd0ceefb5095116929d4e84bbb6732c36841170f521989bbfe.png", "https://cdn.discordapp.com/attachments/449769149061660672/473326130489720839/152536020-20Nigel_Thornberry20Super_Mario_Bros.png", "https://cdn.discordapp.com/attachments/449769149061660672/473325721679429672/FtFLqS6.png"]
voreArray = [ "https://cdn.discordapp.com/attachments/449769149061660672/473319509143584772/TMnO2z2kGN-10.png", "https://cdn.discordapp.com/attachments/449769149061660672/473317569978433546/maxresdefault.png", "https://cdn.discordapp.com/attachments/449769149061660672/473318257130995713/maxresdefault.png", "https://cdn.discordapp.com/attachments/449769149061660672/473318548622540815/44c.png"]

@client.event
async def on_ready():
    os.system('cls')
    print('Running...') ; sleep(1)
    await client.change_presence(game=discord.Game(type=3, name='fuck!help || Version: {}'.format(VERSION)))
    system("title "+INFO)

@client.command()
async def help():
    embed=discord.Embed(title="{}".format(BOT), color=0xFF00FF)
    embed.add_field(name="Prefix", value="fuck!", inline=False)
    embed.add_field(name="invite", value="Invite me to your server!", inline=False)
    embed.add_field(name="me", value="Do I want to fuck you?", inline=True)
    embed.add_field(name="dad", value="Where are you?", inline=True)
    embed.add_field(name="add", value="Adds 2 numbers. fuck!add 1 2", inline=True)
    embed.add_field(name="vore", value="Picks a random vore image.", inline=True)
    embed.add_field(name="you", value="No, you")
    embed.add_field(name="waa", value="Waluigi hentai", inline=True)
    embed.set_footer(text="Version: {} | {}".format(VERSION, AUTHOR))
    await client.say(embed=embed)

@client.command()
async def me():
    await client.say('gladly')

@client.command(pass_context=True)
async def dad(ctx):
    author = ctx.message.author.id
    if author == '251226842764148736':
        await client.say("Please come back, dad")
    else:
        await client.say("You're not dad!")

@client.command(pass_context=True)
async def add(ctx, left : int, right : int):
    answer = left + right
    await client.say('Answer: {}'.format(answer))

@add.error
async def add_error(error, ctx):
    await client.say('You must have 2 numbers.')

@client.command()
async def vore():
    rand = random.randrange(4)
    await client.say('{}'.format(voreArray[rand]))

@client.command()
async def you():
    await client.say('I already fuck myself on a daily basis')

@client.command()
async def waa():
    rand = random.randrange(3)
    await client.say('{}'.format(waaArray[rand]))

@client.command()
async def invite():
    embed=discord.Embed(title="Invite Me!", url="https://discordapp.com/oauth2/authorize?client_id=474266058304520253&scope=bot&permissions=378944")
    embed.set_author(name="SpongBot")
    embed.add_field(name="What I Can Do:", value="fuck!you", inline=True)
    embed.set_footer(text="Version: {} | {}".format(VERSION, AUTHOR))
    await client.say(embed=embed)
    
@client.command()
async def everyone():
    await client.say("@everyone")
    
client.run(TOKEN)
