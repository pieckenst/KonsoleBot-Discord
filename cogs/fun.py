import discord
import asyncio
from discord.ext import commands

class fun(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def echo(self, ctx,*, arg):
       # await ctx.send(arg)
       await ctx.send("bot: Команда отключена")


   # @commands.command()
   # async def flex(self, ctx):
       # channel = ctx.message.channel
       # embed3 = discord.Embed(color=0x00ff00)
       # embed3.set_image(url = "https://media1.tenor.com/images/9eb29f715e91d09378761a71eec3e3f0/tenor.gif")
       # await ctx.send(embed=embed3)

    @commands.command()
    async def ping(self, ctx):
        for pings in range(4):
            await ctx.send("bot: Обмен пакетами с computerteam.discord. Удачно")






def setup(bot):
    bot.add_cog(fun(bot))

