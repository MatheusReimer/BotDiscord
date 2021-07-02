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


#To promote myself
@client.command()
async def comandos(ctx):
  await ctx.channel.send('!matheus\n''!hello\n' '!define lol\n')


@client.command()
async def define(ctx, word):

  quote = dictionary(word)
  await ctx.channel.send(quote)
  return


@client.command()
async def warzone(ctx):

  info = warzoneData()
  await ctx.send("Meu total de vitórias é: "+str(info['br']['wins']))
  await ctx.send("Meu total de  baixas é:"+ str(info['br']['kills']))
  await ctx.send("Meu kd é:"+str(info['br']['kdRatio']))
  await ctx.send("Meu total de derrubados é:  "+str(info['br']['downs']))
  await ctx.send("Meu total de mortes é:"+str(info['br']['deaths']))
  await ctx.send("Meu total de jogos jogados é: "+str(info['br']['gamesPlayed']))
  await ctx.send("Minha pontuação por minuto é:  "+str(info['br']['scorePerMinute']))
  await ctx.send("Meu total de revives é:  "+str(info['br']['revives']))
  
  return
##API SETUP DICTIONARY

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

#API WARZONE
def warzoneData():

  url = "https://call-of-duty-modern-warfare.p.rapidapi.com/warzone/BattimaFernardes/psn"

  headers = {
      'x-rapidapi-key': "509436ea92msh7b7f6e62acc3695p142991jsn49c856f1b7a6",
      'x-rapidapi-host': "call-of-duty-modern-warfare.p.rapidapi.com"
      }

  response = requests.request("GET", url, headers=headers)
  json_data = json.loads(response.text)


 
  return json_data
  

client.run(my_secret)