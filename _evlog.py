#_evlog.py
import time
__all__ = ["uevlog"]
class uevlog:
    LOG = []              #in-memory circular log
    MAX = 500             #max events stored
    FILE = None           #optional log file
    @staticmethod
    def _stamp():
        return time.strftime("%Y-%m-%d %H:%M:%S")
    @classmethod
    def set_file(cls, filepath):
        cls.FILE = filepath
    @classmethod
    def write(cls, event, category="info"):
        entry = f"[{cls._stamp()}] [{category.upper()}] {event}"
        cls.LOG.append(entry)
        if len(cls.LOG) > cls.MAX:
            cls.LOG.pop(0)
        if cls.FILE:
            with open(cls.FILE, "a", encoding="utf-8") as f:
                f.write(entry + "\n")
    @classmethod
    def recent(cls, n=10):
        return cls.LOG[-n:]
    @classmethod
    def dump(cls):
        return list(cls.LOG)
    @classmethod
    def clear(cls):
        cls.LOG.clear()
