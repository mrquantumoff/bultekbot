import nextcord, datetime, pprint, time, config, random, requests
# Base config
prefix = config.prefix
token = config.token
timeout = config.timeout
BASE = "https://discord.com/api/v9/"

class DiscordClient(nextcord.Client):
    async def on_ready(self):
        print('Logged in as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        # Respond on idc or i dont care messages with a rickroll
        if "idc" in message.content.lower() or 'i don\'t care' in message.content.lower() or "i dont care" in message.content.lower():
            await message.channel.send('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        elif "ratio" in message.content.lower():
            await message.reply("Don't care + didn't ask + L + Ratio + beta + cringe + cope + seethe + ok boomer + incel + virgin + Karen + 🤡🤡🤡 + you are not just a clown, you are the entire circus + 💅💅💅 + nah this ain't it + do better + check your privilege + 🤢🤢🤮🤮 + the cognitive dissonance is real with this one + 😂😂🤣🤣 + lol copium + 🚩🚩🚩 + those tears taste delicious + Lisa Simpson meme template saying that your opinion is wrong + 😒🙄🧐🤨 + wojak meme in which I'm the chad + average your opinion fan vs average my opinion enjoyer + random k-pop fancam + cry more + how's your wife's boyfriend doing + Cheetos breath + Intelligence 0 + r/whooooosh + r/downvotedtooblivion + blocked and reported + yo Momma so fat + I fucked your mom last night + what zero pussy does to a mf + Jesse what the fuck are you talking about + holy shit go touch some grass + cry about it + get triggered")
        elif "i want a cupcake" in message.content.lower():
            await message.reply("Are you EDP? Because you're nuts.")
        elif "i want a cookie" in message.content.lower():
            await message.reply("no.")
        elif  "ban me" in message.content.lower():
            await message.reply("Don't care + didn't ask + L + Ratio + beta + cringe + cope + seethe + ok boomer + incel + virgin + Karen + 🤡🤡🤡 + you are not just a clown, you are the entire circus + 💅💅💅 + nah this ain't it + do better + check your privilege + 🤢🤢🤮🤮 + the cognitive dissonance is real with this one + 😂😂🤣🤣 + lol copium + 🚩🚩🚩 + those tears taste delicious + Lisa Simpson meme template saying that your opinion is wrong + 😒🙄🧐🤨 + wojak meme in which I'm the chad + average your opinion fan vs average my opinion enjoyer + random k-pop fancam + cry more + how's your wife's boyfriend doing + Cheetos breath + Intelligence 0 + r/whooooosh + r/downvotedtooblivion + blocked and reported + yo Momma so fat + I fucked your mom last night + what zero pussy does to a mf + Jesse what the fuck are you talking about + holy shit go touch some grass + cry about it + get triggered")
            await message.author.send("suck my big dick and you're kicked so dont bother trying to ban me again and ur momma gay so I fuckeed her yeeeeeeeesterday")
            try:
                await message.author.kick()
            except:
                print("member's dick is bigger than mine")
        elif "lol" in message.content.lower():
            try:
                await message.author.kick()
            except:
                print("member's dick is bigger than mine")
        elif "fuck" in message.content.lower():
            await message.reply("No sex before marriage")
            try:
                await message.author.kick()
            except:
                print("member's dick is bigger than mine")
        elif "meth" in message.content.lower():
            await message.reply("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⠜⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⠿⠿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿\n⣿⣿⡏⠁⠀⠀⠀⠀⠀⣀⣠⣤⣤⣶⣶⣶⣶⣶⣦⣤⡄⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿\n⣿⣿⣷⣄⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡧⠇⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣾⣮⣭⣿⡻⣽⣒⠀⣤⣜⣭⠐⢐⣒⠢⢰⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣏⣿⣿⣿⣿⣿⣿⡟⣾⣿⠂⢈⢿⣷⣞⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣷⣶⣾⡿⠿⣿⠗⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠻⠋⠉⠑⠀⠀⢘⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⡿⠟⢹⣿⣿⡇⢀⣶⣶⠴⠶⠀⠀⢽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡿⠀⠀⢸⣿⣿⠀⠀⠣⠀⠀⠀⠀⠀⡟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠹⣿⣧⣀⠀⠀⠀⠀⡀⣴⠁⢘⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿\n⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⠗⠂⠄⠀⣴⡟⠀⠀⡃⠀⠉⠉⠟⡿⣿⣿⣿⣿\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⠾⠛⠂⢹⠀⠀⠀⢡⠀⠀⠀⠀⠀⠙⠛⠿⢿")
        elif "dick" in message.content.lower():
            await message.reply("how many dicks are in your ass?")
            time.sleep(10)
            await message.reply("The correct answer is "+str(random.randint(631635173,934254131434)))
        elif "putin" in message.content.lower() or "путин" in message.content.lower() or "путін" in message.content.lower():
            await message.reply("хуйло")
        elif "бандера" in message.content.lower():
            await message.reply("батько наш Бандера,\nУкраїна мати,\nМи за Україну підем воювати!")
        elif "shit" in message.content.lower():
            await message.reply("I hate taking shits. Taking shits is the worst function of the human organism after sex. You have to sit on the most uncomfortable seat ever, then you have to go through so much pain to push the shit out of your asshole (not to mention sometimes they get stuck in there). And as if those weren't enough then you have to wipe, you have to take your hand along with toilet paper and shove it up your asshole, this process can sometimes take minutes out of your life, it fucking sucks. \nTL;DR I hate shitting\nI am a human, and this action was not performed automatically. Please go fuck yourself if you have any questions or concerns.")
        elif  message.content.startswith(prefix):
            command = message.content[len(prefix):]
            print(command)
            if command == "help":
                await message.reply("Hi, I am discord shit messaging bot, inspired by r/shitposting's automoderator.\nWhat triggers me is a secret\nPrefix: "+prefix+"\nTimeout in minutes: "+str(timeout)+"\nCommands: *"+prefix+"mute <@user>, "+prefix+"kick <@user>, "+prefix+"(un)ban @<user> and "+prefix+"help*\n**This bot is licensed under the 2-Clause BSD License.\nCopyright ©️, 2022 Demir Yerli**")
            if command.startswith("ban"):
                if message.author.guild_permissions.ban_members and self not in message.mentions:
                    print("trying to ban")
                    for member in message.mentions:
                        try:
                            await member.ban(reason=message.author.name+"'s dick is bigger than your dick")
                            await message.reply("Banned "+member.name) 
                            print("Banned "+member.name)
                        except:
                            print("Couldn't ban "+member.name)
                else:
                    await message.reply("LMAO, his dick is bigger than yours")
                # Unban member
            if command.startswith("unban"):
                if message.author.guild_permissions.ban_members:
                    print("Trying to unban")
                    for member in message.mentions:
                        try:
                            await member.unban()
                            await message.reply("Unbanned "+member.name)
                            print("Unbanned "+member.name)
                        except:
                            print("Couldn't unban "+member.name)
                else:
                    print("LMAO, my dick is bigger than yours")
            if command.startswith("kick"):
                if message.author.guild_permissions.kick_members and self not in message.mentions:
                    print("trying to kick")
                    for member in message.mentions:
                        try:
                            await member.kick()
                            await message.reply("Kicked "+member.name)
                            await message.delete()
                        except:
                            print("Couldn't kick "+member.name)
                else:
                    await message.reply("LMAO, his dick is bigger than yours")
            if command.startswith("mute"):
                if message.author.guild_permissions.manage_roles and self.user not in message.mentions:
                    print("trying to mute")
                    for member in message.mentions:
                        try:
                            await member.timeout(datetime.timedelta(minutes=timeout))
                            await message.reply("Muted "+member.name)
                        except:
                            print("Couldn't mute "+member.name)
                else:
                    await message.reply("LMAO, his dick is bigger than yours")