import discord

from token_cc import token

client = discord.Client()

test_list = ['https://www.youtube.com/watch?v=A67ZkAd1wmI', 'https://www.youtube.com/watch?v=spi6yOS6zy4',
             'https://www.youtube.com/watch?v=FuxGgJ7Ntts']
list_of_det = [
    [['Caramella Girls - Caramelldansen (Official English Version)',
      'https://i.ytimg.com/vi/A67ZkAd1wmI/hqdefault.jpg']],
    [['SEISO 『Doja Cat "Say So" parody cover』', 'https://i.ytimg.com/vi/spi6yOS6zy4/hqdefault.jpg']],
    [['kyOresu - Pumped up Kicks (cover)', 'https://i.ytimg.com/vi/FuxGgJ7Ntts/hqdefault.jpg']]
]

list_of_titles_and_thumbs = [['Caramella Girls - Caramelldansen (Official English Version)',
                              'https://i.ytimg.com/vi/A67ZkAd1wmI/hqdefault.jpg'],
                             ['SEISO 『Doja Cat "Say So" parody cover』',
                              'https://i.ytimg.com/vi/spi6yOS6zy4/hqdefault.jpg'],
                             ['kyOresu - Pumped up Kicks (cover)', 'https://i.ytimg.com/vi/FuxGgJ7Ntts/hqdefault.jpg']]

# for vid in test_list:
# titles_and_thumbs.append(video_details(vid))

print(list_of_titles_and_thumbs)
size = len(list_of_titles_and_thumbs)
embed = discord.Embed(title='Video')
for row in range(0, size):
    print(list_of_titles_and_thumbs[row][0], list_of_titles_and_thumbs[row][1])


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("&&testM"):
        embed = discord.Embed(title='Video')
        for row in range(0, size):
            print(list_of_titles_and_thumbs[row])
            embed.add_field(name=list_of_titles_and_thumbs[row][0], value='[Vid](' + test_list[row] + ')', inline=True)
            embed.set_image(url=list_of_titles_and_thumbs[row][1])
            await message.channel.send(embed=embed)
    if message.content.startswith("&&testC"):
        embed = discord.Embed(title='Video')
        for row in range(0, size):
            print(list_of_titles_and_thumbs[row])
            embed.add_field(name=list_of_titles_and_thumbs[row][0], value='[Vid](' + test_list[row] + ')', inline=True)
            embed.set_image(url=list_of_titles_and_thumbs[row][1])
            await message.channel.send(embed=embed)
            embed.clear_fields()
    if message.content.startswith("&&testV"):
        embed = discord.Embed(title='Video')
        for row in range(0, size):
            print(list_of_titles_and_thumbs[row])
            embed.video(test_list[row])
            await message.channel.send(embed=embed)
    if message.content.startswith("&&exit"):
        await message.channel.send("Exiting")
        await client.close()
        print("Successfully logged out")


client.run(token(), bot=True)

# &&testC works
