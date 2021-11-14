import discord
from discord.ext import commands
from discord.ext.commands.core import has_guild_permissions

class admin(commands.Cog):
	
	
	def __init__(self, bot):
		self.bot =bot
	
	

	@commands.command(help="Mutes the specified user.")
	@commands.has_permissions(manage_messages=True)
	async def mute(self,ctx, member: discord.Member, *, reason=None):
		guild = ctx.guild
		mutedRole = discord.utils.get(guild.roles, name="Muted")

		if not mutedRole:
			mutedRole = await guild.create_role(name="Muted")

			for channel in guild.channels:
				await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)

		await member.add_roles(mutedRole, reason=reason)
		await ctx.send(f"Muted {member.mention} for reason {reason}")
		await member.send(f"You were muted in the server {guild.name} for {reason}")

	@commands.command(help="Unmutes a specified user.")
	@commands.has_permissions(manage_messages=True)
	async def unmute(self,ctx, member: discord.Member):
		mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

		await member.remove_roles(mutedRole)
		await ctx.send(f"Unmuted {member.mention}")
		await member.send(f"You were unmuted in the server {ctx.guild.name}")

	@commands.command(help="Bans a member")
	@commands.has_permissions(ban_members=True)
	async def ban(self,ctx, member: discord.Member, *, reason=None):
		await member.ban(reason=reason)
		await ctx.send(f"{member} was banned!")	

	@commands.command(help="Unbans a member")
	@commands.has_permissions(ban_members=True)
	async def unban(self,ctx, *, member):
		bannedUsers = await ctx.guild.bans()
		name, discriminator = member.split("#")

		for ban in bannedUsers:
				user = ban.user

				if(user.name, user.discriminator) == (name, discriminator):
						await ctx.guild.unban(user)
						await ctx.send(f"{user.mention} was unbanned.")
						return	

	@commands.command()
	async def nick(self,ctx,member: discord.Member,*,nickname):

		
		await member.edit(nick=nickname)
		await ctx.send(f"Nickname was changed to {member.mention}.")
		
		
	@commands.command()
	@commands.has_permissions(manage_channels=True)
	async def lockdown(self,ctx):
		await ctx.channel.set_permissions(ctx.guild.default_role,send_messages=False)
		await ctx.send( ctx.channel.mention + " ***is now in lockdown use ```&unlock``` for reversing it back.***")

	@commands.command()
	@commands.has_permissions(manage_channels=True)
	async def unlock(self,ctx):
		await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
		await ctx.send(ctx.channel.mention + " ***has been unlocked.***")
		
		
	#@commands.Cog.listener()
	#async def on_message(self,message):

		#filters=['nigga','xyz']
		#spam=['fruad']
		#for word in filters:

			#if word in message.content.lower():
#
				#await message.channel.purge(limit=1)
				#await message.channel.send("KEEP IT FRIENDLY BUDDY",delete_after=3)

		#for word in spam:
			#if word in message.content.lower():

			#	await message.channel.purge(limit=1)
			#	await message.channel.send("Probable fraud message check mod logs for more info")	
		





