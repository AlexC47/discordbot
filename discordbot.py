import os
import discord
import requests
import json
import random
from replit import db
from dotenv import load_dotenv

client = discord.Client()

sad_words = ['sad', 'depressed', 'unhappy', 'angry', 'disappointed', 'miserable', 'depressing']

load_dotenv()
TOKEN = os.getenv('TOKEN')


starter_encouragements = [
    'Cheer up !',
    'Hang in there.',
    'You are a great person'
    ]


def get_quote():
    response = requests.get('https://zenquotes.io/api/random/')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + ' - ' + json_data[0]['a']
    return quote


def update_encouragements(encouraging_message):
    if 'encouragements' is not db.keys():
        encouragements = db['encouragements']
        encouragements.append(encouraging_message)
        db['encouragements'] = encouragements
    else:
        db['encouragements'] = [encouraging_message]

def delete_encouragement(index):
    encouragements = db['encouragements']
    if len(encouragements) > index:
        del encouragements[index]
        db['encouragements'] = encouragements

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord !')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if message.content.startswith('$hello'):
        await message.channel.send('Hello !')

    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    options = starter_encouragements
    if 'encouragements' in db.keys():
        options = options + db['encouragements']

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(options))

client.run(TOKEN)
