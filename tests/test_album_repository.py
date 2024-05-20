from lib.album_repository import AlbumRepository
from lib.album import Album

"""
When I call #all 
I get all the albums in the albums table
"""
def test_all(db_connection):
    db_connection.seed("seeds/albums_table.sql")
    repository = AlbumRepository(db_connection)
    assert repository.all() == [
        Album(1, "Voyage", 2022, 1)
    ]

"""
When I call #create
I insert new album into albums
and i can see it back in #all
"""
def test_create(db_connection):
    db_connection.seed("seeds/albums_table.sql")
    repository = AlbumRepository(db_connection)
    album = Album(None, "Test Title", 1000, 2)
    repository.create(album)
    assert repository.all() == [
        Album(1, "Voyage", 2022, 1),
        Album(2, "Test Title", 1000, 2)
    ]