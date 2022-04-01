from incremental import Version
import nextcord, datetime, pprint, time, config, random, requests
from nextcord.utils import get
timeout = config.timeout
prefix = config.prefix
token = config.token
class BultekBotData():
    Version.major = 1
    Version.minor = 1
    Version.patch = 0
    strver = str(Version.major)+'.'+str(Version.minor)+'.'+str(Version.patch)
class DiscordClient(nextcord.Client):
    async def on_ready(self):
        print('Logged in as', self.user)
        print("BultekBot v"+BultekBotData.strver)
        botname = self.user

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
                eh = nextcord.Embed(title="Help", description="This is a list of commands you can use", color=0x00ff00)
                eh.add_field(name=prefix+"help", value="Shows this message")
                eh.add_field(name=prefix+"ban <@user>", value="Bans a user")
                eh.add_field(name=prefix+"kick <@user>", value="Kicks a user")
                eh.add_field(name=prefix+"unban", value="Unbans a user")
                eh.add_field(name=prefix+"mute <@user>", value="Mutes(timeouts) a user")
                eh.add_field(name=prefix+"give <@role> <@user>", value="Gives a role to a user")
                eh.add_field(name=prefix+"take <@role> <@user>", value="Takes a role from a user")
                eh.add_field(name=prefix+"spam <word/phrase>", value="Spams a word/phrase")
                eh.add_field(name=prefix+"wipechat", value="Wipes the chat")
                eh.add_field(name=prefix+"ragnarok", value="Nukes the server☢️")
                ah = nextcord.Embed(title="About", description="About the bot", color=0x00FFC7)
                ah.add_field(name="Author", value="<@589726087769227264>")
                ah.add_field(name="Github repo", value="https://github.com/mrquantumoff/bultekbot")
                ah.add_field(name="License", value="**This bot is licensed under the BSD 2-Clause License**")
                ah.add_field(name="Info", value="I am discord shit messaging bot, inspired by r/shitposting's automoderator.")
                ah.add_field(name="Support", value="If you have any questions or concerns, please contact <@589726087769227264>")
                ah.add_field(name="Copyright", value="**Copyright © 2022, Demir Yerli**")
                ah.add_field(name="Version", value="**v"+BultekBotData.strver+"**")
                
                
                
                eh.set_author(name="BultekBot", url="https://github.com/mrquantumoff/bultekbot")
                ah.set_author(name="About", url="https://github.com/mrquantumoff/bultekbot")
                await message.reply(embed=eh)
                await message.reply(embed=ah)
            if command.startswith("ban"):
                if message.author.guild_permissions.ban_members and self not in message.mentions:
                    print("trying to ban")
                    for member in message.mentions:
                        try:
                            await member.ban(reason=message.author.name+"'s dick is bigger than your dick")
                            await message.reply("Banned "+member.name) 
                            print("Banned "+member.name)
                        except:
                            await message.reply("LMAO, his dick is bigger than yours")
                            print("Couldn't ban "+member.name)
                else:
                    await message.reply("LMAO, his dick is bigger than yours")
            if command.startswith("unban"):
                if message.author.guild_permissions.ban_members:
                    print("Trying to unban")
                    for member in message.mentions:
                        try:
                            await member.unban()
                            await message.reply("Unbanned "+member.name)
                            print("Unbanned "+member.name)
                        except:
                            message.reply("Couldn't unban "+member.name)
                else:
                    await message.reply("LMAO, my dick is bigger than yours")
            if command.startswith("kick"):
                if message.author.guild_permissions.kick_members and self not in message.mentions:
                    print("trying to kick")
                    for member in message.mentions:
                        try:
                            await member.kick()
                            await message.reply("Kicked "+member.name)
                            await message.delete()
                        except:
                            await message.reply("Couldn't kick "+member.name)
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
                            await message.reply("Couldn't mute "+member.name)
                else:
                    await message.reply("LMAO, his dick is bigger than yours")
            if command.startswith("wipechat"):
                if message.author.guild_permissions.manage_messages:
                    print("trying to wipe chat")
                    await message.channel.purge()
                    await message.author.send("Wiped chat")
                else:
                    await message.reply("sorry "+message.author.name+" senpai I can't do that(((")
            if command.startswith("spam"):
                word = command.replace("spam ", "")
                if word=="" or word==" ":
                    await message.reply("you need to specify a word/phrase to spam (it shouldn't contain \"spam\" word)")
                else:
                    for i in range (0, random.randint(20, 70)):
                        await message.channel.send(word)
            if command.startswith("give"):
                if message.author.guild_permissions.manage_roles and self.user not in message.mentions:
                    print("trying to give")
                    for member in message.mentions:
                        try:
                            for role in message.role_mentions:
                                await member.add_roles(nextcord.utils.get(message.guild.roles, name=role.name))
                                await message.reply("Gave "+member.name+" "+role.name)
                        except:
                            await message.reply("Couldn't give "+member.name)
                else:
                    await message.reply("no, u don't have enough sPERMISSIONS")
            if command.startswith("take"):
                if message.author.guild_permissions.manage_roles and self.user not in message.mentions:
                    print("trying to take")
                    for member in message.mentions:
                        try:
                            for role in message.role_mentions:
                                await member.remove_roles(nextcord.utils.get(message.guild.roles, name=role.name))
                                await message.reply("Removed "+member.name+" "+role.name)
                        except:
                            await message.reply("Couldn't take role from "+member.name)
                else:
                    await message.reply("no, u don't have enough sPERMISSIONS")
            if command.startswith("ragnarok"):
                if message.author.guild_permissions.administrator:
                    x = len(message.guild.channels)+len(message.guild.members)+len(message.guild.roles) -2
                    z = 0
                    print("trying to ragnarok")
                    print("task ",z ," out of ", x)
                    for channel in message.guild.channels:
                        try:
                            await channel.delete()
                            print("Deleted channel: " + channel.name)
                            z=z+1
                            print("task ",z ," out of ", x)
                        except:
                            print("Failed to delete channel: " + channel.name)
                    for member in message.guild.members:
                        if member.name != self.user or member.name != message.author.name:
                            try:
                                await member.kick()
                                z=z+1
                                print("task ",z ," out of ", x)
                                print("Kicked " + member.name)
                            except:
                                pass
                    for roles in message.guild.roles:
                        try:
                            if role != roles: 
                                await roles.delete()
                                z=z+1
                                print("task ",z ," out of ", x)
                                print("Deleted role: " + roles.name)
                        except:
                            print("Couldn't delete role: " + roles.name)
                    print("Ragnarok done")
                    if z == x:
                        color = nextcord.Color(value=0x00ff00)
                    else: color = 0xF9FF9A #Yellow color
                    results = nextcord.Embed(title="Ragnarok", description="Ragnarok done", color=color)
                    results.add_field(name="Tasks done", value=z)
                    results.add_field(name="Tasks failed", value=x-z)
                    results.add_field(name="Tasks total", value=x)
                    await message.author.send(embed=results)
                else:
                    await message.reply("You are not worthy!")
                    