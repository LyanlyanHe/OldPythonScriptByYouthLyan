import discord

client = discord.Client()

@client.event
async  def on_ready():
    print("Log in as {}".format(client.user))

    study_buddies = None
    for guild in client.guilds:
        if guild.id == 868051749469036585:
            print("Hack into {}".format(guild.name))
            study_buddies = guild
            break

    general_channel = None
    for channel in study_buddies.channels:
        if channel.name == "general":
            print("Find it!  The {}".format(channel.name))
            general_channel = channel
            break

    captain = None
    for role in study_buddies.roles:
        print(role.name)
        if role.id == 868068804817727498:
            print("FIND THE ROLES : {}".format(role.name))
            captain = role
            break

    while True:
        command = input("> ")

        if command == "/end":
            print("QUIT")
            break
        elif command.startswith("/add"):
            user = await study_buddies.fetch_member(int(input("WHo ???")))

            if (user is None):
                print("Not ofund")
                continue

            await user.add_roles(captain)
            print("SUCESS")

        else:
            await general_channel.send(command)

client.run("ODY5MDU2NjU1Mzg2NjI4MTE3.YP4qFA.FRjns02M9Rd8AyH4e7fu8Pcw-3E")