import discord
import asyncio
import os
from discord.ext import commands
bot = commands.Bot(command_prefix='$') # Префикс бота
@bot.event
async def on_ready():
    print("Бот запущен") # Вывод информации о запуске
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("KDE"))

bot.remove_command("help")

@bot.command()
async def shutdown(ctx): # Команда для выключения бота
    author = ctx.message.author
    if author.id == 579750505736044574:
        await ctx.send("Выключение бота")
        await ctx.bot.logout()
    else:
        await ctx.send("bot: Недостаточно прав для выполнения команды. Необходимые права **Владелец бота**")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="<:info:656202310434816011> KonsoleBot", description="Бот пародирующий терминал UNIX-подобных ОС и оболочку bash", color=0x00ff00)
    embed.add_field(name="Автор", value="NigamanRPG#6937 для Computer Team", inline=False)
    embed.add_field(name="Пригласить", value="Никак, это приватный бот", inline=True)
    embed.add_field(name="Благодарности", value="Gebet94 - Аниме обои, помощь с кодом \n k0tletka - помощь с кодом", inline=False)
    embed.add_field(name="Сервер Computer Team",inline=True, value="https://discord.gg/62qMzb7")
    embed.set_footer(text="Создан для сервера Computer Team. NigamanRPG")
    await ctx.send(embed=embed)

@bot.group(invoke_without_command=True) # Команда Help
async def help(ctx): # help
    embed1=discord.Embed(title="KonsoleBot Справка. Модули.", description="Информация о командах и модулях бота. Подробнее help [модуль].", color=0x00ff00)
    embed1.add_field(name="moderation", value="Информация об админских командах.", inline=True)
    embed1.add_field(name="fun [В разработке]", value="Информация о фан командах.", inline=True)
    embed1.add_field(name="minigames", value="Информация о мини-играх.", inline=True)
    embed1.add_field(name="wallpapers", value="Информация о командах для получения обоев рабочего стола.", inline=True)
    embed1.add_field(name="infosystem", value="Информация о командах для получения данных о сервере, пользователе и т.п.", inline=True)
    embed1.add_field(name="wiki", value="Информация о вики командах.", inline=True)  
    embed1.add_field(name="config", value="Информация о командах для конфигурации и настройки.", inline=True)
    embed1.add_field(name="system", value="Информация о командах для голосования, обращения к администрации и т.п.", inline=True)
    embed1.set_footer(text="Создан для сервера Computer Team. NigamanRPG. Python+Discord.py")
    await ctx.send(embed=embed1)

@help.command(pass_context=True)
async def moderation(ctx):
    modemb = discord.Embed(title="KonsoleBot. Модуль Модерация.", description="Команды модерации", color=0x1fe6ca)
    modemb.add_field(name="devnull [user] {reason} ", value="Бан пользователя", inline=False)
    modemb.add_field(name="userdel [user] {reason}", value="Кик пользователя", inline=False)
    modemb.add_field(name="rmmod [user] [time] {reason}", value="Мут пользователя", inline=False)
    modemb.add_field(name="unrmmod [user]", value="Размут пользователя", inline=False)
    modemb.add_field(name="clear [amount]", value="Очистить сообщения", inline=False)
    modemb.set_footer(text="Создан для сервера Computer Team. NigamanRPG. Python+Discord.py")
    await ctx.send(embed=modemb)

@help.command(pass_context=True)
async def minigames(ctx):
    mgemb = discord.Embed(title="KonsoleBot. Модуль Мини-Игры.", description="Команды для мини-игр", color=0xff9219)
    mgemb.add_field(name="kubik", value="Подбросить кубик (результат: число от 1 до 6)", inline=False)
    mgemb.add_field(name="monetka", value="Подкинуть монетку (2 результата)", inline=False)
    mgemb.add_field(name="casino", value="Сыграть в казино", inline=False)
    mgemb.set_footer(text="Создан для сервера Computer Team. NigamanRPG. Python+Discord.py")
    await ctx.send(embed=mgemb)

