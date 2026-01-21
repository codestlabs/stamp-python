#_shcut.py
import os
import time
all = ["ushcut"]
class ushcut:
    @staticmethod
    def join(*parts):
        return os.path.join(*parts)
    @staticmethod
    def now():
        return time.time()
    @staticmethod
    def stamp():
        return time.strftime("%Y-%m-%d %H:%M:%S")
    @staticmethod
    def short(text, maxlen=20):
        text = str(text)
        return text if len(text) <= maxlen else text[:maxlen-3] + "..."
    @staticmethod
    def clip(num, low, high):
        return max(low, min(high, num))
    @staticmethod
    def flatten(seq):
        out = []
        for s in seq:
            if isinstance(s, (list, tuple)):
                out.extend(ushcut.flatten(s))
            else:
                out.append(s)
        return out