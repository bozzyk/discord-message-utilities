# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


class MyClient(discord.Client):

    async def on_message(self, msg):
        print(msg.content)


client = MyClient()
client.run(TOKEN)
