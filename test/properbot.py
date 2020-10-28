from discord.ext import commands

from token_cc import token

user_dist_tz = {}
user_fav = {}
bot = commands.Bot(command_prefix="?")


@bot.command()
async def ping(ctx):
    await ctx.channel.send("pong")


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


bot.run(token())
