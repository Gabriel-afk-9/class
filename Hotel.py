class RoomOccupiedError(Exception):
    pass

class RoomAlreadyAvailableError(Exception):
    pass

class Hotel:
    def __init__(self, room_numbers):
        self.rooms = {}
        for room in room_numbers:
            self.rooms[room] = "available"
    
    def check_in(self, room_number):
        if self.rooms[room_number] == "occupied":
            raise RoomOccupiedError(f"O quarto {room_number} já está ocupado.")
        self.rooms[room_number] = "occupied"
        print(f"Check-in realizado no quarto {room_number}.")

    def check_out(self, room_number):
        if self.rooms[room_number] == "available":
            raise RoomAlreadyAvailableError(f"O quarto {room_number} já está disponível.")
        self.rooms[room_number] = "available"
        print(f"Check-out realizado no quarto {room_number}.")

    def show_status(self):
        print("Status dos quartos:")
        for room, status in self.rooms.items(): 
            print(f"Quarto {room}: {status}")

if __name__ == "__main__":
    hotel = Hotel([101, 102, 103])

    hotel.show_status()

    hotel.check_in(101)

    hotel.show_status()

    try:
        hotel.check_in(101)
    except RoomOccupiedError as e:
        print(e)

    hotel.check_out(101)

    hotel.show_status()

    try:
        hotel.check_out(101)
    except RoomAlreadyAvailableError as e:
        print(e)
 