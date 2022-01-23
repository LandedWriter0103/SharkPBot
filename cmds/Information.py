import random
from tkinter import E
import discord
from discord.ui import Button, View
from discord.ext import commands
from MainCore.Classes import Cog_Core

class Information(Cog_Core):
    
    #First Content to send in Rules
    #/first
    @commands.command()
    async def first(self, ctx):
        embed = discord.Embed(color=0xb99090)
        embed.set_image(url="https://cdn.discordapp.com/attachments/877511827116945418/924328243811721216/FF.png")
        await ctx.send(embed=embed)

    #Second...
    #/second
    @commands.command()
    async def second(self, ctx):
        embed=discord.Embed(title="<:Minecraft_Heart:924321182768058369> 偶哈優～狗紮蟻貓屎 <:Minecraft_Heart:924321182768058369>"
        , color=0xb99090)
        await ctx.send(embed=embed)

    #Third...
    #/third
    @commands.command()
    async def third(self, ctx):
        embed=discord.Embed(description=
        "===============================" 
        "\n" "\n" 
        "**歡迎來到鯊雕派對**" 
        "\n" "\n" 
        "===============================" 
        "\n" "\n"
        "**在這裡**"
        "\n"
        "你可以做任何你想做的事情"
        "\n"
        "> 合理範圍內"
        "\n"
        "> 不得踩, 遊走於法律邊緣"
        "\n" "\n"
        "**大家也可以在這裡討論各式話題**"
        "\n"
        "> 政治"
        "\n"
        "> 人生"
        "\n"
        "> 經濟"
        "\n"
        "> 娛樂"
        "\n"
        "> 社交"
        "\n"
        "> 生活 etc..."
        "\n" "\n"
        "**伺服器永久連結**"
        "\n"
        "> https://discord.gg/vaYfrrPb9A"
        "\n" "\n"
        "==============================="
        , color=0xb99090)
        await ctx.send(embed=embed)

    #Fourth...
    #/fourth
    @commands.command()
    async def fourth(self, ctx):
        embed = discord.Embed(color=0xb99090)
        embed.set_image(url="https://cdn.discordapp.com/attachments/877511827116945418/924349097081724938/Service.png")
        await ctx.send(embed=embed)

    #Fifth...
    #/fifth
    @commands.command()
    async def fifth(self, ctx):
        embed=discord.Embed(description=
        "===============================" 
        "\n" "\n" 
        "**加入即可擁有福利**" 
        "\n" "\n" 
        "===============================" 
        "\n" "\n"
        "**不用付費!!!**"
        "\n"
        "> 換季式Minecraft模組包伺服器"
        "\n" "\n"
        "**友愛環境!!!**"
        "\n"
        "> 可以每天看到一堆無關緊要的問安訊息"
        "\n" "\n"
        "**命運相遇!!!**"
        "\n"
        "> 或許你能在此找到你的真命天子/女"
        "\n"
        "> 雖然沒找到不是我們的問題 (w"
        "\n" "\n"
        "**運氣試驗!!!**"
        "\n"
        "> 可能不定時會有抽獎"
        "\n"
        "> 一樣 抽不到不是我們的問題 (w"
        "\n" "\n"
        "**可以色色!!!**"
        "\n"
        "> 內含大量帥哥美女 (吧"
        "\n"
        "> 設有專門色色的頻道"
        "\n"
        "> 讓一天疲憊的你可以好好**宣洩**"
        "\n" "\n"
        "==============================="
        , color=0xb99090)
        await ctx.send(embed=embed)

    #Sixth...
    #/sixth
    @commands.command()
    async def sixth(self, ctx):
        embed = discord.Embed(color=0xb99090)
        embed.set_image(url="https://cdn.discordapp.com/attachments/877511827116945418/924351358205845544/Roles.png")
        await ctx.send(embed=embed)

    #Seventh...
    #/seventh
    @commands.command()
    async def seventh(self, ctx):
        embed=discord.Embed(description=
        "===============================" 
        "\n" "\n" 
        "**身份組簡介**" 
        "\n" "\n" 
        "===============================" 
        "\n" "\n"
        "**[ 服主 ]**"
        "\n"
        "> 就...創這伺服器的人"
        "\n" "\n"
        "**[ 板手 ]**"
        "\n"
        "> 管理員這伺服器的團隊"
        "\n"
        "> 目前採邀請制, 而非申請制"
        "\n" "\n"
        "**[ 模組大佬 ]**"
        "\n"
        "> 分組玩時這身份組的人可直接同一組"
        "\n"
        "> 目前採申請制"
        "\n" "\n"
        "**[ 優質虎鯨 ]**"
        "\n"
        "> 比較...優質的虎鯨"
        "\n"
        "> 能有比小虎鯨高一點的權限"
        "\n"
        "> 目前採邀請制, 而非申請制"
        "\n" "\n"
        "**[ 小虎鯨 ]**"
        "\n"
        "> 這伺服器的所有人"
        "\n"
        "> 都是最優質, 最高等的人"
        "\n"
        "> 但在此服內一視同仁, 人人皆平等"
        "\n" "\n"
        "==============================="
        , color=0xb99090)
        await ctx.send(embed=embed)

    #Eighth...
    #/eighth
    @commands.command()
    async def eighth(self, ctx):
        embed = discord.Embed(color=0xb99090)
        embed.set_image(url="https://cdn.discordapp.com/attachments/877511827116945418/924484585499291658/Rules.png")
        await ctx.send(embed=embed)

    #Ninth...
    #/ninth
    @commands.command()
    async def ninth(self, ctx):
        embed=discord.Embed(description=
        "===============================" 
        "\n" "\n" 
        "**規則**" 
        "\n" "\n" 
        "===============================" 
        "\n" "\n"
        "**遵守Discord TOS和基本社群條款**"
        "\n"
        "> https://discord.com/terms"
        "\n" "\n"
        "**不要沒有意義的洗版**"
        "\n"
        "> 視情況Timeout"
        "\n" "\n"
        "**不要出現沒合作的廣告**"
        "\n"
        "> 不要傳你自己的Discord伺服器連結"
        "\n"
        "> 不要傳一些令人懷疑的詭異連結"
        "\n"
        "> 抓到Timeout 2週"
        "\n" "\n"
        "**不要閃**"
        "\n"
        "> 你可以在這裡找你的另一半"
        "\n"
        "> 但不代表別人一定要看你們放閃"
        "\n"
        "> 抓到Timeout 3天"
        "\n" "\n"
        "**不要帶有尖刺或者沈重的言論**"
        "\n"
        "> 視情況Timeout"
        "\n"
        "> 情節嚴重, 視情況永Ban"
        "\n" "\n"
        "**不要濫用身份組地位**"
        "\n"
        "> 除了管理組以外, 大家一視同仁"
        "\n"
        "> 視情況Timeout"
        "\n" "\n"
        "**在對的地方做對的事**"
        "\n"
        "> 只能在指令頻道傳指令"
        "\n"
        "> 只能在NSFW頻道色色"
        "\n"
        "> 視情況Timeout"
        "\n"
        "> 情節嚴重, 視情況永Ban"
        "\n" "\n"
        "==============================="
        , color=0xb99090)
        await ctx.send(embed=embed)

    #Tenth...
    #/tenth
    @commands.command()
    async def tenth(self, ctx):
        embed = discord.Embed(color=0xb99090)
        embed.set_image(url="https://cdn.discordapp.com/attachments/877511827116945418/924486397807722516/welcome.png")
        await ctx.send(embed=embed)

    #Last Content to Send in Rules
    #/last
    @commands.command()
    async def last(self, ctx):
        embed = discord.Embed(title="<:Minecraft_Heart:924321182768058369> 點選下方的 **\"反應\"** <:Minecraft_Heart:924321182768058369>"
        , color=0xb99090)
        await ctx.send(embed=embed)

    #/EmbedOP...
    #/embedop
    @commands.command()
    async def embedop(self, ctx):
        embed = discord.Embed(color=0xb99090)
        embed.set_image(url="https://cdn.discordapp.com/attachments/877511827116945418/934722300924788756/7cf92cb6bb8c9b23.png")
        await ctx.send(embed=embed)

    #/EmbedED...
    #/embeded
    @commands.command()
    async def embeded(self, ctx):
        embed = discord.Embed(color=0xb99090)
        embed.set_image(url="https://cdn.discordapp.com/attachments/877511827116945418/934722301440696380/53c3caeb99592fc0.png")
        await ctx.send(embed=embed)

    #ADD Reaction
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content == "Reaction":
            channel = self.bot.get_channel(922497110115504208)
            message = await channel.fetch_message(924486727886839858)
            await message.add_reaction("<:verify:924298892818919424>")
        

    #ADD Reaction Role
    #小虎鯨
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, data):
        if data.message_id == 924486727886839858:
            emoji = "<:verify:924298892818919424>"
            if str(data.emoji) == emoji:
                guild = self.bot.get_guild(data.guild_id)
                role = guild.get_role(922852347351298139)
                await data.member.add_roles(role)

    #REMOVE Reaction Role
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, data):
        if data.message_id == 924486727886839858:
            emoji = "<:verify:924298892818919424>"
            if str(data.emoji) == emoji:
                guild = self.bot.get_guild(data.guild_id)
                role = guild.get_role(922852347351298139)
                user = await guild.fetch_member(data.user_id)
                await user.remove_roles(role)

    #自動更新
    @commands.command()
    async def op(self, ctx):
        embed = discord.Embed(title="<:Minecraft_Heart:924321182768058369> **以上會每天自動更新喔** <:Minecraft_Heart:924321182768058369>"
        , color=0xb99090)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Information(bot))