import os
import requests
import json
from replit import db
from discord.ext import commands
from xingamentos import xingamentos
##The file above contains the 'complements' in an array called xingamentos
import asyncio

my_secret = os.environ['discordbotkey']


client = commands.Bot(command_prefix="!")



##To tell when compilation is done
@client.event
async def on_ready():
  print('Olá, eu loguei no sistema como {0.user}'.format(client))
## To inform that the user is breaching the server's guidelines 
@client.event
async def on_message(message):
  await client.process_commands(message)
  msg = message.content;
  if message.author ==client.user:
    return
  if any(word in msg for word in xingamentos):
    await message.channel.send(' Por favor, a cordialidade tem de permancer. Sem vulgaridades por obséquio')
  



#To greet
@client.command()
async def hello(ctx):
  await ctx.send("ola")

#To promote myself
@client.command()
async def matheus(ctx):
  await ctx.channel.send('O Github é : https://github.com/MatheusReimer')
  await ctx.channel.send('O Linkedin é : https://www.linkedin.com/in/matheus-reimer-636b10187/')

@client.command()
async def define(ctx, word):

  quote = dictionary(word)
  await ctx.channel.send(quote)
  return


##API SETUP

def dictionary(word):

  url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

  querystring = {"term":word}

  headers = {
      'x-rapidapi-key': "509436ea92msh7b7f6e62acc3695p142991jsn49c856f1b7a6",
      'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com"
      }

  response = requests.request("GET", url, headers=headers, params=querystring)
  json_data = json.loads(response.text)
  
  definition = (json_data['list'][0]['definition'])
  return definition

  

client.run(my_secret)