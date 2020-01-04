import discord
import asyncio
import random
from scripts import desAnime
from scripts import desNature
from discord.ext import commands

class wallpapers(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.group(invoke_without_command=True)
    async def wallpaper(self, ctx):    
        wallinfo = discord.Embed(title="Команда wallpaper", description="Используется для просмотра обоев рабочего стола. ", color=0x00ff00)
        wallinfo.add_field(name="Использование", value="``wallpaper anime`` - обои с персонажами anime. \n``wallpaper nature``- обои с природой.", inline=True)
        await ctx.send(embed=wallinfo)

    @wallpaper.command()
    async def anime(self, ctx):
        imganime = random.choice(desAnime.images)
        embedanime = discord.Embed(title="Обои для рабочего стола. Тематика: Аниме", color=0x00ff00, url=imganime)
        embedanime.set_image(url=imganime)
        embedanime.set_footer(text="Спасибо Gebet94#4491 за предоставленные обои")
        await ctx.send(embed=embedanime)

    @wallpaper.command()
    async def nature(self, ctx):
        imgnat = random.choice(desNature.images)
        embednat = discord.Embed(title="Обои для рабочего стола. Тематика: Природа", color=0x00ff00, url=imgnat)
        embednat.set_image(url=imgnat)
        await ctx.send(embed=embednat)


def setup(bot):
    bot.add_cog(wallpapers(bot))
