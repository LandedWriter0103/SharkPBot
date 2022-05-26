from mcipc.query import Client
from discord.ext import commands
from MainCore.Classes import Cog_Core

import discord
import asyncio

class bgtask(Cog_Core):
    def __init__(self, bot):
        super().__init__(bot)
        
        async def infi_loop_server_info():
            await self.bot.wait_until_ready()

            while not self.bot.is_closed(): #Infi. Loop => Closed When Bot is closed 
                
                try:
                    #Voice Chat Auto Delete
                    VC_List = self.bot.get_channel(925995616390221865).voice_channels
                    VC_BlackList = []
                    VC_BlackList.append(965841503618494464) #Dec
                    VC_BlackList.append(968696824498110484) #Dec
                    VC_BlackList.append(974644887343493151) #Temp
                    VC_BlackList.append(979184947799674880) #Temp
                    VC_BlackList.append(979051165910204486) #Temp
                    for VC in VC_List:
                        BlackList = False
                        if VC.members == []:
                            for VC_B in VC_BlackList:
                                    if VC.id == VC_B:
                                        BlackList = True
                                        break
                        else:
                            BlackList = True
                        if BlackList == False:
                            await VC.delete()
                except:
                    pass

                #=====

                #Server Status
                try:
                    with Client("mc.yuwuy.com", 25576, timeout=2) as client:
                        full_stats = client.stats(full=True)

                    players_list = full_stats.players
                    players_num = full_stats.num_players
                    players_max = full_stats.max_players

                    status_text = "<a:Online:964432372986687498> 開啟"
                    status = True

                except:
                    players_list = []
                    players_num = "N"
                    players_max = "A"
                    status_text = "<a:Offline:964432412673196033> 自閉"
                    status = False

                #Max Online Players
                #Read if >= Old Data
                with open("./cache/max_player.txt", "r") as cache:
                    
                    more_players = False
                    max_players = int(cache.readline())
                    
                    if players_num == "N":
                        pass
                    elif players_num >= max_players:
                        more_players = True
                    else:
                        more_players = False

                #Write if True
                with open("./cache/max_player.txt", "w") as cache:
                    if more_players == True:
                        cache.write(str(players_num))
                    else:
                        cache.write(str(max_players))
                        
                #Take Latest Data
                with open("./cache/max_player.txt", "r") as cache:
                    max_players = int(cache.readline())

                #TC => Target Text Channe => Where you will export the result
                #TM => Target Message => The message you will edit the result
                #TM MUST BE SENT BY BOT
                TC_Server_Info = self.bot.get_channel(962336732404138024) #Target Text Channel
                TM_Server_Info_Mod = await TC_Server_Info.fetch_message(962338706042261566) #Target Message to Edit => Mod Server 
                RT_Server_Info_Mod = discord.Embed(title= #Design & Return Embed
                "❖ ========================= ❖" 
                "\n" "\n" 
                "              **ESSS服 - 現在版本 1.18.2**" 
                "\n" "\n" 
                "❖ ========================= ❖"
                , color=0xb99090)

                RT_Server_Info_Mod.add_field(name="伺服器遊戲", value=f"> Minecraft Java | BE", inline=False)
                RT_Server_Info_Mod.add_field(name="伺服器 IP", value="> mc.yuwuy.com", inline=True)
                RT_Server_Info_Mod.add_field(name="伺服器 Port", value="> 25566", inline=True)
                RT_Server_Info_Mod.add_field(name="伺服器位置", value="> 新北市", inline=True)
                RT_Server_Info_Mod.add_field(name="伺服器狀態", value=f"> {status_text}", inline=True)
                RT_Server_Info_Mod.add_field(name="上線人數", value=f"> {players_num} / {players_max}", inline=True)
                RT_Server_Info_Mod.add_field(name="最大上線人數", value=f"> {max_players}", inline=True)

                #Remove # if You want to show online players' username
                #18 Players Max due to Embeds' field limit
                #if status == True:
                    #num = 1
                    #for player in players_list:
                        #RT_Server_Info_Mod.add_field(name="\a", value=f"```{num} | {player}```", inline=False)
                        #num += 1

                #else:
                    #pass
                
                await TM_Server_Info_Mod.edit(content="", embed=RT_Server_Info_Mod)
                await asyncio.sleep(8)

        self.bg_task = self.bot.loop.create_task(infi_loop_server_info())
        
def setup(bot):
    bot.add_cog(bgtask(bot))