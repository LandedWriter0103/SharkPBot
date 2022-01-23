import os
import time
import discord
from discord.ext import commands 
from Keep_alive import keep_alive
from discord.ui import Button, View

#Keep the Bot 24/7 with UptimeRobot's DashBoard
keep_alive()

#Set the Discord Server Prefix = /
bot = commands.Bot(command_prefix="/")

#Remove Useless Help Command
bot.remove_command("help")

#Bot Online
@bot.event
async def on_ready():
	print(">>> Bot Is Online <<<")
	await bot.change_presence(activity=discord.Game("/help || 加入 SharkParty"))

#Load Cog
#/load {Cog Name}
@bot.command()
async def load(ctx, extension):
	bot.load_extension(f"cmds.{extension}")
	await ctx.send(f"Loaded {extension} Done!") 

#Unload Cog
#/unload {Cog Name}
@bot.command()
async def unload(ctx, extension):
	bot.unload_extension(f"cmds.{extension}")
	await ctx.send(f"Unloaded {extension} Done!")

#Reload Cog
#/reload {Cog Name}
@bot.command()
async def reload(ctx, extension):
	bot.reload_extension(f"cmds.{extension}")
	await ctx.send(f"Reloaded {extension} Done!")

#To tell the Bot what/where are the Cog files
for filename in os.listdir("./cmds"):
	if filename.endswith(".py"):
		bot.load_extension(f"cmds.{filename[:-3]}")

#Load the Bot on
if __name__ == "__main__":
	token = os.getenv("TOKEN")
	bot.run(token)