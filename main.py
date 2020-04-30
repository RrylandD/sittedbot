import os
import os.path

import discord
from dotenv import load_dotenv

from discord.ext import commands

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('./service-account.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='sitlist')
async def sit_list(ctx):

	#Base response
	response = 'Ryland has been sitted by:\n'

	#Get all docs and append names
	docs = db.collection(u'sitlist').stream()
	for doc in docs:
		response += '\t- '+doc.to_dict()["Name"]+'\n'
    
	await ctx.send(response)

@bot.command(name='sit')
async def sit(ctx, *mob_name):

	response = 'Ryland got sitted by ' + ' '.join(mob_name)

	data = {u'Name':' '.join(mob_name)}

	db.collection(u'sitlist').document(' '.join(mob_name)).set(data)

	await ctx.send(response)

bot.run(TOKEN)