import _thread

class Tracker:
    def __init__(self):
        self.peer_list = []
        self.peer_to_add = []
        self.peer_to_remove = []
        self.conn = 0

    # Initialize the connection
    def init_connection(self):
        return self.conn

    # When a peer is connected to the network, add the peer to the list
    def add_peer(self):
        return self.peer_list

    # When a peer is disconnected from the network, remove the peer from the list
    def remove_peer(self):
        return self.peer_list

    # Send a peer list to a specific peer
    def send_peer_list(self):
        return self.peer_list
    
    # Thread that continuously checks for announcement from new peers, so that they may be added to the network
    def recieve_announcement_thread(self):
        return self.conn