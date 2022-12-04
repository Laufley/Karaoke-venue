class Guest:
    def __init__(self, name, age, wallet, favourite_song):
        self.name = name
        self.age = age
        self.wallet = wallet
        self.favourite_song = favourite_song
        
    def pay_entry_fees(self):
        return self.wallet - 15
    # 15 = standard booking fee for this venue
    
    
    def favourite_song_reaction(self, room):
        for piece in room.playlist:
            if self.favourite_song == piece:
                return "Whoo!"
    # note to self: make dict in room test for rooms' playlists