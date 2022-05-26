import discord
from discord.ext import commands
from MainCore.Classes import Cog_Core

class Event(Cog_Core):

    # VC => IN AND OUT => Announcement
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, after, before):

        # Define
        Target_User = member.name
        VC_Join = str(after.channel)
        VC_Leave = str(before.channel)
        TC_IN_OUT = self.bot.get_channel(922889854109507614)
        VC_BlackList = []
        VC_BlackList.append(965841503618494464) #Dec
        VC_BlackList.append(968696824498110484) #Dec
        VC_BlackList.append(976380005028360263) #Temp
        VC_BlackList.append(974644887343493151) #Temp
            
        # Member Joins a VC
        if VC_Join == str(None):
            embed=discord.Embed(color=0x00aaaa)
            embed.set_author(name=f"{Target_User} 進入了語音房", icon_url=member.avatar_url)
            await TC_IN_OUT.send(embed=embed)

        # Member Leaves a VC
        if VC_Leave == str(None):
            embed=discord.Embed(color=0xb99090)
            embed.set_author(name=f"{Target_User} 離開了語音房", icon_url=member.avatar_url)
            await TC_IN_OUT.send(embed=embed)
                
            # Delete the Channel => When No Users
            if after.channel.members == []:
                if after.channel.id not in VC_BlackList:
                    await after.channel.delete()

    @commands.Cog.listener()
    async def on_message(self, msg):

        #用指令創造語音頻道
        CH_A = self.bot.get_channel(934466971112718408)
        if CH_A == msg.channel and msg.author != self.bot.user:
            try:
                if msg.content.startswith("create"):
                    CT_A = msg.content.split()
                    CH_NAME = CT_A[2]
                    CH_NAME = "《🔊》" + CH_NAME
                    CH_LIMITS = int(CT_A[4])
                    guild = self.bot.get_guild(922465596602470420)
                    CA_A = CH_A.category
                    await guild.create_voice_channel(CH_NAME, category=CA_A, user_limit=CH_LIMITS, bitrate=128000, position=1)
            except:
                await CH_A.send(content="**格式錯誤了喔** <:Minecraft_Heart:924321182768058369>")
                
    
    @commands.Cog.listener()
    async def on_raw_message_edit(self, data):

        #會考, 學測倒數
        Channel_A = self.bot.get_channel(934711335424508025) #send會考
        Channel_A1 = self.bot.get_channel(934711397693145149) #send學測
        Channel_B = self.bot.get_channel(935553267780448266) #edit會考, 學測

        MSG = data.message_id #detect
        MSG_A = 935557324356067430 #countdown會考
        MSG_B = 935558077061668914 #for debug會考
        MSG_A1 = 935557986091421746 #countdown學測
        MSG_B1 = 935558095042666506 #for debug學測

        if MSG == MSG_A or MSG == MSG_B:

            MSG_AB = await Channel_A.fetch_message(934729218212913172) #to edit會考
            MSG_O = await Channel_B.fetch_message(MSG_A)
            D_list = MSG_O.content.split()
            Day = D_list[2]
            embed = discord.Embed(description=
            "===============================" 
            "\n" "\n" 
            "**會考倒數**" 
            "\n" "\n" 
            "===============================" 
            "\n" "\n"
            "**國中教育會考為 ...**"
            "\n"
            "> **5月21, 22號**"
            "\n" "\n"
            "**距離~~！世界末日！~~ 只剩下 ...**"
            "\n"
            f"> → → → **{Day}天** ← ← ←"
            "\n" "\n"
            "希望各位**國三**的飼養員, 小虎鯨"
            "\n"
            "> 好好的準備"
            "\n"
            "> 一起把這場戰役拿下！！"
            "\n" "\n"
            "不論是**外考**或者**直升**"
            "\n"
            "> 不要考完再後悔 <:Kappa:934723331301724200>"
            "\n" "\n"
            "**SharkParty 祝您考上自己理想的高中職**"
            "\n" "\n"
            "==============================="
            , color=0xb99090)

            await MSG_AB.edit(embed=embed)

        elif MSG == MSG_A1 or MSG == MSG_B1:

            MSG_AB1 = await Channel_A1.fetch_message(934730648588025906) #to edit學測
            MSG_O1 = await Channel_B.fetch_message(MSG_A1)
            D_list = MSG_O1.content.split()
            Day = D_list[2]

            embed = discord.Embed(title=
            "===============================" 
            "\n" "\n" 
            "**學測倒數**" 
            "\n" "\n" 
            "===============================" 
            "\n" "\n"
            "**明年高中學歷測驗暫定為 ...**"
            "\n"
            "> **1月13, 14, 15號**"
            "\n" "\n"
            "**距離！！真正的世界末日！！ 只剩下 ...**"
            "\n"
            f"> → → → **{Day}天** ← ← ←"
            "\n" "\n"
            "各位高中的的飼養員, 小虎鯨"
            "\n"
            "> ！趕緊好好的準備！"
            "\n"
            "> 不要來年再來一回終局之戰！！"
            "\n" "\n"
            "不論是想考**普大**或者**科大**"
            "\n"
            "> ！！真的不要考完再後悔！！ <:Paimon_Smile:924317746630635580>"
            "\n" "\n"
            "**SharkParty 希望您能有最理想的未來**"
            "\n" "\n"
            "==============================="
            , color=0xb99090)

            await MSG_AB1.edit(embed=embed)

def setup(bot):
    bot.add_cog(Event(bot))
