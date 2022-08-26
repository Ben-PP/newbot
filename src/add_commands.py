from typing import Literal
import discord
from discord import app_commands
import commands.menu as menu

def AddCommands(tree):
    @tree.command(name="ping", description="Pings the bot",guild=discord.Object(id=800338192673931274))
    async def self(interaction: discord.Interaction):
        await interaction.response.send_message("Pong")
    
    # Help
    #
    #Sends help for the user
    @tree.command(name="help", description="Gives a helping hand",guild=discord.Object(id=800338192673931274))
    async def self(interaction: discord.Interaction):
        embed = {
            "title":"Need help?",
            "description":"Here are all the commands that I know! Starting with commands that **everyone** can access.",
            "fields": [
                {
                    "name":"help",
                    "value":"You can add **'help'**\nto get more info\nabout any !command.",
                    "inline":True
                }
            ]
        }
        await interaction.response.send_message(embed=discord.Embed.from_dict(embed))
    
    @tree.command(name="menu", description="Shows the menu of the day for a restaurant", guild=discord.Object(id=800338192673931274))
    async def self(interaction: discord.Interaction, restaurant: menu.Restaurants):
        await menu.Menu.send_menu(interaction.response, restaurant)