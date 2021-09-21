import os
import discord
import requests
import json
import random
from yt import yt_api_search
from dotenv import load_dotenv

client = discord.Client()

sad_words = ['sad', 'depressed', 'unhappy', 'angry', 'disappointed', 'miserable', 'depressing']

load_dotenv()
TOKEN = os.getenv('TOKEN')

# yt_queue = [['https://www.youtube.com/watch?v=IGM1T0t7qts', 'https://www.youtube.com/watch?v=bOtd9P2cD50',
#       'https://www.youtube.com/watch?v=sq2e-SwL91o', 'https://www.youtube.com/watch?v=OUx6ZY60uiI']]

yt_queue = []


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



@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord !')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('$hello'):
        await message.channel.send('Hello !')

    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))

    if msg.startswith('-play'):
        search_keywords = msg.split('-play ', 1)[1]
        yt_results = yt_api_search(search_keywords)
        yt_queue.append(yt_results)
        print(search_keywords)
        print(yt_queue)
        await message.channel.send(yt_queue[0][0])

    if msg.startswith('-other'):
        await message.channel.send(random.choice(yt_queue[0]))

    if msg.startswith('-next'):
        yt_queue.pop(0)
        await message.channel.send(random.choice(yt_queue[0]))

client.run(TOKEN)
