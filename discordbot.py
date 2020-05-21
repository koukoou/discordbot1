#coding:UTF-8
import discord
import datetime
import random
from discord.ext import tasks
TOKEN = 'Njc2Njk5NjgxNzUzMTM3MTUy.XsYQ4w.CmaRk1eXmO32pwJQlO_yg61eXgE' #トークン
CHANNEL_ID = 695170878274666517 #チャンネルID
# 接続に必要なオブジェクトを生成
client = discord.Client()
Answer1 = ['Daisuke☆','大好き!','好き!','普通...','嫌い','大嫌い','まず誰？',]
help1 = ['/おはよう','/こんにちは','/こんばんわ','/ありがとう','/わたしのことどうおもってる？','/だれかのものまねをして']
Habit = ['きっしょ！','え、俺強！','おちゃみずイケメン','こうさん美脚','はい、くそー','ギャアァァァア（断末魔)','は？やーばぁ！','この苦みが最高....','おーまいぐんねすGG','大概にsayよ！','まぅふぃんの顔面は~フロッパーでーす！！']
Man = ['おりーぶ','ともしび','クラメン全員','クラメン一部','おきぶら','しるむ','Kou','しょうとくたいし','BOXINGch','ボドカ','いきりと']
# 起動時に動作する処理
@client.event
async def on_ready():
    print('ready')

# 指定時間に走る処理
async def SendMessage():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('@everyone 活動の時間です！休む方は  #休む場合の報告　に記入お願いします！')
async def NoticeMessage():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('@everyone 活動10分前になりました!そろそろ集まりましょう！')
# 30秒に一回ループ
@tasks.loop(seconds=10)
async def time_check():
    sleepTime = 0
    # 現在の時刻
    ima = datetime.datetime.now()
    youbi = ima.weekday()
    zi = ima.hour
    fun = ima.minute
    if youbi == 5 or youbi == 6:
        if zi == 13:
            if fun == 50:
                await NoticeMessage()
                #該当時間だった場合は２重に投稿しないよう３０秒余計に待機
                await asyncio.sleep(50)
    if youbi == 5 or youbi == 6:
        if zi == 14:
            if fun== 00:
                await SendMessage()
                #該当時間だった場合は２重に投稿しないよう３０秒余計に待機
                await asyncio.sleep(50)

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 使用できるコマンド一覧
    if message.content == '/help':
        await message.channel.send('こちらが受け答えできるコマンド一覧です。')
        for rist1 in help1:
            await message.channel.send(rist1)

    if message.content == '/おはよう':
        await message.channel.send('おはよう!')

    if message.content == '/こんにちは':
        await message.channel.send('こんにちは!')

    if message.content == '/こんばんわ':
        await message.channel.send('こんばんわ!')

    if message.content == '/ありがとう':
        await message.channel.send('どういたしまして!')

    if message.content == '/わたしのことどうおもってる？':
        Answer=random.randint(0,6)
        await message.channel.send(Answer1[Answer])
    if message.content.startswith('/だれかのものまねをして'):
        randomHabit = random.randint(0,10)
        numeral = 0
        channel = message.channel
        def check(m):
            return m.content == 0,1,2,3,4,5,6,7,8,9,10 and m.channel == channel
        await message.channel.send('う～ん')
        await message.channel.send('ではものまねします！誰か当ててみてね！')
        await message.channel.send('ものまね:'+Habit[randomHabit])
        for CandidateNumber in Man:
            await message.channel.send(str(numeral)+':'+CandidateNumber)
            numeral += 1
        await message.channel.send('誰のものまねだと思う？数字で入力してね！:')
        msg = await client.wait_for('message', check=check)
        Expectation = int(msg.content)
        if Expectation<0 or Expectation>10 :
            await message.channel.send('正しい数字を入力してね！')
        else:
            if randomHabit == Expectation:
                await message.channel.send('正解！')
            else:
                await message.channel.send('残念！不正解！また挑戦してね！')
#ループ処理
time_check.start()
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
