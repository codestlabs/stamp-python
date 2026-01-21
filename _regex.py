#_regex.py
import re
__all__ = ["rgx"]
class rgx:
    @staticmethod
    def find(pattern, text):
        return re.findall(pattern, text)
    @staticmethod
    def exists(pattern, text):
        return re.search(pattern, text) is not None
    @staticmethod
    def replace(pattern, repl, text, count=0):
        return re.sub(pattern, repl, text, count)
    @staticmethod
    def extract_groups(pattern, text):
        m = re.search(pattern, text)
        return m.groups() if m else None
    @staticmethod
    def split(pattern, text):
        return re.split(pattern, text)
    @staticmethod
    def match(pattern, text):
        return re.fullmatch(pattern, text) is not None