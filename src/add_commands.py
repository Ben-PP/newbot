import discord

import commands.menu as menu
import commands.help as help
def AddCommands(tree):

    # Help
    #
    # Sends help for the user
    @tree.command(name="help", description="Gives a helping hand",guild=discord.Object(id=800338192673931274))
    async def self(interaction: discord.Interaction):
        await help.help(interaction)
    
    # Menu
    #
    # Shows the menu of the day for given restaurant
    @tree.command(name="menu", description="Shows the menu of the day for a restaurant", guild=discord.Object(id=800338192673931274))
    async def self(interaction: discord.Interaction, restaurant: menu.Restaurants):
        await menu.send_menu(interaction.response, restaurant)