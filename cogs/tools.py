import discord
import asyncio
import random
import math
from scripts import blacklist
from discord.ext import commands


class tools(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def randint(self,ctx, stc1:int, stc2:int):
        result = random.randint(stc1, stc2)
        await ctx.send(f"Результат расчёта рандома между числами {stc1} и {stc2} равен ``{result}``")

    @commands.command()
    async def factorial(self, ctx, num:int):
        result = math.factorial(num)
        await ctx.send(f"Факториал числа {num} равен ``{result}``")

    @commands.command()
    async def sqrt(self, ctx, num:int):
        result = math.sqrt(num)
        await ctx.send(f"Квадратный корень числа {num} равен ``{result}``")

    @commands.command()
    async def embed(self,ctx, name,*, content):
        creator = discord.Embed(title=name, description=content)
        await ctx.send(embed = creator)

    @commands.group(invoke_without_command=True)
    async def remind(self, ctx):
        rinfo = discord.Embed(title="Команда Reminder", description="Используется для создания напоминания. Время указывается в секундах.", color=0x00ff00)
        rinfo.add_field(name="Использование", value="``remind role [Role] [Time]`` - напоминание для роли \n ``remind me [Time] [Message]`` - напоминание для вас", inline=True)
        await ctx.send(embed=rinfo)

    @remind.command()
    async def me(self,ctx, time:int,*, content):
        author = ctx.message.author
        if blacklist.list in content:
            await ctx.send("bot: Недостаточно прав для использования данного текста в напоминании")
        else:
            await ctx.send(f"bot: Напоминание успешно установлено, сработает через {time} секунд")
            await asyncio.sleep(time)
            await ctx.send(f"<:alarm_clock:664007109188255745> **Напоминание для {author.mention} :** {content}")

    @remind.command()
    async def role(self,ctx,role:discord.Role, time:int,*, content):
        if blacklist.list in content:
            await ctx.send("bot: Недостаточно прав для использования данного текста в напоминании")
        else:
            if role.mentionable == True:
                await ctx.send(f"bot: Напоминание успешно установлено, сработает через {time} секунд")
                await asyncio.sleep(time)
                await ctx.send(f"<:alarm_clock:664007109188255745> **Напоминание для {role.mention} :** {content}")
            else:
                await ctx.send("bot: Недостаточно прав. Выберите другую роль.")


def setup(bot):
    bot.add_cog(tools(bot))
