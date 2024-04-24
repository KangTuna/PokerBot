import discord
from discord.ext import commands
from discord import Interaction


import pandas as pd
import asyncio

# 실제사용할땐 TestBot_TOKEN.txt -> RealBot_TOKEN.txt로 바꿔야됨
with open('./TOKEN/TestBot_TOKEN.txt','r') as f:
    TOKEN = f.readline()

client = commands.Bot(command_prefix="!", intents= discord.Intents.all())

poker_user = []

# 봇이 켜지면 바로 발생하는 함수
@client.event
async def on_ready():
    await client.tree.sync()
    await client.change_presence(activity = discord.activity.Game(name='Working'), # 플레이중인 게임 이름
                                 status = discord.Status.online) # 봇의 상태
    
@client.event
async def on_reaction_add(reaction: discord.reaction.Reaction, user: discord.member.Member):
    if user.bot == 1:
        return None
    if str(reaction.emoji) == '🙌':
        dm_channel = await user.create_dm()
        im1 = './images/Cards/spades/01_ace_of_spades.png'
        im2= './images/Cards/spades/02_of_spades.png'
        # poker_user.append()
        await dm_channel.send(file=discord.File(im1))
        await dm_channel.send(file=discord.File(im2))
        await reaction.message.channel.purge()

######################## 테스트용 명령어 ######################################
@client.tree.command(name="ping",description='it will show the ping!')
async def ping(interaction : Interaction):
    bot_latency = round(client.latency*1000)
    await interaction.response.send_message(f'Pong!...{bot_latency}ms')

@client.command(name= 'init')
async def init(ctx: commands.context.Context):
    await ctx.send(ctx.author.name)

@client.command()
async def check(ctx: commands.context.Context):
    im = './images/Cards/spades/01_ace_of_spades.png'
    msg = await ctx.send(file=discord.File(im))
    await msg.add_reaction('🙌')
    
    
##############################################################################
####################### 실제 사용하는 명령어 ###################################




client.run(TOKEN)
