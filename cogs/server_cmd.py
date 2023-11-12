from discord.ext import commands 
import discord

class Server(commands.Cog):
    """class for server related commands"""
    def __init__(self, bot):
        self.bot = bot
        
    @commands.hybrid_command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def lock_all_channels(self, ctx):
        """locks all channels of the current guild"""
        if ctx.message.author.guild_permissions.administrator:
            for channel in ctx.guild.channels:
                await channel.set_permissions(ctx.guild.default_role, send_messages=False)
            embed = discord.Embed()
            embed.add_field(name=':white_check_mark:', value=':lock: Todos os canais foram trancados.')
            await ctx.reply(embed=embed)
        else:
            await ctx.reply('Você não possui autorização para usar esse comando.')
            
            
    @commands.hybrid_command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def unlock_all_channels(self, ctx):
        """unlocks all channels of the current guild"""
        if ctx.message.author.guild_permissions.administrator:
            for channel in ctx.guild.channels:
                await channel.set_permissions(ctx.guild.default_role, send_messages=True)
            embed = discord.Embed()
            embed.add_field(name=':white_check_mark:', value=':unlock: Todos os canais foram destrancados.')
            await ctx.reply(embed=embed)
        else:
            await ctx.reply('Você não possui autorização para usar esse comando.')
            
async def setup(client):
    """adds the class to the cog handler"""
    await client.add_cog(Server(client))
        
    