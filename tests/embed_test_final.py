import discord

from token_cc import token

client = discord.Client()
link_s = None
response = None
list_of_titles_and_thumbs = {}


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("&&send"):
        print(link_s, response)
        embed = discord.Embed(title='Video')
        for item in link_s:
            for data in list_of_titles_and_thumbs:
                if item[0][7:-1] == data[0]:
                    print(data)
                    embed.add_field(name=data[1], value=item[0], inline=True)
                    embed.set_image(url=data[2])
                    await message.channel.send(embed=embed)
                    embed.clear_fields()


client.run(token(), bot=True)

"""    embed = discord.Embed(title='LIST')
    size = len(link_s)
    print("Number of entries =" + str(size))
    for link in link_s:
        for sub_l in obJ_class.titles_and_thumbs:
            if link in sub_l:
                embed.add_field(name=sub_l[1], value='[Video](' + link + ')',
                                inline=True)  # something is wrong here i can't remember what it is tho
                embed.set_image(url=sub_l[2])
                await message.channel.send(embed=embed)
                embed.clear_fields()
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
embed = discord.Embed(title='Video')
    for row in range(0, size):
        print(titles_and_thumbs[row])
        embed.add_field(name=titles_and_thumbs[row][0], value='[Vid](' + test_list[row] + ')', inline=True)
        embed.set_image(url=titles_and_thumbs[row][1])
        await message.channel.send(embed=embed)
        embed.clear_fields()
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
if message.content.startswith("&&testC"):
    embed = discord.Embed(title='Video')
    for row in range(0, size):
        print(titles_and_thumbs[row])
        embed.add_field(name=titles_and_thumbs[row][0], value='[Vid](' + test_list[row] + ')', inline=True)
        embed.set_image(url=titles_and_thumbs[row][1])
        await message.channel.send(embed=embed)
        embed.clear_fields()"""
