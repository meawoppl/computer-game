import threading


class ThreadPairer:
    def __init__(self):
        self.__pair_lock = threading.Lock()
        self.__pair_barrier = threading.Barrier(2, action=self.__pair_lock.acquire)

        self.__sync_barrier = threading.Barrier(2)

    def get_instance(self):
        raise NotImplementedError("Subclass must implement")

    def get_paired_instance(self, timeout_ms=1000):
        try:
            tid = self.__pair_barrier.wait(timeout=timeout_ms / 1000)
        except threading.BrokenBarrierError as e:
            self.__pair_barrier.reset()
            raise TimeoutError() from e

        if tid == 0:
            self._instance = self.get_instance()

        self.__sync_barrier.wait()
        my_inst = self._instance
        self.__sync_barrier.wait()

        if tid == 0:
            self.__pair_lock.release()

        return my_inst
