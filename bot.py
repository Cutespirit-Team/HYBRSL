# -*- coding: UTF-8 -*- 
#導入 Discord.py
import discord
from discord.ext import commands
#client 是我們與 Discord 連結的橋樑

#設定檔
TOKEN='YOUR TOKEN'
client = commands.Bot(command_prefix='!')

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

    if message.content =='晚安':
        await message.channel.send('晚安')

    if message.content =='笨蛋':
        await message.channel.send('對不起啦....')
    if message.content =='/weareroc':
        await message.channel.send('中華民國萬歲，三民主義統一中國，我們是自由民主中國。')
    if message.content =='/menu' or message.content == '/選單':
        text= '''/say 參數 ---說
                 /menu 選單    
                 早安 回覆早安
                 晚安 回覆晚安
                 笨蛋 回覆對不起啦...
                 我好帥,我好可愛,我好棒-刪除信息並回覆
                 /weareroc 中華民國
                 /狀態 參數 改變bot狀態'''
        
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
            await message.channel.send( '你說:' + tmp[0] + f'我是:{self.user}')
          #如果分割後串列長度只有0
        if len(tmp) == 0:
            await message.channel.send("你要我工三小??")
        else:
            await message.channel.send(tmp[1])
    await client.process_commands(message)
        
@client.command(name='clear')
async def clear(ctx ,num:int):
    print('cleared')
    await ctx.channel.purge(limit=num+1)
@client.command(name='kick')
async def kick(ctx, member : discord.Member, *,reason=None):
    await member.kick(reason=reason)

client.run(TOKEN) #TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面
