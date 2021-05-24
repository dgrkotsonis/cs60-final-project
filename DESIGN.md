# CS60, Final Project
# George, Gabe, Boxian and Karim

## Blockchain

A single block will be implemented in class `Block`

The blockchain will be implemented as class `Blockchain`

A single block shall contain the following fields:

- `index`: index of the block in the chain
- `data`: data/transactions stored in the block
- `previous_hash`: hash of the previous block's header
- `nonce`: number for proof of work

To add a block, a node must compute the appropriate nonce such that
the hash fits the difficulty requirement.

Difficuly shall increase with depth but also adjust for computation power.

In case of a fork, the node shall keep the longer/ more difficult branch and discard the 
unwanted one. In case of a draw, it shall keep the earliest one.

The block chain shall make available the following apis to the p2p app:

- `initialize_chain()` returns a new chain w/ genesis block
- `add_block(data)` tries to mine a new block
- `update_chain(chain)` verify and update the local records according to the new chain.

## Peer-To-Peer

The peer-to-peer aspect will require two classes: 

***1.*** `Peer` will essentially be a class designed for clients that will manage the relationship between peers that are connected to the server. It will communicate changes in the Blockchain to all peers and deal with on-boarding and offloading with the server, which will both include a handshake. This class will keep track of the number of connections to the server, a list of all the peers, data ready to be sent out and a dictionary of incoming data. It will allow for the following functionalities:
- `init_connection()`: Returns the connection with the server (aka Tracker)
- `send_handshake()`: Returns bool based on if the ACK sent to initiate the handshake is successfully sent.
- `receive_handshake()`: Returns true if the server responds and the handshake was a success.
- `receive_peers()`: Returns the list of peers currently connected.
- `send_data()`: Returns the data sent to all users (I think we will change this to return a bool signifying the send was a success).
- `receive_data()`: Returns the incoming data from a peer, recieved through the server.
- `disconnect_p2p()`: Returns a bool to signify whether the disconnection handshake attempt was a success.

***2.*** `Tracker` will essentially act as a server and will regularly monitor each connection for updates to assist `Peer` in managing the peer-to-peer relationships. It will have a peer list to keep track of each connection, a list of peers to add, which is a list of new peers joining the server, a list of peers to remove, which is a list of peers that are disconnecting from the server and the number of connections that are currently active. It will allow for the following functionalities:
- `init_connection()`: Returns the new connection with a client
- `add_peer()`: Returns a list of the updated list of peers with the new client.
- `remove_peer()`: Returns a list of the updated list of peers after a client has been removed because they were disconnected.
- `send_peer_list()`: Returns a list of the clients connected. (We might change this to return a bool if the send to all was a success).
- `recieve_announcement_thread()`: Returns the number of connections and will regularly look for activity from the clients and forward this activity to all the peers if deemed necessary. (We might change the return to either a bool or potentially no return.)

## Demo Application

We have not yet decided on this, but are leaning towards implementing a currency.
