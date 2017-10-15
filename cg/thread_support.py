import time
import threading


class ThreadPairer:
    def __init__(self, generator):
        assert callable(generator)
        self.generator = generator
        self.__pair_lock = threading.Lock()
        self.__pair_barrier = threading.Barrier(2, action=self.__pair_lock.acquire)

        self.__sync_barrier = threading.Barrier(2)

    def get_paired_instance(self, timeout_ms=100):
        start_time = time.time()
        end_time = start_time + (timeout_ms / 1000)
        while True:
            remaining_time = end_time - time.time()
            try:
                tid = self.__pair_barrier.wait(timeout=remaining_time / 1000)
                break
            except threading.BrokenBarrierError:
                self.__pair_barrier.reset()

            if time.time() > end_time:
                raise TimeoutError()

        if tid == 0:
            self._instance = self.generator()

        self.__sync_barrier.wait()
        my_inst = self._instance
        self.__sync_barrier.wait()

        if tid == 0:
            del self._instance
            self.__pair_lock.release()

        return my_inst
