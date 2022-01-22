import discord
from discord.ext import commands
from MainCore.Classes import Cog_Core

class test(Cog_Core):

    @commands.Cog.listener()
    async def on_message(self, msg):
        author = str(msg.author)
        user1 = "連得-LandedWriter#0086"
        if author==user1 and msg.content == "WASD":
            print("Yes")
            await msg.channel.send('WASDAWADSDASD')
        else: 
            print("No")
            print(user1)
            print(author)



def setup(bot):
    bot.add_cog(test(bot))