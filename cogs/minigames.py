import discord
import asyncio
import random
from scripts import kubs
from scripts import monet
from scripts import kasinok
from discord.ext import commands

class minigames(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def kubik(self, ctx): #кубик рандом
        kuboid = random.choice(kubs.value)
        embedkub = discord.Embed(title="<:game_die:643509937892229142> Игра в кубик", color=0x00ff00)
        embedkub.add_field(name="Вам выпало:", value=kuboid, inline=False)
        await ctx.send(embed=embedkub)

    @commands.command()
    async def monetka(self, ctx):
        mon = random.choice(monet.str)
        embedmonet = discord.Embed(title="<:moneybag:643869263937011732> Игра в монетку", color=0x00ff00)
        embedmonet.add_field(name="Результат:", value=mon, inline=False)
        await ctx.send(embed=embedmonet)

    @commands.command()
    async def casino(self, ctx):
        kasino1 = random.choice(kasinok.obj1)
        kasino2 = random.choice(kasinok.obj2)
        kasino3 = random.choice(kasinok.obj3)
        embedkas = discord.Embed(title="<:slot_machine:643869263937011732> Казино Три Арча",color=0x00ff00)
        embedkas.add_field(name="Результат:", value=kasino1, inline=True)
        embedkas.add_field(name="Результат:", value=kasino2, inline=True)
        embedkas.add_field(name="Результат:", value=kasino3, inline=True)
        await ctx.send(embed=embedkas)



def setup(bot):
    bot.add_cog(minigames(bot))
