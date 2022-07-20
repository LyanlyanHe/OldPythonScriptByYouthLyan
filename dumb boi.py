import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    print("Log in as {}".format(client.user))

    bot_support = None
    for guild in client.guilds:
        if guild.id == 873095066724487218:
            bot_support = guild
            break

    general_channel = None
    for channel in bot_support.channels:
        if (channel.id == 873448423284670585):
            general_channel = channel
            break

    word_list = ["fuck", "shit", "dummy", "dumbass", "idiot", "pig", "loser", "go eat poop", "#####", "&$(*&$(#&*$", "holy shit"]
    while True:
        await general_channel.send(random.choice(word_list))

@client.event
async  def on_message(message):
    if (message.author == client.user): return

    print("{} saids: >> {}".format(message.author, message.content))

client.run("ODc0MTU1NzUyNTEwNjE5NzI5.YRC2_A.eGufHydLQWu35TR5Z2Vixy1Mb-w")