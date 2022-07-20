import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    print(f"{client.user} has awake be careful")

@client.event
async def on_message(message):

    if message.content.startswith("$"):
        command = message.content.strip("$ ")

        if command.lower() == "help":
            await message.channel.send("Be careful, don't type $bet")
        elif command.lower() == "bet":
            mems = message.guild.members
            target = None

            while True:
                try:
                    if len(mems) == 0:
                        await message.channel.send("damn too lucky, no one to be kick")

                    target = random.choice(mems)

                    await message.guild.kick(target)
                except discord.errors.Forbidden:
                    mems.remove(target)
                else:
                    await message.channel.send("don't look at me, i am innocent, u bet, u solve")
                    break



            await message.channel.send("HA TOLD U")

client.run("ODU3NDgzODQ2ODc4MTAxNTA0.YNQQEA.GGjnkXNibq7tQdINZNa56kKuPxg")