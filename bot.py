# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


class MyClient(discord.Client):

    async def on_message(self, msg: discord.Message):
        if msg.author == self.user:
            return

        print(f'content: {msg.content}')
        print(f'stickers: {msg.stickers}')
        if msg.stickers:
            for i in msg.stickers:
                print(f'sticker type: {i.format}')



client = MyClient()
client.run(TOKEN)
