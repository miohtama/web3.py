import pytest

from web3.providers.rpc import TestRPCProvider


def test_miner_hashrate(web3):
    if isinstance(web3.currentProvider, TestRPCProvider):
        pytest.skip("No miner interface on eth-testrpc")

    hashrate = web3.miner.hashrate
    assert hashrate > 0
