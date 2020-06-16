# discord-bot

Discord bot to do various things. I may add a feature list in the future.

If you want to use this bot for some reason: 

1. Clone the repo
1. Duplicate mylib/keys.py.example as mylib/keys.py and insert your keys (it is gitignored)
1. Duplicate config.py.example as config.py and change things as you need to
1. Install Python 3 and Dependencies
  * discord.py
  * asyncio
If you want to use the maintainer bot launch that python file, otherwise use the discord bot python file

## maintainer bot

This included bot has a command to stop the main bot, pull the latest changes from the current repo, and restart the bot. It also can start and stop the main bot. Useful if you want to put this bot on a raspberry pi and develop else where. This bot is separate and not required to be used.  
