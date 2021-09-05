# coding: utf-8
import discord
from discord.ext import tasks
import datetime
import random
import os

TOKEN = os.environ['DISCORD_BOT_TOKEN']


client = discord.Client()

plan_confirmation_message = None
plan_confirmation_user_data = {}
plan_confirmation_channel_id = 860492700579266560

six_mans_message = None
six_mans_user_data = []
six_mans_channel_id = 863652928501317643

isFirstLoop = True




@client.event
async def on_raw_reaction_add(payload):

    if payload.member.bot:
        return

    global plan_confirmation_user_data
    global six_mans_user_data

    if payload.channel_id == 860492700579266560:
        if payload.emoji.name not in plan_confirmation_user_data:
            plan_confirmation_user_data[payload.emoji.name] = []
        plan_confirmation_user_data[payload.emoji.name].append(payload.member.name)

    if payload.channel_id == 863652928501317643:
        channel = client.get_channel(six_mans_channel_id)

        if payload.member.name not in six_mans_user_data:
            six_mans_user_data.append(payload.member.name)

        print(six_mans_user_data)
        if len(six_mans_user_data) == 2:
            print("ok")
            random.shuffle(six_mans_user_data)
            team1 = [six_mans_user_data[0], six_mans_user_data[1], six_mans_user_data[2]]
            team2 = [six_mans_user_data[1], six_mans_user_data[4], six_mans_user_data[5]]

            embed = discord.Embed(title="6mans", description="チーム確定", color=discord.Colour.red())
            team1str = ":one: "+team1[0]+"\n :two: "+team1[1]+"\n :three: "+team1[2]
            team2str = ":one: "+team2[0]+"\n :two: "+team2[1]+"\n :three: "+team2[2]
            embed.add_field(name="Team1", value=team1str)
            embed.add_field(name="Team2", value=team2str)
            await channel.send('@everyone')
            embedFromBot = await channel.send(embed=embed)
        """
        if payload.emoji.name not in six_mans_user_data:
            six_mans_user_data[payload.emoji.name] = []
        six_mans_user_data[payload.emoji.name].append(payload.member.name)

        for key in six_mans_user_data:
            if len(six_mans_user_data[key]) == 2:
                embed = discord.Embed(title="6mans", description="Team", color=discord.Colour.blue())
                for value in six_mans_user_data().values():
                    embed.add_field(name="参加者", value=value)

                await six_mans_message.channel.send(embed=embed)
        """



