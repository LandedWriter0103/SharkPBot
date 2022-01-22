import discord
from discord.ext import commands
from MainCore.Classes import Cog_Core

class Event(Cog_Core):

    #語音房進出
    #VC in & out 
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, after, before):

        #Define and get the Output Channel
        abcuser = member.name
        channelAfter = str(after.channel)
        channelBefore = str(before.channel)
        channelText = self.bot.get_channel(922889854109507614)
        
        #Member Joins a VC
        if channelAfter == str(None):
            embed=discord.Embed(color=0x75ecea)
            embed.set_author(name=f"{abcuser} 進入了語音房", icon_url=member.avatar)
            await channelText.send(embed=embed)

        #Member leaves a VC
        if channelBefore == str(None):
            embed=discord.Embed(color=0xffcde8)
            embed.set_author(name=f"{abcuser} 離開了語音房", icon_url=member.avatar)
            await channelText.send(embed=embed)

    @commands.Cog.listener()
    async def on_raw_message_edit(self, data):
        
        Channel_A = self.bot.get_channel(818116963141812229)
        Channel_B = self.bot.get_channel(817708730346766356)

        MSG = data.message_id
        MSG_A = 817708865021280296
        MSG_B = 818132525314605087
        MSG_AB = await Channel_A.fetch_message(818129577356427305)
        MSG_O = await Channel_B.fetch_message(MSG_A)

        if MSG == MSG_A or MSG == MSG_B:

            Day = MSG_O.content[11:-5]

            await MSG_AB.edit(content = "**會考倒數**"
                "\n"
                "> 會考為5月15, 16號"
                "\n"
                "\n"
                f'**國中教育會考**只剩下**{Day}**天'
                "\n"
                "\n"
                "希望大家**好好的準備**"
                "\n"
                "> 不論是**外考**或者**直升**"
                "\n"
                "\n"
                "一起把這場**勝仗拿下**！！"
                "\n"
                "> **加油** <:Heart:771905753954779146>"
                "\n"
                "\n"
                "> LaniFarm 祝您一路逆風")

    @commands.command()
    async def op(self, ctx):
        await ctx.send("以上會每天自動更新喔")

    @commands.Cog.listener()
    async def on_message(self, msg):
        LW = "LandedWriter#0086"
        if LW == str(msg.author):
            if msg.content.startswith('Botsend Imp'):
                MessageContent = str(msg.content)
                ImpImformation = self.bot.get_channel(817664852758626314)
                await ImpImformation.send(content = MessageContent[12:])

            if msg.content.startswith('Botsend Ann'):
                MessageContent = str(msg.content)
                Announcements = self.bot.get_channel(827819572157480970)
                await Announcements.send(content = MessageContent[12:])

            if msg.content.startswith('Botsend Vci'):
                MessageContent = str(msg.content)
                VCinout = self.bot.get_channel(818113614035812372)
                await VCinout.send(content = MessageContent[12:])

            if msg.content.startswith('Botsend Con'):
                MessageContent = str(msg.content)
                Main = self.bot.get_channel(817694222077526037)
                await Main.send(content = MessageContent[12:])      

            if msg.content.startswith('Botsend Mus'):
                MessageContent = str(msg.content)
                Music = self.bot.get_channel(817696990514905088)
                await Music.send(content = MessageContent[12:])   

            if msg.content.startswith('Botsend Stu'):
                MessageContent = str(msg.content)
                Study = self.bot.get_channel(817694956101042186)
                await Study.send(content = MessageContent[12:]) 

            if msg.content.startswith('Botsend Gam'):
                MessageContent = str(msg.content)
                Game = self.bot.get_channel(817704625930764289)
                await Game.send(content = MessageContent[12:])
    
def setup(bot):
    bot.add_cog(Event(bot))