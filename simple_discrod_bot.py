import discord
import os
import requests
import json
import random

client = discord.Client()

sad_words = ['sad', 'depressed', 'unhappy', 'angry', 'bad', 'depressing']
starter_encouragments = ['cheer up', 'hang in there', 'you are great']

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " —" + json_data[0]['a']
    return quote

@client.event
async def on_ready():
    print("Logged as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return -1

    msg = message.content
    
    if msg.startswith("$hello"):
        await message.channel.send("Hello!")
    
    elif msg.startswith("$inspare"):
        quote = get_quote()
        await message.channel.send(quote)
    
    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragments))

    client.run(os.getenv('TOKEN'))
    # ! create .env file and make TOKEN = your_token !
