import discord

class Billionaire(discord.Client):
    async def on_ready(self):
        print("Log in as {}".format(self.user))

    async def on_message(self, message : discord.Message):
        if message.author == self.user:
            return

        elif message.content.startswith("$"):


            command = message.content.strip("$ ")


            embed = discord.Embed()
            embed.set_image(url="https://cdn.discordapp.com/attachments/862160098959818762/874449653138071632/new_pfp.png")
            await message.channel.send(embed=embed)

client =  Billionaire()
client.run("ODc0MjcxOTU3MzkzMjE5NjA1.YREjNQ.o1f4UW6yigl_kpfVDAa0X-Zk3Ws")