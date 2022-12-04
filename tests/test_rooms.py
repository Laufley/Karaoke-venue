import unittest
from src.rooms import Room
from src.guests import Guest
from src.songs import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room1 = Room ("blue_room", 4, 20, 15)
        self.room2 = Room ("red_room", 2, 40, 15)
        self.guest1 = Guest ("John", 32, 100, "All Star")
        self.guest2 = Guest ("Sarah", 25, 60, "Rock the Kasbah")
        self.guest3 = Guest ("Pepe", 16, 10, "Barbie girl")
        self.song1 = Song ("All Star", "Smash Mouth","Pop")
        self.song2 = Song ("Hound Dog", "Elvis Presley", "Rock")
        self.song3 = Song ("I don't wanna miss a thing", "Aerosmith", ("Rock", "Metal)"))
        self.song4 = Song ("Feel Good Inc", "Gorillaz", "Hip-hop" )
    
    def test_room_has_name(self):
        self.assertEqual("blue_room", self.room1.room_name)

    def test_room_has_max_capacity(self):   
        self.assertEqual(4, self.room1.max_capacity)
        
    def test_can_find_number_of_default_songs_per_room(self):
        self.assertEqual(20, self.room1.default_songs_number)
        
    def test_can_find_entry_fee(self):
        self.assertEqual(15, self.room1.entry_fee)

    def test_add_guest_to_capacity(self):
        self.room1.add_guest(self.guest1)
        self.assertEqual(1, self.room1.number_of_guests())
        
    def test_substract_guest_from_capacity(self):
        self.room1.add_guest(self.guest1)
        self.room1.substract_guest(self.guest1)
        self.assertAlmostEqual(0, self.room1.number_of_guests())
        
    def test_if_room_available(self):
        self.assertEqual(True, self.room1.room_available())
        
    def test_can_check_in(self):
        result = self.room1.check_in(self.guest1)
        self.assertEqual(1, self.room1.number_of_guests())
        self.assertEqual("The floor is yours, John!", result)
        
    def test_cannot_check_in(self):
        self.room2.check_in(self.guest1)
        self.room2.check_in(self.guest2)
        result = self.room2.check_in(self.guest3)
        self.assertEqual(2, self.room2.number_of_guests())
        self.assertEqual("Oops! this room is full, Pepe. Try with another! :D", result)
    
    def test_can_check_out(self):
        self.room1.add_guest(self.guest1)
        self.room1.add_guest(self.guest2)
        self.room1.add_guest(self.guest3)
        result = self.room1.check_out(self.guest3)
        self.assertEqual(2, self.room1.number_of_guests())
        self.assertEqual("Thanks for coming, Pepe. Please join us again!", result)
        
    def test_cannot_check_out(self):
        guest4 = Guest("Gareth", 36, 50, "Fly me to the moon")
        self.room1.add_guest(self.guest1)
        self.room1.add_guest(self.guest2)
        result = self.room1.check_out(guest4)
        self.assertEqual(2, self.room1.number_of_guests())
        self.assertEqual("Beep-Boop: error", result)
        
    def test_total_songs_in_room(self):
        self.assertEqual(20, self.room1.total_songs_in_room())
        
    def test_add_song(self):
        self.room1.add_song(self.song1)
        self.room1.add_song(self.song2)
        self.assertEqual(22, self.room1.total_songs_in_room())

    def test_cash_in_entry_fees(self):
        self.assertEqual(15, self.room1.cash_in_entry_fees())

    def test_booking_room(self):
        self.assertEqual(45, self.guest2.pay_entry_fees())
        self.assertEqual(15, self.room1.cash_in_entry_fees())
        
    def can_add_song_to_playlist_to_personalise(self):
        self.assertEqual("All Star", self.room1.song1)
        
