import signal
import threading
from datetime import timedelta

import discord
import sys
import time

import bot_with_embeds
from token_cc import token

WAIT_TIME_SECONDS = 60 * 15


class ProgramKilled(Exception):
    pass


def update_demon():
    size_b4 = sys.getsizeof(obJ_class)
    obJ_class.update()
    size_af = sys.getsizeof(obJ_class)
    print("\nSchedule Updated on :", time.ctime(), '\nChange in size : ', size_b4 - size_af)


def signal_handler(signum, frame):
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
obJ_class = bot_with_embeds.ExecFaster()


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_ready():
    for guild in client.guilds:
        print(guild.name)
        members = '\n - '.join([member.name for member in guild.members])
        print(f'Guild Members:\n - {members}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("&&send"):
        text = message.content
        text = text.split(' ')
        name = text[1]
        time_t = text[2]
        stat = text[3]
        name = name.title()
        link_s, response = obJ_class.show_by_name(name, time_t, stat)
        await message.channel.send(response)
        size = len(link_s)  # number of links to process
        list_of_titles_and_thumbs = []
        '''The new idea is to use the vid as the key of the dictionary 
        that will have the thumbs and video tiles and it will be made by the __init__ not here then when necessary
        the key can be used here to get the values and make the embed'''
        for link in link_s:
            list_of_titles_and_thumbs.append(obJ_class.video_details(link[7:-1]))
        print(list_of_titles_and_thumbs)
        embed = discord.Embed(title='Video')
        for row in range(0, size):
            print(list_of_titles_and_thumbs[row])
            embed.add_field(name=list_of_titles_and_thumbs[row][0], value='[Vid](' + link_s[row] + ')', inline=True)
            embed.set_image(url=list_of_titles_and_thumbs[row][1])
            await message.channel.send(embed=embed)
            embed.clear_fields()

    if message.content.startswith("&&exit"):
        await message.channel.send("Exiting")
        await client.close()
        print("Successfully logged out")
    if message.content.startswith("&&update"):
        await message.channel.send("Wait a few seconds")
        obJ_class.update()

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

while True:
    try:
        time.sleep(WAIT_TIME_SECONDS)
    except ProgramKilled:
        print("Program killed")
        job.stop()
        break
