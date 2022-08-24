import discord

def AddCommands(tree):
    @tree.command(name="ping", description="Pings the bot",guild=discord.Object(id=800338192673931274))
    async def self(interaction: discord.Interaction):
        await interaction.response.send_message("Pong")