import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f"Log in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == "(read)":


