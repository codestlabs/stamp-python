import os
import random
import datetime
def join(_K1="", _K2=""):
    return _K1+_K2
class CERTSIF:#main2
    def cert(data=[], name=""):
        filename = f"cert?name={name}&timeid={_lstamp._lstamp()}"
        content = f"_DATA_KB = \n{{\n{data}\n}}"
        with open(filename, "x") as f:
            f.write(content)
class CERTIFS:
    def cert(data=[], name=""):
        filename = f"cert?name={name}&timeid={_lstamp._lstamp()}"
        content = f"_DATA_KB = \n{{\n{data}\n}}"
        with open(filename, "x") as f:
            f.write(content)
class CERTIDS:
    def cert(data=[], name=""):
        filename = f"cert?name={name}&timeid={_lstamp._lstamp()}"
        content = f"_DATA_KB = \n{{\n{data}\n}}"
        with open(filename, "x") as f:
            f.write(content)
class CTIDS:#main1
    def cert(data=[], name=""):
        filename = f"cert?name={name}&timeid={_lstamp._lstamp()}"
        content = f"_DATA_KB = \n{{\n{data}\n}}"
        with open(filename, "x") as f:
            f.write(content)
class CTIFS:
    def cert(data=[], name=""):
        filename = f"cert?name={name}&timeid={_lstamp._lstamp()}"
        content = f"_DATA_KB = \n{{\n{data}\n}}"
        with open(filename, "x") as f:
            f.write(content)
class _lstamp:
    @staticmethod
    def _lstamp(month=datetime.datetime.now().strftime("%m"), year=datetime.datetime.now().strftime("%Y"), day=datetime.datetime.now().strftime("%d"), hour=datetime.datetime.now().strftime("%H")):
        return join(join(month, year), join(day, hour))
    @staticmethod
    def _rstamp(month=datetime.datetime.now().strftime("%m"), year=datetime.datetime.now().strftime("%Y"), day=datetime.datetime.now().strftime("%d"), hour=datetime.datetime.now().strftime("%H")): 
        _Y = join(join(month, year), join(day, hour))
        return _Y
class PCCHK:
    def check(filename=""):
        if os.path.exists(filename):
            if ("cert?name=" in filename and "&timeid=" in filename):
                return True
            else:
                return False
        else:
            return False
class SCETT:
    def cert(data=[], name=""):
        filename = f"c?n={name[:3]}&tid={_lstamp._lstamp()}&s=?True"
        content = f"_DATA_KB = {data}"
        with open(filename, "x") as f:
            f.write(content)
class SPCCHK:
    def check(filename=""):
        if os.path.exists(filename):
            if ("c?n=" in filename and "&tid=" in filename):
                return True
            else:
                return False
        else:
            return False
class CDCIFS:
    def cert(data=[], name=""):
        try: 
            filename = f"cert?name={name}&timeid={_lstamp._lstamp()}"
            content = f"_DATA_KB = {data}"
            with open(filename, "a") as f:
                f.write(content)
        except FileNotFoundError:
            raise FileNotFoundError("file not found")
        except IsADirectoryError:
            raise IsADirectoryError("directory not found")
class CERTID:
    def id(data):
        _K_EW = random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]).upper()
        _K_FW = (str(random.randint(0,9)) + \
                 random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]) + \
                 str(random.randint(0,9)) + \
                 _K_EW) * 3
        result = str(data[1]) + str(data[2]) + "-" + str(data[-1]) + str(data[-2]) + "-" + str(_K_FW)
        return result
import string
import hashlib

def sig32(seed: int) -> str:
    """Generate a 32-character pseudo-random signature for a given seed."""
    full_hash = hashlib.sha256(str(seed).encode()).hexdigest()
    return full_hash[:32]  # truncate to 32 characters

def generate_entries(rangeint=256):
    entries = []
    for i in range(rangeint):
        # Generate signature
        sig = sig32(i)
        # Format address (hex, 6 digits, uppercase)
        adress = f"{i:06X}"
        entries.append(f"{sig} {adress}")
    return entries
if __name__ == "__main__":
    entries = generate_entries(256)
    for e in entries:
        print(e)