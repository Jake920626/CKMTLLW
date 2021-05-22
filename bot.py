import discord
from discord import file
from discord.ext import commands
import json
import random
import os
from dotenv import load_dotenv

#載入token
token = os.getenv("token")

#載入設定
with open ( '/Users/apple/Documents/GitHub/CKMTLLW/setting.json' , 'r' , encoding = 'utf8' ) as settingsfile:
    settings = json.load(settingsfile)

#載入語錄1
with open ( '/Users/apple/Documents/GitHub/CKMTLLW/quotes1.json' , 'r' , encoding = 'utf8' ) as quotesfile1:
    quote1 = json.load(quotesfile1)

#載入語錄1
with open ( '/Users/apple/Documents/GitHub/CKMTLLW/quotes2.json' , 'r' , encoding = 'utf8' ) as quotesfile2:
    quote2 = json.load(quotesfile2)

#BOT初始設定
bot = commands.Bot(command_prefix='!火爆')


#確認啟動
@bot.event
async def on_ready():
    print(">> bot is online <<")

@bot.command()
async def 教數學(ctx):
    r_s1 = random.choice(quote1['f'])
    await ctx.send(r_s1)

@bot.command()
async def 聊聊天(ctx):
    r_s2 = random.choice(quote1['s'])
    await ctx.send(r_s2)

@bot.command()
async def 鼓勵我(ctx):
    r_s3 = random.choice(quote2['c'])
    await ctx.send(r_s3)

@bot.command()
async def 說未來(ctx):
    r_s4 = random.choice(quote2['fu'])
    await ctx.send(r_s4)

@bot.command()
async def 快上課(ctx):
    r_s5 = random.choice(quote2['t'])
    await ctx.send(r_s5)

@bot.command()
async def 幫幫我(ctx):
    await ctx.send(settings['help'])

bot.run(token)