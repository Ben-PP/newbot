#!/usr/bin/env python3

from decouple import config
import discord
from discord import app_commands
from discord.ext import commands

BOT_TOKEN = config('BOT_TOKEN')
description = 'Description yay!'
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

class abot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.synced = False

    async def on_ready(self):
        await tree.sync(guild=discord.Object(id=800338192673931274))
        self.synced = True
        print("Bot is online")

bot = abot()
tree = app_commands.CommandTree(bot)

@tree.command(name="ping", description="Pings the bot",guild=discord.Object(id=800338192673931274))

async def self(interaction: discord.Interaction):
    await interaction.response.send_message("Pong")

def main():
    bot.run(BOT_TOKEN)

if __name__ == "__main__":
    main()