import bot
import config

if (__name__ == "__main__"):
    client = bot.DiscordClient()
    client.run(config.token)
else:
    print("This file is not intended to be imported!")
    exit(1)