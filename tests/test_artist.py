from lib.artist import Artist

'''
constructs with a artist
'''
def test_constructs():
    artist = Artist("Beyonce")
    assert artist.artist == "Beyonce"

'''
Artists with equal contents are equal
'''
def test_compares():
    artist_1 = Artist("Jay-Z")
    artist_2 = Artist("Jay-Z")
    assert artist_1 == artist_2

"""
Artists can be represented as strings
"""
def test_stringifying():
    artist = Artist("Jay-Z")
    assert str(artist) == "Jay-Z"