@client.event
async def on_message(message):
    # 送信者がBotの場合は反応しない
    if message.author.bot:
        return

    global plan_confirmation_channel_id
    plan_confirmation_channel_id = message.channel.id

    """
    if message.content == '/create':
        #print(message.channel.id)
        embed = discord.Embed(title="予定確認", description="今週プライベートマッチを行う曜日のアンケートを取ります", color=discord.Colour.red())
        embed.add_field(name="金曜日",
                        value=":regional_indicator_a: 20:00~ \n :regional_indicator_b: 21:00~ \n :regional_indicator_c: 22:00~")
        embed.add_field(name="土曜日",
                        value=":regional_indicator_d: 20:00~ \n :regional_indicator_e: 21:00~ \n :regional_indicator_f: 22:00~")
        embed.add_field(name="日曜日",
                        value=":regional_indicator_h: 20:00~ \n :regional_indicator_g: 21:00~ \n :regional_indicator_i: 22:00~")
        embed.add_field(name="どれもいけません",
                        value=":regional_indicator_j:")


        await message.channel.send('@everyone')
        embedFromBot = await message.channel.send(embed=embed)
        await embedFromBot.add_reaction("\N{Regional Indicator Symbol Letter A}")
        await embedFromBot.add_reaction("\N{Regional Indicator Symbol Letter B}")
        await embedFromBot.add_reaction("\N{Regional Indicator Symbol Letter C}")
        await embedFromBot.add_reaction("\N{Regional Indicator Symbol Letter D}")
        await embedFromBot.add_reaction("\N{Regional Indicator Symbol Letter E}")
        await embedFromBot.add_reaction("\N{Regional Indicator Symbol Letter F}")
        await embedFromBot.add_reaction("\N{Regional Indicator Symbol Letter G}")
        await embedFromBot.add_reaction("\N{Regional Indicator Symbol Letter H}")
        await embedFromBot.add_reaction("\N{Regional Indicator Symbol Letter I}")
        await embedFromBot.add_reaction("\N{Regional Indicator Symbol Letter J}")

        global plan_confirmation_message
        plan_confirmation_message = embedFromBot
    """
    """
    if message.content == '/decision':
        global plan_confirmation_user_data
        existDicidedPlan = False
        await message.channel.send('@everyone')
        for key in plan_confirmation_user_data:
            if len(plan_confirmation_user_data[key]) >= 2:
                existDicidedPlan = True
                embed = discord.Embed(title="日程決定", description="今週のプライベートマッチの日程が決定しました", color=discord.Colour.blue())

                time = ""

                if key == "\N{Regional Indicator Symbol Letter A}":
                    time = " 金曜日 20:00-"
                elif key == "\N{Regional Indicator Symbol Letter B}":
                    time = " 金曜日 21:00-"
                elif key == "\N{Regional Indicator Symbol Letter C}":
                    time = " 金曜日 22:00-"
                elif key == "\N{Regional Indicator Symbol Letter D}":
                    time = " 土曜日 20:00-"
                elif key == "\N{Regional Indicator Symbol Letter E}":
                    time = " 土曜日 21:00-"
                elif key == "\N{Regional Indicator Symbol Letter F}":
                    time = " 土曜日 22:00-"
                elif key == "\N{Regional Indicator Symbol Letter G}":
                    time = " 日曜日 20:00-"
                elif key == "\N{Regional Indicator Symbol Letter H}":
                    time = " 日曜日 21:00-"
                elif key == "\N{Regional Indicator Symbol Letter I}":
                    time = " 日曜日 22:00-"
                elif key == "\N{Regional Indicator Symbol Letter j}":
                    time = ""


                if key != "\N{Regional Indicator Symbol Letter j}":
                    embed.add_field(name="日程", value=key+time)

                    for value in plan_confirmation_user_data.values():
                        embed.add_field(name="参加者", value=value)

                    await plan_confirmation_message.channel.send(embed=embed)

        if existDicidedPlan == False:
            embed = discord.Embed(title="人数不足", description="今週のプライベートマッチはありません", color=discord.Colour.blue())
            await plan_confirmation_message.channel.send(embed=embed)
    """

    if message.content == '/6mans':
        global six_mans_message
        global six_mans_user_data

        six_mans_message = None
        six_mans_user_data = []


        embed = discord.Embed(title="6mans 参加確認", description="参加する人はリアクションをしてください", color=discord.Colour.red())
        embedFromBot = await message.channel.send(embed=embed)
        await embedFromBot.add_reaction("\N{Ballot Box with Check}")

        six_mans_message = embedFromBot