@help.command(pass_context=True)
async def wallpapers(ctx):    
    wallemb = discord.Embed(title="KonsoleBot. Модуль Обои для рабочего стола.", description="Команды для получения обоев рабочего стола", color=0xff9219)
    wallemb.add_field(name="wallpaper [category]", value="Получить изображение для рабочего стола", inline=False)
    wallemb.add_field(name="Категории", value="``anime`` - обои с аниме \n ``nature`` - обои с природой", inline=False)
    wallemb.set_footer(text="Создан для сервера Computer Team. NigamanRPG. Python+Discord.py")
    await ctx.send(embed=wallemb)

@help.command(pass_context=True)
async def wiki(ctx):
    wikiemb = discord.Embed(title="KonsoleBot. Модуль Вики.", description="Команды для получения Вики-информации", color=0xf417ce)
    wikiemb.add_field(name="manjaro", value="Информация о дистрибутиве Manjaro", inline=False)
    wikiemb.add_field(name="arch", value="Информация о дистрибутиве Arch", inline=False)
    wikiemb.add_field(name="ubuntu", value="Информация о дистрибутиве Ubuntu", inline=False)
    wikiemb.add_field(name="mint", value="Информация о дистрибутиве Linux Mint", inline=False)
    wikiemb.set_footer(text="Создан для сервера Computer Team. NigamanRPG. Python+Discord.py")
    await ctx.send(embed=wikiemb)

@help.command(pass_context=True)
async def infosystem(ctx):
    infemb=discord.Embed(title="KonsoleBot. Модуль ИнфоСистемы.", description="Команды для получения информации о пользователе, сервере и т.д.", color=0x1f8100)
    infemb.add_field(name="neofetch [user]", value="Информация о пользователе", inline=False)
    infemb.add_field(name="guild ", value="Информация о сервере", inline=False)
    infemb.add_field(name="voicedemo [VoiceChannel]", value="Получение ссылки для демонстрации экрана в голосовом чате", inline=False)
    infemb.add_field(name="avatar [user]", value="Аватар пользователя", inline=False)
    infemb.set_footer(text="Создан для сервера Computer Team. NigamanRPG. Python+Discord.py")
    await ctx.send(embed=infemb) 

@help.command(pass_context=True)
async def config(ctx):
    confemb=discord.Embed(title="KonsoleBot. Модуль Конфигурация.", description="Команды для настройки бота", color=0x0034f6)
    confemb.add_field(name="welcome channel [TextChannel] | clear", value="Выбор канала для отправки приветственных сообщений | Очистка конфигурационного файла", inline=False)
    confemb.add_field(name="goodbye channel [TextChannel] | clear", value="Выбор канала для отправки прощальных сообщений | Очистка конфигурационного файла", inline=False)
    confemb.add_field(name="sub channel [TextChannel] | clear", value="Выбор канала для отправки предложений | Очистка конфигурационного файла", inline=False)
    confemb.add_field(name="ticket channel [TextChannel] | clear", value="Выбор канала для отправки тикетов | Очистка конфигурационного файла", inline=False)
    confemb.set_footer(text="Создан для сервера Computer Team. NigamanRPG. Python+Discord.py")
    await ctx.send(embed=confemb) 

@help.command(pass_context=True)
async def system(ctx):
    systememb=discord.Embed(title="KonsoleBot. Модуль Системы.", description="Команды для создания предложения, тикетов и т.д.", color=0xedf41a)
    systememb.add_field(name="sub create [Text] | faq", value="Создание предложения | Получение информации о реакциях и отметках", inline=False)
    systememb.add_field(name="ticket create [Text]", value="Отправка тикета администрации", inline=False)
    systememb.set_footer(text="Создан для сервера Computer Team. NigamanRPG. Python+Discord.py")
    await ctx.send(embed=systememb)


initial_extensions = ["cogs.mod", # Модуль модерации
                      "cogs.minigames", # Модуль мини-игр
                      "cogs.fun", # Модуль фана
                      "cogs.gnulinux", # Модуль wiki
                      "cogs.infosystem", # Модуль инфоСистемы
                      "cogs.goodbye", # Модуль прощальных сообщений
                      "cogs.welcome", # Модуль приветственных сообщений
                      "cogs.tickets", # Модуль тикетов
                      "cogs.submits", # Модуль голосований/предложений
                      "cogs.wallpapers"] # Модуль обоев для рабочего стола

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
            print(f"Модуль {extension} успешно загрузился")
            print("----------------------------------")
        except Exception as e:
            print(f"Модуль {extension} не может загрузиться")
            raise e


bot.run() # Токен бота для запуска





