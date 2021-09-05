# coding: utf-8
import discord
from discord.ext import tasks
import datetime
import random
import os

TOKEN = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()

userdata_id_dictionary = {}

plan_confirmation_message = None
plan_confirmation_user_data = {}
plan_confirmation_channel_id = 483064145516953615
#plan_confirmation_channel_id = 860492700579266560

@client.event
async def on_raw_reaction_add(payload):

    if payload.member.bot:
        return

    global plan_confirmation_user_data

    if payload.channel_id == 483064145516953615:
        channel = client.get_channel(plan_confirmation_channel_id)

        usr = User(payload.member.name, payload.user_id)

        if payload.emoji.name not in plan_confirmation_user_data:
            plan_confirmation_user_data[payload.emoji.name] = []
        plan_confirmation_user_data[payload.emoji.name].append(usr)

        print(plan_confirmation_user_data)

        #await channel.send('Add User '+usr.name+' to '+payload.emoji.name)

@client.event
async def on_raw_reaction_remove(payload):
    global plan_confirmation_user_data

    channel = client.get_channel(plan_confirmation_channel_id)

    for usr in plan_confirmation_user_data[payload.emoji.name]:
        if usr.id == payload.user_id:
            plan_confirmation_user_data[payload.emoji.name].remove(usr)

    print(plan_confirmation_user_data)

    #await channel.send('Remove User ' + usr.name + ' to ' + payload.emoji.name)



@client.event
async def on_message(message):
    # 送信者がBotの場合は反応しない
    if message.author.bot:
        return

    global plan_confirmation_channel_id
    plan_confirmation_channel_id = message.channel.id


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

    if message.content == '/decision':
        global plan_confirmation_user_data
        existDicidedPlan = False
        await message.channel.send('@everyone')
        for key in plan_confirmation_user_data:
            if len(plan_confirmation_user_data[key]) >= 6:
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
                    embed.add_field(name="日程", value=key + time)

                    for value in plan_confirmation_user_data[key]:
                        num = 1
                        embed.add_field(name="参加者"+num, value=value.name, inline=False)
                        num = num + 1

                    await plan_confirmation_message.channel.send(embed=embed)

        if existDicidedPlan == False:
            embed = discord.Embed(title="人数不足", description="今週のプライベートマッチはありません", color=discord.Colour.blue())
            await plan_confirmation_message.channel.send(embed=embed)

class User:
    name: str
    id: int

    def __init__(self, name, id):
        self.name = name
        self.id = id


# ループ処理実行
client.run(TOKEN)
