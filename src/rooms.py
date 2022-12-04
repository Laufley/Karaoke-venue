class Room:
    def __init__(self, room_name, max_capacity, default_songs_number, entry_fee,):
        self.room_name = room_name
        self.max_capacity = max_capacity
        self.entry_fee = entry_fee
        self.default_songs_number = default_songs_number
        self.capacity = []
        self.songs_list = []
        self.total_cash_in_room = 0
        self.playlist = []
        
    def number_of_guests(self):        
        return len(self.capacity)

    def add_guest(self, guest):
        self.capacity.append(guest)
        
    def substract_guest(self, guest):
        self.capacity.remove(guest)
        
    def room_available(self):
        number_of_requests = int(self.number_of_guests())
        if number_of_requests < self.max_capacity:
            return True
        else:
            return False
        
    def check_in(self, guest): 
        if self.room_available() == True:
            self.add_guest(guest)
            return(f"The floor is yours, {guest.name}!")     
        else:
            return f"Oops! this room is full, {guest.name}. Try with another! :D"
    
    def check_out(self, guest): 
        if guest in self.capacity:
            self.substract_guest(guest)
            return f"Thanks for coming, {guest.name}. Please join us again!"
        else:
            return f"Beep-Boop: error"
        
    def total_songs_in_room(self):
        count = len(self.songs_list) + self.default_songs_number
        return count
    
    def add_song(self, song):
        self.songs_list.append(song)
        
    def cash_in_entry_fees(self):
        return self.total_cash_in_room + 15
    
    def booking_room(self, guest):
        guest.pay_entry_fees()
        self.cash_in_entry_fees()
        return "thank you for your booking!"
    
    def add_song_to_playlist_to_personalise(self, song):
        self.playlist.append(song)
    
    
    # make cash_inflow_tracker
    # make check_customer_age
    # make sell_drinks_to_guest
    # make sell_food_to_guest
    

