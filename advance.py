import discord
from discord.ext import commands
from discord.ext.commands.core import has_guild_permissions
import giphy_client
from giphy_client.rest import ApiException
import random
import aiohttp
import json
from discord import Embed,Color
from discord_components import *
from discord.ext.commands import Bot
import DiscordUtils

class advance(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	
	@commands.command(help="Gets info about the user")
	async def userinfo(self,ctx):
		user = ctx.author

		embed=discord.Embed(title="USER INFO",description=f"Here is the info we retrieved about {user}", colour=user.colour)
		embed.set_thumbnail(url=user.avatar_url)
		embed.add_field(name="NAME", value=user.name, inline=True)
		embed.add_field(name="NICKNAME", value=user.nick, inline=True)
		embed.add_field(name="ID", value=user.id, inline=True)
		embed.add_field(name="STATUS", value=user.status, inline=True)
		embed.add_field(name="TOP ROLE", value=user.top_role.name, inline=True)
		await ctx.send(embed=embed)

	@commands.command(help="Gets info about the user")
	async def memberinfo(self,ctx, member: discord.Member=None):
		if member == None:
			member =ctx.author
			try:
				embed=discord.Embed(title="USER INFO",description=f"Here is the info we retrieved about {user}", colour=user.colour)
				embed.set_thumbnail(url=user.avatar_url)
				embed.add_field(name="NAME", value=user.name, inline=True)
				embed.add_field(name="NICKNAME", value=user.nick, inline=True)
				embed.add_field(name="ID", value=user.id, inline=True)
				embed.add_field(name="STATUS", value=user.status, inline=True)
				embed.add_field(name="TOP ROLE", value=user.top_role.name, inline=True)
			except:
				await ctx.send(embed=embed)	


	@commands.command(help="gives a funny meme")
	async def gif(self,ctx,*,q="funny meme"):
		api_key="i5LNUs1AAmqop5JWZOYeszAlhP9ODtRI"
		api_instance = giphy_client.DefaultApi()
		try:
			api_response = api_instance.gifs_search_get(api_key,q,limit=5, rating='g')
			lst = list(api_response.data)
			giff = random.choice(lst)
			emb = discord.Embed(title=q)
			emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')
			await ctx.channel.send(ctx.author)
			await ctx.channel.send(embed=emb)
		except ApiException as e:
			print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)	
	
	@commands.command(help="GIVES A CUTE DOGGO PIC",aliases=['dog'])
	async def doggif(self,ctx,*,q="random cute dog"):
		api_key="i5LNUs1AAmqop5JWZOYeszAlhP9ODtRI"
		api_instance = giphy_client.DefaultApi()
		try:
			api_response = api_instance.gifs_search_get(api_key,q,limit=5, rating='g')
			lst = list(api_response.data)
			giff = random.choice(lst)
			emb = discord.Embed(title=q)
			emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')
		
			await ctx.channel.send(embed=emb)
		except ApiException as e:
			print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)	

	@commands.command(help="GIVES A RANDOM PIC",aliases=['rand'])
	async def randomgif(self,ctx,*,q="random"):
		api_key="i5LNUs1AAmqop5JWZOYeszAlhP9ODtRI"
		api_instance = giphy_client.DefaultApi()
		try:
			api_response = api_instance.gifs_search_get(api_key,q,limit=10, rating='g')
			lst = list(api_response.data)
			giff = random.choice(lst)
			emb = discord.Embed(title=q)
			emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')
		
			await ctx.channel.send(embed=emb)
		except ApiException as e:

			
			print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)				

	@commands.command(help="use it to cheer someone")
	async def cheer(self,ctx,*,member: discord.Member,q="cheer"):
		api_key="i5LNUs1AAmqop5JWZOYeszAlhP9ODtRI"
		api_instance = giphy_client.DefaultApi()
		try:
			api_response = api_instance.gifs_search_get(api_key,q,limit=5, rating='g')
			lst = list(api_response.data)
			giff = random.choice(lst)
			emb = discord.Embed(title=q)
			emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')
			await ctx.channel.send( member.mention)
			await ctx.channel.send(embed=emb)
		except ApiException as e:
			print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)		


	@commands.command(help="funny animal pics")
	async def funnygif(self,ctx,*,q="funny animal pictures"):
		api_key="i5LNUs1AAmqop5JWZOYeszAlhP9ODtRI"
		api_instance = giphy_client.DefaultApi()
		try:
			api_response = api_instance.gifs_search_get(api_key,q,limit=5, rating='g')
			lst = list(api_response.data)
			giff = random.choice(lst)
			emb = discord.Embed(title=q)
			emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')
	
			await ctx.channel.send(embed=emb)
		except ApiException as e:
			print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)	
	
	@commands.command(help="BOOP",aliases=['nose'])
	async def boop(self,ctx,*,q="dog boop"):
		api_key="i5LNUs1AAmqop5JWZOYeszAlhP9ODtRI"
		api_instance = giphy_client.DefaultApi()
		try:
			api_response = api_instance.gifs_search_get(api_key,q,limit=5, rating='g')
			lst = list(api_response.data)
			giff = random.choice(lst)
			emb = discord.Embed(title=q)
			emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')
		
			await ctx.channel.send(embed=emb)
		except ApiException as e:
			print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)
			
	@commands.command()
	async def botinfo(self,ctx):
		em = discord.Embed(color=discord.Color.green())
		em.title = 'Bot Info'
		em.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
		try:
			em.description = self.bot.psa + '\n[Support Server](https://discord.gg/RzsYQ9f)'
		except AttributeError:
			em.description = 'A multipurpose bot made by Akashgreninja aka John Wick#9788 using pycharm,replit.\n[Support Server](https://discord.gg/sSCnXnj2)'
			em.add_field(name="Servers", value=len(self.bot.guilds))
			em.add_field(name="Online Users", value=str(len({m.id for m in self.bot.get_all_members() if m.status is not discord.Status.offline})))
			em.add_field(name='Total Users', value=len(self.bot.users))
			em.add_field(name='Channels', value=f"{sum(1 for g in self.bot.guilds for _ in g.channels)}")
			em.add_field(name="Library", value=f"discord.py")
			em.add_field(name="Bot Latency", value=f"{self.bot.ws.latency * 1000:.0f} ms")
			em.add_field(name="Invite", value=f"[Click Here](https://discord.com/api/oauth2/authorize?bot_id=846282882716663820&permissions=4294441975&scope=bot)")
			em.add_field(name="Github", value=f"Coming soon")
			em.add_field(name="Upvote this bot!", value=f"[Click here](https://top.gg/bot/846282882716663820) :reminder_ribbon:")
			em.set_footer(text="GreninjaBot | Powered by discord.py")
			await ctx.send(embed=em)
			
			
			
	@commands.command()
	@commands.is_owner()
	async def servers(self,ctx):
		await ctx.send(len(self.bot.guilds))









			


	        
