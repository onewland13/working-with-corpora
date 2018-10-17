from dataAccess.DataAccessError import DataAccessError

class DataAccess(): 

    def __init__(self, dataSource):
        pass
    # Create
    def addSong(self, songObject):
        raise DataAccessError("addSong", "Tried to addSong with no defined data source.")
    # Read
    def findSong(self, songTitle):
        raise DataAccessError("findSong", "Tried to find a song with no defined data source.")
    def findSongsByArtist(self, artist):
        raise DataAccessError("findSongsByArtist", "Tried to findSongsByArtist with no defined data source.")
    def findSongsByArtistId(self, artistId): 
        raise DataAccessError("findSongsByArtistID", "Tried to findSongsByArtistID with no defined data source.")
    def findSongsByAlbum(self, album):
        raise DataAccessError("findSongsByAlbum", "Tried to findSongsByAlbum with no defined data source.")
    def findSongsByAlbumId(self, albumId):
        raise DataAccessError("findSongsByAlbumID", "Tried to findSongsByAlbumID with no defined data source.")
    # Update
    def updateSongById(self, songId, newSongObject): 
        raise DataAccessError("updateSong", "Tried to updateSong with no defined data source.")
    # Delete
    def removeSong(self, songId): 
        raise DataAccessError("removeSong", "Tried to removeSong with no defined data source.")
