from turtle import position
import discord
import time
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
            embed=discord.Embed(color=0x00aaaa)
            embed.set_author(name=f"{abcuser} 進入了語音房", icon_url=member.avatar)
            await channelText.send(embed=embed)

        #Member leaves a VC
        if channelBefore == str(None):
            embed=discord.Embed(color=0xb99090)
            embed.set_author(name=f"{abcuser} 離開了語音房", icon_url=member.avatar)
            await channelText.send(embed=embed)
            
            #Delete the Channel when Nobody is in the Voice Chat
            if after.channel.members == []:
                await after.channel.delete()

    @commands.Cog.listener()
    async def on_message(self, msg):
        
        #用指令創造語音頻道
        CH_A = self.bot.get_channel(934466971112718408)
        if CH_A == msg.channel and msg.author != self.bot.user:

            if msg.content.startswith("create"):
                CT_A = msg.content.split()
                CH_NAME = CT_A[2]
                CH_NAME = "《🔊》" + CH_NAME
                CH_LIMITS = int(CT_A[4])
                guild = self.bot.get_guild(922465596602470420)
                CA_A = CH_A.category
                await guild.create_voice_channel(CH_NAME, category=CA_A, user_limit=CH_LIMITS, position=1)

            else:
                await CH_A.send(content="**格式錯誤了喔** <:Minecraft_Heart:924321182768058369>")

    
    @commands.Cog.listener()
    async def on_raw_message_edit(self, data):

        #會考, 學測倒數
        Channel_A = self.bot.get_channel(934711335424508025) #send會考
        Channel_A1 = self.bot.get_channel(934711397693145149) #send學測
        Channel_B = self.bot.get_channel(934711497840549908) #edit會考, 學測

        MSG = data.message_id #detect
        MSG_A = 934805151418564628 #countdown會考
        MSG_B = 934717378934239274 #for debug會考
        MSG_A1 = 934805228455338046 #countdown學測
        MSG_B1 = 934730217560367124 #for debug學測

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

            embed = discord.Embed(description=
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

        #麥塊服狀態 ?服
        CH_A = self.bot.get_channel(934745445979291660) #send狀態
        MSG_A2 = 934823740620025876 #status?服
        MSG_B2 = 934752880060157962 #for debug?服
        if MSG == MSG_A2 or MSG == MSG_B2:
            MSG_AB2 = await CH_A.fetch_message(934812225040973887) #to edit狀態
            MSG_O2 = await Channel_B.fetch_message(MSG_A2)

            em = MSG_O2.embeds[0]
            em_d1 = str(em.fields[4])
            em_d1 = em_d1[35:-15]
            em_d2 = str(em.fields[5])
            em_d2 = em_d2[43:-15]
            em_d3 = str(em.fields[7])
            em_d3 = em_d3[33:-15]
            
            embed = discord.Embed(description=
            "===============================" 
            "\n" "\n" 
            "**一服 - All The Mods 6**" 
            "\n" "\n" 
            "==============================="
            "\n" "\n"
            "**伺服器狀態**"
            "\n"
            f"> {em_d1}"
            "\n" "\n"
            "**上線人數**"
            "\n"
            f"> {em_d2}"
            "\n" "\n", 
            color=0xb99090)

            em_d4 = str(em.image)
            em_d4 = em_d4.split()
            em_d4 = em_d4[0]
            em_d4 = em_d4[16:-3]
            embed.set_image(url=em_d4)
            await MSG_AB2.edit(embed=embed)

        #麥塊服狀態 3服
        CH_A = self.bot.get_channel(934745445979291660) #send狀態
        MSG_A2 = 934804498826809384 #status佬服
        MSG_B2 = 934752880060157962 #for debug佬服
        if MSG == MSG_A2 or MSG == MSG_B2:
            MSG_AB2 = await CH_A.fetch_message(934812230988488704) #to edit狀態
            MSG_O2 = await Channel_B.fetch_message(MSG_A2)

            em = MSG_O2.embeds[0]
            em_d1 = str(em.fields[4])
            em_d1 = em_d1[35:-15]
            em_d2 = str(em.fields[5])
            em_d2 = em_d2[43:-15]
            em_d3 = str(em.fields[7])
            em_d3 = em_d3[33:-15]
            
            embed = discord.Embed(description=
            "===============================" 
            "\n" "\n" 
            "**三服 - FTB Infinity Evolved**" 
            "\n" "\n" 
            "==============================="
            "\n" "\n"
            "**伺服器狀態**"
            "\n"
            f"> {em_d1}"
            "\n" "\n"
            "**上線人數**"
            "\n"
            f"> {em_d2}"
            "\n" "\n", 
            color=0xb99090)

            em_d4 = str(em.image)
            em_d4 = em_d4.split()
            em_d4 = em_d4[0]
            em_d4 = em_d4[16:-3]
            embed.set_image(url=em_d4)
            await MSG_AB2.edit(embed=embed)

    @commands.Cog.listener() 
    async def on_guild_channel_create(self, ch):
        time.sleep(3)
        if ch.members == [] and ch.category_id == 925995616390221865:
            time.sleep(10)
            await ch.delete()
            
    
def setup(bot):
    bot.add_cog(Event(bot))