class Peer:
    def __init__(self):
        self.conn = 0
        self.peer_list = []
        self.data = ""
        self.data_received = {}

    # Initialize the connection
    def init_connection(self):
        return self.conn

    # Send Handshake ack to tracker so that the tracker knows a new peer has connected
    def send_handshake(self):
        return True

    # Receive Handshake ack from tracker to confirm connection
    def receive_handshake(self):
        return True

    # Recieve the peer list from the tracker
    def receive_peers(self):
        return self.peer_list

    # Send data to all the other peers
    def send_data(self):
        return self.data
    
    # Receive data from the other peers
    def receive_data(self):
        return self.data_received

    # Disconnect from the p2p. Let the tracker know that this peer has disconnected
    def disconnect_p2p(self):
        return True