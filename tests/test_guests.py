import unittest

from src.guests import Guest


class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest1 = Guest("John", 32, 100, "All Star")
        # self.room1 = Room ("blue_room", 4, 20, 15)

    def test_guest_has_name(self):
        self.assertEqual("John", self.guest1.name)

    def test_guest_has_age(self):
        self.assertEqual(32, self.guest1.age)

    def test_guest_has_wallet(self):
        self.assertEqual(100, self.guest1.wallet)

    def test_can_pay_entry_fees(self):
        self.assertEqual(85, self.guest1.pay_entry_fees())
    
    def test_can_find_favourite_song(self):
        self.assertEqual("All Star", self.guest1.favourite_song)

    # def test_favourite_song_reaction(self):
    #     reaction = self.guest1.favourite_song_reaction()
    #     self.assertEqual("Whoo!", reaction)
