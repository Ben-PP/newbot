#!/usr/bin/env python3

from decouple import config
import discord
from discord import app_commands
import add_commands as add_commands

BOT_TOKEN = config('BOT_TOKEN')

class NewBot(discord.Client):
    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True

    def __init__(self):
        super().__init__(intents=self.intents)
        self.synced = False

    async def on_ready(self):
        await tree.sync(guild=discord.Object(id=800338192673931274))
        self.synced = True
        print(f"Logged in as: {str(self.user)}")

bot = NewBot()
tree = app_commands.CommandTree(bot)
add_commands.AddCommands(tree)

def main():
    bot.run(BOT_TOKEN)

if __name__ == "__main__":
    main()