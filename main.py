import os
import os.path

import discord
from dotenv import load_dotenv
from keep_alive import keep_alive

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='sitlist')
async def sit_list(ctx):

	file_exists = os.path.isfile("sitlist.txt")
	if file_exists:
		response = 'Ryland has been sitted by:\n'
		with open("sitlist.txt", "r") as txt_file:
			for name in txt_file:
				response+= '\t- ' + name

	else:
		open("sitlist.txt", "a+")
		response = 'Ryland hasn\'t been sitted\n'
    
	await ctx.send(response)

@bot.command(name='sit')
async def sit(ctx, *mob_name):

	response = 'Ryland got sitted by ' + ' '.join(mob_name)
	with open("sitlist.txt", "a+") as txt_file:
		txt_file.write(' '.join(mob_name)+'\n')
	await ctx.send(response)

keep_alive()
bot.run(TOKEN)