import json, os, sys
from dataAccess.DataAccessError import DataAccessError
from dataAccess.DataAcces import DataAccess

class FileJSONDataAccess(DataAccess): 
    def __init__(self, dataSource="SongsDB copy 2.json"):
        dirname = os.path.dirname(__file__)
        filePath = os.path.join(dirname, dataSource)
        with open(filePath) as f:
            self.data = json.load(f)
    
    def findSong(self, songTitle): 
        for song in self.data: 
            if song["Title"] == songTitle: 
                return song
        raise DataAccessError("findSong", f"couldn't find song in FileJSONDataAccess with song title {songTitle}")
