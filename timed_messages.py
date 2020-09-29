import signal
import threading
from datetime import timedelta

import discord
import time

import bot_friendly
from token_cc import token

WAIT_TIME_SECONDS = 60 * 15


class ProgramKilled(Exception):
    pass


def updt():
    obJ_class.update()
    print("Schedule Updated on :", time.ctime())


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
obJ_class = bot_friendly.ExecFaster()


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
        time_f = text[2]
        stat = text[3]
        name = name.title()
        link_s, response = obJ_class.show_by_name(name, time_f, stat)
        await message.channel.send(response)
        embed = discord.Embed(title='Links')
        for row in range(0, len(link_s)):
            embed.add_field(name='[' + str(row) + ']', value=link_s[row], inline=True)

        await message.channel.send(embed=embed)

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


client.run(token(), bot=True)
signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGINT, signal_handler)
print(time.ctime())
job = Job(interval=timedelta(seconds=WAIT_TIME_SECONDS), execute=updt)
job.start()

while True:
    try:
        time.sleep(WAIT_TIME_SECONDS)
    except ProgramKilled:
        print("Program killed")
        job.stop()
        break
