import discord
import time
from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('bot is ready:p')

@client.command()
async def kick(ctx, member: discord.Member, reason = None):
    if member.display_name == "BotKicker":
        await ctx.send('You can not kick me :D')

    else:
        await ctx.channel.purge(limit=1)
        message = await ctx.send(f"```Kick: {member.display_name} ?```\n**❎ = No**\n\n**✅ = Yes**")
        await message.add_reaction('❎')
        await message.add_reaction('✅')


        await ctx.send("*30 seconds remainng*")
        time.sleep(25)
        await ctx.send("*5 seconds remainng!*")
        time.sleep(5)

        message = await ctx.fetch_message(message.id)

        most_voted = max(message.reactions, key=lambda r: r.count)
        if most_voted.emoji == "❎":
            await ctx.send(f"**{member.display_name} stays**")

        else:
            await ctx.send(f"** {member.display_name}is kicked out!**")
            await member.kick(reason=reason)

    
client.run('OTE5OTg4ODg1OTczNTE2MzUw.Ybd0ag.T_XJ4agYNmeG8lL1QWgsh5hFuvk')