import discord
from discord.ext import commands
from discord import Interaction

import pandas as pd
import asyncio

from UserData import User
from PokerGame import PokerGame

with open('./TOKEN/TestBot_TOKEN.txt','r') as f:
    TOKEN = f.readline()

client = commands.Bot(command_prefix="!", intents= discord.Intents.all())

poker_user = {}

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
        poker_user[user.display_name] = User(user)
    if len(poker_user) >= 1:
        await reaction.message.channel.purge()
        Poker = PokerGame()
        await reaction.message.channel.send('포커 게임을 시작합니다')

        ############# 프리플랍 페이즈 ##############
        await reaction.message.channel.send('프리플랍 페이즈')
        Poker.pre_flop(poker_user) # 유저들 카드 2장씩 배분
        for u in poker_user.values():
            dm_channel = await u.get_user_class().create_dm() # DM 채널 생성
            hand_img = Poker.merge_image(u.get_hands()) # 카드 두장을 한 사진으로 만들어서 저장 후 그 경로 리턴
            await dm_channel.send(file=discord.File(hand_img)) # 이미지 DM
        await reaction.message.channel.send('카드 분배가 완료됐습니다 배팅을 시작해주세요.')

        # TODO: 배팅하는 코드 짜야됨
        # 버튼식으로 만들어서 하면 좋을듯?
        await asyncio.sleep(5)
        ############ 플랍 페이즈 #################
        await reaction.message.channel.purge()
        Poker.flop()
        commuity_img = Poker.merge_image(Poker.get_community_card())
        await reaction.message.channel.purge()
        await reaction.message.channel.send('플랍 카드')
        await reaction.message.channel.send(file=discord.File(commuity_img))

        # TODO: 배팅하는 코드 짜야됨
        # 버튼식으로 만들어서 하면 좋을듯?
        await asyncio.sleep(5)
        ############ 턴 페이즈 ##################
        Poker.turn()
        commuity_img = Poker.merge_image(Poker.get_community_card())
        await reaction.message.channel.purge(limit=2)
        await reaction.message.channel.send('턴 카드')
        await reaction.message.channel.send(file=discord.File(commuity_img))
        # TODO: 배팅하는 코드 짜야됨
        # 버튼식으로 만들어서 하면 좋을듯?
        await asyncio.sleep(5)
        ############ 리버 페이즈 ################
        Poker.river()
        commuity_img = Poker.merge_image(Poker.get_community_card())
        await reaction.message.channel.purge(limit=2)
        await reaction.message.channel.send('리버 카드')
        await reaction.message.channel.send(file=discord.File(commuity_img))
        # TODO: 배팅하는 코드 짜야됨
        # 버튼식으로 만들어서 하면 좋을듯?
        await asyncio.sleep(5)
        ############ 결과 확인 ##################
        # poker_user.clear()

@client.command()
async def check(ctx: commands.context.Context):
    msg = await ctx.send('포커 게임이 생성되었습니다 참여하실분은 아래 이모지를 눌러주세요.')
    await msg.add_reaction('🙌')

client.run(TOKEN)

# users = [first, second, third]
# Poker.pre_flop(users)
# Poker.flop()
# Poker.turn()
# Poker.river()
# for i in users:
#     print(i.get_hands())

# print(Poker.get_community_card())