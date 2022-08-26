import requests
import discord
from bs4 import BeautifulSoup
from enum import Enum

class Restaurants(Enum):
    taide="https://www.foodandco.fi/modules/MenuRss/MenuRss/CurrentDay?costNumber=0301&language=fi"
    piato="https://www.semma.fi/modules/MenuRss/MenuRss/CurrentDay?costNumber=1408&language=fi"
    maija="https://www.semma.fi/modules/MenuRss/MenuRss/CurrentDay?costNumber=1402&language=fi"
    lozzi="https://www.semma.fi/modules/MenuRss/MenuRss/CurrentDay?costNumber=1401&language=fi"
    tilia="https://www.semma.fi/modules/MenuRss/MenuRss/CurrentDay?costNumber=1413&language=fi"
    syke="https://www.semma.fi/modules/MenuRss/MenuRss/CurrentDay?costNumber=1405&language=fi"
    belvedere="https://www.semma.fi/modules/MenuRss/MenuRss/CurrentDay?costNumber=1404&language=fi"
    uno="https://www.semma.fi/modules/MenuRss/MenuRss/CurrentDay?costNumber=1414&language=fi"
    ylistö="https://www.semma.fi/modules/MenuRss/MenuRss/CurrentDay?costNumber=1403&language=fi"
    rentukka="https://www.semma.fi/modules/MenuRss/MenuRss/CurrentDay?costNumber=1416&language=fi"

async def send_menu(response: discord.Interaction.response, key: Enum):
    rss_url = key.value
    url = requests.get(rss_url)
    soup = BeautifulSoup(url.text, "xml")
    title = soup.find("title")
    item = soup.find("item")
    date = soup.find("item").find("title")
    description = item.find("description")

    menu = description.text.split("<br>")
    fields = list()
    for menu_item in menu:
        data = menu_item.split(":")
        if len(data) >= 2:
            if data[1] != "\n\n\n":
                fields.append({"name":data[0],"value":data[1],"inline":False})
    
    content = {
        "title":title.text,
        "description":date.string+"\n",
        "fields":fields
    }
    embed = discord.Embed.from_dict(content)
    await response.send_message(embed=embed)