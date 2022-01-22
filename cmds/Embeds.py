import discord
from discord.ext import commands
from MainCore.Classes import Cog_Core

class Embeds(Cog_Core):

    #LaniBanner
    @commands.command()
    async def infBanner(self, ctx):
        await ctx.send("https://i.ibb.co/XjJ5Q7k/Lani-Banner-Long-Ver.png")

    #Server Banner
    @commands.command()
    async def inf1(self, ctx):
        await ctx.send( 
            "\n"
            "**誒？歡迎來到這個伺服器！！**"
            "\n"
            "這裡可以"
            "\n"
            "> 讓你好好讀書"
            "\n"
            "> 和其他人文字, 語音同樂"
            "\n"
            "> 發揮想像力讓這裡變得更完美"
            "\n"
            "\n"
            "**伺服器永久連結:**https://discord.gg/cdvVr5Tkug"
            "\n"
            "\n"
            "**身份組介紹**"
            "\n"
            "> 管理員:"
            "\n"
            "> @[農場主人] - 創造這裡的我和表妹"
            "\n"
            "> @[板手] - 管理農場的板板們"
            "\n"
            "\n"
            "> 特殊身份組:"
            "\n"
            "> @[老司機] - 發夠多車圖讓我關注到你"
            "\n"
            "> @[PP農夫] - 在OSU達到5-Digits"
            "\n"
            "\n"
            "> 普通身份組:"
            "\n"
            "> @[農夫] - 普通的成員"
            "\n"
            "\n"
            "**規則**"
            "\n"
            "> 和平 包容 友善"
            "\n"
            "> 不要對他人有衝動的言論"
            "\n"
            "> 不要在公頻有NFSW的圖, 言論"
            "\n"
            "> 可以適度地批評他人, 但過度會被板手敲"
            "\n"
            "> 不要隨便Tag大家, 抓到一樣會被板手敲"
            "\n"
            "> 不要挑釁管理員, 後果自負"
            "\n"
            "> 可以討論功課, 但不能過度的比較成績")

    @commands.command()
    async def inf2(self, ctx):
        await ctx.send("點選下方的反應來代表以詳細閱讀規則")

    #Welcome Banner
    @commands.command()
    async def emb1(self, ctx):
        embed=discord.Embed(color=0xffcde8)
        embed.set_image(url="https://i.ibb.co/XszMqCg/Welcome-Banner.png")
        await ctx.send(embed=embed)

    #Welcome Text
    @commands.command()
    async def emb2(self, ctx):
        embed=discord.Embed(title="歡迎來到ラニ討論區!", 
            description=
            "𝕝━━━━━━━━━━━━━━━━━━𝕝" 
            "\n" "\n" 
            "-先去詳細閱讀<#650508257168850971>" 
            "\n" "\n" 
            "-再去<#767235816375713803>" 
            "\n" "\n" 
            "-接著就可以到<#769595752900722738>" 
            "\n" "\n" 
            "-一起同樂哦<:yukino_mega:771910854852476968>" 
            "\n" "\n" 
            "𝕝━━━━━━━━━━━━━━━━━━𝕝", color=0xffcde8)
        embed.set_author(name="LaniServer")
        await ctx.send(embed=embed)

    #Rules Banner
    @commands.command()
    async def emb3(self, ctx):
        embed=discord.Embed(color=0xffcde8)
        embed.set_image(url="https://i.ibb.co/Bs07GsY/Rules.png")
        await ctx.send(embed=embed)

    #Rules Text1
    @commands.command()
    async def emb4(self, ctx):
        embed=discord.Embed(title="<:heart:771905753954779146>請遵守以下規定<:heart:771905753954779146>", 
            description=""
            , color=0xffcde8)
        await ctx.send(embed=embed)

    #Rules Text2
    @commands.command()
    async def emb5(self, ctx):
        embed=discord.Embed(title="<:miku_angry:771909713284956201>違者三次**BAN**<:miku_angry:771909713284956201>", 
            description=
            "1.和平包容友善"
            "\n"
            "2.不要一直開人玩笑"
            "\n"
            "2-1.除非那人允許"
            "\n"
            "3.不要過度批評他人"
            "\n"
            "4.發車請在司機區"
            "\n"
            "5.不要洗版"
            "\n"
            "6.尊重各種黨派(Ex.貓派,狗派)"
            "\n"
            "以上暫時條款"
            "\n"
            "更新於:11/01(日) 上午11:36"
            , color=0xffcde8)
        await ctx.send(embed=embed)

    #Roles Banner
    @commands.command()
    async def emb6(self, ctx):
        embed=discord.Embed(color=0xffcde8)
        embed.set_image(url="https://i.ibb.co/KVpwjzW/Role-Banner.png")
        await ctx.send(embed=embed)

    #Roles1
    @commands.command()
    async def emb7(self, ctx):
        embed=discord.Embed(title="<:heart:771905753954779146>點取下方反應來領取身份組<:heart:771905753954779146>", 
            description=""
            , color=0xffcde8)
        await ctx.send(embed=embed)  

    #Roles2
    @commands.command()
    async def emb8(self, ctx):
        embed=discord.Embed(title="<:heart:771905753954779146>基礎身份組", 
            description=
            "\n"
            "<:yukino_mega:771910854852476968> - **成員**"
            "\n" "\n"
            "-能看到普通區,包廂聊天區,音樂區"
            "\n" "\n"
            "<:controller:771904128569966593>  - **玩家**"
            "\n" "\n"
            "-能看到遊戲聊天區"
            "\n" "\n"
            "<:nico:771904853882175508> - **動漫迷**"
            "\n" "\n"
            "-能看到動漫區"
            "\n" "\n"
            "<:__:771902010755907594> - **觀眾**"
            "\n" "\n"
            "-能看到直播區"
            "\n" "\n"
            "<:02smile:771908399633399839> - **車手**"
            "\n" "\n"
            "-能看到成人區"
            , color=0xffcde8)
        await ctx.send(embed=embed) 

    #Roles2
    @commands.command()
    async def emb9(self, ctx):
        embed=discord.Embed(title="<:heart:771905753954779146>真實性別", 
            description=
            "\n"
            "<:YellingWoman:777016933231886366> - **女性**"
            "\n" "\n"
            "<:ConfusedCat:777016969781051402> - **男性**"
            , color=0xffcde8)
        await ctx.send(embed=embed) 

    #Roles3
    @commands.command()
    async def emb10(self, ctx):
        embed=discord.Embed(title="<:heart:771905753954779146>恆毅中學學生", 
            description=
            "\n"
            "<:miku_shock:771910372017438730> - 直升"
            "\n" "\n"
            "<:miku_angry:771909713284956201> - 外考"
            "\n" "\n" "\n"
            "**<:YellingWoman:777016933231886366>不是恆毅中學的就不用填<:ConfusedCat:777016969781051402>**"
            , color=0xffcde8)
        await ctx.send(embed=embed) 

    #RolesWarn
    @commands.command()
    async def emb11(self, ctx):
        embed=discord.Embed(description=
            "\n"
            "<:heart:771905753954779146>基礎身份組可以**全選**"
            "\n" "\n"
            "<:heart:771905753954779146>也可以只選**需要的**"
            "\n" "\n"
            "<:upset:771906578705809408>亂點抓到先**封禁三天**"
            "\n" "\n"
            "<:yukino_mega:771910854852476968>**至少**要點**成員**喔～"
            , color=0xffcde8)
        await ctx.send(embed=embed)

    #Warn Banner
    @commands.command()
    async def emb100(self, ctx):
        embed=discord.Embed(color=0xffcde8)
        embed.set_image(url="https://i.ibb.co/vckL1J7/Warn.png")
        await ctx.send(embed=embed)

    #Test !!
    @commands.command()
    async def sl(self, ctx):
        await ctx.send("plz go to <#650508257168850971> first")

def setup(bot):
    bot.add_cog(Embeds(bot))