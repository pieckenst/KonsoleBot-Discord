import discord
import asyncio
from discord.ext import commands

class gnulinux(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command() # GNU/Linux Distr Wiki
    async def arch(self, ctx):
        channel = ctx.message.channel
        await ctx.send("bot: Команда выполнена, результат ниже")
        archl = discord.Embed(title="Arch Linux", url="https://www.archlinux.org/download/", description="Arch Linux — независимый дистрибутив GNU/Linux общего назначения, оптимизированный для архитектуры x86-64, который стремится предоставить последние стабильные версии программ, следуя модели rolling release. По умолчанию пользователю предоставляется минималистичная базовая система, в которую пользователь может добавить то, что ему требуется. Для установки, удаления и обновления пакетов используется пакетный менеджер Pacman.", color=0x1793d1)
        archl.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Archlinux-vert-dark.svg/1280px-Archlinux-vert-dark.svg.png")
        archl.add_field(name="Рекомендации", value="Ставить только руками", inline=True)
        await ctx.send(embed=archl)

    @commands.command()
    async def ubuntu(self, ctx): # Ubuntu
        channel = ctx.message.channel
        await ctx.send("bot: Команда выполнена, результат ниже")
        ubuntu1=discord.Embed(title="Ubuntu", url="https://ubuntu.com/", description="Ubuntu — операционная система, основанная на Debian GNU/Linux. Основным разработчиком и спонсором является компания Canonical. В настоящее время проект активно развивается и поддерживается свободным сообществом.", color=0xde4714)
        ubuntu1.set_thumbnail(url="https://i.imgur.com/TfVgK1v.png")
        await ctx.send(embed=ubuntu1)

    @commands.command()
    async def debian(self, ctx): # Debian
        channel = ctx.message.channel
        await ctx.send("bot: Команда выполнена, результат ниже")
        debian1=discord.Embed(title="Debian", url="https://www.debian.org/", description="Debian — операционная система, состоящая из свободного ПО с открытым исходным кодом. В настоящее время Debian GNU/Linux — один из самых популярных и важных дистрибутивов GNU/Linux, в первичной форме оказавший значительное влияние на развитие этого типа ОС в целом. Также существуют проект на основе другого ядра: Debian GNU/Hurd. Debian может использоваться в качестве операционной системы как для серверов, так и для рабочих станций.", color=0xd80150)
        debian1.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Debian-OpenLogo.svg/800px-Debian-OpenLogo.svg.png")
        await ctx.send(embed=debian1)

    @commands.command()
    async def manjaro(self, ctx): # Manjaro
         channel = ctx.message.channel
         await ctx.send("bot: Команда выполнена, результат ниже")
         manjaro1=discord.Embed(title="Manjaro", url="https://manjaro.org/", description="Manjaro Linux или Manjaro — дистрибутив GNU/Linux, основанный на Arch Linux, использующий модель обновлений rolling release.Официально доступно несколько версий: с рабочим окружением XFCE, KDE или GNOME.", color=0x35bf5c)
         manjaro1.set_thumbnail(url="https://fost.ws/uploads/posts/2019-05/1557568788_manjaro-logo.png")
         manjaro1.add_field(name="Рекомендации", value="Подходит для новичков (© suXin)", inline=True)
         await ctx.send(embed=manjaro1)

    @commands.command()
    async def mint(self, ctx): # Mint
        channel = ctx.message.channel
        await ctx.send("bot: Команда выполнена, результат ниже")
        mint1=discord.Embed(title="Linux Mint", url="https://linuxmint.com/", description="Linux Mint — развиваемый сообществом бесплатный дистрибутив Linux, основанный на Ubuntu и Debian, который ставит целью предоставить пользователю «современную, элегантную и удобную операционную систему, которая одновременно является мощной и простой в использовании». Linux Mint предоставляет полную поддержку разнообразных форматов мультимедиа, включает в себя некоторые проприетарные программы и поставляется в комплекте с обширным набором приложений с открытым исходным кодом. Основатель проекта — Клемент Лефевр, в развитии также активно участвуют команда разработчиков (Mint Linux Team) и сообщество пользователей. ", color=0xb1ea77)
        mint1.set_thumbnail(url="https://i.imgur.com/cyRjcbp.png")
        await ctx.send(embed=mint1)




def setup(bot):
    bot.add_cog(gnulinux(bot))
