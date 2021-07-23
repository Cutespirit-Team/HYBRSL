# -*- coding: UTF-8 -*- 
#導入 Discord.py
import discord
import youtube_dl
import subprocess
from discord.ext import commands
import os
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
from discord.utils import get
from discord_slash.utils.manage_commands import create_choice, create_option
from discord_slash import SlashCommand
import time


#client 是我們與 Discord 連結的橋樑

#設定檔
TOKEN='ODY2NTQ1MzAwMjgxNjIyNTI4.YPUHMw.SgUcPla07tp0GdW7w2AKnFZDrYU'
intents = discord.Intents().all()
client = discord.Client(intents=intents)
client = commands.Bot(command_prefix='!')
players = {}
localtime = time.localtime(time.time())
slash = SlashCommand(client, sync_commands=True) 

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
    
    if message.content =='笨蛋':
        await message.channel.send('對不起啦....')

    if message.content =='/menu' or message.content == '/選單':
        text= '''
                --------- !say 參數 ---說
                 !menu 選單    
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
                 !+ num num 加法
                 !- num num 減法
                 !* num num 乘法
                 !/ num num 除法
                 !time 時間'''
    if message.content =='/nowtime':
        await message.channel.send (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )

        
        await message.channel.send(text)
          
    if message.content.startswith('/狀態'):
      
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
       
    if message.content.startswith('/say'):   #如果以「說」開頭
    #分割訊息成兩份
        tmp = message.content.split(" ")
        if '--showme' in tmp:
          await message.channel.send( '你說:' + tmp[0] + f'我是:({self.user}')
          #如果分割後串列長度只有0
        if len(tmp) == 0:
            await message.channel.send("你要我工三小??")
        else:
            await message.channel.send(tmp[1])
    await client.process_commands(message)

@slash.slash(description='加法')
async def add(ctx ,x,y):
    await ctx.send(str(int(x)+int(y)))

@slash.slash(description='減法')
async def cut(ctx ,x,y):
    await ctx.send(str(int(x)*int(y)))

@slash.slash(description='乘法')
async def times(ctx ,x,y):
    await ctx.send(str(int(x)*int(y)))   

@slash.slash(description='除法')
async def into(ctx ,x,y):
    await ctx.send(str(int(x)/int(y)))   

@slash.slash(description='延遲')
async def ping(ctx):
    await ctx.send(f'{round(client.latency*1000)}(ms)')

@slash.slash(description='清除信息')

async def clear(ctx, num):
    print('cleared')
    await ctx.channel.purge(limit=int(num)+1)
    await ctx.send('成功刪除')

@slash.slash(description='踢人')
@commands.has_any_role('版主')
async def kick(ctx, member : discord.Member, *,reason=None):
    await member.kick(reason=reason)
@slash.slash(description='封鎖人')
@commands.has_any_role('版主')
async def ban(ctx,member : discord.Member, *,reason=None):
    await member.ban(reason=reason)
    await ctx.send('完成操作')

@slash.slash(description='解除封鎖人')
@commands.has_any_role('版主')
async def unban(ctx,*,member):
    banned_users =await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user =ban_entry.user

        if (user.name, user.discriminator) ==(member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send('成功')
            return

@slash.slash(description='加入語音頻道')
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.send('進入到語音頻道')
    print('Connected')

@slash.slash(description='離開語音頻道')
async def leave(ctx):
    if (ctx.guild.voice_client): # If the bot is in a voice channel 
        await ctx.guild.voice_client.disconnect() # Leave the channel
        await ctx.send('我先離開瞜!')
        print('Bot left')
    

@slash.slash(description='播放')
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

@slash.slash(description='繼續播放')
async def resume(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        voice.resume()
        await ctx.send('繼續中')


# command to pause voice if it is playing
@slash.slash(description='暫停')
async def pause(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.pause()
        await ctx.send('暫停''')


# command to stop voice
@slash.slash(description='停止')
async def stop(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.stop()
        await ctx.send('停止中...')

@slash.slash(description='關於')
async def about(ctx):
    embed=discord.Embed(title="About ", url="https://github.com/Cutespirit-Team/HYBRSL", description="關於此機器人", color=0x4b7e7e)
    embed.set_author(name="哈密瓜", url="http://hybrsl.tk/me/", icon_url="https://hybrsl.tk/cute.jpg")
    embed.set_thumbnail(url="https://hybrsl.tk/cute.jpg")
    embed.add_field(name="開發日期", value="2021/07/19", inline=True)
    embed.add_field(name="目前版本", value="v0.3", inline=True)
    embed.add_field(name="幫助", value="!選單", inline=True)
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
#@client.command()
#async def ping(ctx):
#  await ctx.send(f'{round(client.latency*1000)}(ms)')
@slash.slash(description='選單')
async def 選單(ctx):
    embed=discord.Embed(title="HYBRSL", url="https://github.com/Cutespirit-Team/HYBRSL", description="指令", color=0x281f56)
    embed.set_author(name="指令列表", url="http://hybrsl.tk/me/", icon_url="https://hybrsl.tk/cute.jpg")
    embed.set_thumbnail(url="https://hybrsl.tk/cute.jpg")
    embed.add_field(name="DISCORD", value="指令區", inline=False)
    embed.add_field(name="/kick ", value="踢掉使用者", inline=True)
    embed.add_field(name="/ban ", value="封鎖使用者", inline=True)
    embed.add_field(name="/unban ", value="解封使用者", inline=True)
    embed.add_field(name="/join", value="加入到語音頻道", inline=True)
    embed.add_field(name="/leave", value="從語音頻道離開", inline=True)
    embed.add_field(name="/狀態 ", value="改變bot 狀態", inline=True)
    embed.add_field(name="Youtube ", value="音樂指令", inline=False)
    embed.add_field(name="/play ", value="播放(請先/join)", inline=True)
    embed.add_field(name="/pause", value="暫停播放", inline=True)
    embed.add_field(name="/resume", value="恢復播放", inline=True)
    embed.add_field(name="/stop", value="停止播放", inline=True)
    embed.add_field(name="計算機", value="add,cut,times,into加減乘除  後面加兩個要運算的數字", inline=False)
    embed.add_field(name="範例加法 /add ", value="指令/add num num  ", inline=True)
    embed.add_field(name="/nowtime ", value="現在時間", inline=True)
    embed.set_footer(text="更新日期7/21")
    await ctx.send(embed=embed)
@slash.slash(description='中華民國') 
async def weareroc(ctx):
    await ctx.send('中華民國萬歲，三民主義統一中國，我們是自由民主中國。')











client.run(TOKEN) #TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面
