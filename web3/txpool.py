class TxPool(object):
    def __init__(self, request_manager):
        self.request_manager = request_manager

    @property
    def content(self):
        raise NotImplementedError("Not Implemented")

    @property
    def inspect(self):
        raise NotImplementedError("Not Implemented")

    @property
    def status(self):
        raise NotImplementedError("Not Implemented")
