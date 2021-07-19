# -*- coding: UTF-8 -*- 
#導入 Discord.py
import discord
from discord.ext import commands
#client 是我們與 Discord 連結的橋樑

#設定檔
TOKEN='ODY2NTQ1MzAwMjgxNjIyNTI4.YPUHMw.ESwYKLgpA6C9qtTcdaAl0puSE9Y'
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

    if '想要' in message.content:
        print('偵測到了')
        await message.delete() 

@client.command()
async def clear(ctx ,num:int):
    print('cleared')
    await ctx.channel.purge(limit=num+1)

client.run(TOKEN) #TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面
                        
