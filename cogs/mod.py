import discord
import datetime
import asyncio
from discord.ext import commands
time = datetime.datetime.now()


class mod(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def userdel(self, ctx, member : discord.Member,*, reason=None ): # pacmanR - кик пользователя
        author = ctx.message.author
        if author.guild_permissions.kick_members:
            await member.kick(reason=reason)
            await ctx.send(f"bot: Пользователь был кикнут по причине: {reason}")
        else:
                await ctx.send("bot: Недостаточно прав для выполнения команды")

    @commands.command()
    async def devnull(self, ctx, member : discord.Member,*, reason=None ): # devnull - бан пользователя
        author = ctx.message.author
        if author.guild_permissions.ban_members:
                await member.ban(reason=reason)
                await ctx.send(f"bot: Пользователь был забанен по причине: {reason}")
        else:
                await ctx.send("bot: Недостаточно прав для выполнения команды")

    @commands.command()
    async def clear(self, ctx,*,number:int=None): # clear - Очистка сообщений
        channel = ctx.guild.get_channel(645307856773578782)
        author = ctx.message.author
        if author.guild_permissions.manage_messages:
            if number is None:
                await ctx.send("bot: Введите количество сообщений")
            else:
                await ctx.channel.purge(limit=number)
                await ctx.send(f"bot: Сообщения были очищены")
        else:
            await ctx.send("bot: Недостаточно прав для выполнения команды")


    @commands.command()
    async def rmmod(self, ctx, member: discord.Member,time,*, reason=None):
        author = ctx.message.author
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        if author.guild_permissions.kick_members:
            await member.add_roles(role)
            await ctx.send(f"bot: Пользователь был замьючен по причине: {reason}")
            channel = ctx.guild.get_channel(645307856773578782)
            mutemb = discord.Embed(title="Пользователь был замьючен", color=0x00ff00)
            mutemb.add_field(name="Нарушитель", value=member.mention, inline=False)
            mutemb.add_field(name="Срок мута", value=time, inline=False)
            mutemb.add_field(name="Причина", value=reason, inline=False)
            mutemb.add_field(name="Модератор", value=f"{ctx.message.author.mention}", inline=False)
            await channel.send(embed=mutemb)

        else:
            await ctx.send("bot: Недостаточно прав для выполнения команды")

    @commands.command()
    async def unrmmod(self, ctx, member: discord.Member):
        author = ctx.message.author
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        if author.guild_permissions.kick_members:
            await member.remove_roles(role)
            await ctx.send(f"bot: Пользователь был размьючен")
            channel = ctx.guild.get_channel(645307856773578782)
            unmutemb = discord.Embed(title="Пользователь был размьючен", color=0x00ff00)
            unmutemb.add_field(name="Нарушитель", value=member.mention, inline=False)
            unmutemb.add_field(name="Модератор", value=f"{ctx.message.author.mention}", inline=False)
            await channel.send(embed=unmutemb)
        else:
            await ctx.send("bot: Недостаточно прав для выполнения команды")


def setup(bot):
    bot.add_cog(mod(bot))
