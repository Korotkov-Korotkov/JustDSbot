import os
import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('дратути') or ('привет') or ('здрасте'):
        await message.channel.send('здрасте')

    if message.content.startswith('как настроение?') or ('как самочувствие?'):
        await message.channel.send('Всё норм')
        
    if message.content.startswith('досвидания') or ('пока'):
        await message.channel.send('пока')


my_secret = os.environ['TOKEN']
client.run(my_secret)