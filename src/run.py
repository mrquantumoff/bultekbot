import main
import config

if (__name__ == "__main__"):
    client = main.DiscordClient()
    client.run(config.token)