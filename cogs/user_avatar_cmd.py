from typing import Union
from discord.ext import commands
import discord 

class UserAvatarCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def user_avatar(self, ctx, *,  user: discord.User=None):
        user = ctx.message.author if user == None else user

        avatar_url = user.avatar
        embed = discord.Embed(title=f"Avatar of {user.name}")
        embed.set_author(name=f"{user}", icon_url=f"{avatar_url}")
        embed.set_image(url=avatar_url)
        embed.set_footer(text=f"Requested by: {ctx.message.author}", icon_url=ctx.author.avatar)
        await ctx.reply(embed=embed)

    

async def setup(client):
    await client.add_cog(UserAvatarCmd(client))