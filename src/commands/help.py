import discord

async def help(interaction: discord.Interaction):
    embed = {
        "title":"Need help?",
        "description":"Here are all the commands that I know! Starting with commands that **everyone** can access.",
        "fields": [
            {
                "name":"menu",
                "value":"Shows you the menu of the day for given restaurant.",
                "inline":True
            }
        ]
    }
    await interaction.response.send_message(embed=discord.Embed.from_dict(embed))