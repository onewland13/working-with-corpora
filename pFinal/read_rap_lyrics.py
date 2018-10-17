import json, sys
from pprint import pprint

def setOfArtists():
    with open('./SongsDB copy 2.json') as f:
        data = json.load(f)
    set_of_artists = set()
    for song in data: 
        try:
            set_of_artists.add(song["Primary Arist"])
        except:
            e = sys.exc_info()[0]
            print(e)
    return set_of_artists

if __name__ == "__main__": 
    setOfArtists()

"""
Shape of song objects: 
    'Primary Album': 
        string,
    'Primary Album ID': 
        int,
    'Primary Arist': 
        string,
    'Primary Artist ID': 
        int,
    'Song ID': 
        int,
    'Title': 
        string,
    'lyrics':
        string
"""