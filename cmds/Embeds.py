import discord
from discord.ext import commands
from MainCore.Classes import Cog_Core

class Embeds(Cog_Core):
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("<a:Online:964432372986687498>")

def setup(bot):
    bot.add_cog(Embeds(bot))