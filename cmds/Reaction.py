import discord
from discord.ext import commands
from MainCore.Classes import Cog_Core

class Reaction(Cog_Core):
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, data):
        if data.message_id == 777187836213460992:
            if str(data.emoji) == '<:yukino_mega:771910854852476968>':
                guild = self.bot.get_guild(data.guild_id)
                role = guild.get_role(769779076722065448)       #成員
                await data.member.add_roles(role)

            if str(data.emoji) == '<:controller:771904128569966593>':
                guild = self.bot.get_guild(data.guild_id)
                role = guild.get_role(650512524667781120)        #玩家
                await data.member.add_roles(role)

            if str(data.emoji) == '<:nico:771904853882175508>':
                guild = self.bot.get_guild(data.guild_id)
                role = guild.get_role(680041125658230891)       #動漫迷
                await data.member.add_roles(role)

            if str(data.emoji) == '<:__:771902010755907594>':
                guild = self.bot.get_guild(data.guild_id)
                role = guild.get_role(743853198757986324)      #觀眾
                await data.member.add_roles(role)

            if str(data.emoji) == '<:02smile:771908399633399839>':
                guild = self.bot.get_guild(data.guild_id)
                role = guild.get_role(771927928597774366)      #車手
                await data.member.add_roles(role)

        if data.message_id == 777187848217559100:
            if str(data.emoji) == '<:YellingWoman:777016933231886366>':
                guild = self.bot.get_guild(data.guild_id)
                role = guild.get_role(773555093194276874)     #女生
                await data.member.add_roles(role)

            if str(data.emoji) == '<:ConfusedCat:777016969781051402>':
                guild = self.bot.get_guild(data.guild_id)
                role = guild.get_role(773554853065523270)    #男生
                await data.member.add_roles(role)

        if data.message_id == 777187858741329941:
            if str(data.emoji) == '<:miku_shock:771910372017438730>':
                guild = self.bot.get_guild(data.guild_id)
                role = guild.get_role(772303970605596702)    #直升
                role1 = guild.get_role(772305227831181332)
                await data.member.add_roles(role1)
                await data.member.add_roles(role)              

            if str(data.emoji) == '<:miku_angry:771909713284956201>':
                guild = self.bot.get_guild(data.guild_id)
                role = guild.get_role(772303673019334656)    #外考
                role1 = guild.get_role(772305227831181332)
                await data.member.add_roles(role1)
                await data.member.add_roles(role) 

        if data.message_id == 817700415075778560:
            if str(data.emoji) == '<:thumbsup:771906490948780052>':
                guild = self.bot.get_guild(data.guild_id)
                role = guild.get_role(777486448907386890)
                await data.member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, data):
        if data.message_id == 777187836213460992:
            if str(data.emoji) == '<:yukino_mega:771910854852476968>':
                guild = self.bot.get_guild(data.guild_id)
                user = await guild.fetch_member(data.user_id)
                role = guild.get_role(769779076722065448)      #成員
                await user.remove_roles(role)      

            if str(data.emoji) == '<:controller:771904128569966593>':
                guild = self.bot.get_guild(data.guild_id)
                role = guild.get_role(650512524667781120)        #玩家
                user = await guild.fetch_member(data.user_id)
                await user.remove_roles(role)

            if str(data.emoji) == '<:nico:771904853882175508>':
                guild = self.bot.get_guild(data.guild_id)
                role = guild.get_role(680041125658230891)       #動漫迷
                user = await guild.fetch_member(data.user_id)
                await user.remove_roles(role)

            if str(data.emoji) == '<:__:771902010755907594>':
                guild = self.bot.get_guild(data.guild_id)
                role = guild.get_role(743853198757986324)      #觀眾
                user = await guild.fetch_member(data.user_id)
                await user.remove_roles(role)

            if str(data.emoji) == '<:02smile:771908399633399839>':
                guild = self.bot.get_guild(data.guild_id)
                role = guild.get_role(771927928597774366)      #車手
                user = await guild.fetch_member(data.user_id)
                await user.remove_roles(role)

        if data.message_id == 777187848217559100:
            if str(data.emoji) == '<:YellingWoman:777016933231886366>':
                guild = self.bot.get_guild(data.guild_id)
                role = guild.get_role(773555093194276874)     #女生
                user = await guild.fetch_member(data.user_id)
                await user.remove_roles(role)

            if str(data.emoji) == '<:ConfusedCat:777016969781051402>':
                guild = self.bot.get_guild(data.guild_id)
                role = guild.get_role(773554853065523270)    #男生
                user = await guild.fetch_member(data.user_id)
                await user.remove_roles(role)

        if data.message_id == 777187858741329941:
            if str(data.emoji) == '<:miku_shock:771910372017438730>':
                guild = self.bot.get_guild(data.guild_id)
                role = guild.get_role(772303970605596702)    #直升
                role1 = guild.get_role(772305227831181332)
                user = await guild.fetch_member(data.user_id)
                await user.remove_roles(role)  
                await user.remove_roles(role1)            

            if str(data.emoji) == '<:miku_angry:771909713284956201>':
                guild = self.bot.get_guild(data.guild_id)
                role = guild.get_role(772303673019334656, )    #外考
                role1 = guild.get_role(772305227831181332)
                user = await guild.fetch_member(data.user_id)
                await user.remove_roles(role) 
                await user.remove_roles(role1)  

        if data.message_id == 817700415075778560:
            if str(data.emoji) == '<:thumbsup:771906490948780052>':
                guild = self.bot.get_guild(data.guild_id)
                role = guild.get_role(777486448907386890)
                user = await guild.fetch_member(data.user_id)
                await user.remove_roles(role)

def setup(bot):
    bot.add_cog(Reaction(bot))
