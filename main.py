from http.client import FORBIDDEN
from sys import prefix
import discord
from discord.ext import commands
import time
import random
# Base config
prefix = "bb!"
token = "Njg4NzQ0ODY1MjMxNTM2MjEx.Xm4xpA.7chLlq0OWPzkaGVPkCLMVC786SY"
class DiscordClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        # Respond on idc or i dont care messages with a rickroll
        if "idc" in message.content.lower() or 'i don\'t care' in message.content.lower() or "i dont care" in message.content.lower():
            await message.channel.send('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        if "ratio" in message.content.lower():
            await message.reply("Don't care + didn't ask + L + Ratio + beta + cringe + cope + seethe + ok boomer + incel + virgin + Karen + 🤡🤡🤡 + you are not just a clown, you are the entire circus + 💅💅💅 + nah this ain't it + do better + check your privilege + 🤢🤢🤮🤮 + the cognitive dissonance is real with this one + 😂😂🤣🤣 + lol copium + 🚩🚩🚩 + those tears taste delicious + Lisa Simpson meme template saying that your opinion is wrong + 😒🙄🧐🤨 + wojak meme in which I'm the chad + average your opinion fan vs average my opinion enjoyer + random k-pop fancam + cry more + how's your wife's boyfriend doing + Cheetos breath + Intelligence 0 + r/whooooosh + r/downvotedtooblivion + blocked and reported + yo Momma so fat + I fucked your mom last night + what zero pussy does to a mf + Jesse what the fuck are you talking about + holy shit go touch some grass + cry about it + get triggered")
        if "i want a cupcake" in message.content.lower():
            await message.reply("Are you EDP? Because you're nuts.")
        if "i want a cookie" in message.content.lower():
            await message.reply("no.")
        if  "ban me" in message.content.lower():
            await message.reply("Don't care + didn't ask + L + Ratio + beta + cringe + cope + seethe + ok boomer + incel + virgin + Karen + 🤡🤡🤡 + you are not just a clown, you are the entire circus + 💅💅💅 + nah this ain't it + do better + check your privilege + 🤢🤢🤮🤮 + the cognitive dissonance is real with this one + 😂😂🤣🤣 + lol copium + 🚩🚩🚩 + those tears taste delicious + Lisa Simpson meme template saying that your opinion is wrong + 😒🙄🧐🤨 + wojak meme in which I'm the chad + average your opinion fan vs average my opinion enjoyer + random k-pop fancam + cry more + how's your wife's boyfriend doing + Cheetos breath + Intelligence 0 + r/whooooosh + r/downvotedtooblivion + blocked and reported + yo Momma so fat + I fucked your mom last night + what zero pussy does to a mf + Jesse what the fuck are you talking about + holy shit go touch some grass + cry about it + get triggered")
            await message.author.send("suck my big dick and you're banned so dont bother trying to ban me again and ur momma gay so I fuckeed her yeeeeeeeesterday")
            await time.sleep(2)
            try:
                await message.author.kick()
            except:
                print("member's dick is bigger than mine")
        if "lol" in message.content.lower():
            try:
                await message.author.kick()
            except:
                print("member's dick is bigger than mine")
        if "fuck" in message.content.lower():
            await message.reply("No sex before marriage")
            try:
                await message.author.kick()
            except:
                print("member's dick is bigger than mine")
        if "meth" in message.content.lower():
            await message.reply("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⠜⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⠿⠿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿\n⣿⣿⡏⠁⠀⠀⠀⠀⠀⣀⣠⣤⣤⣶⣶⣶⣶⣶⣦⣤⡄⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿\n⣿⣿⣷⣄⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡧⠇⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣾⣮⣭⣿⡻⣽⣒⠀⣤⣜⣭⠐⢐⣒⠢⢰⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣏⣿⣿⣿⣿⣿⣿⡟⣾⣿⠂⢈⢿⣷⣞⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣷⣶⣾⡿⠿⣿⠗⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠻⠋⠉⠑⠀⠀⢘⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⡿⠟⢹⣿⣿⡇⢀⣶⣶⠴⠶⠀⠀⢽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡿⠀⠀⢸⣿⣿⠀⠀⠣⠀⠀⠀⠀⠀⡟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠹⣿⣧⣀⠀⠀⠀⠀⡀⣴⠁⢘⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿\n⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⠗⠂⠄⠀⣴⡟⠀⠀⡃⠀⠉⠉⠟⡿⣿⣿⣿⣿\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⠾⠛⠂⢹⠀⠀⠀⢡⠀⠀⠀⠀⠀⠙⠛⠿⢿")
        if "dick" in message.content.lower():
            await message.reply("how many dicks are in your ass?")
            time.sleep(10)
            await message.reply("The correct answer is "+str(random.randint(631635173,934254131434)))
        if  message.content.startswith(prefix):
            command = message.content[1:]
            print(command)
        

client = DiscordClient()

client.run(token)