
import os
import random

from database import *

## discord stuff
import discord
from discord.ext import commands

## env stuff
from dotenv import dotenv_values
config = dotenv_values(".env")

db = Users(config["dbfile"])

## BOT CONfig
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

### COMANDS ---------
@bot.command()
async def rps(ctx, choice):
    possible = ["rock", "paper", "scissors"]
    if choice not in possible:
        await ctx.send(":x: Invalid choice")
        return
    db.insert(ctx.author.id, ctx.author.name)
    player_wins_txt = ":person_tipping_hand: Player wins"
    bot_wins_txt = ":robot: Bot wins"
    bot_choice = random.choice(possible)
    emo = {
        "rock": ":moyai: Rock",
        "paper": ":page_facing_up: Paper",
        "scissors": ":scissors: Scissors",
    }
    choice_txt = emo[choice]
    bot_choice_txt = emo[bot_choice]
    if choice == bot_choice:
        result = ":person_gesturing_ok: Draw"
        db.update(ctx.author.id, "draw")
    elif choice == "rock" and bot_choice == "scissors":
        result = player_wins_txt
        db.update(ctx.author.id, "win")
    elif choice == "paper" and bot_choice == "rock":
        result = player_wins_txt
        db.update(ctx.author.id, "win")
    elif choice == "scissors" and bot_choice == "paper":
        result = player_wins_txt
        db.update(ctx.author.id, "win")
    else:
        result = bot_wins_txt
        db.update(ctx.author.id, "lose")
    out_text = """
    Rock Paper Scissors:
    Player: {}
    Bot: {}
    Result: {}
    """.format(choice_txt, bot_choice_txt, result)
    await ctx.send(out_text)

@bot.command()
async def rpslist(ctx):
    await ctx.send("Rock, Paper, Scissors")

@bot.command()
async def rpsinfo(ctx):
    out = db.select(ctx.author.id)
    out_txt = """\n
    :white_check_mark: {} | :x: {} | :crossed_swords: {}
    """.format(out[4],
               out[5],
               out[6])
    await ctx.send("{}".format(out_txt))


bot.run(config["token"])
