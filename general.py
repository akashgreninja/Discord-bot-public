import discord
from discord.ext import commands
import datetime
import time
import random

today = datetime.datetime.now()
date_time = today.strftime("%m/%d/%Y, %H:%M:%S")

class general(commands.Cog):
	def __init__(self, bot):
		self.bot = bot




	@commands.command(help = 'the bot code')
	async def code(self,ctx):
		await ctx.send('**GUYS FEEL FREE TO USE MY CODE WOULD APPRICIATE IF YOU DONT DELETE THE &creator COMMAND ** https://github.com/akashgreninja/DISCORD')

	

	
	@commands.command(help = ' time')
	async def time(self,ctx):
		await ctx.send(date_time)


	@commands.command(help = ' date')
	async def date(self,ctx):
		await ctx.send(date_time)

	@commands.command(help = 'are you sus')	
	async def sus(self,ctx,*,member:discord.Member):
		responses=[' was a imposter',
          ' was not a imposter',
					' was ejected']
		await ctx.send(f'{member.mention} {random.choice(responses)}')				





	@commands.command(help = 'want to become a tester')
	async def tester(self,ctx):
  		await ctx.send('WANT TO TEST THIS BOT DM John Wick#9788 ON DISCORD HE WILL ADD YOU')	



	@commands.command(help = 'greets you')
	async def heybot(self,ctx):
  		await ctx.send('**hey human nice to have you here**')	
        

	
	@commands.command(help = 'tells whats new')
	async def new(self,ctx):
  		await ctx.send('  &clear use &help to see what they do ')



	@commands.command(help = 'who made me')
	async def creator(self,ctx):
  		await ctx.send(' Made by akash uday  \n Still improving it  \n made  using python,replit.com  \n')	



	@commands.command(help = 'WANT TO INVITE ME TO YOUR SERVER??')
	async def invite(self,ctx):
		await ctx.author.send('https://top.gg/bot/846282882716663820 ')
		await ctx.send("Check your DM for the link")
		

	
	@commands.command(help= 'sends the bot display picture')
	async def dp(self,ctx):
		await ctx.send(file=discord.File('GRENINJA BOT ori.jpg'))



	@commands.command(help = 'website still under development')
	async def website(self,ctx):
		await ctx.send('https://sites.google.com/view/greninjabot/home')	

	@commands.command(help="a toss")
	async def toss(self,ctx):
		toss=["HEADS",
		"TAILS"]
		await ctx.send(f'{random.choice(toss)}')

	@commands.command(help="support me by voting")
	async def vote(slef,ctx):
		await ctx.send("https://top.gg/bot/846282882716663820 \n **You can help me by voting **")
		
			

	@commands.command()
	async def serverinfo(self, ctx):
				"""Shows server info"""

				server = ctx.message.guild

				roles = str(len(server.roles))
				emojis = str(len(server.emojis))
				channels = str(len(server.channels))

				embeded = discord.Embed(title=server.name, description='Server Info', color=0xEE8700)
				embeded.set_thumbnail(url=server.icon_url)
				embeded.add_field(name="Created on:", value=server.created_at.strftime('%d %B %Y at %H:%M UTC+3'), inline=False)
				embeded.add_field(name="Server ID:", value=server.id, inline=False)
				embeded.add_field(name="Users on server:", value=server.member_count, inline=True)
				embeded.add_field(name="Server owner:", value=server.owner, inline=True)

				
				embeded.add_field(name="Server Region:", value=server.region, inline=True)
				embeded.add_field(name="Verification Level:", value=server.verification_level, inline=True)

				embeded.add_field(name="Role Count:", value=roles, inline=True)
				embeded.add_field(name="Emoji Count:", value=emojis, inline=True)
				embeded.add_field(name="Channel Count:", value=channels, inline=True)

	
				await ctx.send(embed=embeded)
				
 


