# Work with Python 3.6
import discord

TOKEN = 'NjA1ODM2MTM4NzIwMjY0MTky.XUCTGA.yyt_WAkCuRi9ANVcmnU3uG_J-I4'

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')
        
        if message.content == '!stop': 
            await client.logout()

client = MyClient()
client.run(TOKEN)