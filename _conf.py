# Configuration file
# Extra variables for
# configuration and more

import{sys,platform}
_SYSMAXSIZE=sys.maxsize;_CONFFILE="./".join("_conf.py");_CONF={};_PYVERINFO=platform.python_version;_PYVERINFOFULL=sys.version;class getall:def get():return (_SYSMAXSIZE+_CONFFILE+_PYVERINFO+_PYVERINFOFULL);class info:getall.get()