import asyncio

import discord
from discord.ext import commands

from token_cc import token

user_dist_tz = {}
user_fav = {}
bot = commands.Bot(command_prefix="?")
dict_emo = {}


@bot.command(
    help="input = name,  show what?(nor_over/all), your timezone <no commas needed>",
    brief="test to see if dicts work"
)
async def show(ctx, *args):
    name = ''
    time_z = ''
    stat = ''
    usr = ctx.author
    print(str(args))
    print(usr)
    try:
        name = args[0]
    except IndexError:
        try:
            if name == '' or name == "''":
                name = user_fav[usr]
        except KeyError:
            await ctx.channel.send('Set the fav or provide a name')
            return
    try:
        stat = args[1]
    except IndexError:
        if stat == '':
            stat = 'not_over'
    try:
        time_z = args[2]
    except IndexError:
        try:
            if time_z == '' or time_z == "''":
                time_z = user_dist_tz[usr]
        except KeyError:
            await ctx.channel.send('Set the timezone or provide one')
            return
    response = name.title() + stat + time_z
    await ctx.channel.send(response)


@bot.command(
    help="input = your time zone , see from the list using command list_tz",
    brief="test to see if dicts work"
)
async def add_tz(ctx, *args):
    print(str(args))
    usr = ctx.author
    user_dist_tz[usr] = args[0]
    await ctx.channel.send("Saved")


@bot.command(
    help="input = name of your favorite",
    brief="test to see if dicts work"
)
async def add_fav(ctx, *args):
    print(str(args))
    usr = ctx.author
    user_fav[usr] = args[0]
    await ctx.channel.send("Saved")


@bot.command(
    help="input : none",
    brief="stops the bot"
)
async def stop(ctx):
    await ctx.channel.send("Exiting")
    await bot.close()
    print("Successfully logged out")
    # sys.exit(0)


@bot.event
async def on_error(event, *args, **kwargs):
    print(len(kwargs))
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise


@bot.command(
    help="input : name, show what?(nor_over/all), your timezone <no commas needed>   use '' to escape a field",
    brief="shows the simplest list and embeds last three items of the list also allows reminders to be set"
)
async def addrem(ctx, *args):
    name = ''
    time_z = ''
    stat = ''
    usr = ctx.author
    print(str(args))
    print(usr)
    try:
        name = args[0]
    except IndexError:
        try:
            if name == '' or name == "''":
                name = user_fav[usr]
        except KeyError:
            await ctx.channel.send('Set the fav or provide a name')
            return
    try:
        stat = args[1]
    except IndexError:
        if stat == '':
            stat = 'not_over'
    try:
        time_z = args[2]
    except IndexError:
        try:
            if time_z == '' or time_z == "''":
                time_z = user_dist_tz[usr]
        except KeyError:
            await ctx.channel.send('Set the timezone or provide one')
            return
    link_s, response, dict_rem = ['https://youtu.be/spi6yOS6zy4',
                                  'https://youtu.be/wivauAE2_e8', 'https://youtu.be/sW0WaBoKrWw'], 'Well it works', {
                                     'https://youtu.be/wivauAE2_e8': 300, 'https://youtu.be/spi6yOS6zy4': 340,
                                     'https://youtu.be/sW0WaBoKrWw': 580}
    await ctx.channel.send(response)
    embed = discord.Embed(title='Video')
    size = len(link_s)
    link_s = [link_s[-3], link_s[-2], link_s[-1]]
    embed.add_field(name=response, value=str(link_s),
                    inline=True)
    embed.set_image(url='https://i.redd.it/725ovf8iixv51.png')
    await ctx.channel.send(embed=embed)
    resp = await ctx.channel.send('Add a reaction in 30 sec to set reminder')
    await resp.add_reaction(emoji=dict_emo['keycap1'])
    await resp.add_reaction(emoji=dict_emo['keycap2'])
    await resp.add_reaction(emoji=dict_emo['keycap3'])

    async def rem(choice):
        seconds = dict_rem[link_s[choice]] - 300
        await asyncio.sleep(seconds)
        await ctx.author.send(link_s[choice])
        if seconds <= 0:
            await ctx.author.send('Stream starting is live')
        else:
            await ctx.author.send('Stream starting in' + str(seconds))

    def check(ree, ur):
        em = ree.emoji
        if ctx.author == ur:
            if em == dict_emo['keycap1'] or em == dict_emo['keycap2'] or em == dict_emo['keycap3']:
                return True
        return False

    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=30.0, check=check)
        emo = reaction.emoji
        try:
            if emo == dict_emo['keycap1']:
                await rem(0)
            if emo == dict_emo['keycap2']:
                await rem(1)
            if emo == dict_emo['keycap3']:
                await rem(2)
        except (asyncio.TimeoutError, TypeError):
            pass
    except asyncio.TimeoutError:
        await ctx.channel.send('Failed to react')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    for emo_g in bot.emojis:
        dict_emo[emo_g.name] = emo_g
        print(emo_g)


bot.run(token())
