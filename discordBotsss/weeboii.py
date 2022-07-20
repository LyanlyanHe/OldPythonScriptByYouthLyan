import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f"Log in as {client.user}")

@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return
    
    await message.channel.send(message.content)
    # if message.content.startswith("$"):
        
    #     command = message.content.strip("$ ")

    #     args = command.split()

    #     if args[0] == "ban":
            
    #         target_id = int(args[1].strip("<!@>"))

    #         await message.guild.ban([x for x in filter(lambda member: member if member.id == target_id else None, message.guild.members) if x is not None][0], reason="")



client.run("ODQ3OTkyODk5NzkzODQ2MzIz.YLGI7g.gLDizGrm6GKjv4JKR0S6vWmCEvo")