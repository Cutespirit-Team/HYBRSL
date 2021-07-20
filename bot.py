# -*- coding: UTF-8 -*- 
#導入 Discord.py
import discord
import youtube_dl
import subprocess
from discord.ext import commands
import os
from dotenv import load_dotenv
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
from discord.utils import get
import time


#client 是我們與 Discord 連結的橋樑

#設定檔
TOKEN='ODY2NTQ1MzAwMjgxNjIyNTI4.YPUHMw.78GiB5ql0d_hxjV5ngWAeg4vaPE'
intents = discord.Intents().all()
client = discord.Client(intents=intents)
client = commands.Bot(command_prefix='!')
players = {}
localtime = time.localtime(time.time())

@client.event
async def on_ready():
    print('bot已經登入')

@client.event
async def on_message(message):
    #排除自己的訊息，避免陷入無限循環
    if message.author == client.user:
             return
        #如果包含 ping，機器人回傳 pong
    if message.content == '早安':
        await message.channel.send('早安')
    #檢測髒話類    
    if message.content == '品恩智障' or message.content =='品恩垃圾' or message.content =='品恩沒懶覺':
        await message.delete() 
        await message.channel.send('請勿罵我老公')

    if message.content =='晚安':
        await message.channel.send('晚安')
    if message.content =='!time':
        await message.channel.send (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )

    if message.content =='笨蛋':
        await message.channel.send('對不起啦....')
    if message.content =='!weareroc':
        await message.channel.send('中華民國萬歲，三民主義統一中國，我們是自由民主中國。')
    if message.content =='!menu' or message.content == '!選單':
        text= '''/say 參數 ---說
                 /menu 選單    
                 早安 回覆早安
                 晚安 回覆晚安
                 笨蛋 回覆對不起啦...
                 我好帥,我好可愛,我好棒-刪除信息並回覆
                 !weareroc 中華民國
                 !狀態 參數 改變bot狀態
                 !kick USER | 踢掉使用者
                 !ban USER | 封鎖使用者
                 !unban USER | 解封使用者
                 !join | 加入到語音頻道
                 !leabe|從語音頻道離開
                 !play URL | 播放YouTube音樂
                 !pause | 暫停播放YouTube音樂
                 !resume | 恢復播放YouTube音樂
                 !stop | 停止播放YouTube音樂
                 '''

        
        await message.channel.send(text)

    if message.content.startswith('!狀態'):
        tmp = message.content.split(' ')
        text = ''
        for i in range(1,len(tmp)):
            text = text + str(tmp[i])
        game = discord.Game(text)
        await client.change_presence(status=discord.Status.idle, activity=game)
    #discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible

    if message.content == '我好帥' or message.content == '我好棒' or message.content =='我好可愛':
        #刪除傳送者的訊息
        await message.delete()
    #然後回傳訊息
        await message.channel.send('不好意思，不要騙人啦') 
       
    if message.content.startswith('!say'):   #如果以「說」開頭
    #分割訊息成兩份
        tmp = message.content.split(" ")
        if '--showme' in tmp:
            await message.channel.send( '你說:' + tmp[0] + f'我是:{self.user}')
          #如果分割後串列長度只有0
        if len(tmp) == 0:
            await message.channel.send("你要我工三小??")
        else:
            await message.channel.send(tmp[1])
    await client.process_commands(message)
@client.command(name='+')
async def add(ctx ,x,y):
    await ctx.send(int(x)+int(y))

@client.command(name='-')
async def add(ctx ,x,y):
    await ctx.send(int(x)-int(y))

@client.command(name='*')
async def add(ctx ,x,y):
    await ctx.send(int(x)*int(y))

@client.command(name='/')
async def add(ctx ,x,y):
    await ctx.send(int(x)/int(y))    

@client.command(name='clear')
async def clear(ctx ,num:int):
    print('cleared')
    await ctx.channel.purge(limit=num+1)
@client.command(name='kick')
async def kick(ctx, member : discord.Member, *,reason=None):
    await member.kick(reason=reason)
@client.command(name='ban')
async def ban(ctx,member : discord.Member, *,reason=None):
    await member.ban(reason=reason)
    await ctx.send('完成操作')

@client.command(name='unban')
async def unban(ctx,*,member):
    banned_users =await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user =ban_entry.user

        if (user.name, user.discriminator) ==(member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send('成功')
            return

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    await message.channel.send('Connected!')
    print('Connected')

@client.command(pass_context=True)
async def leave(ctx):
    if (ctx.voice_client): # If the bot is in a voice channel 
        await ctx.guild.voice_client.disconnect() # Leave the channel
        await ctx.send('我先離開瞜!')
        print('Bot left')
    else: # But if it isn't
        await ctx.send("I'm not in a voice channel, use the join command to make me join")
        print("I'm not in a voice channel, use the join command to make me join")

@client.command(pass_context=True)
async def play(ctx, url):
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    voice = get(client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['url']
        voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        voice.is_playing()
        await ctx.send('正在播放')

@client.command()
async def resume(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        voice.resume()
        await ctx.send('繼續中')


# command to pause voice if it is playing
@client.command()
async def pause(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.pause()
        await ctx.send('暫停''')


# command to stop voice
@client.command()
async def stop(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.stop()
        await ctx.send('停止中...')

@client.command()
async def about(ctx):
    embed=discord.Embed(title="About ", url="https://github.com/Cutespirit-Team/HYBRSL", description="關於此機器人", color=0x4b7e7e)
    embed.set_author(name="哈密瓜", url="http://hybrsl.tk/me/", icon_url="https://hybrsl.tk/cute.jpg")
    embed.set_thumbnail(url="https://hybrsl.tk/cute.jpg")
    embed.add_field(name="開發日期", value="2021/07/19", inline=True)
    embed.add_field(name="目前版本", value="v0.3", inline=True)
    embed.add_field(name="幫助", value="/選單", inline=True)
    embed.add_field(name="語言", value="python3", inline=True)
    embed.add_field(name="目前運行系統", value="kali linux", inline=True)
    embed.add_field(name="最想說的話", value="早安~~~", inline=True)
    embed.add_field(name="關於作者", value=":", inline=True)
    embed.add_field(name="網路稱號", value="哈密瓜", inline=True)
    embed.add_field(name="目前年齡", value="15", inline=True)
    embed.add_field(name="年級", value="升高一", inline=True)
    embed.add_field(name="創作心得", value="這是我一直看教學還有大神的幫助弄出來的 原創性20趴 嗯我好棒", inline=True)
    embed.set_footer(text="撰寫日期2021/07/20")
    await ctx.send(embed=embed)












client.run(TOKEN) #TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面
