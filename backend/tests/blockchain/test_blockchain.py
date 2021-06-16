import pytest

from backend.tests.blockchain.test_block import block
from backend.blockchain.blockchain import Blockchain
from backend.blockchain.block import Block, GENESIS_DATA


def test_blockchain_instance():
    # To test if the first block's hash is the same as gensis block's hash
    blockchain = Blockchain()
    assert blockchain.chain[0].hash == GENESIS_DATA['hash']


def test_add_block():
    # To test latest block's data matches data added with add_block method
    blockchain = Blockchain()
    data = 'test-data'
    blockchain.add_block(data)

    assert blockchain.chain[-1].data == data


@pytest.fixture
def blockchain_three_blocks():
    blockchain = Blockchain()
    for i in range(3):
        blockchain.add_block(i)
    return blockchain


def test_is_valid_chain(blockchain_three_blocks):
    # Test to check is_valid_chain when a valid chain is given
    Blockchain.is_valid_chain(blockchain_three_blocks.chain)


def test_is_valid_chain_bad_genesis(blockchain_three_blocks):
    # Test to see if an exception is raised when bad genesis block
    blockchain_three_blocks.chain[0].hash = 'evil_hash'
    with pytest.raises(Exception, match='genesis block must be valid'):
        Blockchain.is_valid_chain(blockchain_three_blocks.chain)


def test_replace_chain(blockchain_three_blocks):
    # Test that a longer chain replaces a shorter chain of blockchain
    blockchain = Blockchain()
    blockchain.replace_chain(blockchain_three_blocks.chain)

    assert blockchain.chain == blockchain_three_blocks.chain


def test_replace_chain_not_longer(blockchain_three_blocks):
    # Test when the incoming chain is shorter
    blockchain = Blockchain()
    with pytest.raises(Exception, match='incoming chain must be longer'):
        blockchain_three_blocks.replace_chain(blockchain.chain)


def test_replace_chain_bad_chain(blockchain_three_blocks):
    # Test when the incoming chain is bad
    blockchain = Blockchain()
    blockchain_three_blocks.chain[1].hash = 'evil_hash'

    with pytest.raises(Exception, match='incoming chain is invalid'):
        blockchain.replace_chain(blockchain_three_blocks.chain)
