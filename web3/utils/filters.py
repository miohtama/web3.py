import random
import gevent


class BaseFilter(gevent.Greenlet):
    callbacks = None
    running = None
    stopped = False

    def __init__(self, web3, filter_id):
        self.web3 = web3
        self.filter_id = filter_id
        self.callbacks = []
        gevent.Greenlet.__init__(self)

    def __str__(self):
        return "Filter for {0}".format(self.filter_id)

    def _run(self):
        if self.stopped:
            raise ValueError("Cannot restart a Filter")
        self.running = True

        while self.running:
            changes = self.web3.eth.getFilterChanges(self.filter_id)
            for change in changes:
                for callback_fn in self.callbacks:
                    callback_fn(change)
            gevent.sleep(random.random())

    def watch(self, *callbacks):
        if self.stopped:
            raise ValueError("Cannot watch on a filter that has been stopped")
        self.callbacks.extend(callbacks)

        if not self.running:
            self.start()

    def stop_watching(self, timeout=0):
        self.running = False
        self.stopped = True
        self.web3.eth.uninstallFilter(self.filter_id)
        self.join(timeout)

    stopWatching = stop_watching


class BlockFilter(BaseFilter):
    pass


class TransactionFilter(BaseFilter):
    pass


class LogFilter(BaseFilter):
    def get(self, only_changes=True):
        if self.running:
            raise ValueError(
                "Cannot call `get` on a filter object which is actively watching"
            )
        if only_changes:
            return self.web3.eth.getFilterChanges(self.filter_id)
        else:
            return self.web3.eth.getFilterChanges(self.filter_id)
