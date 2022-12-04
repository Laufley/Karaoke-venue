import unittest
from src.songs import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song = Song("All_star", "Smash_Mouth", "Pop")

    def test_song_has_title(self):
        self.assertEqual("All_star", self.song.title)

    def test_song_has_artist(self):
        self.assertAlmostEqual("Smash_Mouth", self.song.artist)

    def test_song_has_genre(self):
        self.assertEqual("Pop", self.song.genre)

        