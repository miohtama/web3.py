class Miner(object):
    def __init__(self, request_manager):
        self.request_manager = request_manager

    @property
    def hashrate(self):
        return self.request_manager.request_blocking("eth_hashrate", [])

    def makeDAG(self, number):
        raise NotImplementedError("Not Implemented")

    def setExtra(self, data):
        raise NotImplementedError("Not Implemented")

    def setGasPrice(self, gas_price):
        raise NotImplementedError("Not Implemented")

    def start(self, threads):
        raise NotImplementedError("Not Implemented")

    def stop(self):
        raise NotImplementedError("Not Implemented")

    def startAutoDAG(self):
        raise NotImplementedError("Not Implemented")

    def stopAutoDAG(self):
        raise NotImplementedError("Not Implemented")
