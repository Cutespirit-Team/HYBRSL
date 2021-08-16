# HYBRSL - Discord
A Discord bot which made by Tershi. 一個由哈密瓜製作的Discord機器人
這是一款使用Python寫的Discord Bot，這是利用discord.py做成的，目前也正在維護中，也有在定時更新。<br>
目前功能(有些指令變成slash功能 且join功能需要安裝PaNyCl套件):<br>

| 用法： /指令 | [選項...] [參數...] |
|-----|-----|
|/say 參數| ---說|             
|/menu |選單   | 
|早安 |回覆早安|
|晚安 |回覆晚安|
|笨蛋 |回覆對不起啦...|
|我好帥,我好可愛,我好棒|刪除信息並回覆|
|/weareroc |中華民國|
|/狀態 參數| 改變bot狀態|
|/kick USER | 踢掉使用者|
|/ban USER | 封鎖使用者|
|/unban USER | 解封使用者|
|/join | 加入到語音頻道|
|/leabe|從語音頻道離開|
|/play URL | 播放YouTube音樂|
|/pause | 暫停播放YouTube音樂|
|/resume | 恢復播放YouTube音樂|
|/stop | 停止播放YouTube音樂|
|/選單|指令區|

             
                

[![Build Status](http://img.shields.io/travis/badges/badgerbadgerbadger.svg?style=flat-square)](https://travis-ci.org/badges/badgerbadgerbadger)

### 點這看更新日誌：[更新日誌](/updateInfo.md)

## Installation 安裝<br>
### **Quick install**
``chmod +x install.sh``<br>
``./install.sh``

### **Arch-Linux**<br>
**Step 1.** ``sudo pacman -Syy python3 python3-pip httpd`` <br>
**Step 2.**``pip3 install discord.py``<br>
**Step 3.**``sudo systemctl start httpd``<br>
**Step 4.**``mkdir /srv/http/yt``<br>
**Step 5.**``sudo chown USER:USER /srv/http/yt``<br>

### **Debian/Ubuntu**<br>
**Step 1.**``sudo apt update&&sudo apt upgrade -y``<br>
**Step 2.**``sudo apt install httpd python3 python3-pip``<br>
**Step 3.**``pip3 install discord.py``<br>
**Step 4.**``sudo mkdir /var/www/html/yt``<br>
**Step 5.**``sudo chown USER:USER /var/www/html/yt``<br>
**Step 6.**``sudo service httpd start``<br>

### **Termux(For Android)**<br>
**Step 1.**``pkg update&&pkg upgrade``<br>
**Step 2.**``pkg install httpd python3 python3-pip``<br>
**Step 3.**``pip3 install discord.py``<br>
**Step 4.**``mkdir /var/www/html/yt``<br>
**Step 5.**``apachectl``<br>

### Run 運行
**Step 1.**``git clone https://github.com/Cutespirit-Team/CutespiritDiscordBot``<br>
**Step 2.**``mkdir CutespiritDiscordBot/yt``<br>
**Step 3.**``vim CutespiritDiscordBot/bot.py``<br>
**Step 4.**``python3 CutespiritDiscordBot/bot.py``<br>

## 心得與建構思路:
這是我一直看教學還有大神的幫助弄出來的 原創性20趴 我好棒 

## 關於我們 About Us

[Team Website](https://www.cutespirit.org) <br>
[哈密瓜個人web](https://hybrsl.tk/me) <br>
[哈密瓜 Facebook](https://www.facebook.com/shanling.team/) <br>
[哈密瓜 YouTube](https://www.youtube.com/channel/UCet_gHUIfoGs3uQaKc-OxCQ) <br>
[XiaTerShi FaceBook](https://www.facebook.com/Tershi25648) <br>
[Tershi MailServer](https://mail.tershi.ml) <br>
[Tershi Official WebSite](https://cutespirit.tershi.ml) <br>
[Tershi Gitbook](https://gitbook.tershi.ml) <br>
[Tershi Telegram](https://t.me/TershiXia) <br>
以上關於因為域名為免費域 因此隨時會網域更換！ <br>
Licence:© Cutespirit 2021 All right reversed 此程式除了「關於」頁面不可重製及發布之外，其餘頁面及功能可進行重製發布。
