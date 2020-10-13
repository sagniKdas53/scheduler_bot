import pickle as pk


def make_pick(list_url, titles_and_thumbs, main_storage):
    pick_f = {'list_url': list_url, 'titles_and_thumbs': titles_and_thumbs, 'main_storage': main_storage}
    pk.dump(pick_f, open('pickled_data', 'ab'))


def get_picked():
    unpack = open('pickled_data', 'rb')
    db = pk.load(unpack)
    for keys in db:
        print(keys, '=>', db[keys])
    unpack.close()


make_pick()
get_picked()
