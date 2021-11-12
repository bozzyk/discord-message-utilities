# bot.py
import os

import discord
from datetime import datetime, timedelta
import requests
import random
import json
import asyncio
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
TENOR_TOKEN = os.getenv('TENOR_TOKEN')

class MyClient(discord.Client):
    
    async def setup_server(self, server):
        
        self.default_channel[server.id] = discord.utils.get(server.channels, name='kabachok')
    
    async def on_ready(self):
        
        self.default_channel = {}
        for server in client.guilds:
            await self.setup_server(server)
        
        self.dead_chat_threshold = timedelta(days=0, seconds=0, minutes=60)
        self.dead_chats = {server.id: False for server in client.guilds}
        
        for server_id, is_dead in self.dead_chats.items():
            if not is_dead:
                server = discord.utils.get(client.guilds, id=server_id)
                await self.dead_chat_xd_check(server)
            
    async def dead_chat_xd_check(self, server):
        
        print('checking dead chat xd')
        if self.dead_chats[server.id]:
            return
        
        last_message_dt = datetime.min
        for channel in server.text_channels:
            latest_msg = await channel.history(limit=1).flatten()
            latest_msg = latest_msg[0] # FIXME: empty channels

            last_message_dt = max(last_message_dt, latest_msg.created_at)
            
        self.last_message_dt = last_message_dt
        
        dt_diff =  datetime.utcnow() - self.last_message_dt
        if dt_diff > self.dead_chat_threshold:
            self.dead_chats[server.id] = True
            print('dead chat XD')
            await self.send_tenor_msg(self.default_channel[server.id], 'dead chat XD')
        else:
            await asyncio.sleep((dt_diff - self.dead_chat_threshold).total_seconds())
            await self.dead_chat_xd_check(server)
            
    async def send_tenor_msg(self, channel, query, limit=20):

        r = requests.get(
            f"https://g.tenor.com/v1/search?q={query}&key={TENOR_TOKEN}&limit={limit}")

        if r.status_code == 200:
            gifs = json.loads(r.content)
        else:
            print("Got status code {r.status_code}") # TODO: logging
            return
            
        chosen_gif = random.randrange(limit)
        gif_url = gifs['results'][chosen_gif]['media'][0]['gif']['url']
        
        await channel.send(gif_url)

    async def on_message(self, msg: discord.Message):
        
        if msg.author == self.user:
            return
        
        if not msg.author.bot and self.dead_chats[msg.guild.id]:
            self.dead_chats[msg.guild.id] = False
            await asyncio.sleep(self.dead_chat_threshold.total_seconds())
            await self.dead_chat_xd_check(msg.guild)

intents = discord.Intents().all() # FIXME:

client = MyClient(intents=intents)
client.run(DISCORD_TOKEN)
