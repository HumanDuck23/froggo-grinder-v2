import threading
import time


class Scheduler:
    @staticmethod
    def setTimeout(func, ms):
        def a():
            time.sleep(ms / 1000)
            func()
        threading.Thread(target=a).start()