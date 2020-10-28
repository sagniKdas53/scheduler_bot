"""
NOW THIS IS THE MAIN ONE.
"""
import asyncio
import signal
import threading
from datetime import timedelta

import discord
import sys
import time

import working_bot_newer
from token_cc import token

WAIT_TIME_SECONDS = 60 * 60 * 4  # 4 hours should be enough?
dict_emo = {}


class ProgramKilled(Exception):
    pass


def update_demon():
    size_b4 = sys.getsizeof(obJ_class)
    obJ_class.update()
    size_af = sys.getsizeof(obJ_class)
    print("\nSchedule Updated on :", time.ctime(), '\nChange in size : ', size_b4 - size_af)


def signal_handler(signum, frame):
    print("Killed by :", signum, "\nIn Frame :" + frame)
    raise ProgramKilled


class Job(threading.Thread):
    def __init__(self, interval, execute, *args, **kwargs):
        threading.Thread.__init__(self)
        self.daemon = False
        self.stopped = threading.Event()
        self.interval = interval
        self.execute = execute
        self.args = args
        self.kwargs = kwargs

    def stop(self):
        self.stopped.set()
        self.join()

    def run(self):
        while not self.stopped.wait(self.interval.total_seconds()):
            self.execute(*self.args, **self.kwargs)


client = discord.Client()
obJ_class = working_bot_newer.ExecFaster()


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    for emo_g in client.emojis:
        dict_emo[emo_g.name] = emo_g
        

@client.event
async def on_message(message):
    user = message.author
    if user == client.user:
        return
    if message.content.startswith("&&simp"):
        text = message.content
        text = text.split(' ')
        name = text[1]
        time_z = text[2]
        stat = text[3]
        name = name.title()
        link_s, response, dict_rem = obJ_class.show_by_name(name, time_z, stat)
        await message.channel.send(response)

    if message.content.startswith("&&send"):
        text = message.content
        text = text.split(' ')
        name = text[1]
        time_i = text[2]
        stat = text[3]
        name = name.title()
        link_s, response, dict_rem = obJ_class.show_by_name(name, time_i, stat)
        await message.channel.send(response)
        embed = discord.Embed(title='Video')
        size = len(link_s)
        if size > 3:
            link_s = [link_s[-3], link_s[-2], link_s[-1]]
        for link in link_s:
            sub_l = obJ_class.titles_and_thumbs[link[7:-1]]
            embed.add_field(name=sub_l[0], value=link,
                            inline=True)
            embed.set_image(url=sub_l[1])
        await message.channel.send(embed=embed)

    if message.content.startswith("&&rem"):
        text = message.content
        text = text.split(' ')
        name = text[1]
        time_i = text[2]
        stat = text[3]
        name = name.title()
        link_s, response, dict_rem = obJ_class.show_by_name(name, time_i, stat)
        await message.channel.send(response)
        embed = discord.Embed(title='Video')
        size = len(link_s)
        if size > 3:
            link_s = [link_s[-3], link_s[-2], link_s[-1]]
        for link in link_s:
            sub_l = obJ_class.titles_and_thumbs[link[7:-1]]
            embed.add_field(name=sub_l[0], value=link,
                            inline=True)
            embed.set_image(url=sub_l[1])
        await message.channel.send(embed=embed)
        resp = await message.channel.send('Add a reaction in 30 sec to set reminder')
        await resp.add_reaction(emoji=dict_emo['keycap1'])
        await resp.add_reaction(emoji=dict_emo['keycap2'])
        await resp.add_reaction(emoji=dict_emo['keycap3'])

        async def rem(choice):
            seconds = dict_rem[link_s[choice]] - 300
            await asyncio.sleep(seconds)
            await message.author.send(link_s[choice])
            if seconds <= 0:
                await message.author.send('Stream starting is live')
            else:
                await message.author.send('Stream starting in' + seconds)

        def check(ree, ur):
            em = str(ree.emoji)
            if message.author == ur:
                if em == '<:keycap1:770320921113264158>' or em == '<:keycap2:770321327193718824>' \
                        or em == '<:keycap3:770321274110083072>':
                    return True
            return False

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=30.0, check=check)
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
            await message.channel.send('Failed to react')

    if message.content.startswith("&&exit"):
        await message.channel.send("Exiting")
        await client.close()
        print("Successfully logged out")
        job.stop()
        # sys.exit(0)

    if message.content.startswith("&&age"):
        await message.channel.send('Last updated:' + obJ_class.now)

    if message.content.startswith("&&update"):
        await message.channel.send("Wait a minute")
        getD = obJ_class.update()
        if getD:
            await message.channel.send("Done updating")

    elif message.content == 'raise-exception':
        raise discord.DiscordException


@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise


signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGINT, signal_handler)
print(time.ctime())
job = Job(interval=timedelta(seconds=WAIT_TIME_SECONDS), execute=update_demon)
job.start()
client.run(token(), bot=True)
