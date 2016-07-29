def test_filter_against_latest_blocks(web3, wait_for_block):
    seen_blocks = []
    txn_filter = web3.eth.filter("latest")
    txn_filter.watch(seen_blocks.append)

    current_block = web3.eth.blockNumber

    wait_for_block(web3, current_block + 3)

    txn_filter.stop_watching(30)

    expected_block_hashes = [
        web3.eth.getBlock(n)['hash'] for n in range(current_block + 1, current_block + 3)
    ]

    assert set(expected_block_hashes) == set(seen_blocks)
