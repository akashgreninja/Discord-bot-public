import os
import discord
from discord.ext import commands
from discord.ext.commands.core import has_guild_permissions
from pistonapi import PistonAPI
import requests
import DiscordUtils
from discord.ext import tasks
from datetime import date
intents= discord.Intents.default()
intents.members=True
client = commands.Bot(command_prefix='&', intents=intents)
import asyncio
from discord import Embed,Color



from music import music
from intermediate import intermediate
from advance import advance
from admin import admin
from general import general
piston = PistonAPI()




client.add_cog(music(client))
client.add_cog(general(client))
client.add_cog(intermediate(client))
client.add_cog(advance(client))
client.add_cog(admin(client))


	

	

@client.event
async def on_ready():
	watching = discord.Activity(type=discord.ActivityType.watching, name=f'over {len(client.users)} users')
	await client.change_presence(activity=watching)
	
	
	
@client.event
async def on_guild_join(guild):
	for channel in guild.text_channels:
		if channel.permissions_for(guild.me).send_messages:
			guildname=guild.name
			await channel.send(f'Thank you for adding me in {guildname}  you may start by using the ``welcomemessage`` to add the channel to send the welcome me to and then the ``&help`` command to get started ')
		break	
      	
      		
	
	


@client.command()
async def run(ctx, n, *, code):
    nm = n.lower()
    a = code.replace("```", "")

    if nm == "py":
        b = (piston.execute(language="py", version="3.9", code=a))
        c = str(b)
        em = discord.Embed(title="Python Code Output!",
                           description=f'```py\nOutput:\n{c}```',
                           color=discord.Color.red())

    elif nm == "java":
        b = (piston.execute(language="java", version="15.0.2", code=a))
        c = str(b)
        em = discord.Embed(title="Java Code Output!",
                           description=f'```py\nOutput:\n{c}```',
                           color=discord.Color.red())

    elif nm == "js":
        b = (piston.execute(language="js", version="15.10.0", code=a))
        c = str(b)
        em = discord.Embed(title="JavaScript Code Output!",
                           description=f'```py\nOutput:\n{c}```',
                           color=discord.Color.red())

    elif nm == "go":
        b = (piston.execute(language="go", version="1.16.2", code=a))
        c = str(b)
        em = discord.Embed(title="Go Code Output!",
                           description=f'```py\nOutput:\n{c}```',
                           color=discord.Color.red())

    elif nm == "ts":
        b = (piston.execute(language="typescript", version="4.2.3", code=a))
        c = str(b)
        em = discord.Embed(title="TypeScript Code Output!",
                           description=f'```py\nOutput:\n{c}```',
                           color=discord.Color.red())

    elif nm == "bf":
        b = (piston.execute(language="brainfuck", version="2.7.3", code=a))
        c = str(b)
        em = discord.Embed(title="BrainFuck Code Output!",
                           description=f'```py\nOutput:\n{c}```',
                           color=discord.Color.red())

    else:
        em = discord.Embed(title="**Not a supported language!!**")

    await ctx.send(embed=em)



client.run('Enter your token')	
	

			



