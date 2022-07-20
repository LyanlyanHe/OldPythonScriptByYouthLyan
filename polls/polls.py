import discord

client = discord.Client()
holding_poll = False
host = discord.User

@client.event
async def on_ready():
    print("Log in as {}".format(client.user))

@client.event
async def on_message(message : discord.Message):
    if (message.author == client.user):
        return

    if (message.content.startswith("$")):
        global holding_poll, host, msg, polls_title, polls_emojis, msg_channel
        command = message.content.strip("$")

        if (command.lower() == "help"):
            await message.channel.send("$polls Title 'description' { choice1: emoji1, choice2: emoji2, ..., choiceN: emojiN }")
        elif (command.startswith("polls")):
            if (holding_poll):
                await message.channel.send("There is already a polls holding by {}".format(host.mention))
                return

            try:
                polls_args = command.rstrip("$polls").strip()
                polls_title = polls_args.split(" ")[0]
                polls_description = between("'", "'", polls_args) + "\n\n"
                polls_emojis = [x.strip() for x in between("{", "}", polls_args).split(",")]
            except Exception:
                await message.channel.send("FUCK UR POLLS IS WRONG")
                return

            holding_poll = True
            host = message.author

            emojis_to_add = []
            for choice in polls_emojis:
                text, emo = [x.strip() for x in choice.split(":")]

                emojis_to_add.append(emo)
                polls_description += "{} = {}\n".format(text, emo)

            await message.channel.send("Guys {} has host a polls. Check Out".format(message.author.mention))
            msg = await message.channel.send(embed=discord.Embed(title=polls_title, description=polls_description))
            msg_channel = msg.channel

            for emoji in emojis_to_add:
                await msg.add_reaction(emoji)
        elif (command.lower() == "result"):
            if (not holding_poll or msg_channel != message.channel):
                await message.channel.send("No polls is host yet! (or) Please use the command in the channel where the polls is host")
                return
            else:
                result_title = "Polls result for {}".format(polls_title)
                result_description = ""
                current_msg = discord.utils.get(await msg_channel.history().flatten(), id=msg.id)


                for choice in polls_emojis:
                    text, emo = [x.strip() for x in choice.split(":")]

                    result_description += text + "  "

                    for react in current_msg.reactions:
                        if (react.emoji == emo):
                            result_description += str(react.count - 1) + " "

                            for _ in range(react.count - 1):
                                result_description += emo + " "
                            result_description += "\n"
                            break

                await message.channel.send(embed=discord.Embed(title=result_title, description=result_description))
        elif (command.lower() == "end"):
            if (not holding_poll):
                await message.channel.send("No polls hold yet what the fuck are you thinking")
                return
            elif (message.author != host):
                await message.channel.send("Only host can quit polls (Pro hint: host is {})".format(host.mention))
                return
            else:
                await message.channel.send("Polls reset.")


def between(start : str, end : str, text: str):
    output = ""
    is_between = False

    for letter in text:
        if (letter == start and is_between == False):
            is_between = True
        elif (letter == end):
            return output
        elif (is_between):
            output += letter


client.run("ODY5NDkzNDQ0MDI2OTU3ODY1.YP_A3w.dYSAlOVphXkgxBaznX0SiZjHqj0")