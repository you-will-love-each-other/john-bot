import discord
import random
import math
import asyncio
import variables

client = discord.Client()

@client.event
async def on_ready():
    print('HEALTHbot is online')

@client.event
async def on_message(message):
    if message.author.id == 742315532472025109:
        if message.content.startswith("!mute"):
            embed=discord.Embed(title=" ", color=0xff0000)
            embed.set_author(name="JohnBot has been muted.", icon_url="https://cdn.discordapp.com/avatars/838174410987798558/b3c2fe802ce0d94db463135df5069bd9.png")
            await client.get_channel(variables.hotlineID).send(embed= embed)

client.run(variables.healthbot)