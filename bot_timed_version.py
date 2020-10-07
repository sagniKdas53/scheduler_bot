import json
from urllib import request, parse

import discord

import internal_working_bot_primitive
from token_cc import token

client = discord.Client()
obJ_class = internal_working_bot_primitive.ExecFaster()


def video_details(vid):
    params = {"format": "json", "url": vid}
    url = "https://www.youtube.com/oembed"
    query_string = parse.urlencode(params)
    url = url + "?" + query_string
    with request.urlopen(url) as response:
        response_text = response.read()
        data = json.loads(response_text.decode())
        details = [data['title'], data['thumbnail_url']]
    return details


# need to check wtf is going on here

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
        time = text[2]
        stat = text[3]
        name = name.title()
        print(name)
        link_s, response = obJ_class.show_by_name(name, time, stat)
        print(link_s, response)
        await message.channel.send(response)
        size = len(link_s)
        print(size)
        list_of_titles_and_thumbs = []
        for link in link_s:
            list_of_titles_and_thumbs.append(video_details(link[7:-1]))
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


client.run(token(), bot=True)
