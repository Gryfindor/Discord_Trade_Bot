import discord
from discord.ext import commands
from discord.ext.commands import Bot
from bs4 import BeautifulSoup
import requests, fake_useragent

weapon = 'tag_weapon_awp'
quality = 'tag_normal'
exterior = 'tag_WearCategory2'
skin = 'Asiimov'


def get_html(url, header):
    r = requests.get(url, headers=header)
    print(r.status_code)
    return r.text


def get_price(html):
    soap = BeautifulSoup(html, 'html.parser')

    answear = soap.select('span.market_table_value.normal_price')

    for price in answear:
        full_price = price.next.next.next.next.next
    f = open('price.txt', 'w')
    f.write(full_price)
    f.close()

def main():
    ua = fake_useragent.UserAgent()
    user = ua.random
    header = {'User-Agent': str(user)}

    url = "https://steamcommunity.com/market/search?q=" + str(skin) + "&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=" + str(weapon) + "&category_730_Exterior%5B%5D=" + str(exterior) + "&category_730_Quality%5B%5D=" + str(quality) + "&appid=730#p1_price_asc"
    html = get_html(url, header)
    get_price(html)
    f = open('price.txt', 'r')
    pricing = f.read()
    return(pricing)

#Bot Turn

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def cs_skin(ctx):
    await ctx.send('Ceny zaczynają sie od')
    await ctx.send(str(main()))




bot.run(process.env.BOT_TOKEN)
