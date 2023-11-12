from typing import Union
from discord.ext import commands
import discord 
class User(commands.Cog):
    """class for user related commands"""
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def user_avatar(self, ctx, *,  user: discord.User=None):
        """sends the user avatar"""
        user = ctx.message.author if user == None else user

        avatar_url = user.avatar
        embed = discord.Embed(title=f"Avatar de {user.name}")
        embed.set_author(name=f"{user}", icon_url=f"{avatar_url}")
        embed.set_image(url=avatar_url)
        embed.set_footer(text=f"Requerido por: {ctx.message.author}", icon_url=ctx.author.avatar)
        await ctx.reply(embed=embed)

    @commands.hybrid_command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def user_info(self, ctx, *, user: discord.User=None):
        """sends the user info"""
        user = ctx.message.author if user == None else user 

        embed = discord.Embed(title=f"Info de {user.name}")
        embed.set_thumbnail(url=user.avatar)
        embed.set_author(name=f"{user}", icon_url=user.avatar)
        embed.add_field(name="ID", value=user.id, inline=True)
        embed.add_field(name='Username', value=f"@{user.name}", inline=True)
        embed.add_field(name='Nome global', value=user.global_name, inline=True)  
        embed.add_field(name="Criado em", value=user.created_at, inline=True)
        await ctx.reply(embed=embed)
    

async def setup(client):
    """adds the class to the cog handler"""
    await client.add_cog(User(client))