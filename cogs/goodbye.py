import discord
import asyncio
from datetime import datetime
import functools
import os
from discord.ext import commands
class goodbye(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        byetxt = os.path.join(f"db/goodbye/goodbye_{member.guild.id}.txt")
        with open(byetxt, "r") as file:
            set = file.read()
            setchan = int(set)
        #now  = datetime.now()
        #time = now.strftime("%H:%M:%S")
        gb = discord.Embed(title="Пользователь вышел", description=f"{member} пока.", color=0xf4211a)
        #gb.add_field(name="Время", value=time, inline=False)
        gb.set_author(name=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
        gb.set_thumbnail(url=f"{member.avatar_url}")
        channel = self.bot.get_channel(setchan)
        await channel.send(embed=gb)


    @commands.group(invoke_without_command=True)
    async def goodbye(self, ctx):
        await ctx.send("bot: Назначьте канал для отправки прощальных сообщений")

    @goodbye.command()
    async def channel(self, ctx, channel: discord.TextChannel):
        author =  ctx.message.author
        byetxt = os.path.join(f"db/goodbye/goodbye_{author.guild.id}.txt")
        if author.guild_permissions.administrator:
                if os.path.exists(byetxt):
                    os.remove(byetxt)
                with open(byetxt,"a") as goodbye_f:
                     goodbye_f.write(f"{channel.id}")
                await ctx.send(f"bot: Каналом для прощальных сообщений был установлен {channel.mention}")
    @goodbye.command()
    async def clear(self, ctx):
        author =  ctx.message.author
        if author.guild_permissions.administrator:
            byeclear = os.path.join(f"db/goodbye/goodbye_{author.guild.id}.txt")
            if os.path.exists(byeclear):
                 os.remove(byeclear)
            await ctx.send("bot: Файл конфигурации был успешно очищен или он не существует")
        else:
           await ctx.send("bot: Недостаточно прав для выполнения команды. Необходимые права: **Администратор**")


def setup(bot):
    bot.add_cog(goodbye(bot))
