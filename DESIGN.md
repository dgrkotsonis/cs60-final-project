# CS60, Final Project

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
