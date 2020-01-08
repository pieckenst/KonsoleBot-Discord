import discord
import asyncio
import os
from discord.ext import commands

class infosystem(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def neofetch(self, ctx, member: discord.Member=None):
        if member is None:
            member = ctx.message.author
        username = member.nick
        join = member.joined_at
        stat = member.status
        activ = member.activity
        ava = member.avatar_url
        id = member.id
        create = member.created_at
        neoembed = discord.Embed(title="Информация о пользователе", color=0x00ff00)
        neoembed.add_field(name="Тэг", value=member, inline=False)
        neoembed.add_field(name="Статус", value=stat, inline=False)
        neoembed.add_field(name="Локальный Ник-Нейм", value=username, inline=False)
        neoembed.add_field(name="ID пользователя", value=id, inline=False)
        neoembed.add_field(name="Дата прихода", value=join, inline=False)
        neoembed.add_field(name="Дата создания аккаунта", value=create, inline=False)
        neoembed.add_field(name="Активити", value=activ, inline=False)
        neoembed.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=neoembed)

    @commands.command()
    async def avatar(self, ctx, member : discord.Member=None):
        if member is None:
            member = ctx.message.author
        avaembed = discord.Embed(title=f"Аватар пользователя {member}",color=0x00ff00)
        avaembed.set_image(url=member.avatar_url)
        avaembed.set_footer(text=f"ID пользователя: {member.id}")
        await ctx.send(embed=avaembed)

    @commands.command()
    async def guild(self, ctx):
        member = ctx.message.author
        servinfo = discord.Embed(title="Информация о сервере", color=0x00ff00)
        servinfo.set_author(name=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
        servinfo.add_field(name="Регион", value=f"{member.guild.region}", inline=True)
        servinfo.set_thumbnail(url=f"{member.guild.icon_url}")
        servinfo.add_field(name="Владелец", value=f"{member.guild.owner.mention}", inline=True)
        servinfo.add_field(name="Уровень защиты", value=f"{member.guild.verification_level}", inline=False)
        servinfo.add_field(name="Пользователей", value=f"{member.guild.member_count}", inline=True)
        servinfo.add_field(name="ID", value=f"{member.guild.id}", inline=False)
        await ctx.send(embed=servinfo)
    
    @commands.command(pass_context=True)
    async def voicedemo(self,ctx, voice: discord.VoiceChannel):
        member = ctx.message.author
        await ctx.send(f"**Ссылка не демонстрацию экрана в канале {voice.mention}**: https://discordapp.com/channels/{member.guild.id}/{voice.id}")
        



def setup(bot):
    bot.add_cog(infosystem(bot)) 

