import discord
import os
from discord.ext import commands

def read_token():
  with open("token.txt", "r") as f:
    lines = f.readlines()
    return lines[0].strip()

client = commands.Bot(command_prefix = '!')

@client.command()
async def load(ctx, extension):
  client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
  client.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')


token = read_token()
client.run(token)
