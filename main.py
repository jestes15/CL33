"""
This is a Discord Bot created by Joshua Estes
Use of this bot must comply with Discord ToS and other government regulations.
Release Date: October 27, 2020

Disclaimer:
Me or my fellow associates are not liable for any mishandling of the
bot by any other foreign entities, sole responsibility will be on the user of said
program.
"""

import os
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from dotenv import load_dotenv
from pretty_help import PrettyHelp

load_dotenv()
TOKEN = os.getenv("DT")

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=["Hey Google, ", "$ ", "<> "], intents=intents)

Discord_ID = '<@!610469915442282526> or DarthBane#8863'


@bot.event
async def on_ready():
    channel = bot.get_channel(756568695320608910)
    await bot.change_presence(activity=discord.Game(name="COD WW2"))
    message = await channel.send(f'{bot.user.name} has connected to discord')
    embed_var = discord.Embed(title='Thank you for using me!', description="Powered by:", color=0xff000b)
    embed_var.set_thumbnail(url='https://www.python.org/static/community_logos/python-logo-master-v3-TM.png')
    await message.edit(embed=embed_var)


@bot.command(name="add_role")
@has_permissions(manage_roles=True)
async def add_role(ctx, role: discord.role.Role, *, args):
    users = args.split()
    role_obj = discord.utils.get(ctx.guild.roles, name=role.name)
    member = await discord.Guild.chunk(ctx.guild)

    for user in users:
        user_id = user.replace("<@!", "").replace(">", "")
        mem = await bot.fetch_user(user_id)
        member_obj = discord.utils.get(member, name=mem.name)
        await discord.Member.add_roles(member_obj, role_obj)


@bot.command(name="remove_role")
@has_permissions(manage_roles=True)
async def remove_role(ctx, role: discord.role.Role, *, args):
    users = args.split()
    role_obj = discord.utils.get(ctx.guild.roles, name=role.name)
    member = await discord.Guild.chunk(ctx.guild)

    for user in users:
        user_id = user.replace("<@!", "").replace(">", "")
        mem = await bot.fetch_user(user_id)
        member_obj = discord.utils.get(member, name=mem.name)
        await discord.Member.remove_roles(member_obj, role_obj)


bot.run(TOKEN)
