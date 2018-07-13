import Room


class UsefulLists:
    def __init__(self, room_list, connections_list):
        self.room_list = room_list
        self.connections_list = connections_list

    def add_room(self, new_room):
        self.room_list.append(new_room)

    def add_connection(self, place1, place2):
        if type(place1) is Room and type(place2) is Room:
            self.connections_list.append([place1, place2])
            return True
        return False

    def check_connection(self, place1, place2):
        for connection in self.connections_list:
            if place1 in connection and place2 in connection:
                return True
        return False

    def remove_connection(self, place1, place2):
        for connection in self.connections_list:
            if place1 in connection and place2 in connection:
                self.connections_list.remove(connection)
                return True
            return False
