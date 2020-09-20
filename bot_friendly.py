import glob
from datetime import datetime

from de_nihongfi import translate_export
from get_page import pre_read_check
from localize_csv_bot_ver import _convert_to_local
from read_and_make_csv import start_reading

'''Here i will write the functions that could and would be imported in the bot finally'''


def show_in_time_zone(time_x):
    out_pt = _convert_to_local('export_translated.csv', time_x, 'all')  # takes in export_translated.csv and time zone
    print(out_pt)  # table of names and status in input time zone.


def show_by_name(name_to_show, time_x, boole):
    if boole == 'not over':
        out_pt = _convert_to_local('export_translated.csv', time_x,
                                   name_to_show, False)  # takes in export_translated.csv and time zone
    else:
        out_pt = _convert_to_local('export_translated.csv', time_x,
                                   name_to_show, True)
    return out_pt  # table of names and status in input time zone.


def main():
    file_glob = glob.glob('./*.html')
    now = datetime.now()
    name_f = str(now).replace(' ', '~')
    file_name = ''
    try:
        file_name = str(file_glob[0])[2:]
        print('Working on: ', file_name)
    except IndexError:
        file_name = name_f + '.html'
        # make_file_html(file_name, False)

    checked_f = pre_read_check(file_name, now)  # this returns the source html file
    start_reading(checked_f)  # makes the export.csv (delocalized and untranslated)
    translate_export('export.csv', 'names.txt', 'translate_names.txt')  # makes export_translated.csv


'''show_by_name()
takes first argument as name,
second is timezone third is Show all or over 
for seeing not over ones not over is the only input
for all anyting goes
print(show_by_name('Fubuki', 'Asia/Kolkata','all'))
print(show_by_name('all','Asia/Kolkata','not over'))

client = discord.Client()
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("&&send"):
        text = message.content.split()
        response = show_by_name('Fubuki', 'Asia/Kolkata', 'all')
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException


'''
