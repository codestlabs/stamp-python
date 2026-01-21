from .main import edit
import hashlib
_X = 0.0
_Y = 0.0
_V = 0.0
_P = None
_F = None
_S = None
_NAME = ""
_SC = 0
_SNL = []
_FL = []
class hasher:
    def rh8(value: str) -> str:
        return hashlib.sha256(str(value).encode()).hexdigest()[:8]
    def h8(value: str) -> str:
        global _R
        _R = hashlib.sha256(str(value).encode()).hexdigest()[:8]
hasher.h8(edit.join(_X[:4], _Y[:4]))
_HASH = _R
_ID = edit.join(edit.join(_X[:4], _Y[:4]), edit.join(_V[:2], _HASH[:4]))
class ItemError(Exception): pass
class EmptySpriteListError(Exception): pass
_SNL = []
_FL = []
class Sprite:
    def setx(x=0.0):
        _X = x
    def sety(y=0.0):
        _Y = y
    def setv(v=0.0):
        _V = v
    def rgethash():
        _H = _HASH
    def gethash():
        return _HASH
    def getid():
        return _ID
    def getx():
        return _X
    def gety():
        return _Y
    def getv():
        return _V
    def rgetx():
        _P = _X
    def rgety():
        _F = _Y
    def rgetv():
        _S = _V
    def reset():
        _X = 0.0
        _Y = 0.0
        _V = 0.0
        _P = None
        _F = None
        _S = None
        _R = None
        _HASH = None
        _ID = None
        _CNAME = ""
        _SC = 0
        _SNL = []
        _FL = []
    def new(name=f"Sprite{_SC + 1}", x=0.0, y=0.0, v=0.0):
        _SC += 1
        _CNAME = name
        _X = x
        _Y = y
        _V = v
        _SNL.append(_NAME)
        _HASH = hasher.h8(edit.join(_X[:4], _Y[:4]))
        _ID = edit.join(edit.join(_X[:4], _Y[:4]), edit.join(_V[:2], _HASH[:4]))
        _FL.append(edit.join(edit.join(edit.join(_NAME, " "), _X), edit.join(" ", edit.join(_Y, edit.join(" ", edit.join(_V, " ")), edit.join(" ", _HASH), edit.join(" ", _ID)))))
        print(f" - Sprite Created (\" + {_NAME} + \")")
        print(f"  - x: {_X}")
        print(f"  - y: {_Y}")
        print(f"  - v: {_V}")
        print(f"  - hash: {_HASH}")
        print(f"  - id: {_ID}")
    def delete(sname=f"Sprite{_SC + 1}"):
        _CNAME = ""
        try:
            _SNL.remove(sname)
            _SNL.remove(_X)#FIXME
            _SNL.remove(_Y)#FIXME
            _SNL.remove(_V)#FIXME
            _SNL.remove(_HASH)#FIXME
            _SNL.remove(_ID)#FIXME
        except ValueError:
            raise ItemError("sprite to delete must exist")
        try:
            _FL.remove(sname)
            _FL.remove(_X)#FIXME
            _FL.remove(_Y)#FIXME
            _FL.remove(_V)#FIXME
            _FL.remove(_HASH)#FIXME
            _FL.remove(_ID)#FIXME
        except ValueError:
            raise ItemError("sprite to delete must exist")
        print(f" - Sprite Deleted (\" + {_NAME} + \")")
    def info():
        if _SNL == [] and _FL == []:
            raise EmptySpriteListError("sprite list is empty")
        print(edit.join(edit.join(_SNL, "\n"), _FL))
class spriteinfo:
    def sinfo(sname):
        for sprite_full_info in _FL:
            if sname in sprite_full_info:
                parts = sprite_full_info.split(" ")
                name = parts[0]
                _KX = float(parts[1])
                _KY = float(parts[2])
                _KV = float(parts[3])
                _SHASH = parts[4]
                _SID = parts[5]
                return {
                    "name": name,
                    "x": _KX,
                    "y": _KY,
                    "v": _KV,
                    "hash": _SHASH,
                    "id": _SID
                }
            raise EmptySpriteListError("sprite list is empty")