@tasks.loop(seconds=60)
async def loop():

    global isFirstLoop

    if isFirstLoop == True:
        isFirstLoop = False

    else:
        channel = client.get_channel(plan_confirmation_channel_id)

        # 現在の時刻
        #now = datetime.now().strftime('%H:%M')

        today = datetime.datetime.today()
        weekday = datetime.date(today.year, today.month, today.day).weekday()

        #print(channel_id)

        global plan_confirmation_message
        global plan_confirmation_user_data

        #botの更新(先週までのデータを削除)
        if weekday == 6:
            if today.hour == 12 and today.minute == 0:

                plan_confirmation_message = None

                plan_confirmation_user_data = {}

        #曜日が月曜日であるとき、予定表の発行を実施(とりあえず、月曜日の12:00に実施)
        if weekday == 0:
            if today.hour == 12 and today.minute == 0:

                embed = discord.Embed(title="予定確認", description="今週プライベートマッチを行う曜日のアンケートを取ります", color=discord.Colour.red())
                embed.add_field(name="金曜日",
                        value=":regional_indicator_a: 20:00~ \n :regional_indicator_b: 21:00~ \n :regional_indicator_c: 22:00~")
                embed.add_field(name="土曜日",
                        value=":regional_indicator_d: 20:00~ \n :regional_indicator_e: 21:00~ \n :regional_indicator_f: 22:00~")
                embed.add_field(name="日曜日",
                        value=":regional_indicator_h: 20:00~ \n :regional_indicator_g: 21:00~ \n :regional_indicator_i: 22:00~")

                await channel.send('@everyone')
                embedFromBot = await channel.send(embed=embed)
                await embedFromBot.add_reaction("\N{Regional Indicator Symbol Letter A}")
                await embedFromBot.add_reaction("\N{Regional Indicator Symbol Letter B}")
                await embedFromBot.add_reaction("\N{Regional Indicator Symbol Letter C}")
                await embedFromBot.add_reaction("\N{Regional Indicator Symbol Letter D}")
                await embedFromBot.add_reaction("\N{Regional Indicator Symbol Letter E}")
                await embedFromBot.add_reaction("\N{Regional Indicator Symbol Letter F}")
                await embedFromBot.add_reaction("\N{Regional Indicator Symbol Letter G}")
                await embedFromBot.add_reaction("\N{Regional Indicator Symbol Letter H}")
                await embedFromBot.add_reaction("\N{Regional Indicator Symbol Letter I}")


                #global plan_confirmation_message
                plan_confirmation_message = embedFromBot

        if weekday == 3:
            if today.hour == 12 and today.minute == 0:
                #global plan_confirmation_user_data
                existDicidedPlan = False
                await channel.send('@everyone')
                for key in plan_confirmation_user_data:
                    if len(plan_confirmation_user_data[key]) >= 2:
                        existDicidedPlan = True
                        embed = discord.Embed(title="日程決定", description="今週のプライベートマッチの日程が決定しました",
                                              color=discord.Colour.blue())

                        time = ""

                        if key == "\N{Regional Indicator Symbol Letter A}":
                            time = " 金曜日 20:00-"
                        elif key == "\N{Regional Indicator Symbol Letter B}":
                            time = " 金曜日 21:00-"
                        elif key == "\N{Regional Indicator Symbol Letter C}":
                            time = " 金曜日 22:00-"
                        elif key == "\N{Regional Indicator Symbol Letter D}":
                            time = " 土曜日 20:00-"
                        elif key == "\N{Regional Indicator Symbol Letter E}":
                            time = " 土曜日 21:00-"
                        elif key == "\N{Regional Indicator Symbol Letter F}":
                            time = " 土曜日 22:00-"
                        elif key == "\N{Regional Indicator Symbol Letter G}":
                            time = " 日曜日 20:00-"
                        elif key == "\N{Regional Indicator Symbol Letter H}":
                            time = " 日曜日 21:00-"
                        elif key == "\N{Regional Indicator Symbol Letter I}":
                            time = " 日曜日 22:00-"
                        elif key == "\N{Regional Indicator Symbol Letter j}":
                            time = ""

                        if key != "\N{Regional Indicator Symbol Letter j}":
                            embed.add_field(name="日程", value=key + time)
                            embed.add_field(name="参加者", value=plan_confirmation_user_data[key])

                            await plan_confirmation_message.channel.send(embed=embed)

                if existDicidedPlan == False:
                    embed = discord.Embed(title="人数不足", description="今週のプライベートマッチはありません", color=discord.Colour.blue())
                    await plan_confirmation_message.channel.send(embed=embed)


# ループ処理実行
loop.start()
client.run(TOKEN)
